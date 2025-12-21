import sys
import argparse
import time
import json
from pathlib import Path

# Add project root to sys.path
# This script is in src/publish/, so root is ../../
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.publish.wx_channel import WeChatChannelPublisher, VideoPublishTask

def main():
    parser = argparse.ArgumentParser(description="Publish lesson video to WeChat Channel.")
    parser.add_argument("lesson_path", help="Lesson path (e.g., sunzi/lesson05, sunzi/lesson06)")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode (generate screenshots and HTML dumps)")
    args = parser.parse_args()

    # Parse lesson path: sunzi/lesson0x -> series/sunzi/lesson0x
    lesson_path_str = args.lesson_path.strip()
    parts = lesson_path_str.split('/')
    
    if len(parts) != 2:
        print(f"Invalid lesson path format. Expected: sunzi/lesson0x, got: {lesson_path_str}")
        return
    
    series_name, lesson_dir_name = parts
    
    # Build path to lesson directory: series/{series_name}/{lesson_dir_name}
    lesson_source_dir = project_root / "series" / series_name / lesson_dir_name
    
    if not lesson_source_dir.exists():
        print(f"Lesson source directory not found: {lesson_source_dir}")
        return

    # Media directory is inside the lesson directory
    lesson_media_dir = lesson_source_dir / "media"
    
    if not lesson_media_dir.exists():
        print(f"Media directory not found: {lesson_media_dir}")
        return

    # 1. Find Video File
    # Try multiple possible locations within lesson/media/videos
    video_path = None
    
    # Try the nested path: lesson/media/videos/animate/1920p60/*.mp4
    video_dir = lesson_media_dir / "videos/animate/1920p60"
    if video_dir.exists():
        # Find any mp4 file, preferably one ending with Vertical.mp4
        video_files = list(video_dir.glob("*Vertical.mp4"))
        if not video_files:
            video_files = list(video_dir.glob("*.mp4"))
        
        if video_files:
            video_path = video_files[0]
            print(f"Found video: {video_path}")
    
    if not video_path:
        print(f"No video files found. Tried:")
        print(f"  - {lesson_media_dir / 'videos/animate/1920p60/*.mp4'}")
        return

    # 2. Read Title, Description, and Hashtags from script.json
    script_json_path = lesson_source_dir / "script.json"
    title = ""
    description = ""
    
    if not script_json_path.exists():
        print(f"Error: script.json not found at {script_json_path}")
        print("Please ensure script.json exists with a 'wechat' field containing 'title' and 'description'.")
        return
    
    try:
        with open(script_json_path, 'r', encoding='utf-8') as f:
            script_data = json.load(f)
        
        if 'wechat' not in script_data:
            print(f"Error: 'wechat' field not found in script.json")
            print("Please ensure script.json contains a 'wechat' field with 'title' and 'description'.")
            return
        
        wechat_data = script_data['wechat']
        
        # Get title
        title = wechat_data.get('title', '')
        if not title:
            print(f"Error: 'title' not found in script.json wechat field")
            return
        
        # WeChat Channel short title limit is 16 characters
        if len(title) > 16:
            print(f"Warning: Title '{title}' is longer than 16 characters. Truncating.")
            title = title[:16]
        
        # Get description
        description = wechat_data.get('description', '').strip()
        if not description:
            print(f"Error: 'description' not found or empty in script.json wechat field")
            return
        
        # Get hashtags and append to description
        hashtags = wechat_data.get('hashtags', [])
        if hashtags:
            hashtags_str = ' '.join(hashtags)
            # Append hashtags to description if not already present
            if hashtags_str not in description:
                description = f"{description}\n\n{hashtags_str}"
        
        print(f"Loaded metadata from script.json wechat field")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in script.json: {e}")
        return
    except Exception as e:
        print(f"Error reading script.json: {e}")
        return

    # 3. Initialize and Run Publisher
    # We point auth_path to project root to reuse existing auth_wx.json
    auth_path = project_root 
    
    try:
        with WeChatChannelPublisher(headless=False, auth_path=str(auth_path), debug=args.debug) as publisher:
            # Login check
            publisher.login()
            
            # Create task
            task = VideoPublishTask(
                video_path=video_path,
                title=title,
                description=description,
                cover_path=None
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

