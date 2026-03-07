"""Shared path and config helpers for the creator workflow."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG_PATH = WORKSPACE_ROOT / "creator" / "config" / "target.json"
DEFAULT_OUTPUT_DIR = WORKSPACE_ROOT / "creator" / "output"


@dataclass(frozen=True)
class CreatorPaths:
    """Resolved paths used by the creator CLI."""

    config_path: Path
    output_dir: Path

    @property
    def articles_dir(self) -> Path:
        return self.output_dir / "articles"

    @property
    def analysis_path(self) -> Path:
        return self.output_dir / "analysis_report.json"

    @property
    def analysis_markdown_path(self) -> Path:
        return self.output_dir / "analysis_report.md"

    @property
    def plans_dir(self) -> Path:
        return self.output_dir / "plans"


def resolve_creator_paths(
    config_path: str | Path | None = None,
    output_dir: str | Path | None = None,
) -> CreatorPaths:
    """Resolve CLI paths with repository-aware defaults."""

    resolved_config = Path(config_path).resolve() if config_path else DEFAULT_CONFIG_PATH
    resolved_output = Path(output_dir).resolve() if output_dir else DEFAULT_OUTPUT_DIR
    return CreatorPaths(config_path=resolved_config, output_dir=resolved_output)


def load_config(config_path: Path) -> dict[str, Any]:
    """Load the creator config JSON."""

    if not config_path.exists():
        raise FileNotFoundError(
            f"creator config not found: {config_path}. "
            "Please create it from creator/config/target.json."
        )
    return json.loads(config_path.read_text(encoding="utf-8"))


def ensure_output_dir(output_dir: Path) -> None:
    """Create the output directory if needed."""

    output_dir.mkdir(parents=True, exist_ok=True)
