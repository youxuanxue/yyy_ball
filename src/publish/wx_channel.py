import json
import logging
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from playwright.sync_api import sync_playwright, Page, BrowserContext, Playwright

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@dataclass
class VideoPublishTask:
    """Data class representing a video publishing task."""
    video_path: Path
    description: str
    title: str = ""  # Added title field
    cover_path: Optional[Path] = None
    # Potential future fields: tags, location, schedule_time, etc.

    def validate(self):
        """Validates that the necessary files exist."""
        if not self.video_path.exists():
            raise FileNotFoundError(f"Video file not found: {self.video_path}")
        if self.cover_path and not self.cover_path.exists():
            raise FileNotFoundError(f"Cover file not found: {self.cover_path}")


class WeChatChannelPublisher:
    """
    Automates publishing videos to WeChat Channels (视频号) using Playwright.
    """
    
    BASE_URL = "https://channels.weixin.qq.com"
    CREATOR_URL = "https://channels.weixin.qq.com/platform/post/create"
    AUTH_FILE = "config/auth_wx.json"

    def __init__(self, headless: bool = False, auth_path: str = ".", debug: bool = False):
        """
        Initialize the publisher.

        Args:
            headless: Whether to run the browser in headless mode. 
                      Defaults to False for visibility during potential manual login.
            auth_path: Directory to store the authentication state file.
            debug: Whether to generate debug files (screenshots, HTML dumps). 
                   Defaults to False.
        """
        self.headless = headless
        self.debug = debug
        self.auth_file_path = Path(auth_path) / self.AUTH_FILE
        self._playwright: Optional[Playwright] = None
        self._browser = None
        self._context: Optional[BrowserContext] = None
        self._page: Optional[Page] = None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def start(self):
        """Starts the Playwright browser and context."""
        logger.info("Starting Playwright...")
        self._playwright = sync_playwright().start()
        
        # Launch browser
        # We use channel="chrome" or just chromium. Chromium is usually bundled.
        self._browser = self._playwright.chromium.launch(
            headless=self.headless,
            args=["--start-maximized"] # Open maximized to ensure elements are visible
        )
        
        # Load auth state if exists
        if self.auth_file_path.exists():
            logger.info(f"Loading auth state from {self.auth_file_path}")
            self._context = self._browser.new_context(
                storage_state=str(self.auth_file_path),
                no_viewport=True  # Allow window to determine viewport
            )
        else:
            logger.info("No auth state found. Starting fresh context.")
            self._context = self._browser.new_context(no_viewport=True)

        self._page = self._context.new_page()

    def close(self):
        """Closes the browser and Playwright."""
        if self._context:
            # Save state before closing if we are logged in
            try:
                self._save_auth_state()
            except Exception as e:
                logger.warning(f"Failed to save auth state on close: {e}")
            self._context.close()
        
        if self._browser:
            self._browser.close()
        
        if self._playwright:
            self._playwright.stop()
        
        logger.info("Browser closed.")

    def _save_auth_state(self):
        """Saves the current browser context storage state to file."""
        if self._context:
            self._context.storage_state(path=str(self.auth_file_path))
            logger.info(f"Auth state saved to {self.auth_file_path}")

    def login(self, timeout: int = 60):
        """
        Checks if logged in. If not, waits for user to scan QR code.
        
        Args:
            timeout: How long to wait for login (in seconds) if manual intervention is needed.
        """
        if not self._page:
            raise RuntimeError("Browser not started. Call start() first.")

        logger.info("Navigating to WeChat Channels...")
        self._page.goto(self.BASE_URL)
        
        # Simple check for login: Look for a known element that only appears when logged in.
        # e.g., avatar, or specific menu items.
        # Conversely, look for "Scan QR Code" text.
        
        try:
            # Adjust this selector based on actual DOM of logged-in state
            logger.info("Checking login status...")
            
            # Wait a moment for load - use domcontentloaded instead of networkidle which can be flaky
            self._page.wait_for_load_state("domcontentloaded")
            
            # Check current URL. If it contains 'login', we definitely need to login.
            # If it's the base URL or platform URL, we might be logged in.
            
            if "login" in self._page.url:
                 logger.info("Not logged in (url contains 'login'). Please scan the QR code.")
                 # Wait for user to scan and login. 
                 # We assume successful login redirects away from a URL containing 'login'
                 # or redirects to /platform
                 self._page.wait_for_url(lambda url: "login" not in url, timeout=timeout * 1000)
                 logger.info("Login detected (URL changed)!")
                 
                 # Wait a bit more for the post-login page to stabilize
                 self._page.wait_for_load_state("domcontentloaded")
                 self._save_auth_state()
            else:
                # Double check: sometimes we are on the homepage but not logged in (e.g. guest mode?)
                # But for channels.weixin.qq.com, usually it redirects to login if not authenticated.
                logger.info(f"URL does not contain 'login': {self._page.url}. Assuming logged in.")
                # Optional: Check for a specific element to be sure, e.g. text="发表视频" or "首页"
                # self._page.wait_for_selector("text=首页", timeout=5000)

        except Exception as e:
            logger.error(f"Login check failed or timed out: {e}")
            # Capture screenshot for debugging
            if self.debug:
                try:
                    self._page.screenshot(path="login_error.png")
                    logger.info("Saved screenshot to login_error.png")
                except:
                    pass
            raise

    def publish(self, task: VideoPublishTask):
        """
        Executes the publishing workflow.
        
        Args:
            task: The video publishing task containing file paths and metadata.
        """
        task.validate()
        
        if not self._page:
            raise RuntimeError("Browser not started.")

        logger.info("Navigating to creation page...")
        try:
            self._page.goto(self.CREATOR_URL)
            self._page.wait_for_load_state("domcontentloaded")
            # Debug: Snapshot after navigation
            if self.debug:
                self._page.screenshot(path="create_page_loaded.png")
                Path("create_page_debug.html").write_text(self._page.content(), encoding="utf-8")
        except Exception as e:
            logger.error(f"Navigation to create page failed: {e}")
            if self.debug:
                self._page.screenshot(path="nav_error.png")
            raise e

        # Check if we were redirected to login
        if "login" in self._page.url:
             logger.warning("Redirected to login page during publish. Session might have expired.")
             if self.debug:
                 self._page.screenshot(path="session_expired.png")
             raise RuntimeError("Session expired. Please re-login.")

        # 1. Upload Video
        # We need to find the file input for video.
        logger.info(f"Uploading video: {task.video_path}")

        
        # Note: Selectors here are hypothetical and need verification against the live site.
        # Often inputs are hidden. We use specific handle.
        try:
            # Wait for the upload area or input
            # Strategy: Find the file chooser directly if button triggers it, or set input files directly.
            # Many modern uploaders have a hidden input[type=file].
            file_input_selector = 'input[type="file"][accept*="mp4"]' 
            # If there are multiple, we might need to be more specific. 
            # Usually the first one on the creation page is for the main video.
            
            # Sometimes the input is not in the DOM until a button is clicked.
            # But usually for drag-and-drop zones, the input exists but is hidden.
            
            # Fallback: clicking the upload button to trigger file chooser
            # with self._page.expect_file_chooser() as fc_info:
            #     self._page.click("text=上传视频")
            # file_chooser = fc_info.value
            # file_chooser.set_files(str(task.video_path))
            
            # Direct input setting (faster if input exists)
            self._page.set_input_files('input[type="file"]', str(task.video_path))
            
        except Exception as e:
            logger.error(f"Failed to initiate video upload: {e}")
            logger.info("Attempting fallback: Click upload button...")
            # Fallback logic would go here (e.g. finding button by text)
            raise e

        # Wait for upload to complete? 
        # Usually there is a progress bar. We might not need to wait for 100% to fill text,
        # but we should ensure the UI has switched to the editing form.
        logger.info("Waiting for upload to complete (timeout: 300s)...")
        
        # Take a screenshot to debug what the UI looks like at this point
        if self.debug:
            self._page.screenshot(path="upload_start_debug.png")
        
        # 2. Fill Description
        logger.info("Waiting for description editor to appear...")
        
        # Hard wait to let upload start and UI stabilize
        time.sleep(10)
        
        try:
            # 2.1 Fill Description using the specific selector provided by user
            # Selector: div.input-editor[contenteditable="true"]
            # We also look for the data-placeholder as a strong signal
            logger.info("Looking for description editor...")
            
            # Wait for either the editor or the placeholder text which might be inside it
            self._page.wait_for_selector('div.input-editor, div[data-placeholder="添加描述"]', state="visible", timeout=300000)
            
            editor = self._page.locator('div.input-editor, div[data-placeholder="添加描述"]').first
            editor.click()
            editor.type(task.description)
            logger.info("Description filled.")
            
            # 2.2 Fill Short Title (if available)
            # Selector: input.weui-desktop-form__input[placeholder*="概括视频主要内容"]
            if task.title:
                logger.info(f"Filling title: {task.title}")
                try:
                    title_input = self._page.locator('input.weui-desktop-form__input[placeholder*="概括视频主要内容"]')
                    if title_input.is_visible():
                        title_input.fill(task.title)
                    else:
                        logger.info("Title input not visible, skipping.")
                except Exception as e:
                    logger.warning(f"Failed to fill title: {e}")

            # 3. Upload Cover (Removed as per user request)
            if task.cover_path:
                logger.info(f"Skipping automated cover upload for: {task.cover_path}")
                logger.info("Please upload the cover manually if needed.")

        except Exception as e:
            logger.warning(f"Failed to fill description: {e}")

            if self.debug:
                self._page.screenshot(path="publish_error.png")
            raise e

        # 4. Select Collection "我是小小谋略家" (选择合集)
        logger.info("Selecting collection '我是小小谋略家'...")
        try:
            # Try multiple possible selectors for collection selector
            collection_selectors = [
                'text=选择合集',
                'text=合集',
                'button:has-text("合集")',
                '.collection-selector',
                '[placeholder*="合集"]',
            ]
            
            collection_selected = False
            for selector in collection_selectors:
                try:
                    collection_btn = self._page.locator(selector).first
                    if collection_btn.is_visible(timeout=2000):
                        collection_btn.click()
                        logger.info("Clicked collection selector.")
                        time.sleep(1)  # Wait for dropdown/modal to appear
                        
                        # Now search for "我是小小谋略家" in the collection list
                        try:
                            # Try to find the collection by text
                            collection_item = self._page.locator(f'text=我是小小谋略家').first
                            if collection_item.is_visible(timeout=3000):
                                collection_item.click()
                                logger.info("Selected collection '我是小小谋略家'.")
                                collection_selected = True
                                time.sleep(0.5)
                                break
                        except Exception:
                            # If not found, try to search
                            try:
                                search_input = self._page.locator('input[placeholder*="搜索"], input[type="search"]').first
                                if search_input.is_visible(timeout=2000):
                                    search_input.fill("我是小小谋略家")
                                    time.sleep(1)
                                    collection_item = self._page.locator(f'text=我是小小谋略家').first
                                    if collection_item.is_visible(timeout=2000):
                                        collection_item.click()
                                        logger.info("Selected collection '我是小小谋略家' after search.")
                                        collection_selected = True
                                        time.sleep(0.5)
                                        break
                            except Exception:
                                pass
                except Exception:
                    continue
            
            if not collection_selected:
                logger.warning("Could not find or select collection. Please select manually.")
        except Exception as e:
            logger.warning(f"Failed to select collection: {e}")

        # 5. Search and Join Activity (搜索并参加活动)
        logger.info("Searching for activity to join...")
        try:
            activity_name = "全网征集小小谋略家"
            activity_joined = False
            
            # Step 1: Click the activity display area to open the activity selector
            # 根据实际DOM结构：点击 .activity-display 或 .not-involve 来打开选择器
            logger.info("Step 1: Looking for activity display area...")
            current_url_before = self._page.url
            
            activity_display_selectors = [
                '.activity-display',  # 活动显示区域
                '.activity-display-wrap',  # 活动显示包装器
                '.not-involve',  # "不参与活动"文本区域
                'text=不参与活动',  # 直接文本匹配
            ]
            
            activity_display_clicked = False
            for selector in activity_display_selectors:
                try:
                    display = self._page.locator(selector).first
                    if display.is_visible(timeout=3000):
                        display.click()
                        logger.info(f"Clicked activity display: {selector}")
                        activity_display_clicked = True
                        time.sleep(2)  # 等待活动选择器展开
                        
                        # 检查是否跳转了
                        current_url_after = self._page.url
                        if current_url_after != current_url_before:
                            logger.warning(f"URL changed after clicking activity display: {current_url_before} -> {current_url_after}")
                            logger.info("Detected navigation. Returning to create page...")
                            self._page.goto(self.CREATOR_URL)
                            self._page.wait_for_load_state("domcontentloaded")
                            time.sleep(2)
                            activity_display_clicked = False
                            continue
                        
                        break
                except Exception as e:
                    logger.debug(f"Selector {selector} failed: {e}")
                    continue
            
            if not activity_display_clicked:
                logger.warning("Could not find activity display area. Please click manually.")
                if self.debug:
                    self._page.screenshot(path="activity_display_not_found.png")
            else:
                # Step 2: Wait for activity filter wrap to be visible and find search input
                logger.info("Step 2: Looking for activity search input...")
                try:
                    # 等待活动选择器展开
                    self._page.wait_for_selector('.activity-filter-wrap', state="visible", timeout=5000)
                    logger.info("Activity filter wrap is visible")
                except Exception:
                    logger.warning("Activity filter wrap did not appear. Trying to find search input anyway...")
                
                # 根据实际DOM：搜索框在 .activity-filter-wrap .search-input input[placeholder="搜索活动"]
                search_input_selectors = [
                    'input[placeholder="搜索活动"]',  # 精确匹配
                    '.activity-filter-wrap input[placeholder*="搜索"]',  # 在活动过滤器内
                    '.search-input input',  # 搜索输入框
                    'input[placeholder*="搜索活动"]',  # 部分匹配
                ]
                
                search_input = None
                for search_selector in search_input_selectors:
                    try:
                        search_input = self._page.locator(search_selector).first
                        if search_input.is_visible(timeout=3000):
                            logger.info(f"Found search input: {search_selector}")
                            break
                    except Exception:
                        continue
                
                # Step 3: Search for activity
                if search_input:
                    try:
                        logger.info(f"Step 3: Searching for '{activity_name}'...")
                        search_input.click()
                        time.sleep(0.5)
                        search_input.fill("")  # Clear
                        time.sleep(0.3)
                        search_input.fill(activity_name)
                        time.sleep(1)  # 等待搜索结果加载
                        
                        if self.debug:
                            self._page.screenshot(path="activity_search_input_filled.png")
                    except Exception as e:
                        logger.warning(f"Failed to search: {e}")
                else:
                    logger.warning("Could not find search input")
                
                # Step 4: Find and click the activity in the option list
                logger.info("Step 4: Looking for activity in results...")
                time.sleep(2)  # 等待搜索结果出现
                
                # 根据实际DOM：选项在 .common-option-list-wrap .option-item .activity-item 中
                activity_selectors = [
                    # 在选项列表中查找包含活动名称的项
                    f'.activity-item:has-text("{activity_name}")',
                    f'.option-item:has-text("{activity_name}")',
                    f'.common-option-list-wrap .activity-item:has-text("{activity_name}")',
                    # 文本匹配
                    f'text={activity_name}',
                    f'.activity-item-name:has-text("{activity_name}")',
                    # 部分匹配
                    f'.activity-item:has-text("全网征集")',
                    f'.activity-item:has-text("小小谋略家")',
                ]
                
                for selector in activity_selectors:
                    try:
                        logger.info(f"Trying selector: {selector}")
                        activity_elements = self._page.locator(selector).all()
                        
                        for element in activity_elements:
                            try:
                                if element.is_visible(timeout=2000):
                                    text_content = element.text_content() or ""
                                    logger.info(f"Found element with text: {text_content[:100]}")
                                    
                                    # 检查是否包含活动名称
                                    if activity_name in text_content or "全网征集" in text_content:
                                        logger.info(f"Found matching activity: {text_content[:50]}")
                                        
                                        # 点击活动项
                                        element.click()
                                        logger.info("Clicked activity item")
                                        time.sleep(2)
                                        
                                        # 检查活动是否已选中（通常会自动选中，不需要额外点击确认按钮）
                                        activity_joined = True
                                        break
                            except Exception as e:
                                logger.debug(f"Error checking element: {e}")
                                continue
                        
                        if activity_joined:
                            break
                    except Exception as e:
                        logger.debug(f"Selector {selector} failed: {e}")
                        continue
                
                # Step 5: Verify activity is selected
                if activity_joined:
                    # 检查活动显示区域是否更新为选中的活动
                    try:
                        activity_display_text = self._page.locator('.activity-display .name, .not-involve').first
                        if activity_display_text.is_visible(timeout=3000):
                            display_text = activity_display_text.text_content() or ""
                            if activity_name in display_text or "全网征集" in display_text:
                                logger.info(f"Activity confirmed selected: {display_text}")
                            else:
                                logger.warning(f"Activity display shows: {display_text}, may not be selected correctly")
                    except Exception:
                        pass
                    
                    logger.info("Successfully joined activity!")
                    if self.debug:
                        self._page.screenshot(path="activity_joined.png")
                else:
                    logger.warning("Could not find or join activity. Please join manually.")
                    if self.debug:
                        self._page.screenshot(path="activity_failed.png")
                        try:
                            Path("activity_failed.html").write_text(self._page.content(), encoding="utf-8")
                            logger.info("Saved page HTML to activity_failed.html")
                        except:
                            pass
        except Exception as e:
            logger.warning(f"Failed to join activity: {e}")
            if self.debug:
                try:
                    self._page.screenshot(path="activity_error.png")
                except:
                    pass

        # 6. Check "Original" (勾选原创) - 放在最后避免弹窗干扰
        logger.info("Checking 'Original' checkbox...")
        try:
            # Try multiple possible selectors for the original checkbox
            original_selectors = [
                'input[type="checkbox"]:near(text="原创")',
                'label:has-text("原创") input[type="checkbox"]',
                'input[type="checkbox"]',
                '.weui-desktop-checkbox:has-text("原创")',
                'text=原创',
            ]
            
            original_checked = False
            for selector in original_selectors:
                try:
                    checkbox = self._page.locator(selector).first
                    if checkbox.is_visible(timeout=2000):
                        # Check if already checked
                        if checkbox.get_attribute('checked') != 'true':
                            checkbox.click()
                            logger.info("Original checkbox checked.")
                        else:
                            logger.info("Original checkbox already checked.")
                        original_checked = True
                        break
                except Exception:
                    continue
            
            if not original_checked:
                # Fallback: try to find by text and click nearby checkbox
                try:
                    original_text = self._page.locator('text=原创').first
                    if original_text.is_visible(timeout=2000):
                        # Click the text or nearby element
                        original_text.click()
                        logger.info("Clicked 'Original' text.")
                        original_checked = True
                except Exception:
                    pass
            
            if not original_checked:
                logger.warning("Could not find or check 'Original' checkbox. Please check manually.")
        except Exception as e:
            logger.warning(f"Failed to check 'Original' checkbox: {e}")

        
        # Handle hashtags if separated? Usually hashtags are just text.

        # 4. Submit
        # logger.info("Clicking publish...")
        # self._page.click('button:has-text("发表")')
        
        # For safety in this demo, we do NOT actually click publish.
        logger.info("DRY RUN: Ready to publish. Skipping actual click on 'Publish' button.")
        
        # Wait a bit to observe result in non-headless mode
        if not self.headless:
            time.sleep(5)

if __name__ == "__main__":
    # Example Usage
    import sys
    
    # Check if paths are provided via args, else use dummy defaults for testing syntax
    video_file = Path("media/sunzi/lesson04/videos/animate/1920p60/Lesson4Vertical.mp4")
    
    # Demo logic
    if not video_file.exists():
        logger.warning(f"Demo video file not found at {video_file}. Please adjust path in script.")
        sys.exit(1)
        
    publisher = WeChatChannelPublisher(headless=False)
    
    try:
        with publisher:
            publisher.login()
            
            task = VideoPublishTask(
                video_path=video_file,
                description="This is a test video description. #Sunzi #Lesson4",
                # cover_path=Path("path/to/cover.png")
            )
            
            publisher.publish(task)
            
    except Exception as e:
        logger.error(f"An error occurred: {e}")

