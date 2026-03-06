#!/usr/bin/env python3
"""Sync skill files between local workspace and agent-skills repository.

Usage examples:
  uv run python scripts/sync_skills.py check-local
  uv run python scripts/sync_skills.py export --agent-dir /path/to/agent-skills
  uv run python scripts/sync_skills.py import --agent-dir /path/to/agent-skills
  uv run python scripts/sync_skills.py report --agent-dir /path/to/agent-skills --fail-on-diff
"""

from __future__ import annotations

import argparse
import hashlib
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


def file_digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fp:
        while True:
            chunk = fp.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def collect_file_map(root: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    if not root.exists():
        return mapping
    for item in sorted(root.rglob("*")):
        if item.is_file():
            rel = item.relative_to(root).as_posix()
            mapping[rel] = file_digest(item)
    return mapping


def report_agent_diff(agent_dir: Path, fail_on_diff: bool = False) -> int:
    """Report local-vs-agent skill differences."""
    ensure_path_exists(agent_dir, "agent-skills repo dir")
    source_root = agent_dir / "skills"
    ensure_path_exists(source_root, "agent-skills skills dir")

    has_diff = False
    for skill in SKILLS:
        local_dir = CURSOR_SKILLS_DIR / skill
        remote_dir = source_root / skill
        ensure_path_exists(local_dir, f"Local skill dir {skill}")
        ensure_path_exists(remote_dir, f"Remote skill dir {skill}")

        local_files = collect_file_map(local_dir)
        remote_files = collect_file_map(remote_dir)

        local_set = set(local_files.keys())
        remote_set = set(remote_files.keys())
        only_local = sorted(local_set - remote_set)
        only_remote = sorted(remote_set - local_set)
        common = sorted(local_set & remote_set)
        changed = [p for p in common if local_files[p] != remote_files[p]]

        print(f"\n=== {skill} ===")
        print(
            f"local={len(local_files)} remote={len(remote_files)} "
            f"only_local={len(only_local)} only_remote={len(only_remote)} changed={len(changed)}"
        )

        if only_local:
            print("  only_local:")
            for p in only_local[:20]:
                print(f"    - {p}")
        if only_remote:
            print("  only_remote:")
            for p in only_remote[:20]:
                print(f"    - {p}")
        if changed:
            print("  changed:")
            for p in changed[:20]:
                print(f"    - {p}")

        if only_local or only_remote or changed:
            has_diff = True

    if has_diff:
        print("\n⚠️ report detected differences between local and agent-skills")
        return 1 if fail_on_diff else 0

    print("\n✅ report: local and agent-skills are identical for managed skills")
    return 0


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

    report_parser = subparsers.add_parser("report", help="report diff between local and agent-skills")
    report_parser.add_argument("--agent-dir", required=True, help="path to local clone of agent-skills")
    report_parser.add_argument(
        "--fail-on-diff",
        action="store_true",
        help="return non-zero when differences are detected",
    )

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
        elif args.command == "report":
            code = report_agent_diff(
                Path(args.agent_dir).expanduser().resolve(),
                fail_on_diff=args.fail_on_diff,
            )
        else:
            code = 1
            print(f"❌ Unsupported command: {args.command}")
    except FileNotFoundError as exc:
        print(f"❌ {exc}")
        code = 1

    sys.exit(code)


if __name__ == "__main__":
    main()
