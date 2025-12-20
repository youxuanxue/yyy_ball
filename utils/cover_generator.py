import os
import base64
from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright

def generate_cover(
    output_path: str,
    title_main: str,
    title_sub: str,
    tag_left: str,
    tag_right: str,
    main_image_path: str,
    bg_image_path: str = None,
    footer_text: str = "孙子兵法 · 谋攻篇"
):
    """
    Generate a video cover image using HTML/CSS and Playwright.
    
    Args:
        output_path: Path to save the generated image.
        title_main: Main title.
        title_sub: Subtitle.
        tag_left: Left tag text.
        tag_right: Right tag text.
        main_image_path: Absolute path to the main subject image (foreground).
        bg_image_path: Absolute path to the background texture image. Defaults to main_image_path if None.
        footer_text: Footer text.
    """
    # 0. Default bg to main if not provided
    if bg_image_path is None:
        bg_image_path = main_image_path

    # 1. Setup paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir, "templates")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    # 2. Convert images to Base64
    def get_b64_src(path):
        with open(path, "rb") as img_file:
            b64_data = base64.b64encode(img_file.read()).decode("utf-8")
            ext = os.path.splitext(path)[1].lower()
            mime_type = "image/png" if ext == ".png" else "image/jpeg"
            return f"data:{mime_type};base64,{b64_data}"

    main_img_src = get_b64_src(main_image_path)
    bg_img_src = get_b64_src(bg_image_path)

    # 3. Render HTML with Jinja2
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("cover_template.html")
    
    # Auto-scale font size based on title length
    # Base: 150px for 6 chars (~900px width)
    # 1080px width limit.
    char_count = len(title_main)
    if char_count <= 6:
        font_size = 150
    elif char_count == 7:
        font_size = 130
    elif char_count == 8:
        font_size = 115
    else:
        font_size = 100

    html_content = template.render(
        title_main=title_main,
        title_sub=title_sub,
        tag_left=tag_left,
        tag_right=tag_right,
        main_image_path=main_img_src,
        bg_image_path=bg_img_src,
        footer_text=footer_text,
        title_font_size=font_size
    )
    
    # 4. Use Playwright to screenshot
    with sync_playwright() as p:
        # Launch browser (chromium is fine)
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1080, "height": 1920})
        
        # Load the HTML content directly
        page.set_content(html_content)
        
        # Ensure image is loaded before screenshot
        # Since we use Base64, it should be instant, but waiting for naturalHeight check is safe.
        try:
            page.wait_for_function("""
                () => {
                    const imgs = Array.from(document.querySelectorAll('img'));
                    return imgs.every(img => img.complete && img.naturalHeight > 0);
                }
            """, timeout=5000) # 5s timeout should be enough for base64
        except Exception as e:
            print(f"Warning: Image load wait timed out or failed: {e}")
        
        # Select the canvas element to screenshot exactly that area
        element = page.locator(".canvas")
        
        # Take screenshot
        element.screenshot(path=output_path, type="png")
        
        browser.close()
        
    print(f"Cover generated at: {output_path}")

if __name__ == "__main__":
    # Test run
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_img = os.path.abspath(os.path.join(base_dir, "../series/sunzi/images/1.jpg"))
    generate_cover(
        output_path="test_cover.png",
        title_main="是不打架？",
        title_sub="最好的胜利",
        tag_left="打架",
        tag_right="智慧",
        main_image_path=test_img,
        bg_image_path=test_img # Use same for test
    )
