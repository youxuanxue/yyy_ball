import sys
import os
import random

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from utils.cover_generator import generate_cover

def main():
    # Configuration for Lesson 5
    output_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../media/sunzi/lesson05/images/cover_design.png"))
    
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

    # Randomly select one
    main_image = random.choice(valid_images)
    print(f"Randomly selected image: {os.path.basename(main_image)}")
    
    print(f"Generating cover for Lesson 5...")
    
    generate_cover(
        output_path=output_file,
        title_main="谁是战场魔术师？",
        title_sub="治众如治寡",
        tag_left="造势",
        tag_right="奇正",
        main_image_path=main_image,
        footer_text="孙子兵法 · 兵势篇"
    )

if __name__ == "__main__":
    main()

