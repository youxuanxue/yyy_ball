import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "sync_skills.py"


def load_sync_module():
    spec = importlib.util.spec_from_file_location("sync_skills_script", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class TestSyncSkills(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_sync_module()

    def test_check_local_pass_without_claude_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cursor = root / ".cursor" / "skills"
            claude = root / ".claude" / "skills"
            write_text(cursor / "video-workflow" / "SKILL.md", "video")
            write_text(cursor / "moneywise-workflow" / "SKILL.md", "moneywise")

            with patch.object(self.mod, "CURSOR_SKILLS_DIR", cursor), patch.object(self.mod, "CLAUDE_SKILLS_DIR", claude):
                self.assertEqual(self.mod.check_local(), 0)

    def test_check_local_fails_if_claude_skills_exists(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cursor = root / ".cursor" / "skills"
            claude = root / ".claude" / "skills"
            write_text(cursor / "video-workflow" / "SKILL.md", "video")
            write_text(cursor / "moneywise-workflow" / "SKILL.md", "moneywise")
            write_text(claude / "x" / "SKILL.md", "deprecated")

            with patch.object(self.mod, "CURSOR_SKILLS_DIR", cursor), patch.object(self.mod, "CLAUDE_SKILLS_DIR", claude):
                self.assertEqual(self.mod.check_local(), 1)

    def test_report_detects_diff_with_fail_on_diff(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cursor = root / ".cursor" / "skills"
            agent = root / "agent"
            write_text(cursor / "video-workflow" / "SKILL.md", "video-local")
            write_text(cursor / "moneywise-workflow" / "SKILL.md", "money-local")
            write_text(agent / "skills" / "video-workflow" / "SKILL.md", "video-remote")
            write_text(agent / "skills" / "moneywise-workflow" / "SKILL.md", "money-local")

            with patch.object(self.mod, "CURSOR_SKILLS_DIR", cursor):
                code = self.mod.report_agent_diff(agent, fail_on_diff=True)
                self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
