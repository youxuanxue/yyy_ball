import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import sys


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "sync_skills.py"
SCRIPTS_DIR = SCRIPT_PATH.parent


def load_sync_module():
    if str(SCRIPTS_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPTS_DIR))
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

    def test_report_detects_diff_with_fail_on_diff(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cursor = root / ".cursor" / "skills"
            agent = root / "agent"
            managed = ("video-core-protocol", "chinese-series-orchestrator")
            write_text(cursor / "video-core-protocol" / "SKILL.md", "core-local")
            write_text(cursor / "chinese-series-orchestrator" / "SKILL.md", "orchestrator-local")
            write_text(agent / "skills" / "video-core-protocol" / "SKILL.md", "core-local")
            write_text(agent / "skills" / "chinese-series-orchestrator" / "SKILL.md", "orchestrator-remote")

            with patch.object(self.mod, "CURSOR_SKILLS_DIR", cursor), patch.object(self.mod, "SKILLS", managed):
                code = self.mod.report_agent_diff(agent, fail_on_diff=True)
                self.assertEqual(code, 1)

    def test_export_uses_managed_skill_list(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cursor = root / ".cursor" / "skills"
            agent = root / "agent"
            managed = ("video-core-protocol", "moneywise-series-orchestrator")
            write_text(cursor / "video-core-protocol" / "SKILL.md", "core")
            write_text(cursor / "moneywise-series-orchestrator" / "SKILL.md", "moneywise")
            agent.mkdir(parents=True, exist_ok=True)

            with patch.object(self.mod, "CURSOR_SKILLS_DIR", cursor), patch.object(self.mod, "SKILLS", managed):
                code = self.mod.export_to_agent_repo(agent)
                self.assertEqual(code, 0)
                self.assertTrue((agent / "skills" / "video-core-protocol" / "SKILL.md").exists())
                self.assertTrue((agent / "skills" / "moneywise-series-orchestrator" / "SKILL.md").exists())


if __name__ == "__main__":
    unittest.main()
