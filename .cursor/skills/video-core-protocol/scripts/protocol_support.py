#!/usr/bin/env python3
"""Shared support helpers for the video core protocol skill."""

from __future__ import annotations

from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_PROFILE = WORKSPACE_ROOT / "profiles" / "yyy_ball.yaml"
DEFAULT_REJECT_HARDCODED_PATH_PREFIXES = ("/Users/", "/home/ubuntu/Codes/")
REFERENCE_DOCS_BY_SKILL = {
    "video-core-protocol": (Path(".cursor/skills/video-core-protocol/REFERENCE.md"),),
    "lesson-content-planning": (Path(".cursor/skills/lesson-content-planning/REFERENCE.md"),),
    "lesson-animation-authoring": (Path(".cursor/skills/lesson-animation-authoring/REFERENCE.md"),),
    "lesson-render-publish": (Path(".cursor/skills/lesson-render-publish/REFERENCE.md"),),
    "series-zsxq-adapter": (Path(".cursor/skills/series-zsxq-adapter/REFERENCE.md"),),
    "series-sunzi-adapter": (Path(".cursor/skills/series-sunzi-adapter/REFERENCE.md"),),
    "series-moneywise-adapter": (Path(".cursor/skills/series-moneywise-adapter/REFERENCE.md"),),
    "skill-evolver": (Path(".cursor/skills/skill-evolver/REFERENCE.md"),),
    "chinese-series-orchestrator": (Path(".cursor/skills/chinese-series-orchestrator/REFERENCE.md"),),
    "moneywise-series-orchestrator": (Path(".cursor/skills/moneywise-series-orchestrator/REFERENCE.md"),),
}
ASSET_PATHS_BY_SKILL = {
    "lesson-content-planning": (
        Path("series/prompts/zsxq_100ke_script.prompt"),
        Path("series/prompts/sunzi_script.prompt"),
        Path("series/prompts/moneywise_script.prompt"),
    ),
    "lesson-animation-authoring": (
        Path("series/prompts/zsxq_100ke_annimate.prompt"),
        Path("series/prompts/sunzi_annimate.prompt"),
        Path("series/prompts/moneywise_annimate.prompt"),
    ),
    "series-sunzi-adapter": (
        Path("series/template/sunzi/cover_template.html"),
    ),
}
SOURCE_PATHS_BY_SKILL = {
    "video-core-protocol": (
        Path("src/animate/__init__.py"),
        Path("src/animate/lesson_vertical.py"),
        Path("src/utils/anim_helper.py"),
    ),
    "lesson-animation-authoring": (
        Path("src/animate/__init__.py"),
        Path("src/animate/lesson_vertical.py"),
        Path("src/utils/anim_helper.py"),
    ),
    "lesson-render-publish": (
        Path("src/animate/lesson_vertical.py"),
        Path("src/utils/anim_helper.py"),
        Path("src/utils/voice_edgetts.py"),
        Path("src/utils/cover_generator.py"),
        Path("src/utils/icon_helper.py"),
    ),
    "series-sunzi-adapter": (
        Path("src/utils/cover_generator.py"),
    ),
}


def _read_profile_lines(profile_path: Path) -> list[str]:
    if not profile_path.exists():
        raise FileNotFoundError(f"profile not found: {profile_path}")
    return profile_path.read_text(encoding="utf-8").splitlines()


def _load_top_level_list(profile_path: Path, key: str) -> tuple[str, ...]:
    values: list[str] = []
    in_section = False

    for raw_line in _read_profile_lines(profile_path):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if not in_section:
            if stripped == f"{key}:":
                in_section = True
            continue

        if raw_line.startswith("  - "):
            value = raw_line.split("-", 1)[1].strip()
            if value:
                values.append(value)
            continue

        if not raw_line.startswith(" "):
            break

    return tuple(values)


def load_managed_skills(profile_path: Path = DEFAULT_PROFILE) -> tuple[str, ...]:
    skills = _load_top_level_list(profile_path, "managed_skills")
    if not skills:
        raise ValueError(f"managed_skills is empty in {profile_path}")
    return skills


def load_reject_hardcoded_path_prefixes(profile_path: Path = DEFAULT_PROFILE) -> tuple[str, ...]:
    prefixes: list[str] = []
    in_guards = False
    in_reject_list = False

    for raw_line in _read_profile_lines(profile_path):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if not in_guards:
            if stripped == "guards:":
                in_guards = True
            continue

        if in_guards and not in_reject_list:
            if raw_line.startswith("  reject_hardcoded_path_prefixes:"):
                in_reject_list = True
                continue
            if not raw_line.startswith(" "):
                break
            continue

        if in_reject_list:
            if raw_line.startswith("    - "):
                value = raw_line.split("-", 1)[1].strip()
                if value:
                    prefixes.append(value)
                continue
            break

    return tuple(prefixes) or DEFAULT_REJECT_HARDCODED_PATH_PREFIXES


def managed_skill_targets(profile_path: Path = DEFAULT_PROFILE) -> list[Path]:
    return [Path(".cursor/skills") / skill for skill in load_managed_skills(profile_path)]


def reference_docs_for_managed_skills(profile_path: Path = DEFAULT_PROFILE) -> tuple[Path, ...]:
    docs: list[Path] = []
    for skill in load_managed_skills(profile_path):
        docs.extend(REFERENCE_DOCS_BY_SKILL.get(skill, ()))
    return tuple(docs)


def asset_paths_for_managed_skills(profile_path: Path = DEFAULT_PROFILE) -> tuple[Path, ...]:
    paths: list[Path] = []
    for skill in load_managed_skills(profile_path):
        paths.extend(ASSET_PATHS_BY_SKILL.get(skill, ()))
    return tuple(paths)


def source_paths_for_managed_skills(profile_path: Path = DEFAULT_PROFILE) -> tuple[Path, ...]:
    paths: list[Path] = []
    for skill in load_managed_skills(profile_path):
        paths.extend(SOURCE_PATHS_BY_SKILL.get(skill, ()))
    seen = set()
    ordered_unique = []
    for path in paths:
        if path not in seen:
            seen.add(path)
            ordered_unique.append(path)
    return tuple(ordered_unique)


def validate_local_skills(
    *,
    cursor_skills_dir: Path,
    profile_path: Path = DEFAULT_PROFILE,
    workspace_root: Path = WORKSPACE_ROOT,
) -> list[str]:
    errors: list[str] = []

    for skill in load_managed_skills(profile_path):
        path = cursor_skills_dir / skill / "SKILL.md"
        if not path.exists():
            errors.append(f"Cursor skill {skill} not found: {path}")

    for rel_path in reference_docs_for_managed_skills(profile_path):
        path = workspace_root / rel_path
        if not path.exists():
            errors.append(f"Required reference doc not found: {path}")

    for rel_path in asset_paths_for_managed_skills(profile_path):
        path = workspace_root / rel_path
        if not path.exists():
            errors.append(f"Required prompt/template asset not found: {path}")

    for rel_path in source_paths_for_managed_skills(profile_path):
        path = workspace_root / rel_path
        if not path.exists():
            errors.append(f"Required src runtime asset not found: {path}")

    reject_tokens = load_reject_hardcoded_path_prefixes(profile_path)
    scan_targets = []
    if cursor_skills_dir.exists():
        scan_targets.extend(cursor_skills_dir.rglob("*.md"))

    prompts_dir = workspace_root / "series" / "prompts"
    if prompts_dir.exists():
        scan_targets.extend(prompts_dir.rglob("*.prompt"))

    template_dir = workspace_root / "series" / "template"
    if template_dir.exists():
        for pattern in ("*.html", "*.json", "*.py", "*.md"):
            scan_targets.extend(template_dir.rglob(pattern))

    for rel_path in source_paths_for_managed_skills(profile_path):
        path = workspace_root / rel_path
        if path.exists():
            scan_targets.append(path)

    for text_file in scan_targets:
        text = text_file.read_text(encoding="utf-8")
        for token in reject_tokens:
            if token in text:
                errors.append(f"disallowed hardcoded path in {text_file}: contains {token}")

    return errors


def run_local_skill_checks(
    *,
    cursor_skills_dir: Path,
    profile_path: Path = DEFAULT_PROFILE,
    workspace_root: Path = WORKSPACE_ROOT,
) -> int:
    errors = validate_local_skills(
        cursor_skills_dir=cursor_skills_dir,
        profile_path=profile_path,
        workspace_root=workspace_root,
    )
    if errors:
        print("❌ Local skill checks failed:")
        for item in errors:
            print(f"  - {item}")
        return 1

    print("✅ Local skill checks passed")
    return 0
