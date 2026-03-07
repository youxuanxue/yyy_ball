"""CLI entrypoint for the yyy_ball creator workflow."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

from .analyzer import run_analysis
from .config import ensure_output_dir
from .config import load_config
from .config import resolve_creator_paths
from .planner import generate_plan
from .scraper import GzhScraper


def _setup_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(message)s",
    )


def _emit(message: str) -> None:
    print(message)


def _add_shared_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--config",
        default=None,
        help="creator 配置文件路径，默认使用 creator/config/target.json",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="输出目录，默认使用 creator/output",
    )


def cmd_scrape(args: argparse.Namespace) -> None:
    paths = resolve_creator_paths(args.config, args.output_dir)
    ensure_output_dir(paths.output_dir)
    config = load_config(paths.config_path)
    with GzhScraper(headless=args.headless, log_fn=_emit) as scraper:
        scraper.authenticate(timeout=args.timeout)
        scraper.scrape_all(config, paths.output_dir)
    _emit(f"抓取完成，数据目录: {paths.articles_dir}")


def cmd_analyze(args: argparse.Namespace) -> None:
    paths = resolve_creator_paths(args.config, args.output_dir)
    ensure_output_dir(paths.output_dir)
    config = load_config(paths.config_path)
    run_analysis(config, paths.output_dir, log_fn=_emit)
    _emit("")
    _emit(f"请先审阅报告: {paths.analysis_markdown_path}")
    _emit(f"如需修正，可编辑: {paths.analysis_path}")


def cmd_plan(args: argparse.Namespace) -> None:
    paths = resolve_creator_paths(args.config, args.output_dir)
    ensure_output_dir(paths.output_dir)
    config = load_config(paths.config_path)
    if not args.yes:
        print(f"分析报告: {paths.analysis_path}")
        confirm = input("确认已审阅分析报告？[y/N] ").strip().lower()
        if confirm != "y":
            _emit("已取消。请先审阅分析报告后再继续。")
            return
    mock_response_path = Path(args.mock_response_file).resolve() if args.mock_response_file else None
    generate_plan(
        config,
        paths.analysis_path,
        paths.output_dir,
        log_fn=_emit,
        mock_response_path=mock_response_path,
    )


def cmd_run(args: argparse.Namespace) -> None:
    cmd_scrape(args)
    print("")
    cmd_analyze(args)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m src.creator",
        description="yyy_ball creator 工作台：抓取公众号、分析内容、生成规划。",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="输出详细日志")
    _add_shared_args(parser)

    subparsers = parser.add_subparsers(dest="command")

    scrape = subparsers.add_parser("scrape", help="抓取目标账号与参考账号文章数据")
    _add_shared_args(scrape)
    scrape.add_argument("--headless", action="store_true", help="使用无头浏览器")
    scrape.add_argument(
        "--timeout", type=int, default=120, help="等待公众号扫码登录超时秒数"
    )
    scrape.set_defaults(func=cmd_scrape)

    analyze = subparsers.add_parser("analyze", help="分析抓取到的内容并生成报告")
    _add_shared_args(analyze)
    analyze.set_defaults(func=cmd_analyze)

    plan = subparsers.add_parser("plan", help="基于分析报告生成内容规划")
    _add_shared_args(plan)
    plan.add_argument("-y", "--yes", action="store_true", help="跳过人工确认")
    plan.add_argument(
        "--mock-response-file",
        default=None,
        help="离线调试用，直接读取预置 LLM 响应文本",
    )
    plan.set_defaults(func=cmd_plan)

    run = subparsers.add_parser("run", help="执行抓取与分析，停在人工确认节点")
    _add_shared_args(run)
    run.add_argument("--headless", action="store_true", help="使用无头浏览器")
    run.add_argument(
        "--timeout", type=int, default=120, help="等待公众号扫码登录超时秒数"
    )
    run.set_defaults(func=cmd_run)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    _setup_logging(args.verbose)
    if not getattr(args, "command", None):
        parser.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()
