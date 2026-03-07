import tempfile
import unittest
from pathlib import Path
import sys


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from protocol_support import (
    asset_paths_for_managed_skills,
    load_managed_skills,
    reference_docs_for_managed_skills,
    run_local_skill_checks,
    source_paths_for_managed_skills,
    validate_local_skills,
)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def make_profile(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "project: demo",
                "managed_skills:",
                "  - video-core-protocol",
                "  - lesson-content-planning",
                "  - lesson-animation-authoring",
                "  - lesson-render-publish",
                "  - series-sunzi-adapter",
                "  - chinese-series-orchestrator",
                "",
                "guards:",
                "  reject_hardcoded_path_prefixes:",
                "    - /Users/",
                "    - /home/ubuntu/Codes/",
                "",
            ]
        ),
        encoding="utf-8",
    )


class TestCheckProtocol(unittest.TestCase):
    def test_load_managed_skills_from_profile(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile = Path(tmp) / "profile.yaml"
            make_profile(profile)
            self.assertEqual(
                load_managed_skills(profile),
                (
                    "video-core-protocol",
                    "lesson-content-planning",
                    "lesson-animation-authoring",
                    "lesson-render-publish",
                    "series-sunzi-adapter",
                    "chinese-series-orchestrator",
                ),
            )

    def test_reference_and_asset_sets_follow_profile(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile = Path(tmp) / "profile.yaml"
            make_profile(profile)
            self.assertIn(Path(".cursor/skills/lesson-content-planning/REFERENCE.md"), reference_docs_for_managed_skills(profile))
            self.assertIn(Path(".cursor/skills/lesson-render-publish/REFERENCE.md"), reference_docs_for_managed_skills(profile))
            self.assertIn(Path("series/prompts/sunzi_script.prompt"), asset_paths_for_managed_skills(profile))
            self.assertIn(Path("series/template/sunzi/cover_template.html"), asset_paths_for_managed_skills(profile))
            self.assertIn(Path("src/utils/voice_edgetts.py"), source_paths_for_managed_skills(profile))

    def _make_closed_loop_workspace(self, root: Path, profile: Path) -> Path:
        cursor = root / ".cursor" / "skills"
        for skill in load_managed_skills(profile):
            write_text(cursor / skill / "SKILL.md", skill)
        for rel in reference_docs_for_managed_skills(profile):
            write_text(root / rel, f"# {rel.name}")
        for rel in asset_paths_for_managed_skills(profile):
            write_text(root / rel, f"asset: {rel.name}")
        for rel in source_paths_for_managed_skills(profile):
            write_text(root / rel, f"source: {rel.name}")
        return cursor

    def test_validate_local_skills_passes_for_valid_layout(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            profile = root / "profile.yaml"
            make_profile(profile)
            cursor = self._make_closed_loop_workspace(root, profile)

            errors = validate_local_skills(
                cursor_skills_dir=cursor,
                profile_path=profile,
                workspace_root=root,
            )
            self.assertEqual(errors, [])

    def test_validate_local_skills_reports_disallowed_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            profile = root / "profile.yaml"
            make_profile(profile)
            cursor = self._make_closed_loop_workspace(root, profile)
            write_text(cursor / "chinese-series-orchestrator" / "SKILL.md", "/Users/demo/skill")

            errors = validate_local_skills(
                cursor_skills_dir=cursor,
                profile_path=profile,
                workspace_root=root,
            )
            self.assertEqual(len(errors), 1)
            self.assertIn("disallowed hardcoded path", errors[0])

    def test_run_local_skill_checks_fails_when_skill_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            profile = root / "profile.yaml"
            make_profile(profile)
            cursor = self._make_closed_loop_workspace(root, profile)
            (cursor / "lesson-animation-authoring" / "SKILL.md").unlink()

            code = run_local_skill_checks(
                cursor_skills_dir=cursor,
                profile_path=profile,
                workspace_root=root,
            )
            self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
