import sys
import os
import random

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from utils.cover_generator import generate_cover

def main():
    # Configuration for Lesson 3
    output_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../media/sunzi/lesson03/images/cover_design.png"))
    
    # Image directory
    images_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../images"))
    
    # Get all valid images
    valid_images = [
        os.path.join(images_dir, f) 
        for f in os.listdir(images_dir) 
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    ]
    
    if not valid_images:
        print(f"Warning: No images found in {images_dir}")
        return

    # Randomly select one (Useful for future lessons to have variety)
    main_image = random.choice(valid_images)
    print(f"Randomly selected image: {os.path.basename(main_image)}")
    
    # Option: Manually override for specific lesson (e.g. Lesson 3 uses 4.jpg)
    # main_image = os.path.join(images_dir, "4.jpg")

    # You can set a different background image here if you have one
    # bg_image = os.path.abspath(os.path.join(os.path.dirname(__file__), "../images/bg_texture.jpg"))
    
    print(f"Generating cover for Lesson 3...")
    
    generate_cover(
        output_path=output_file,
        title_main="是不打架？",
        title_sub="最好的胜利",
        tag_left="打架",
        tag_right="智慧",
        main_image_path=main_image,
        # bg_image_path=bg_image, # Optional: pass different background
        footer_text="孙子兵法 · 谋攻篇"
    )

if __name__ == "__main__":
    main()

