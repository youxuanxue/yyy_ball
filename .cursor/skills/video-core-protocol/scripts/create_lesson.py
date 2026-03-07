#!/usr/bin/env python3
"""
Create lesson directories for all managed series.

Usage:
    python create_lesson.py --series zsxq 002
    python create_lesson.py --series sunzi 07
    python create_lesson.py --series moneywise 021
"""

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from lesson_num import normalize_lesson_num

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent

SERIES_CONFIG = {
    "zsxq": {
        "name": "日日生金",
        "dir": PROJECT_ROOT / "series" / "book_zsxq_100ke",
        "num_digits": 3,
        "script_prompt": "zsxq_100ke_script.prompt",
        "animate_prompt": "zsxq_100ke_annimate.prompt",
        "data_source": "assets/zsxq/jingpin_100ke_posts.json",
        "pre_render_content_outputs": ("script.json", "wechat.md"),
        "post_publish_content_outputs": (),
    },
    "sunzi": {
        "name": "孙子兵法（小小谋略家）",
        "dir": PROJECT_ROOT / "series" / "book_sunzibingfa",
        "num_digits": 2,
        "script_prompt": "sunzi_script.prompt",
        "animate_prompt": "sunzi_annimate.prompt",
        "data_source": "origin.md",
        "pre_render_content_outputs": ("script.json", "wechat.md"),
        "post_publish_content_outputs": (),
    },
    "moneywise": {
        "name": "MoneyWise Global",
        "dir": PROJECT_ROOT / "series" / "moneywise_global",
        "num_digits": 3,
        "script_prompt": "moneywise_script.prompt",
        "animate_prompt": "moneywise_annimate.prompt",
        "data_source": "assets/zsxq/jingpin_100ke_posts.json",
        "pre_render_content_outputs": ("script.json",),
        "post_publish_content_outputs": ("website_mdx",),
    },
}


def get_series_config(series: str) -> dict:
    if series not in SERIES_CONFIG:
        raise ValueError(f"未知系列 '{series}'，可选: {list(SERIES_CONFIG.keys())}")
    return SERIES_CONFIG[series]


def _format_outputs(outputs: tuple[str, ...]) -> str:
    return ", ".join(outputs) if outputs else "无"


def create_lesson_dir(series: str, lesson_num: str):
    config = get_series_config(series)
    lesson_num = normalize_lesson_num(lesson_num, config["num_digits"])
    lesson_dir = config["dir"] / f"lesson{lesson_num}"

    if not config["dir"].exists():
        print(f"❌ 系列目录不存在: {config['dir']}")
        sys.exit(1)

    if lesson_dir.exists():
        print(f"⚠️ 目录已存在: {lesson_dir}")
        return

    lesson_dir.mkdir(parents=True)
    print(f"✅ 创建目录: {lesson_dir}")

    print(f"\n🧭 [{config['name']}] 分层执行顺序")
    if series == "sunzi":
        print("   0. 准备 `origin.md` 作为内容源素材")

    print(
        f"   1. `lesson-content-planning`：读取 {config['data_source']} + {config['script_prompt']}，"
        f"生成 {_format_outputs(config['pre_render_content_outputs'])}"
    )
    print(
        f"   2. `lesson-animation-authoring`：读取 script.json + {config['animate_prompt']}，"
        "生成 animate.py"
    )
    print(
        "   3. `lesson-render-publish`：调用 "
        "`.cursor/skills/video-core-protocol/scripts/workflow.py` 做 status/render/publish"
    )
    if config["post_publish_content_outputs"]:
        print(
            "   4. `lesson-content-planning`：在拿到发布元数据后，补生成 "
            f"{_format_outputs(config['post_publish_content_outputs'])}"
        )


def main():
    parser = argparse.ArgumentParser(
        description="创建新课程目录（支持日日生金、孙子兵法、MoneyWise）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --series zsxq 002
  %(prog)s --series sunzi 07
  %(prog)s --series moneywise 021
        """,
    )
    parser.add_argument(
        "--series",
        "-s",
        choices=["zsxq", "sunzi", "moneywise"],
        default="zsxq",
        help="系列代号: zsxq / sunzi / moneywise",
    )
    parser.add_argument("lesson", help="课程编号 (如 002 / 07 / 021)")

    args = parser.parse_args()
    try:
        create_lesson_dir(args.series, args.lesson)
    except ValueError as exc:
        print(f"❌ 错误: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
