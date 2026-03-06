#!/usr/bin/env python3
"""
创建新课程目录（支持日日生金、孙子兵法、MoneyWise 三个系列）

用法:
    python create_lesson.py --series zsxq 002       # 创建日日生金 lesson002 目录
    python create_lesson.py --series sunzi 07       # 创建孙子兵法 lesson07 目录
    python create_lesson.py --series moneywise 021  # 创建 MoneyWise lesson021 目录
"""

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent

# 系列配置
SERIES_CONFIG = {
    "zsxq": {
        "name": "日日生金",
        "dir": PROJECT_ROOT / "series" / "book_zsxq_100ke",
        "num_digits": 3,  # 3位数编号 (001-999)
        "script_prompt": "zsxq_100ke_script.prompt",
        "animate_prompt": "zsxq_100ke_annimate.prompt",
        "data_source": "posts.json",
    },
    "sunzi": {
        "name": "孙子兵法（小小谋略家）",
        "dir": PROJECT_ROOT / "series" / "book_sunzibingfa",
        "num_digits": 2,  # 2位数编号 (01-99)
        "script_prompt": "sunzi_script.prompt",
        "animate_prompt": "sunzi_annimate.prompt",
        "data_source": "origin.md",
    },
    "moneywise": {
        "name": "MoneyWise Global",
        "dir": PROJECT_ROOT / "series" / "moneywise_global",
        "num_digits": 3,  # 3位数编号 (001-999)
        "script_prompt": "moneywise_script.prompt",
        "animate_prompt": "moneywise_annimate.prompt",
        "data_source": "assets/zsxq/jingpin_100ke_posts.json",
    },
}


def get_series_config(series: str) -> dict:
    """获取系列配置"""
    if series not in SERIES_CONFIG:
        print(f"❌ 错误: 未知系列 '{series}'，可选: {list(SERIES_CONFIG.keys())}")
        sys.exit(1)
    return SERIES_CONFIG[series]


def normalize_lesson_num(series: str, lesson_num: str) -> str:
    """归一化课程编号，兼容 001 / 01 / lesson001 / lesson01"""
    config = get_series_config(series)
    cleaned = lesson_num.strip()
    if cleaned.lower().startswith("lesson"):
        cleaned = cleaned[6:]

    if not cleaned.isdigit():
        print(f"❌ 错误: 非法课程编号 '{lesson_num}'，请使用纯数字或 lesson+数字")
        sys.exit(1)

    return cleaned.zfill(config["num_digits"])


def create_lesson_dir(series: str, lesson_num: str):
    """创建课程目录"""
    config = get_series_config(series)
    lesson_num = normalize_lesson_num(series, lesson_num)
    lesson_dir = config["dir"] / f"lesson{lesson_num}"

    if not config["dir"].exists():
        print(f"❌ 系列目录不存在: {config['dir']}")
        sys.exit(1)

    if lesson_dir.exists():
        print(f"⚠️ 目录已存在: {lesson_dir}")
        return
    
    # 只创建目录，不生成中间文件
    lesson_dir.mkdir(parents=True)
    print(f"✅ 创建目录: {lesson_dir}")
    
    print(f"\n📝 [{config['name']}] 下一步：让 AI 生成以下文件")
    
    if series == "sunzi":
        print(f"   0. origin.md    - 准备原始素材（兵法原文+解读）")
    
    print(f"   1. script.json  - 读取 {config['data_source']} + {config['script_prompt']}")
    print(f"   2. animate.py   - 读取 script.json + {config['animate_prompt']}")
    print(f"   3. wechat.md    - 根据 script.json 生成")
    
    if series == "zsxq":
        print(f"\n💡 提示：直接告诉 AI「制作日日生金第 {lesson_num} 课」即可")
    elif series == "sunzi":
        print(f"\n💡 提示：直接告诉 AI「制作孙子兵法第 {lesson_num} 课」即可")
    else:
        print(f"\n💡 提示：直接告诉 AI「制作 MoneyWise 第 {lesson_num} 课」即可")


def main():
    parser = argparse.ArgumentParser(
        description="创建新课程目录（支持日日生金、孙子兵法、MoneyWise）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --series zsxq 002       创建日日生金 lesson002 目录
  %(prog)s --series sunzi 07       创建孙子兵法 lesson07 目录
  %(prog)s --series moneywise 021  创建 MoneyWise lesson021 目录

系列代号:
  zsxq      - 日日生金（精品100课），3位数编号
  sunzi     - 孙子兵法（小小谋略家），2位数编号
  moneywise - MoneyWise Global，3位数编号
        """
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
    create_lesson_dir(args.series, args.lesson)


if __name__ == "__main__":
    main()
