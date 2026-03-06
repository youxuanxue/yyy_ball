import unittest
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[4]


class TestSkillDocsConsistency(unittest.TestCase):
    def test_required_cursor_skill_docs_exist(self):
        for rel in [
            ".cursor/skills/video-workflow/SKILL.md",
            ".cursor/skills/moneywise-workflow/SKILL.md",
        ]:
            path = WORKSPACE_ROOT / rel
            self.assertTrue(path.exists(), f"Missing file: {path}")

    def test_claude_skills_dir_is_removed(self):
        claude_skills = WORKSPACE_ROOT / ".claude" / "skills"
        self.assertFalse(claude_skills.exists(), f"{claude_skills} should be removed")

    def test_no_legacy_hardcoded_users_path(self):
        roots = [WORKSPACE_ROOT / ".cursor" / "skills"]
        legacy_tokens = ["/Users/", "/home/ubuntu/Codes/"]
        offenders = []
        for root in roots:
            for path in root.rglob("*.md"):
                text = path.read_text(encoding="utf-8")
                for token in legacy_tokens:
                    if token in text:
                        offenders.append(f"{path} ({token})")
        self.assertEqual(offenders, [], f"Legacy hardcoded path found in: {offenders}")


if __name__ == "__main__":
    unittest.main()
