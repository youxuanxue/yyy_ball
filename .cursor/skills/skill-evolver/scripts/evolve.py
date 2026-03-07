#!/usr/bin/env python3
"""Record skill observations and generate evolution recommendations."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


WORKSPACE_ROOT = Path(__file__).resolve().parents[4]
SKILL_ROOT = WORKSPACE_ROOT / ".cursor" / "skills" / "skill-evolver"
DEFAULT_OBSERVATIONS_DIR = SKILL_ROOT / "data" / "observations"
DEFAULT_REPORTS_DIR = SKILL_ROOT / "reports"


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def record_observation(
    *,
    series: str,
    lesson: str,
    stage: str,
    status: str,
    failure_type: str,
    affects: str,
    summary: str,
    notes: str,
    commands: list[str],
    files: list[str],
    observations_dir: Path,
) -> Path:
    timestamp = utc_now().strftime("%Y%m%dT%H%M%SZ")
    safe_failure = failure_type or "none"
    output_path = ensure_dir(observations_dir) / f"{timestamp}_{series}_{lesson}_{stage}_{safe_failure}.json"
    payload = {
        "timestamp": timestamp,
        "series": series,
        "lesson": lesson,
        "stage": stage,
        "status": status,
        "failure_type": failure_type,
        "affects": affects,
        "summary": summary,
        "notes": notes,
        "commands": commands,
        "files": files,
    }
    output_path.write_text(json.dumps(payload, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    return output_path


def load_observations(observations_dir: Path) -> list[dict[str, Any]]:
    if not observations_dir.exists():
        return []

    rows: list[dict[str, Any]] = []
    for path in sorted(observations_dir.glob("*.json")):
        rows.append(json.loads(path.read_text(encoding="utf-8")))
    return rows


def group_failed_observations(rows: list[dict[str, Any]]) -> dict[tuple[str, str], list[dict[str, Any]]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row.get("status") != "failed":
            continue
        key = (row.get("stage", "unknown"), row.get("failure_type", "unknown"))
        grouped[key].append(row)
    return dict(grouped)


def recommend_target(rows: list[dict[str, Any]]) -> str:
    series = sorted({row.get("series", "unknown") for row in rows})
    affects = {row.get("affects", "unknown") for row in rows}

    if len(series) >= 2:
        return "core"
    if affects == {"adapter"} and len(series) == 1:
        return f"adapter:{series[0]}"
    if affects == {"core"}:
        return "core-candidate"
    return "review"


def build_report(rows: list[dict[str, Any]]) -> str:
    total = len(rows)
    failed = [row for row in rows if row.get("status") == "failed"]
    grouped = group_failed_observations(rows)

    lines = [
        "# Skill Evolver Report",
        "",
        f"- total_observations: {total}",
        f"- failed_observations: {len(failed)}",
        f"- unique_failure_groups: {len(grouped)}",
        "",
        "## Recommendations",
        "",
    ]

    if not grouped:
        lines.extend(["No failed observations found.", ""])
        return "\n".join(lines)

    for (stage, failure_type), items in sorted(grouped.items()):
        impacted_series = ", ".join(sorted({item["series"] for item in items}))
        target = recommend_target(items)
        lines.extend(
            [
                f"### {stage} / {failure_type}",
                f"- count: {len(items)}",
                f"- series: {impacted_series}",
                f"- recommended_target: {target}",
                f"- sample_summary: {items[-1]['summary']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Promotion Policy",
            "",
            "- Keep single-series fixes in the adapter first.",
            "- Promote to core only after repeated cross-series evidence.",
            "- Re-run smoke validation before editing shared rules.",
            "",
        ]
    )
    return "\n".join(lines)


def summarize_observations(observations_dir: Path, output_path: Path | None) -> Path | None:
    rows = load_observations(observations_dir)
    report = build_report(rows)
    if output_path is None:
        print(report)
        return None

    ensure_dir(output_path.parent)
    output_path.write_text(report + "\n", encoding="utf-8")
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Record and summarize skill evolution observations")
    subparsers = parser.add_subparsers(dest="command", required=True)

    record_parser = subparsers.add_parser("record", help="record one lesson observation")
    record_parser.add_argument("--series", required=True)
    record_parser.add_argument("--lesson", required=True)
    record_parser.add_argument("--stage", required=True)
    record_parser.add_argument("--status", choices=["passed", "failed"], required=True)
    record_parser.add_argument("--failure-type", default="none")
    record_parser.add_argument("--affects", choices=["adapter", "core", "unknown"], default="unknown")
    record_parser.add_argument("--summary", required=True)
    record_parser.add_argument("--notes", default="")
    record_parser.add_argument("--command", dest="commands", action="append", default=[])
    record_parser.add_argument("--file", action="append", default=[])
    record_parser.add_argument(
        "--observations-dir",
        default=str(DEFAULT_OBSERVATIONS_DIR),
        help="directory for stored JSON observations",
    )

    summarize_parser = subparsers.add_parser("summarize", help="summarize recorded observations")
    summarize_parser.add_argument(
        "--observations-dir",
        default=str(DEFAULT_OBSERVATIONS_DIR),
        help="directory containing JSON observations",
    )
    summarize_parser.add_argument(
        "--output",
        default="",
        help="optional markdown output path; prints to stdout when omitted",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.command == "record":
        output_path = record_observation(
            series=args.series,
            lesson=args.lesson,
            stage=args.stage,
            status=args.status,
            failure_type=args.failure_type,
            affects=args.affects,
            summary=args.summary,
            notes=args.notes,
            commands=args.commands,
            files=args.file,
            observations_dir=Path(args.observations_dir).expanduser().resolve(),
        )
        print(f"✅ recorded observation: {output_path}")
        return

    output = Path(args.output).expanduser().resolve() if args.output else None
    report_path = summarize_observations(
        Path(args.observations_dir).expanduser().resolve(),
        output,
    )
    if report_path:
        print(f"✅ wrote report: {report_path}")


if __name__ == "__main__":
    main()
