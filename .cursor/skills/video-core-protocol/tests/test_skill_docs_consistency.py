import unittest
from pathlib import Path
import sys


WORKSPACE_ROOT = Path(__file__).resolve().parents[4]
PROTOCOL_SCRIPTS_DIR = WORKSPACE_ROOT / ".cursor" / "skills" / "video-core-protocol" / "scripts"
if str(PROTOCOL_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(PROTOCOL_SCRIPTS_DIR))

from protocol_support import load_managed_skills, load_reject_hardcoded_path_prefixes


class TestSkillDocsConsistency(unittest.TestCase):
    def test_required_cursor_skill_docs_exist(self):
        for skill in load_managed_skills():
            rel = f".cursor/skills/{skill}/SKILL.md"
            path = WORKSPACE_ROOT / rel
            self.assertTrue(path.exists(), f"Missing file: {path}")

    def test_no_disallowed_hardcoded_path_prefixes(self):
        roots = [WORKSPACE_ROOT / ".cursor" / "skills"]
        reject_tokens = load_reject_hardcoded_path_prefixes()
        offenders = []
        for root in roots:
            for path in root.rglob("*.md"):
                text = path.read_text(encoding="utf-8")
                for token in reject_tokens:
                    if token in text:
                        offenders.append(f"{path} ({token})")
        self.assertEqual(offenders, [], f"Disallowed hardcoded path found in: {offenders}")


if __name__ == "__main__":
    unittest.main()
