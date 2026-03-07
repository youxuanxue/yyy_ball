#!/usr/bin/env python3
"""
内容研究与规划工具 CLI

用法:
    uv run python .cursor/skills/content-creator/scripts/cli.py scrape
    uv run python .cursor/skills/content-creator/scripts/cli.py analyze
    uv run python .cursor/skills/content-creator/scripts/cli.py plan
    uv run python .cursor/skills/content-creator/scripts/cli.py run
"""

import argparse
import json
import logging
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
CONFIG_PATH = SKILL_DIR / "config" / "target.json"
OUTPUT_DIR = SKILL_DIR / "output"

try:
    from rich.console import Console
    from rich.logging import RichHandler
    from rich.panel import Panel

    console = Console()
    HAS_RICH = True
except ImportError:
    HAS_RICH = False
    console = None

if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))


def _setup_logging(verbose: bool = False):
    level = logging.DEBUG if verbose else logging.INFO
    if HAS_RICH:
        logging.basicConfig(
            level=level,
            format="%(message)s",
            handlers=[RichHandler(console=console, show_time=False, show_path=False)],
        )
    else:
        logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def _load_config() -> dict:
    if not CONFIG_PATH.exists():
        _log(f"配置文件不存在: {CONFIG_PATH}")
        _log(f"请从 config/target_sample.json 复制并编辑为 config/target.json")
        sys.exit(1)
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def _log(msg: str):
    if HAS_RICH:
        console.print(msg)
    else:
        print(msg)


def cmd_scrape(args):
    """抓取公众号文章数据"""
    from scraper import GzhScraper

    config = _load_config()

    if HAS_RICH:
        console.print(Panel("公众号文章抓取", style="bold blue"))
    _log(f"目标账号: {config['target']['name']}")
    refs = [r["name"] for r in config.get("references", [])]
    _log(f"参考账号: {', '.join(refs)}")

    with GzhScraper(headless=args.headless, log_fn=_log) as scraper:
        scraper.authenticate(timeout=args.timeout)
        scraper.scrape_all(config, OUTPUT_DIR)

    _log(f"抓取完成！数据保存在 {OUTPUT_DIR / 'articles'}")


def cmd_analyze(args):
    """分析数据并生成报告"""
    from analyzer import run_analysis

    config = _load_config()

    if HAS_RICH:
        console.print(Panel("内容分析", style="bold blue"))
    run_analysis(config, OUTPUT_DIR, log_fn=_log)

    report_path = OUTPUT_DIR / "analysis_report.md"
    if report_path.exists():
        _log(f"\n分析完成！请审阅报告: {report_path}")
        _log(f"确认无误后，运行 plan 命令生成日更规划。")


def cmd_plan(args):
    """生成日更内容规划"""
    from planner import generate_plan

    config = _load_config()
    analysis_path = OUTPUT_DIR / "analysis_report.json"

    if not analysis_path.exists():
        _log("未找到分析报告，请先运行 analyze 命令")
        sys.exit(1)

    if HAS_RICH:
        console.print(Panel("日更规划生成", style="bold blue"))

    if not args.yes:
        _log(f"分析报告: {analysis_path}")
        confirm = input("确认已审阅分析报告？[y/N] ").strip().lower()
        if confirm != "y":
            _log("已取消。请先审阅分析报告后再运行。")
            return

    generate_plan(config, analysis_path, OUTPUT_DIR, log_fn=_log)


def cmd_run(args):
    """一键执行 scrape + analyze"""
    if HAS_RICH:
        console.print(Panel("一键执行: 抓取 + 分析", style="bold blue"))
    cmd_scrape(args)
    cmd_analyze(args)


def main():
    parser = argparse.ArgumentParser(
        prog="content-creator",
        description="内容研究与规划工具 — 抓取、分析、生成日更规划",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="详细日志输出")

    subparsers = parser.add_subparsers(dest="command", help="子命令")

    p_scrape = subparsers.add_parser("scrape", help="抓取公众号文章数据")
    p_scrape.add_argument("--headless", action="store_true", help="无头模式")
    p_scrape.add_argument("--timeout", type=int, default=120, help="等待扫码登录超时秒数")

    subparsers.add_parser("analyze", help="分析数据并生成报告")

    p_plan = subparsers.add_parser("plan", help="生成日更内容规划")
    p_plan.add_argument("-y", "--yes", action="store_true", help="跳过确认直接生成")

    p_run = subparsers.add_parser("run", help="一键执行 scrape + analyze")
    p_run.add_argument("--headless", action="store_true", help="无头模式")
    p_run.add_argument("--timeout", type=int, default=120, help="等待扫码登录超时秒数")

    args = parser.parse_args()
    _setup_logging(args.verbose)

    if not args.command:
        parser.print_help()
        return

    commands = {
        "scrape": cmd_scrape,
        "analyze": cmd_analyze,
        "plan": cmd_plan,
        "run": cmd_run,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
