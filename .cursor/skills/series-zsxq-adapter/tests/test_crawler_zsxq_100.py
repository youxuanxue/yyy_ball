import os
import sys
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import crawler_zsxq_100 as crawler


class TestCrawlerZsxq100(unittest.TestCase):
    def test_output_paths_stay_under_workspace_assets(self):
        self.assertEqual(crawler.OUTPUT_DIR, crawler.WORKSPACE_ROOT / "assets" / "zsxq")
        self.assertEqual(crawler.OUTPUT_FILE, crawler.OUTPUT_DIR / "jingpin_100ke_posts.json")
        self.assertEqual(crawler.RAW_OUTPUT_FILE, crawler.OUTPUT_DIR / "jingpin_100ke_posts_raw.json")

    def test_build_cookies_requires_token(self):
        old = os.environ.pop("ZSXQ_ACCESS_TOKEN", None)
        try:
            with self.assertRaises(RuntimeError):
                crawler.build_cookies()
        finally:
            if old is not None:
                os.environ["ZSXQ_ACCESS_TOKEN"] = old

    def test_extract_content_keeps_core_fields(self):
        topic = {
            "topic_id": "123",
            "create_time": "2024-01-01T00:00:00.000+0800",
            "type": "talk",
            "owner": {"name": "demo", "user_id": "u1"},
            "talk": {
                "text": "第001课：现金流",
                "images": [{"image_id": "img-1", "large": {"url": "https://example.com/large.png"}}],
                "files": [{"file_id": "f-1", "name": "notes.pdf", "size": 128, "download_url": "https://example.com/file"}],
            },
            "likes_count": 8,
            "comments_count": 3,
            "rewards_count": 1,
            "reading_count": 99,
        }

        extracted = crawler.extract_content(topic)

        self.assertEqual(extracted["topic_id"], "123")
        self.assertEqual(extracted["author"]["name"], "demo")
        self.assertEqual(extracted["text"], "第001课：现金流")
        self.assertEqual(extracted["images"][0]["url"], "https://example.com/large.png")
        self.assertEqual(extracted["files"][0]["name"], "notes.pdf")
        self.assertEqual(extracted["reading_count"], 99)


if __name__ == "__main__":
    unittest.main()
