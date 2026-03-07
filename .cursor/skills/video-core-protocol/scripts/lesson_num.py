#!/usr/bin/env python3
"""Shared helpers for lesson number normalization."""


def normalize_lesson_num(lesson_num: str, num_digits: int) -> str:
    """Normalize lesson number supporting forms like 001 / 01 / lesson001 / lesson01."""
    cleaned = lesson_num.strip()
    if cleaned.lower().startswith("lesson"):
        cleaned = cleaned[6:]

    if not cleaned.isdigit():
        raise ValueError(f"非法课程编号 '{lesson_num}'，请使用纯数字或 lesson+数字")

    value = int(cleaned)
    max_value = (10**num_digits) - 1
    if value <= 0:
        raise ValueError(f"课程编号必须大于 0，当前: {lesson_num}")
    if value > max_value:
        raise ValueError(
            f"课程编号超出范围，当前: {lesson_num}，该系列最多 {num_digits} 位（最大 {max_value}）"
        )

    return str(value).zfill(num_digits)
