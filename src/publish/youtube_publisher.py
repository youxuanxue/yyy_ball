import json
import logging
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# YouTube API 配置
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# YouTube Shorts 类别 ID (Shorts 使用类别 26 - People & Blogs，但更常用的是通过标签和视频格式识别)
# 实际上，YouTube 会自动识别竖屏视频（9:16）为 Shorts
YOUTUBE_SHORTS_CATEGORY_ID = "26"  # People & Blogs


@dataclass
class YouTubePublishTask:
    """Data class representing a YouTube video publishing task."""
    video_path: Path
    title: str
    description: str
    tags: Optional[List[str]] = None
    category_id: str = YOUTUBE_SHORTS_CATEGORY_ID
    privacy_status: str = "private"  # "public", "unlisted", "private"
    made_for_kids: bool = False
    playlist_title: Optional[str] = None  # Playlist title to add video to

    def validate(self):
        """Validates that the necessary files exist."""
        if not self.video_path.exists():
            raise FileNotFoundError(f"Video file not found: {self.video_path}")
        if not self.title:
            raise ValueError("Title is required")
        if not self.description:
            raise ValueError("Description is required")


class YouTubePublisher:
    """
    Automates publishing videos to YouTube Shorts using YouTube Data API v3.
    """
    
    def __init__(self, credentials_path: str = "config/youtube_credentials.json", 
                 token_path: str = "config/youtube_token.json"):
        """
        Initialize the YouTube publisher.

        Args:
            credentials_path: Path to OAuth2 credentials JSON file (from Google Cloud Console).
            token_path: Path to store/load OAuth2 token.
        """
        self.credentials_path = Path(credentials_path)
        self.token_path = Path(token_path)
        self.credentials: Optional[Credentials] = None
        self.youtube = None

    def authenticate(self):
        """
        Authenticate with YouTube API using OAuth2.
        If token exists and is valid, use it. Otherwise, run OAuth flow.
        """
        creds = None
        
        # Load existing token if available
        if self.token_path.exists():
            try:
                creds = Credentials.from_authorized_user_file(str(self.token_path), SCOPES)
                logger.info("Loaded existing credentials from token file")
            except Exception as e:
                logger.warning(f"Failed to load credentials from token file: {e}")

        # If there are no (valid) credentials available, let the user log in
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                logger.info("Refreshing expired credentials...")
                try:
                    creds.refresh(Request())
                except Exception as e:
                    logger.error(f"Failed to refresh credentials: {e}")
                    creds = None

            if not creds:
                if not self.credentials_path.exists():
                    raise FileNotFoundError(
                        f"Credentials file not found: {self.credentials_path}\n"
                        "Please download OAuth2 credentials from Google Cloud Console:\n"
                        "1. Go to https://console.cloud.google.com/\n"
                        "2. Create/select a project\n"
                        "3. Enable YouTube Data API v3\n"
                        "4. Create OAuth 2.0 credentials (Desktop app)\n"
                        "5. IMPORTANT: Add authorized redirect URI: http://localhost:8080/\n"
                        "   (Go to OAuth 2.0 Client IDs > Edit > Authorized redirect URIs)\n"
                        "6. Download and save as config/youtube_credentials.json"
                    )
                
                logger.info("Starting OAuth2 flow...")
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(self.credentials_path), SCOPES)
                # Use fixed port 8080 - make sure to add http://localhost:8080/ 
                # as authorized redirect URI in Google Cloud Console
                try:
                    creds = flow.run_local_server(port=8080, open_browser=True)
                except OSError as e:
                    if "Address already in use" in str(e):
                        logger.warning(f"Port 8080 is already in use. Trying random port...")
                        logger.warning("Note: If you get redirect_uri_mismatch error, you need to:")
                        logger.warning("1. Check the port number shown in the authorization URL")
                        logger.warning("2. Add http://localhost:<port>/ to authorized redirect URIs in Google Cloud Console")
                        creds = flow.run_local_server(port=0, open_browser=True)
                    else:
                        raise
                except Exception as e:
                    error_str = str(e)
                    if "redirect_uri_mismatch" in error_str.lower() or "400" in error_str:
                        raise RuntimeError(
                            "OAuth redirect_uri_mismatch 错误！\n"
                            "解决方法：\n"
                            "1. 访问 Google Cloud Console: https://console.cloud.google.com/\n"
                            "2. 进入 APIs & Services > Credentials\n"
                            "3. 点击你的 OAuth 2.0 客户端 ID\n"
                            "4. 在 '已授权的重定向 URI' 中添加: http://localhost:8080/\n"
                            "5. 保存更改后重新运行脚本\n"
                            f"\n原始错误: {error_str}"
                        ) from e
                    raise
                logger.info("OAuth2 authentication successful")

            # Save the credentials for the next run
            self.token_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.token_path, 'w') as token:
                token.write(creds.to_json())
            logger.info(f"Saved credentials to {self.token_path}")

        self.credentials = creds
        self.youtube = build(API_SERVICE_NAME, API_VERSION, credentials=creds)
        logger.info("YouTube API client initialized")

    def find_or_create_playlist(self, playlist_title: str) -> str:
        """
        Find a playlist by title, or create it if it doesn't exist.
        
        Args:
            playlist_title: Title of the playlist
            
        Returns:
            Playlist ID
        """
        if not self.youtube:
            raise RuntimeError("Not authenticated. Call authenticate() first.")
        
        try:
            # Search for existing playlist
            logger.info(f"Searching for playlist: {playlist_title}")
            request = self.youtube.playlists().list(
                part="snippet",
                mine=True,
                maxResults=50
            )
            response = request.execute()
            
            # Check if playlist exists
            for item in response.get('items', []):
                if item['snippet']['title'] == playlist_title:
                    playlist_id = item['id']
                    logger.info(f"Found existing playlist: {playlist_title} (ID: {playlist_id})")
                    return playlist_id
            
            # Create new playlist if not found
            logger.info(f"Playlist not found. Creating new playlist: {playlist_title}")
            request = self.youtube.playlists().insert(
                part="snippet,status",
                body={
                    'snippet': {
                        'title': playlist_title,
                        'description': f'自动创建的播放列表: {playlist_title}',
                    },
                    'status': {
                        'privacyStatus': 'public'
                    }
                }
            )
            response = request.execute()
            playlist_id = response['id']
            logger.info(f"Created new playlist: {playlist_title} (ID: {playlist_id})")
            return playlist_id
            
        except HttpError as e:
            logger.error(f"Failed to find/create playlist: {e}")
            raise

    def add_video_to_playlist(self, video_id: str, playlist_id: str):
        """
        Add a video to a playlist.
        
        Args:
            video_id: YouTube video ID
            playlist_id: YouTube playlist ID
        """
        if not self.youtube:
            raise RuntimeError("Not authenticated. Call authenticate() first.")
        
        try:
            logger.info(f"Adding video {video_id} to playlist {playlist_id}")
            request = self.youtube.playlistItems().insert(
                part="snippet",
                body={
                    'snippet': {
                        'playlistId': playlist_id,
                        'resourceId': {
                            'kind': 'youtube#video',
                            'videoId': video_id
                        }
                    }
                }
            )
            response = request.execute()
            logger.info(f"Successfully added video to playlist")
            
        except HttpError as e:
            logger.error(f"Failed to add video to playlist: {e}")
            raise

    def publish(self, task: YouTubePublishTask):
        """
        Upload video to YouTube as a Short.

        Args:
            task: YouTube publishing task containing file paths and metadata.
        """
        task.validate()

        if not self.youtube:
            raise RuntimeError("Not authenticated. Call authenticate() first.")

        try:
            logger.info(f"Uploading video: {task.video_path}")
            
            # Prepare video metadata
            body = {
                'snippet': {
                    'title': task.title,
                    'description': task.description,
                    'tags': task.tags or [],
                    'categoryId': task.category_id,
                },
                'status': {
                    'privacyStatus': task.privacy_status,
                    'selfDeclaredMadeForKids': task.made_for_kids,
                }
            }

            # Create media upload object
            media = MediaFileUpload(
                str(task.video_path),
                chunksize=-1,
                resumable=True,
                mimetype='video/*'
            )

            # Insert video
            insert_request = self.youtube.videos().insert(
                part=','.join(body.keys()),
                body=body,
                media_body=media
            )

            # Execute upload with progress tracking
            response = None
            error = None
            retry = 0
            while response is None:
                try:
                    logger.info("Uploading file...")
                    status, response = insert_request.next_chunk()
                    if response is not None:
                        if 'id' in response:
                            video_id = response['id']
                            video_url = f"https://www.youtube.com/watch?v={video_id}"
                            logger.info(f"✅ Video uploaded successfully!")
                            logger.info(f"Video ID: {video_id}")
                            logger.info(f"Video URL: {video_url}")
                            
                            # Add to playlist if specified
                            if task.playlist_title:
                                try:
                                    playlist_id = self.find_or_create_playlist(task.playlist_title)
                                    self.add_video_to_playlist(video_id, playlist_id)
                                    logger.info(f"✅ Added video to playlist: {task.playlist_title}")
                                except Exception as e:
                                    logger.warning(f"Failed to add video to playlist: {e}")
                                    # Don't fail the entire upload if playlist operation fails
                            
                            return video_id, video_url
                        else:
                            raise Exception(f"Upload failed: {response}")
                except HttpError as e:
                    if e.resp.status in [500, 502, 503, 504]:
                        error = f"A retriable HTTP error {e.resp.status} occurred:\n{e.content}"
                        logger.warning(error)
                        retry += 1
                        if retry > 3:
                            raise Exception(f"Upload failed after {retry} retries: {error}")
                    else:
                        raise Exception(f"An HTTP error {e.resp.status} occurred:\n{e.content}")

        except HttpError as e:
            logger.error(f"An HTTP error {e.resp.status} occurred:\n{e.content}")
            raise
        except Exception as e:
            logger.error(f"An error occurred during upload: {e}")
            raise

    def __enter__(self):
        self.authenticate()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # No cleanup needed for YouTube API client
        pass


if __name__ == "__main__":
    # Example usage
    import sys
    
    video_file = Path("test_video.mp4")
    if not video_file.exists():
        logger.warning(f"Demo video file not found at {video_file}")
        sys.exit(1)
    
    publisher = YouTubePublisher()
    
    try:
        with publisher:
            task = YouTubePublishTask(
                video_path=video_file,
                title="Test YouTube Short",
                description="This is a test video description.\n\n#Test #Shorts",
                tags=["test", "shorts"],
                privacy_status="private"  # Start with private for testing
            )
            
            video_id, video_url = publisher.publish(task)
            print(f"Video uploaded: {video_url}")
            
    except Exception as e:
        logger.error(f"An error occurred: {e}")
