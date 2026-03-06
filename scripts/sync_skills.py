#!/usr/bin/env python3
"""Sync skill files between local workspace and agent-skills repository.

Usage examples:
  uv run python scripts/sync_skills.py check-local
  uv run python scripts/sync_skills.py export --agent-dir /path/to/agent-skills
  uv run python scripts/sync_skills.py import --agent-dir /path/to/agent-skills
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
CURSOR_SKILLS_DIR = WORKSPACE_ROOT / ".cursor" / "skills"
CLAUDE_SKILLS_DIR = WORKSPACE_ROOT / ".claude" / "skills"
SKILLS = ("video-workflow", "moneywise-workflow")


def ensure_path_exists(path: Path, description: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"{description} not found: {path}")


def compare_text_file(path_a: Path, path_b: Path) -> bool:
    text_a = path_a.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip() + "\n"
    text_b = path_b.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip() + "\n"
    return text_a == text_b


def check_local() -> int:
    """Validate local skill consistency."""
    errors = []

    cursor_moneywise = CURSOR_SKILLS_DIR / "moneywise-workflow" / "SKILL.md"
    claude_moneywise = CLAUDE_SKILLS_DIR / "moneywise-workflow" / "SKILL.md"
    try:
        ensure_path_exists(cursor_moneywise, "Cursor moneywise skill")
        ensure_path_exists(claude_moneywise, "Claude moneywise skill")
        if not compare_text_file(cursor_moneywise, claude_moneywise):
            errors.append("moneywise SKILL.md mismatch between .cursor and .claude")
    except FileNotFoundError as exc:
        errors.append(str(exc))

    legacy_tokens = ["/Users/", "/home/ubuntu/Codes/"]
    for root in (CURSOR_SKILLS_DIR, CLAUDE_SKILLS_DIR):
        if not root.exists():
            continue
        for md_file in root.rglob("*.md"):
            text = md_file.read_text(encoding="utf-8")
            for token in legacy_tokens:
                if token in text:
                    errors.append(f"legacy hardcoded path in {md_file}: contains {token}")

    if errors:
        print("❌ Local skill checks failed:")
        for item in errors:
            print(f"  - {item}")
        return 1

    print("✅ Local skill checks passed")
    return 0


def sync_local_moneywise() -> int:
    """Sync .cursor moneywise skill into .claude."""
    src = CURSOR_SKILLS_DIR / "moneywise-workflow" / "SKILL.md"
    dst = CLAUDE_SKILLS_DIR / "moneywise-workflow" / "SKILL.md"
    ensure_path_exists(src, "Source moneywise skill")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"✅ Synced {src} -> {dst}")
    return 0


def export_to_agent_repo(agent_dir: Path) -> int:
    """Export local .cursor skills into agent-skills repo layout."""
    ensure_path_exists(agent_dir, "agent-skills repo dir")
    target_root = agent_dir / "skills"
    target_root.mkdir(parents=True, exist_ok=True)

    for skill in SKILLS:
        src = CURSOR_SKILLS_DIR / skill
        dst = target_root / skill
        ensure_path_exists(src, f"Local skill dir {skill}")
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"✅ Exported {src} -> {dst}")

    return 0


def import_from_agent_repo(agent_dir: Path) -> int:
    """Import skills from agent-skills repo layout into local .cursor."""
    ensure_path_exists(agent_dir, "agent-skills repo dir")
    source_root = agent_dir / "skills"
    ensure_path_exists(source_root, "agent-skills skills dir")

    for skill in SKILLS:
        src = source_root / skill
        dst = CURSOR_SKILLS_DIR / skill
        ensure_path_exists(src, f"Remote skill dir {skill}")
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"✅ Imported {src} -> {dst}")

    print("ℹ️ 建议随后执行: uv run python scripts/sync_skills.py sync-local-moneywise")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync skills with agent-skills repository")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("check-local", help="check local skill consistency")
    subparsers.add_parser("sync-local-moneywise", help="sync .cursor moneywise skill to .claude")

    export_parser = subparsers.add_parser("export", help="export local skills to agent-skills repo")
    export_parser.add_argument("--agent-dir", required=True, help="path to local clone of agent-skills")

    import_parser = subparsers.add_parser("import", help="import skills from agent-skills repo")
    import_parser.add_argument("--agent-dir", required=True, help="path to local clone of agent-skills")

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    try:
        if args.command == "check-local":
            code = check_local()
        elif args.command == "sync-local-moneywise":
            code = sync_local_moneywise()
        elif args.command == "export":
            code = export_to_agent_repo(Path(args.agent_dir).expanduser().resolve())
        elif args.command == "import":
            code = import_from_agent_repo(Path(args.agent_dir).expanduser().resolve())
        else:
            code = 1
            print(f"❌ Unsupported command: {args.command}")
    except FileNotFoundError as exc:
        print(f"❌ {exc}")
        code = 1

    sys.exit(code)


if __name__ == "__main__":
    main()
