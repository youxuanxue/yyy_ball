#!/usr/bin/env python3
"""Run export->import migration rehearsal for agent-skills, then rollback."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PROTOCOL_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / ".cursor" / "skills" / "video-core-protocol" / "scripts"
if str(PROTOCOL_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(PROTOCOL_SCRIPTS_DIR))

from protocol_support import managed_skill_targets


WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
SYNC_SCRIPT = WORKSPACE_ROOT / "scripts" / "sync_skills.py"
ROLLBACK_SCRIPT = WORKSPACE_ROOT / "scripts" / "rollback_skills.py"
CHECK_PROTOCOL_SCRIPT = WORKSPACE_ROOT / ".cursor" / "skills" / "video-core-protocol" / "scripts" / "check_protocol.py"
MANAGED_TARGETS = managed_skill_targets()


def run_cmd(args: list[str], cwd: Path) -> None:
    proc = subprocess.run(args, cwd=cwd)
    if proc.returncode != 0:
        raise RuntimeError(f"command failed ({proc.returncode}): {' '.join(args)}")


def create_backup_snapshot() -> Path:
    backup_root = Path(tempfile.mkdtemp(prefix="skill_migration_backup_"))
    for rel_target in MANAGED_TARGETS:
        src = WORKSPACE_ROOT / rel_target
        dst = backup_root / rel_target
        if not src.exists():
            raise FileNotFoundError(f"managed target not found: {src}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dst)
    return backup_root


def rehearse(agent_dir: Path, keep_backup: bool) -> int:
    if not agent_dir.exists():
        print(f"❌ agent-skills dir not found: {agent_dir}")
        return 1

    backup_dir = create_backup_snapshot()
    print(f"ℹ️ backup snapshot: {backup_dir}")

    code = 0
    try:
        run_cmd([sys.executable, str(SYNC_SCRIPT), "export", "--agent-dir", str(agent_dir)], WORKSPACE_ROOT)
        run_cmd([sys.executable, str(SYNC_SCRIPT), "import", "--agent-dir", str(agent_dir)], WORKSPACE_ROOT)
        run_cmd([sys.executable, str(CHECK_PROTOCOL_SCRIPT)], WORKSPACE_ROOT)
        run_cmd(
            [
                sys.executable,
                str(SYNC_SCRIPT),
                "report",
                "--agent-dir",
                str(agent_dir),
                "--fail-on-diff",
            ],
            WORKSPACE_ROOT,
        )
        print("✅ rehearsal passed (before rollback)")
    except Exception as exc:  # noqa: BLE001
        print(f"❌ rehearsal failed: {exc}")
        code = 1
    finally:
        rollback_code = subprocess.run(
            [sys.executable, str(ROLLBACK_SCRIPT), "--backup-dir", str(backup_dir)],
            cwd=WORKSPACE_ROOT,
        ).returncode
        if rollback_code != 0:
            print("❌ rollback failed")
            code = 1
        else:
            print("✅ rollback completed")

        if not keep_backup:
            shutil.rmtree(backup_dir, ignore_errors=True)
            print("ℹ️ backup deleted")
        else:
            print(f"ℹ️ backup retained: {backup_dir}")

    return code


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rehearse skill migration and rollback")
    parser.add_argument("--agent-dir", required=True, help="path to local clone of agent-skills")
    parser.add_argument("--keep-backup", action="store_true", help="keep backup directory after rollback")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    code = rehearse(Path(args.agent_dir).expanduser().resolve(), args.keep_backup)
    sys.exit(code)


if __name__ == "__main__":
    main()
