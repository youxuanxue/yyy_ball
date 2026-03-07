#!/usr/bin/env python3
"""Self-contained validation entrypoint for the video core protocol skill."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from protocol_support import DEFAULT_PROFILE, WORKSPACE_ROOT, run_local_skill_checks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the video core protocol skill contract")
    parser.add_argument(
        "--profile",
        default=str(DEFAULT_PROFILE),
        help="profile yaml path used to resolve managed skills and guard rules",
    )
    parser.add_argument(
        "--cursor-skills-dir",
        default=str(WORKSPACE_ROOT / ".cursor" / "skills"),
        help="Cursor skills directory to validate",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    code = run_local_skill_checks(
        cursor_skills_dir=Path(args.cursor_skills_dir).expanduser().resolve(),
        profile_path=Path(args.profile).expanduser().resolve(),
    )
    sys.exit(code)


if __name__ == "__main__":
    main()
