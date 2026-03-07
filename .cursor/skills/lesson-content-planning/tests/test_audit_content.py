import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "audit_content.py"


def load_module():
    spec = importlib.util.spec_from_file_location("lesson_content_audit_script", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class TestAuditContent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module()

    def test_moneywise_evergreen_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            lesson_dir = root / "series" / "moneywise_global" / "lesson001"
            write_text(lesson_dir / "animate.py", "pass")
            write_text(
                lesson_dir / "script.json",
                json.dumps(
                    {
                        "meta": {"lesson_title": "2025 lesson"},
                        "seo": {},
                        "social": {},
                        "youtube": {},
                        "blog": {},
                        "icons": ["gold.png"] * 12,
                        "scenes": [{"scene_index": 1, "voiceover_script": "In 2025 this happened."}],
                    },
                    ensure_ascii=False,
                ),
            )
            original_dir = self.mod.SERIES_RULES["moneywise"]["lesson_dir"]
            with patch.object(self.mod, "WORKSPACE_ROOT", root):
                self.mod.SERIES_RULES["moneywise"]["lesson_dir"] = root / "series" / "moneywise_global"
                errors, warnings = self.mod.audit_lesson("moneywise", "001")
                self.mod.SERIES_RULES["moneywise"]["lesson_dir"] = original_dir
            self.assertEqual(errors, [])
            self.assertTrue(any("evergreen" in item for item in warnings))

    def test_sunzi_warns_on_emoji_title_and_missing_icons(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            lesson_dir = root / "series" / "book_sunzibingfa" / "lesson06"
            write_text(lesson_dir / "origin.md", "source")
            write_text(lesson_dir / "animate.py", "pass")
            write_text(lesson_dir / "wechat.md", "# article")
            write_text(
                lesson_dir / "script.json",
                json.dumps(
                    {
                        "meta": {},
                        "wechat": {"title": "🎯 title"},
                        "youtube": {},
                        "icons": ["idea.png"],
                        "scenes": [{"scene_index": 6, "interactive_content": {"question": "q", "options": []}}],
                    },
                    ensure_ascii=False,
                ),
            )
            original_dir = self.mod.SERIES_RULES["sunzi"]["lesson_dir"]
            with patch.object(self.mod, "WORKSPACE_ROOT", root):
                self.mod.SERIES_RULES["sunzi"]["lesson_dir"] = root / "series" / "book_sunzibingfa"
                errors, warnings = self.mod.audit_lesson("sunzi", "06")
                self.mod.SERIES_RULES["sunzi"]["lesson_dir"] = original_dir
            self.assertEqual(errors, [])
            self.assertTrue(any("emoji" in item for item in warnings))
            self.assertTrue(any("icon count" in item for item in warnings))


if __name__ == "__main__":
    unittest.main()
