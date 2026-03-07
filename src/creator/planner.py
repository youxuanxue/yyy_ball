"""Generate a reviewable content plan from an approved analysis report."""

from __future__ import annotations

import json
import logging
import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Callable

import requests

logger = logging.getLogger(__name__)

WEEKDAY_NAMES = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


def _call_llm(system_prompt: str, user_prompt: str) -> str:
    base_url = os.environ.get("OPENAI_API_BASE", os.environ.get("OPENAI_BASE_URL", ""))
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        raise RuntimeError(
            "未配置 LLM API key。请设置 OPENAI_API_KEY；"
            "若使用兼容 API，请额外设置 OPENAI_BASE_URL。"
        )

    api_root = base_url.rstrip("/") if base_url else "https://api.openai.com/v1"
    model = os.environ.get("OPENAI_MODEL", "gpt-4o")
    response = requests.post(
        f"{api_root}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.8,
            "max_tokens": 8000,
        },
        timeout=180,
    )
    response.raise_for_status()
    payload = response.json()
    choices = payload.get("choices", [])
    if not choices:
        raise ValueError("LLM 响应缺少 choices 字段")
    return choices[0].get("message", {}).get("content", "") or ""


def _render_personas(target: dict) -> str:
    personas = target.get("personas", [])
    family = target.get("family", {})
    lines = []
    if personas:
        lines.extend(f"- {item}" for item in personas)
    for value in family.values():
        if value:
            lines.append(f"- {value}")
    return "\n".join(lines) if lines else "- 未配置"


def _build_system_prompt(config: dict, analysis: dict) -> str:
    target = config.get("target", {})
    style_profile = analysis.get("style_profile", {})
    covered_topics = analysis.get("covered_topics", [])
    recommendations = analysis.get("recommended_directions", [])
    target_rules = config.get("target_rules", {})

    ref_top_articles = []
    for insight in analysis.get("reference_insights", []):
        for article in insight.get("top_articles", [])[:3]:
            ref_top_articles.append(f"- [{insight['name']}] {article['title']}")

    must_have = target_rules.get("must_have_themes", target.get("must_have_themes", []))
    forbidden = target_rules.get(
        "forbidden_themes", target.get("forbidden_themes", [])
    )

    return f"""你是一个内容策划编辑，负责为「{target.get('name', '目标账号')}」生成高质量内容规划。

## 账号定位
{target.get('positioning', '')}

## 受众/角色
{_render_personas(target)}

## 风格要求
- {target.get('style_notes', '')}
- 叙事人称: {style_profile.get('narrative_voice', '混合人称')}
- 平均文章长度: {style_profile.get('avg_article_length', 1200)} 字左右
- 标题平均长度: {style_profile.get('title_avg_length', 16)} 字
- 高频表达: {', '.join(item[0] for item in style_profile.get('top_expressions', [])[:5])}

## 已覆盖主题（避免重复）
{', '.join(covered_topics) if covered_topics else '暂无'}

## 优先强化主题
{', '.join(must_have) if must_have else '暂无'}

## 应避免主题
{', '.join(forbidden) if forbidden else '暂无'}

## 参考账号高互动样本
{chr(10).join(ref_top_articles) if ref_top_articles else '暂无'}

## 方向建议
{chr(10).join(f'- {item}' for item in recommendations) if recommendations else '- 暂无'}

## 核心约束
1. 不要输出套路化 AI 文风，不要使用空泛总结句。
2. 场景必须具体到人物、地点、情境，不要泛泛而谈。
3. 标题要自然、可执行、便于后续扩写成图文或短视频脚本。
4. 每个提纲 3-5 点，前后有叙事推进。
5. 选题既要保持定位一致，也要避免和历史内容高度重复。"""


def _build_column_prompt(columns: list[dict]) -> str:
    if not columns:
        return "## 栏目体系\n- 当前未配置固定栏目，可按主题自由分配。"
    lines = ["## 栏目体系（每周固定轮转）"]
    for column in columns:
        weekday = column.get("weekday", 0)
        weekday_name = WEEKDAY_NAMES[weekday - 1] if 1 <= weekday <= 7 else f"第{weekday}天"
        lines.append(f"- {weekday_name}·{column['name']}: {column['focus']}")
    return "\n".join(lines)


def _build_generation_prompt(
    start_date: datetime,
    days: int,
    columns: list[dict],
    existing_titles: list[str],
    spare_count: int,
) -> str:
    dates_info = []
    for idx in range(days):
        current = start_date + timedelta(days=idx)
        weekday = current.isoweekday()
        column = next((item for item in columns if item.get("weekday") == weekday), None)
        column_name = column["name"] if column else "自由选题"
        dates_info.append(
            f"Day {idx + 1} ({current.strftime('%m月%d日')} {WEEKDAY_NAMES[weekday - 1]}) — {column_name}"
        )

    existing_titles_block = ""
    if existing_titles:
        existing_titles_block = "\n## 已发内容标题（必须避免重复）\n"
        existing_titles_block += "\n".join(f"- {title}" for title in existing_titles)

    return f"""请为以下 {days} 天各生成 1 个选题，另生成 {spare_count} 个备用选题。

## 日期与栏目安排
{chr(10).join(dates_info)}
{existing_titles_block}

## 输出格式
严格输出一个 JSON 数组，每项包含以下字段：
- day: 正常选题使用 1..{days}，备用选题使用 0
- date: 例如 "03月03日"，备用选题留空
- weekday: 例如 "周一"，备用选题留空
- column: 栏目名称
- title: 标题
- outline: 3-5 条提纲
- scene: 具体故事场景或切入情境
- writing_tips: 2-4 条执行提醒
- is_spare: true/false

关键要求：
1. 正常选题共 {days} 条，备用选题共 {spare_count} 条。
2. 不同栏目之间要体现差异。
3. 标题不能与历史标题重复或高度相似。
4. 如果是短视频/图文双用选题，也要先按图文叙事结构组织。
5. 只输出 JSON，不要附带解释。"""


def _parse_topics_from_response(text: str, log_fn: Callable[[str], None]) -> list[dict]:
    match = re.search(r"```(?:json)?\s*\n(\[[\s\S]*?\])\s*\n```", text)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError as exc:
            log_fn(f"JSON 解析失败（代码块）: {exc}")

    match = re.search(r"\[[\s\S]*\]", text)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError as exc:
            log_fn(f"JSON 解析失败（裸数组）: {exc}")

    return []


def _validate_topics(
    topics: list[dict],
    days: int,
    spare_count: int,
    existing_titles: list[str],
) -> list[str]:
    errors = []
    daily_topics = [item for item in topics if not item.get("is_spare")]
    spare_topics = [item for item in topics if item.get("is_spare")]
    if len(daily_topics) != days:
        errors.append(f"正常选题数量不正确: 期望 {days}，实际 {len(daily_topics)}")
    if len(spare_topics) != spare_count:
        errors.append(f"备用选题数量不正确: 期望 {spare_count}，实际 {len(spare_topics)}")

    seen_titles = set()
    existing_title_set = {title.strip() for title in existing_titles if title.strip()}
    for idx, topic in enumerate(topics, start=1):
        title = topic.get("title", "").strip()
        if not title:
            errors.append(f"第 {idx} 条缺少标题")
        elif title in seen_titles:
            errors.append(f"存在重复标题: {title}")
        else:
            seen_titles.add(title)

        if title in existing_title_set:
            errors.append(f"标题与历史内容重复: {title}")

        for field in ["column", "scene"]:
            if not topic.get(field):
                errors.append(f"第 {idx} 条缺少字段: {field}")

        outline = topic.get("outline", [])
        if not isinstance(outline, list) or not (3 <= len(outline) <= 5):
            errors.append(f"第 {idx} 条提纲数量异常，应为 3-5 条")

    return errors


def _build_plan_markdown(topics: list[dict], start_date: datetime, config: dict) -> str:
    target_name = config.get("target", {}).get("name", "目标账号")
    plan_config = config.get("plan_config", {})
    days = plan_config.get("duration_days", 30)
    end_date = start_date + timedelta(days=days - 1)

    lines = [
        f"# 「{target_name}」内容规划",
        "",
        (
            f"> 规划周期: {start_date.strftime('%Y年%m月%d日')} - "
            f"{end_date.strftime('%Y年%m月%d日')}"
        ),
        f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
    ]

    daily_topics = [item for item in topics if not item.get("is_spare")]
    spare_topics = [item for item in topics if item.get("is_spare")]
    current_week = None
    lines.append(f"## 日常选题（{len(daily_topics)} 条）")
    lines.append("")

    for topic in sorted(daily_topics, key=lambda item: item.get("day", 0)):
        day = topic.get("day", 0)
        week_num = (day - 1) // 7 + 1
        if week_num != current_week:
            current_week = week_num
            lines.extend(["---", "", f"### 第 {week_num} 周", ""])
        lines.extend(
            [
                f"#### Day {day} ({topic.get('date', '')} {topic.get('weekday', '')}) — {topic.get('column', '')}",
                "",
                f"**标题**: {topic.get('title', '')}",
                "",
                "**提纲**:",
            ]
        )
        for index, outline in enumerate(topic.get("outline", []), start=1):
            lines.append(f"{index}. {outline}")
        lines.extend(
            [
                "",
                f"**故事场景**: {topic.get('scene', '')}",
                "",
                "**写作要点**:",
            ]
        )
        for tip in topic.get("writing_tips", []):
            lines.append(f"- {tip}")
        lines.append("")

    if spare_topics:
        lines.extend(["---", "", f"## 备用选题（{len(spare_topics)} 条）", ""])
        for index, topic in enumerate(spare_topics, start=1):
            lines.extend(
                [
                    f"#### 备用 {index} — {topic.get('column', '自由选题')}",
                    "",
                    f"**标题**: {topic.get('title', '')}",
                    "",
                    "**提纲**:",
                ]
            )
            for outline_index, outline in enumerate(topic.get("outline", []), start=1):
                lines.append(f"{outline_index}. {outline}")
            lines.extend(["", f"**故事场景**: {topic.get('scene', '')}", ""])

    lines.extend(
        [
            "---",
            "",
            "*本规划由 yyy_ball 的 creator 工作台生成，正式发布前请结合真实素材复核。*",
        ]
    )
    return "\n".join(lines)


def generate_plan(
    config: dict,
    analysis_path: Path,
    output_dir: Path,
    log_fn: Callable[[str], None] | None = None,
    mock_response_path: Path | None = None,
) -> tuple[Path, Path]:
    emit = log_fn or (lambda message: logger.info(message))
    if not analysis_path.exists():
        raise FileNotFoundError(f"未找到分析报告: {analysis_path}")

    analysis = json.loads(analysis_path.read_text(encoding="utf-8"))
    plan_config = config.get("plan_config", {})
    days = plan_config.get("duration_days", 30)
    spare = plan_config.get("spare_topics", 5)
    columns = analysis.get("suggested_columns") or config.get("columns", [])
    start_date_str = plan_config.get("start_date", "auto")
    start_date = (
        datetime.now() + timedelta(days=1)
        if start_date_str == "auto"
        else datetime.strptime(start_date_str, "%Y-%m-%d")
    )
    existing_titles = [
        article.get("title", "")
        for article in analysis.get("target", {}).get("article_list", [])
        if article.get("title")
    ]

    emit("准备生成内容规划...")
    emit(f"  起始日期: {start_date.strftime('%Y-%m-%d')}")
    emit(f"  规划天数: {days}")
    emit(f"  备用选题: {spare}")

    if mock_response_path:
        emit(f"  使用离线响应文件: {mock_response_path}")
        raw_text = mock_response_path.read_text(encoding="utf-8")
    else:
        system_prompt = _build_system_prompt(config, analysis)
        system_prompt += "\n\n" + _build_column_prompt(columns)
        user_prompt = _build_generation_prompt(
            start_date, days, columns, existing_titles, spare
        )
        raw_text = _call_llm(system_prompt, user_prompt)

    topics = _parse_topics_from_response(raw_text, emit)
    if not topics:
        fallback_path = output_dir / "plans" / "raw_response.txt"
        fallback_path.parent.mkdir(parents=True, exist_ok=True)
        fallback_path.write_text(raw_text, encoding="utf-8")
        raise ValueError(f"无法解析 LLM 输出，原始响应已保存到: {fallback_path}")

    validation_errors = _validate_topics(topics, days, spare, existing_titles)
    if validation_errors:
        validation_path = output_dir / "plans" / "validation_errors.txt"
        validation_path.parent.mkdir(parents=True, exist_ok=True)
        validation_path.write_text("\n".join(validation_errors), encoding="utf-8")
        raise ValueError(
            "规划结果未通过校验，详情见: "
            f"{validation_path}"
        )

    plans_dir = output_dir / "plans"
    plans_dir.mkdir(parents=True, exist_ok=True)
    filename = f"plan_{start_date.strftime('%Y%m%d')}_{days}d"
    md_path = plans_dir / f"{filename}.md"
    json_path = plans_dir / f"{filename}.json"
    md_path.write_text(
        _build_plan_markdown(topics, start_date, config), encoding="utf-8"
    )
    json_path.write_text(
        json.dumps(topics, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    emit(f"规划已生成: {md_path}")
    emit(f"结构化结果: {json_path}")
    return md_path, json_path
