#!/usr/bin/env python3
"""Rollback managed skills from a backup snapshot."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

PROTOCOL_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / ".cursor" / "skills" / "video-core-protocol" / "scripts"
if str(PROTOCOL_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(PROTOCOL_SCRIPTS_DIR))

from protocol_support import managed_skill_targets


WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
MANAGED_TARGETS = managed_skill_targets()


def rollback(backup_dir: Path) -> int:
    if not backup_dir.exists():
        print(f"❌ backup dir not found: {backup_dir}")
        return 1

    for rel_target in MANAGED_TARGETS:
        src = backup_dir / rel_target
        dst = WORKSPACE_ROOT / rel_target
        if not src.exists():
            print(f"❌ missing backup snapshot: {src}")
            return 1

        if dst.exists():
            shutil.rmtree(dst)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dst)
        print(f"✅ restored {rel_target}")

    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rollback managed skills from backup snapshot")
    parser.add_argument("--backup-dir", required=True, help="backup root directory")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    code = rollback(Path(args.backup_dir).expanduser().resolve())
    sys.exit(code)


if __name__ == "__main__":
    main()
