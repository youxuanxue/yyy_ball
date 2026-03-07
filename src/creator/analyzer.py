"""Analyze scraped article data and emit a reviewable report."""

from __future__ import annotations

import json
import logging
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable

logger = logging.getLogger(__name__)


DEFAULT_TOPIC_KEYWORDS = {
    "谋略/兵法": [
        "兵法",
        "谋略",
        "战术",
        "策略",
        "孙子",
        "将军",
        "打仗",
        "布局",
        "选择",
        "判断",
    ],
    "财商/理财": [
        "财商",
        "理财",
        "存钱",
        "金钱",
        "投资",
        "预算",
        "消费",
        "赚钱",
        "复利",
        "现金流",
    ],
    "学习/教育": [
        "学习",
        "教育",
        "课堂",
        "老师",
        "学校",
        "阅读",
        "写作",
        "数学",
        "语文",
        "英语",
        "孩子",
    ],
    "成长/心理": [
        "成长",
        "心理",
        "情绪",
        "焦虑",
        "挫折",
        "勇气",
        "坚持",
        "习惯",
        "自信",
        "拖延",
    ],
    "家庭/亲子": [
        "爸爸",
        "妈妈",
        "家长",
        "亲子",
        "兄妹",
        "家庭",
        "陪伴",
        "育儿",
        "沟通",
        "相处",
    ],
    "故事/案例": [
        "故事",
        "案例",
        "经历",
        "那天",
        "后来",
        "一次",
        "一个孩子",
        "一个家庭",
    ],
    "技术/工具": [
        "AI",
        "自动化",
        "工具",
        "代码",
        "Python",
        "脚本",
        "系统",
        "流程",
        "效率",
    ],
    "国际/英语": [
        "英语",
        "global",
        "world",
        "海外",
        "国际",
        "表达",
        "英文",
    ],
}

DEFAULT_ENTITY_PATTERNS = {
    "people": [
        r"爸爸",
        r"妈妈",
        r"老师",
        r"同学",
        r"孩子",
        r"家长",
        r"儿子",
        r"女儿",
    ],
    "scenes": [
        r"学校",
        r"教室",
        r"家里",
        r"餐桌",
        r"书房",
        r"操场",
        r"公园",
        r"办公室",
        r"地铁",
        r"车上",
    ],
}


def _safe_average(values: list[int]) -> int:
    return round(sum(values) / len(values)) if values else 0


@dataclass
class AnalysisContext:
    topic_keywords: dict[str, list[str]]
    entity_patterns: dict[str, list[str]]


class ContentAnalyzer:
    """Config-aware analyzer for scraped article data."""

    def __init__(self, config: dict):
        analysis_cfg = config.get("analysis", {})
        self.context = AnalysisContext(
            topic_keywords=analysis_cfg.get("topic_keywords", DEFAULT_TOPIC_KEYWORDS),
            entity_patterns=analysis_cfg.get("entity_patterns", DEFAULT_ENTITY_PATTERNS),
        )

    def classify_topic(self, title: str, content: str = "") -> list[str]:
        text = f"{title} {content[:500]}".lower()
        topics = []
        for topic, keywords in self.context.topic_keywords.items():
            if any(keyword.lower() in text for keyword in keywords):
                topics.append(topic)
        return topics or ["其他"]

    def analyze_title_style(self, titles: list[str]) -> dict:
        lengths = [len(t) for t in titles]
        total = len(titles) or 1
        return {
            "avg_length": round(sum(lengths) / total, 1) if lengths else 0,
            "min_length": min(lengths) if lengths else 0,
            "max_length": max(lengths) if lengths else 0,
            "question_ratio": round(
                sum(1 for t in titles if "？" in t or "?" in t) / total, 2
            ),
            "number_ratio": round(
                sum(1 for t in titles if re.search(r"\d", t)) / total, 2
            ),
            "colon_ratio": round(
                sum(1 for t in titles if "：" in t or ":" in t) / total, 2
            ),
            "ellipsis_ratio": round(
                sum(1 for t in titles if "…" in t or "..." in t) / total, 2
            ),
        }

    def analyze_writing_style(self, articles: list[dict]) -> dict:
        contents = [a.get("content", "") for a in articles if a.get("content")]
        if not contents:
            return {"note": "无正文内容，无法分析写作风格"}

        avg_length = sum(len(c) for c in contents) / len(contents)
        first_person = sum(
            len(re.findall(r"我[^们]|我的|我们", content)) for content in contents
        )

        expressions = Counter()
        common_phrases = [
            "其实",
            "后来",
            "结果",
            "没想到",
            "当时",
            "发现",
            "突然",
            "终于",
            "但是",
            "然后",
            "于是",
        ]
        for content in contents:
            for phrase in common_phrases:
                count = content.count(phrase)
                if count:
                    expressions[phrase] += count

        para_counts = [
            len([paragraph for paragraph in content.split("\n") if paragraph.strip()])
            for content in contents
        ]
        endings = []
        for content in contents:
            lines = [line.strip() for line in content.strip().split("\n") if line.strip()]
            if lines:
                endings.append(lines[-1][:50])

        return {
            "article_count": len(contents),
            "avg_content_length": round(avg_length),
            "first_person_freq": first_person,
            "top_expressions": expressions.most_common(10),
            "avg_paragraph_count": round(sum(para_counts) / len(para_counts), 1)
            if para_counts
            else 0,
            "sample_endings": endings[:5],
        }

    def analyze_interaction(self, articles: list[dict]) -> dict:
        with_data = [
            article
            for article in articles
            if article.get("read_count", 0) > 0 or article.get("like_count", 0) > 0
        ]
        if not with_data:
            return {"note": "无互动数据"}

        sorted_by_read = sorted(
            with_data, key=lambda item: item.get("read_count", 0), reverse=True
        )
        return {
            "articles_with_data": len(with_data),
            "avg_read": _safe_average([a["read_count"] for a in with_data]),
            "max_read": max(a["read_count"] for a in with_data),
            "avg_like": _safe_average([a["like_count"] for a in with_data]),
            "max_like": max(a["like_count"] for a in with_data),
            "top_articles": [
                {
                    "title": article.get("title", ""),
                    "read_count": article.get("read_count", 0),
                    "like_count": article.get("like_count", 0),
                    "create_date": article.get("create_date", ""),
                }
                for article in sorted_by_read[:10]
            ],
        }

    def extract_entities(self, articles: list[dict]) -> dict:
        entities = {}
        for bucket, patterns in self.context.entity_patterns.items():
            counter = Counter()
            for article in articles:
                text = f"{article.get('title', '')} {article.get('content', '')}"
                for pattern in patterns:
                    count = len(re.findall(pattern, text))
                    if count:
                        counter[pattern] += count
            entities[bucket] = dict(counter.most_common())
        return entities

    def analyze_target(self, articles: list[dict]) -> dict:
        topic_counter = Counter()
        for article in articles:
            for topic in self.classify_topic(
                article.get("title", ""), article.get("content", "")
            ):
                topic_counter[topic] += 1

        return {
            "total_articles": len(articles),
            "topic_distribution": dict(topic_counter.most_common()),
            "title_style": self.analyze_title_style(
                [article.get("title", "") for article in articles]
            ),
            "writing_style": self.analyze_writing_style(articles),
            "interaction": self.analyze_interaction(articles),
            "mentioned_entities": self.extract_entities(articles),
            "article_list": [
                {
                    "title": article.get("title", ""),
                    "create_date": article.get("create_date", ""),
                    "topics": self.classify_topic(
                        article.get("title", ""), article.get("content", "")
                    ),
                    "read_count": article.get("read_count", 0),
                    "like_count": article.get("like_count", 0),
                }
                for article in articles
            ],
        }

    def analyze_reference(self, articles: list[dict], name: str) -> dict:
        topic_counter = Counter()
        topic_reads = defaultdict(list)
        for article in articles:
            topics = self.classify_topic(article.get("title", ""), article.get("content", ""))
            for topic in topics:
                topic_counter[topic] += 1
                if article.get("read_count", 0) > 0:
                    topic_reads[topic].append(article["read_count"])

        return {
            "name": name,
            "total_articles": len(articles),
            "topic_distribution": dict(topic_counter.most_common()),
            "topic_avg_reads": {
                topic: _safe_average(reads) for topic, reads in topic_reads.items() if reads
            },
            "title_style": self.analyze_title_style(
                [article.get("title", "") for article in articles]
            ),
            "interaction": self.analyze_interaction(articles),
        }

    def build_style_profile(self, target: dict) -> dict:
        writing_style = target.get("writing_style", {})
        title_style = target.get("title_style", {})
        return {
            "narrative_voice": (
                "第一人称为主"
                if writing_style.get("first_person_freq", 0) > 5
                else "混合人称"
            ),
            "avg_article_length": writing_style.get("avg_content_length", 0),
            "title_avg_length": title_style.get("avg_length", 0),
            "title_features": {
                "prefers_questions": title_style.get("question_ratio", 0) > 0.3,
                "uses_numbers": title_style.get("number_ratio", 0) > 0.3,
                "uses_colons": title_style.get("colon_ratio", 0) > 0.3,
            },
            "top_expressions": writing_style.get("top_expressions", []),
            "avg_paragraphs": writing_style.get("avg_paragraph_count", 0),
        }

    def build_reference_insights(self, refs: list[dict]) -> list[dict]:
        insights = []
        for ref in refs:
            top_topics = sorted(
                ref.get("topic_avg_reads", {}).items(),
                key=lambda item: item[1],
                reverse=True,
            )[:5]
            insights.append(
                {
                    "name": ref["name"],
                    "top_topics_by_read": [
                        {"topic": topic, "avg_read": avg_read}
                        for topic, avg_read in top_topics
                    ],
                    "top_articles": ref.get("interaction", {}).get("top_articles", [])[:5],
                    "total_articles": ref["total_articles"],
                }
            )
        return insights

    def build_recommendations(self, target: dict, refs: list[dict]) -> list[str]:
        covered = set(target.get("topic_distribution", {}).keys())
        ref_popular = Counter()
        for ref in refs:
            for topic, avg_read in ref.get("topic_avg_reads", {}).items():
                ref_popular[topic] += avg_read

        recommendations = []
        for topic, _score in ref_popular.most_common():
            if topic not in covered and topic != "其他":
                recommendations.append(f"新方向「{topic}」：参考账号该主题互动表现更强。")

        top_articles = target.get("interaction", {}).get("top_articles", [])
        if top_articles:
            top_topics = set()
            for article in top_articles[:3]:
                top_topics.update(self.classify_topic(article.get("title", "")))
            for topic in sorted(top_topics):
                if topic != "其他":
                    recommendations.append(f"延续强项「{topic}」：目标账号已有较好互动表现。")

        return recommendations or ["建议围绕已有定位保持主题轮换，并逐步试验新方向。"]

    def build_markdown_report(self, target: dict, refs: list[dict], config: dict) -> str:
        target_name = config.get("target", {}).get("name", "目标账号")
        lines = [
            "# 内容分析报告",
            "",
            f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
            f"## 一、目标账号「{target_name}」深度分析",
            "",
            f"- 历史文章总数: **{target.get('total_articles', 0)}** 篇",
            "",
            "### 1.1 主题分布",
        ]

        for topic, count in target.get("topic_distribution", {}).items():
            lines.append(f"- {topic}: {count} 篇")
        lines.extend(["", "### 1.2 标题风格"])

        title_style = target.get("title_style", {})
        lines.extend(
            [
                f"- 平均标题长度: {title_style.get('avg_length', 0)} 字",
                f"- 疑问句比例: {title_style.get('question_ratio', 0):.0%}",
                f"- 含数字比例: {title_style.get('number_ratio', 0):.0%}",
                f"- 冒号比例: {title_style.get('colon_ratio', 0):.0%}",
                "",
                "### 1.3 写作风格",
            ]
        )

        writing_style = target.get("writing_style", {})
        if writing_style.get("note"):
            lines.append(f"- {writing_style['note']}")
        else:
            lines.extend(
                [
                    f"- 平均文章长度: {writing_style.get('avg_content_length', 0)} 字",
                    f"- 平均段落数: {writing_style.get('avg_paragraph_count', 0)}",
                    f"- 第一人称频次: {writing_style.get('first_person_freq', 0)}",
                ]
            )
            expressions = writing_style.get("top_expressions", [])
            if expressions:
                lines.append(
                    "- 高频表达: "
                    + "、".join(f"「{item[0]}」({item[1]}次)" for item in expressions[:8])
                )
        lines.extend(["", "### 1.4 已使用素材"])

        entities = target.get("mentioned_entities", {})
        for bucket, values in entities.items():
            if values:
                lines.append(
                    f"- {bucket}: " + ", ".join(f"{name}({count}次)" for name, count in values.items())
                )

        lines.extend(["", "### 1.5 互动表现"])
        interaction = target.get("interaction", {})
        if interaction.get("note"):
            lines.append(f"- {interaction['note']}")
        else:
            lines.extend(
                [
                    f"- 平均阅读量: {interaction.get('avg_read', 0)}",
                    f"- 最高阅读量: {interaction.get('max_read', 0)}",
                    f"- 平均点赞数: {interaction.get('avg_like', 0)}",
                ]
            )

        lines.extend(["", "### 1.6 历史文章清单", "", "| 日期 | 标题 | 主题 | 阅读 | 点赞 |", "|------|------|------|------|------|"])
        for article in target.get("article_list", []):
            lines.append(
                f"| {article.get('create_date', '')} | {article.get('title', '')} | "
                f"{'/'.join(article.get('topics', []))} | {article.get('read_count', 0)} | "
                f"{article.get('like_count', 0)} |"
            )

        lines.extend(["", "## 二、参考账号分析", ""])
        for ref in refs:
            lines.extend([f"### {ref['name']}", "", f"- 文章总数: {ref['total_articles']} 篇"])
            top_topics = sorted(
                ref.get("topic_distribution", {}).items(),
                key=lambda item: item[1],
                reverse=True,
            )[:3]
            if top_topics:
                lines.append(
                    "- 主要主题: " + ", ".join(f"{topic}({count}篇)" for topic, count in top_topics)
                )
            ref_interaction = ref.get("interaction", {})
            if ref_interaction.get("avg_read"):
                lines.append(f"- 平均阅读量: {ref_interaction['avg_read']}")
            top_articles = ref_interaction.get("top_articles", [])
            if top_articles:
                lines.append("")
                lines.append("**Top 高互动文章**")
                lines.append("")
                for idx, article in enumerate(top_articles[:10], start=1):
                    lines.append(
                        f"{idx}. 「{article['title']}」 阅读 {article.get('read_count', 0)} / "
                        f"点赞 {article.get('like_count', 0)}"
                    )
            lines.append("")

        lines.extend(["## 三、建议的内容方向", ""])
        for rec in self.build_recommendations(target, refs):
            lines.append(f"- {rec}")

        lines.extend(["", "## 四、建议栏目体系", ""])
        columns = config.get("columns", [])
        if columns:
            lines.extend(["| 星期 | 栏目 | 聚焦方向 |", "|------|------|----------|"])
            weekdays = ["", "周一", "周二", "周三", "周四", "周五", "周六", "周日"]
            for column in columns:
                weekday = column.get("weekday", 0)
                weekday_name = weekdays[weekday] if weekday < len(weekdays) else f"第{weekday}天"
                lines.append(
                    f"| {weekday_name} | {column.get('name', '')} | {column.get('focus', '')} |"
                )
        else:
            lines.append("- 当前未配置固定栏目，建议先审阅主题结构再决定栏目轮转。")

        lines.extend(
            [
                "",
                "---",
                "",
                "**请先审阅分析结论，再运行 `plan` 生成正式规划。**",
            ]
        )
        return "\n".join(lines)

    def generate_report(
        self,
        target_analysis: dict,
        reference_analyses: list[dict],
        config: dict,
        output_dir: Path,
    ) -> tuple[Path, Path]:
        output_dir.mkdir(parents=True, exist_ok=True)
        report = {
            "generated_at": datetime.now().isoformat(),
            "target": target_analysis,
            "references": reference_analyses,
            "style_profile": self.build_style_profile(target_analysis),
            "covered_topics": list(target_analysis.get("topic_distribution", {}).keys()),
            "reference_insights": self.build_reference_insights(reference_analyses),
            "recommended_directions": self.build_recommendations(
                target_analysis, reference_analyses
            ),
            "suggested_columns": config.get("columns", []),
        }
        json_path = output_dir / "analysis_report.json"
        md_path = output_dir / "analysis_report.md"
        json_path.write_text(
            json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        md_path.write_text(
            self.build_markdown_report(target_analysis, reference_analyses, config),
            encoding="utf-8",
        )
        return json_path, md_path


def run_analysis(config: dict, output_dir: Path, log_fn: Callable[[str], None] | None = None) -> None:
    """Run the full analysis workflow."""

    emit = log_fn or (lambda message: logger.info(message))
    articles_dir = output_dir / "articles"
    target_name = config["target"]["name"]
    target_file = articles_dir / f"{target_name}.json"
    if not target_file.exists():
        raise FileNotFoundError(f"未找到目标账号数据: {target_file}")

    analyzer = ContentAnalyzer(config)
    emit(f"分析目标账号: {target_name}")
    target_articles = json.loads(target_file.read_text(encoding="utf-8"))
    target_analysis = analyzer.analyze_target(target_articles)

    ref_analyses = []
    for ref in config.get("references", []):
        ref_name = ref["name"]
        ref_file = articles_dir / f"{ref_name}.json"
        if not ref_file.exists():
            emit(f"未找到参考账号数据，跳过: {ref_file}")
            continue
        emit(f"分析参考账号: {ref_name}")
        ref_articles = json.loads(ref_file.read_text(encoding="utf-8"))
        ref_analyses.append(analyzer.analyze_reference(ref_articles, ref_name))

    emit("生成分析报告...")
    json_path, md_path = analyzer.generate_report(
        target_analysis, ref_analyses, config, output_dir
    )
    emit(f"分析完成: {md_path}")
    emit(f"结构化报告: {json_path}")
