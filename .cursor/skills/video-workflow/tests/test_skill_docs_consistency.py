import unittest
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[4]


def _normalize_doc(text: str) -> str:
    return text.replace("\r\n", "\n").rstrip() + "\n"


class TestSkillDocsConsistency(unittest.TestCase):
    def test_moneywise_skill_docs_are_in_sync(self):
        cursor_doc = WORKSPACE_ROOT / ".cursor" / "skills" / "moneywise-workflow" / "SKILL.md"
        claude_doc = WORKSPACE_ROOT / ".claude" / "skills" / "moneywise-workflow" / "SKILL.md"
        self.assertTrue(cursor_doc.exists(), f"Missing file: {cursor_doc}")
        self.assertTrue(claude_doc.exists(), f"Missing file: {claude_doc}")
        self.assertEqual(
            _normalize_doc(cursor_doc.read_text(encoding="utf-8")),
            _normalize_doc(claude_doc.read_text(encoding="utf-8")),
            "moneywise-workflow SKILL.md in .cursor and .claude should stay identical",
        )

    def test_no_legacy_hardcoded_users_path(self):
        roots = [
            WORKSPACE_ROOT / ".cursor" / "skills",
            WORKSPACE_ROOT / ".claude" / "skills",
        ]
        legacy_token = "/Users/xuejiao"
        offenders = []
        for root in roots:
            for path in root.rglob("*.md"):
                text = path.read_text(encoding="utf-8")
                if legacy_token in text:
                    offenders.append(str(path))
        self.assertEqual(offenders, [], f"Legacy hardcoded path found in: {offenders}")


if __name__ == "__main__":
    unittest.main()
