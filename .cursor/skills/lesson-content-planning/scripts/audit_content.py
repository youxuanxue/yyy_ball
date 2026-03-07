#!/usr/bin/env python3
"""Audit generated lesson content for structure and quality signals."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[4]

YEAR_RE = re.compile(r"\b20\d{2}\b")
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]")

SERIES_RULES = {
    "zsxq": {
        "lesson_dir": WORKSPACE_ROOT / "series" / "book_zsxq_100ke",
        "num_digits": 3,
        "required_files": ("script.json", "animate.py", "wechat.md"),
        "required_script_keys": ("meta", "wechat", "youtube", "icons", "scenes"),
        "min_icons": 12,
        "icon_extension_policy": "warn",
        "banned_phrases": ("稳赚", "不会亏", "全面碾压", "赌的是国运", "低到没朋友", "赚翻"),
    },
    "sunzi": {
        "lesson_dir": WORKSPACE_ROOT / "series" / "book_sunzibingfa",
        "num_digits": 2,
        "required_files": ("origin.md", "script.json", "animate.py", "wechat.md"),
        "required_script_keys": ("meta", "wechat", "youtube", "icons", "scenes"),
        "min_icons": 6,
        "icon_extension_policy": "warn",
        "banned_phrases": ("讨好别人", "别傻傻地", "越补越差"),
        "wechat_title_no_emoji": True,
        "require_interactive_scene": True,
    },
    "moneywise": {
        "lesson_dir": WORKSPACE_ROOT / "series" / "moneywise_global",
        "num_digits": 3,
        "required_files": ("script.json", "animate.py"),
        "required_script_keys": ("meta", "seo", "social", "youtube", "blog", "icons", "scenes"),
        "min_icons": 12,
        "icon_extension_policy": "warn",
        "evergreen": True,
        "banned_phrases": ("ultimate safety net", "outdated myths"),
    },
}


def normalize_lesson_num(lesson: str, num_digits: int) -> str:
    cleaned = lesson.strip()
    if cleaned.lower().startswith("lesson"):
        cleaned = cleaned[6:]
    if not cleaned.isdigit():
        raise ValueError(f"非法课程编号: {lesson}")
    return str(int(cleaned)).zfill(num_digits)


def get_lesson_dir(series: str, lesson: str) -> Path:
    cfg = SERIES_RULES[series]
    lesson_num = normalize_lesson_num(lesson, cfg["num_digits"])
    return cfg["lesson_dir"] / f"lesson{lesson_num}"


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def audit_lesson(series: str, lesson: str) -> tuple[list[str], list[str]]:
    cfg = SERIES_RULES[series]
    lesson_dir = get_lesson_dir(series, lesson)
    errors: list[str] = []
    warnings: list[str] = []

    if not lesson_dir.exists():
        return [f"lesson dir not found: {lesson_dir}"], warnings

    for rel in cfg["required_files"]:
        path = lesson_dir / rel
        if not path.exists():
            errors.append(f"missing required file: {path}")

    script_path = lesson_dir / "script.json"
    if not script_path.exists():
        return errors, warnings

    data = _load_json(script_path)
    for key in cfg["required_script_keys"]:
        if key not in data:
            errors.append(f"missing top-level key '{key}' in {script_path}")

    icons = data.get("icons", [])
    if len(icons) < cfg["min_icons"]:
        warnings.append(f"icon count below target ({len(icons)} < {cfg['min_icons']})")
    if cfg["icon_extension_policy"] == "warn":
        for icon in icons:
            if isinstance(icon, str) and icon.lower().endswith(".png"):
                warnings.append(f"icon uses .png suffix; canonical form should be bare name: {icon}")
                break

    script_text = script_path.read_text(encoding="utf-8")
    if cfg.get("evergreen") and YEAR_RE.search(script_text):
        warnings.append("dated year references found in MoneyWise content; evergreen rule violated")

    for phrase in cfg.get("banned_phrases", ()):
        if phrase in script_text:
            warnings.append(f"risky or AI-ish phrase found in script output: {phrase}")

    if cfg.get("wechat_title_no_emoji"):
        title = data.get("wechat", {}).get("title", "")
        if EMOJI_RE.search(title):
            warnings.append("wechat.title contains emoji but current Sunzi contract expects plain title text")

    if cfg.get("require_interactive_scene"):
        scenes = data.get("scenes", [])
        if not any(scene.get("interactive_content") for scene in scenes):
            errors.append("interactive_content missing from Sunzi quiz scene")

    wechat_path = lesson_dir / "wechat.md"
    if wechat_path.exists():
        wechat_text = wechat_path.read_text(encoding="utf-8")
        for phrase in cfg.get("banned_phrases", ()):
            if phrase in wechat_text:
                warnings.append(f"risky or AI-ish phrase found in article output: {phrase}")
        if series == "zsxq" and ("不会亏" in wechat_text or "稳如老狗" in wechat_text):
            warnings.append("wechat.md contains overly absolute beginner-finance wording")

    return errors, warnings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit generated lesson content for structure and quality")
    parser.add_argument("--series", choices=sorted(SERIES_RULES.keys()), required=True)
    parser.add_argument("--lesson", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    errors, warnings = audit_lesson(args.series, args.lesson)
    print(f"lesson={args.series}:{args.lesson}")
    if errors:
        print("errors:")
        for item in errors:
            print(f"  - {item}")
    if warnings:
        print("warnings:")
        for item in warnings:
            print(f"  - {item}")
    if not errors and not warnings:
        print("clean")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
