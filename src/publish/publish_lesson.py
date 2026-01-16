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
from src.publish.youtube_publisher import YouTubePublisher, YouTubePublishTask

def main():
    parser = argparse.ArgumentParser(description="Publish lesson video to WeChat Channel or YouTube Shorts.")
    parser.add_argument("lesson_path", help="Lesson path (e.g., book_sunzibingfa/lesson05, book_sunzibingfa/lesson06)")
    parser.add_argument("--platform", choices=["wechat", "youtube", "both"], default="wechat",
                        help="Platform to publish to (default: wechat)")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode (generate screenshots and HTML dumps)")
    parser.add_argument("--privacy", choices=["public", "unlisted", "private"], default="private",
                        help="YouTube video privacy status (default: private)")
    args = parser.parse_args()

    # Parse lesson path: book_sunzibingfa/lesson0x -> series/book_sunzibingfa/lesson0x
    lesson_path_str = args.lesson_path.strip()
    parts = lesson_path_str.split('/')
    
    if len(parts) != 2:
        print(f"Invalid lesson path format. Expected: book_sunzibingfa/lesson0x, got: {lesson_path_str}")
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
    
    if not script_json_path.exists():
        print(f"Error: script.json not found at {script_json_path}")
        print("Please ensure script.json exists with platform-specific fields (e.g., 'wechat' or 'youtube').")
        return
    
    try:
        with open(script_json_path, 'r', encoding='utf-8') as f:
            script_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in script.json: {e}")
        return
    except Exception as e:
        print(f"Error reading script.json: {e}")
        return
    
    # Extract metadata for each platform
    wechat_title = ""
    wechat_description = ""
    youtube_title = ""
    youtube_description = ""
    youtube_tags = []
    youtube_playlist = None
    
    # Get WeChat metadata
    publish_wechat = args.platform in ["wechat", "both"]
    publish_youtube = args.platform in ["youtube", "both"]
    
    if publish_wechat:
        if 'wechat' not in script_data:
            print(f"Warning: 'wechat' field not found in script.json")
            print("Skipping WeChat publishing.")
            publish_wechat = False
        else:
            wechat_data = script_data['wechat']
            wechat_title = wechat_data.get('title', '')
            if not wechat_title:
                print(f"Error: 'title' not found in script.json wechat field")
                return
            
            # WeChat Channel short title limit is 16 characters
            if len(wechat_title) > 16:
                print(f"Warning: Title '{wechat_title}' is longer than 16 characters. Truncating.")
                wechat_title = wechat_title[:16]
            
            wechat_description = wechat_data.get('description', '').strip()
            if not wechat_description:
                print(f"Error: 'description' not found or empty in script.json wechat field")
                return
            
            # Get hashtags and append to description
            hashtags = wechat_data.get('hashtags', [])
            if hashtags:
                hashtags_str = ' '.join(hashtags)
                if hashtags_str not in wechat_description:
                    wechat_description = f"{wechat_description}\n\n{hashtags_str}"
            
            print(f"Loaded WeChat metadata from script.json")
    
    # Get YouTube metadata
    if publish_youtube:
        if 'youtube' in script_data:
            youtube_data = script_data['youtube']
            youtube_title = youtube_data.get('title', '')
            youtube_description = youtube_data.get('description', '').strip()
            youtube_tags = youtube_data.get('tags', [])
            youtube_playlist = youtube_data.get('playlists', None)
            print(f"Loaded YouTube metadata from script.json youtube field")
            if youtube_playlist:
                print(f"将添加到播放列表: {youtube_playlist}")
        else:
            # Fallback to wechat data if youtube field doesn't exist
            print(f"Warning: 'youtube' field not found in script.json, using 'wechat' data as fallback")
            if 'wechat' in script_data:
                wechat_data = script_data['wechat']
                youtube_title = wechat_data.get('title', '')
                youtube_description = wechat_data.get('description', '').strip()
                # Convert hashtags to tags (remove #)
                hashtags = wechat_data.get('hashtags', [])
                youtube_tags = [tag.replace('#', '') for tag in hashtags if tag.startswith('#')]
            else:
                print(f"Error: No metadata found for YouTube publishing")
                return
        
        if not youtube_title:
            print(f"Error: YouTube title is required")
            return
        if not youtube_description:
            print(f"Warning: YouTube description is empty")

    # 3. Publish to selected platform(s)
    auth_path = project_root
    
    # Publish to WeChat
    if publish_wechat:
        print("\n" + "="*50)
        print("发布到微信视频号")
        print("="*50)
        try:
            with WeChatChannelPublisher(headless=False, auth_path=str(auth_path), debug=args.debug) as publisher:
                # Login check
                publisher.login()
                
                # Create task
                task = VideoPublishTask(
                    video_path=video_path,
                    title=wechat_title,
                    description=wechat_description,
                    cover_path=None
                )
                
                # Publish
                publisher.publish(task)
                
                print("微信视频号发布流程完成，请检查浏览器窗口。")
                
                # Wait for user confirmation
                try:
                    print("请在浏览器中确认发布信息。完成后按回车键继续...")
                    input()
                except EOFError:
                    print("检测到非交互式环境，脚本将保持浏览器打开 5 分钟，然后自动关闭。")
                    time.sleep(300)
        except Exception as e:
            print(f"微信视频号发布过程中出错: {e}")
            if publish_youtube:
                print("继续尝试发布到 YouTube...")
    
    # Publish to YouTube
    if publish_youtube:
        print("\n" + "="*50)
        print("发布到 YouTube Shorts")
        print("="*50)
        try:
            credentials_path = project_root / "config" / "youtube_credentials.json"
            token_path = project_root / "config" / "youtube_token.json"
            
            publisher = YouTubePublisher(
                credentials_path=str(credentials_path),
                token_path=str(token_path)
            )
            
            with publisher:
                # Create task
                task = YouTubePublishTask(
                    video_path=video_path,
                    title=youtube_title,
                    description=youtube_description,
                    tags=youtube_tags,
                    privacy_status=args.privacy,
                    made_for_kids=False,
                    playlist_title=youtube_playlist
                )
                
                # Publish
                video_id, video_url = publisher.publish(task)
                print(f"\n✅ YouTube Shorts 上传成功！")
                print(f"视频 ID: {video_id}")
                print(f"视频链接: {video_url}")
                print(f"隐私设置: {args.privacy}")
                print(f"\n请在 YouTube Studio 中查看和管理视频: https://studio.youtube.com/")
                
        except FileNotFoundError as e:
            print(f"❌ YouTube 认证文件未找到: {e}")
            print("\n请按照以下步骤设置 YouTube API：")
            print("1. 访问 https://console.cloud.google.com/")
            print("2. 创建或选择项目")
            print("3. 启用 YouTube Data API v3")
            print("4. 创建 OAuth 2.0 凭据（桌面应用）")
            print("5. ⚠️  重要：添加授权重定向 URI: http://localhost:8080/")
            print("   （进入 OAuth 2.0 客户端 ID > 编辑 > 已授权的重定向 URI）")
            print(f"6. 下载并保存为: {credentials_path}")
        except Exception as e:
            error_msg = str(e)
            if "redirect_uri_mismatch" in error_msg.lower() or "400" in error_msg:
                print(f"\n❌ OAuth 重定向 URI 不匹配错误")
                print("\n解决方法：")
                print("1. 访问 Google Cloud Console: https://console.cloud.google.com/")
                print("2. 进入  APIs & Services > Credentials")
                print("3. 点击你的 OAuth 2.0 客户端 ID")
                print("4. 在 '已授权的重定向 URI' 中添加: http://localhost:8080/")
                print("5. 保存更改后重新运行脚本")
                print(f"\n原始错误: {error_msg}")
            else:
                print(f"❌ YouTube 发布过程中出错: {e}")
                import traceback
                traceback.print_exc()

if __name__ == "__main__":
    main()

