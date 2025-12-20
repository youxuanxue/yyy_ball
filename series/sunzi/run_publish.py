import sys
import argparse
import time
from pathlib import Path

# Add project root to sys.path to allow importing from 'publish'
# This script is in series/sunzi/, so root is ../../
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from publish import WeChatChannelPublisher, VideoPublishTask

def main():
    parser = argparse.ArgumentParser(description="Publish Sunzi lesson video to WeChat Channel.")
    parser.add_argument("lesson", help="Lesson directory name (e.g., lesson03, lesson04)")
    args = parser.parse_args()

    lesson_dir_name = args.lesson
    
    # Base directory for this script (series/sunzi)
    script_dir = Path(__file__).parent
    
    # Path to the specific lesson in series/sunzi (for description)
    lesson_source_dir = script_dir / lesson_dir_name
    
    # Path to the specific lesson in media/sunzi (for video/cover)
    # media is at project_root/media
    media_lesson_dir = project_root / "media/sunzi" / lesson_dir_name
    
    if not lesson_source_dir.exists():
        print(f"Lesson source directory not found: {lesson_source_dir}")
        return
        
    if not media_lesson_dir.exists():
        print(f"Media lesson directory not found: {media_lesson_dir}")
        return

    # 1. Find Video File
    # Expected path: media/sunzi/{lesson}/videos/animate/1920p60/*.mp4
    video_dir = media_lesson_dir / "videos/animate/1920p60"
    if not video_dir.exists():
        print(f"Video directory not found: {video_dir}")
        return
        
    # Find any mp4 file, preferably one ending with Vertical.mp4
    video_files = list(video_dir.glob("*Vertical.mp4"))
    if not video_files:
        video_files = list(video_dir.glob("*.mp4"))
    
    if not video_files:
        print(f"No video files found in {video_dir}")
        return
        
    video_path = video_files[0]
    print(f"Found video: {video_path}")

    # 2. Find Cover File
    cover_path = media_lesson_dir / "images/cover_design.png"
    if not cover_path.exists():
        print(f"Cover file not found: {cover_path}")
        # Proceed without cover?
    else:
        print(f"Found cover: {cover_path}")

    # 3. Read Description
    desc_path = lesson_source_dir / "social_media.md"
    title = ""
    description = ""
    
    if not desc_path.exists():
        print(f"Description file not found: {desc_path}")
        title = f"孙子兵法 {lesson_dir_name}"
        description = "这是测试文案 #孙子兵法 #自动化发布"
    else:
        full_text = desc_path.read_text(encoding="utf-8")
        lines = full_text.strip().split('\n')
        if lines:
            title = lines[0].strip()
            # WeChat Channel short title limit is 16 characters
            if len(title) > 16:
                print(f"Warning: Title '{title}' is longer than 16 characters. Truncating.")
                title = title[:16]
            
            description = "\n".join(lines[1:]).strip()
        else:
             title = "未命名视频"
             description = full_text

    # 4. Initialize and Run Publisher
    # We point auth_path to project root to reuse existing auth_wx.json
    auth_path = project_root 
    
    try:
        with WeChatChannelPublisher(headless=False, auth_path=str(auth_path)) as publisher:
            # Login check
            publisher.login()
            
            # Create task
            task = VideoPublishTask(
                video_path=video_path,
                title=title,
                description=description,
                cover_path=cover_path if cover_path.exists() else None
            )
            
            # Publish
            publisher.publish(task)
            
            print("脚本执行完毕，请检查浏览器窗口。")
            
            # Wait for user confirmation
            try:
                print("请在浏览器中确认发布信息。完成后按回车键关闭浏览器...")
                input()
            except EOFError:
                print("检测到非交互式环境，脚本将保持浏览器打开 5 分钟，然后自动关闭。")
                time.sleep(300)

    except Exception as e:
        print(f"发布过程中出错: {e}")

if __name__ == "__main__":
    main()

