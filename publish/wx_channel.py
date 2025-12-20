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
    AUTH_FILE = "auth_wx.json"

    def __init__(self, headless: bool = False, auth_path: str = "."):
        """
        Initialize the publisher.

        Args:
            headless: Whether to run the browser in headless mode. 
                      Defaults to False for visibility during potential manual login.
            auth_path: Directory to store the authentication state file.
        """
        self.headless = headless
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
            self._page.screenshot(path="create_page_loaded.png")
            Path("create_page_debug.html").write_text(self._page.content(), encoding="utf-8")
        except Exception as e:
            logger.error(f"Navigation to create page failed: {e}")
            self._page.screenshot(path="nav_error.png")
            raise e

        # Check if we were redirected to login
        if "login" in self._page.url:
             logger.warning("Redirected to login page during publish. Session might have expired.")
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

            self._page.screenshot(path="publish_error.png")
            raise e

        
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

