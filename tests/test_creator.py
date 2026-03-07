from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from src.creator.analyzer import run_analysis
from src.creator.planner import generate_plan


class CreatorWorkflowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.workspace = Path(self.temp_dir.name)
        self.output_dir = self.workspace / "output"
        self.articles_dir = self.output_dir / "articles"
        self.articles_dir.mkdir(parents=True, exist_ok=True)

        self.config = {
            "target": {
                "name": "目标账号",
                "positioning": "把教育和财商内容做成故事化内容。",
                "style_notes": "真实、具体、不过度总结。",
                "personas": ["小学生家长", "教育内容创作者"],
            },
            "references": [{"name": "参考账号"}],
            "plan_config": {
                "duration_days": 2,
                "spare_topics": 1,
                "start_date": "2026-03-09",
            },
            "columns": [
                {"weekday": 1, "name": "成长故事", "focus": "成长冲突与决策"},
                {"weekday": 2, "name": "财商故事", "focus": "金钱选择与价值判断"},
            ],
        }

        target_articles = [
            {
                "title": "旧标题",
                "content": "爸爸和孩子在餐桌上讨论存钱和选择。",
                "create_date": "2026-03-01",
                "read_count": 1000,
                "like_count": 120,
            },
            {
                "title": "孩子第一次自己做预算",
                "content": "一次真实的预算练习，带出财商启蒙和家庭沟通。",
                "create_date": "2026-03-02",
                "read_count": 900,
                "like_count": 80,
            },
        ]
        ref_articles = [
            {
                "title": "为什么孩子总说不想学",
                "content": "老师、孩子、家长在学校场景中的冲突。",
                "create_date": "2026-03-03",
                "read_count": 3000,
                "like_count": 200,
            }
        ]
        (self.articles_dir / "目标账号.json").write_text(
            json.dumps(target_articles, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        (self.articles_dir / "参考账号.json").write_text(
            json.dumps(ref_articles, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_run_analysis_generates_expected_reports(self) -> None:
        run_analysis(self.config, self.output_dir)

        analysis_json = json.loads(
            (self.output_dir / "analysis_report.json").read_text(encoding="utf-8")
        )
        analysis_md = (self.output_dir / "analysis_report.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("style_profile", analysis_json)
        self.assertIn("recommended_directions", analysis_json)
        self.assertIn("内容分析报告", analysis_md)
        self.assertIn("目标账号", analysis_md)

    def test_generate_plan_supports_mock_response(self) -> None:
        run_analysis(self.config, self.output_dir)
        mock_response = """```json
[
  {
    "day": 1,
    "date": "03月09日",
    "weekday": "周一",
    "column": "成长故事",
    "title": "孩子第一次主动承认自己算错了",
    "outline": [
      "事情发生在晚饭后的作业时间",
      "孩子为什么一开始不愿承认",
      "我没有立刻纠正而是先追问原因"
    ],
    "scene": "餐桌旁检查数学作业时，孩子把草稿本推过来说自己好像算错了。",
    "writing_tips": [
      "保留停顿和犹豫",
      "不要急着总结道理"
    ],
    "is_spare": false
  },
  {
    "day": 2,
    "date": "03月10日",
    "weekday": "周二",
    "column": "财商故事",
    "title": "零花钱到底该不该一次发完",
    "outline": [
      "孩子为什么想一次拿完零花钱",
      "我们怎样谈预算",
      "最后达成了什么临时约定"
    ],
    "scene": "出门去文具店前，孩子要求预支整周零花钱。",
    "writing_tips": [
      "保留对话感",
      "让选择过程比结论更重要"
    ],
    "is_spare": false
  },
  {
    "day": 0,
    "date": "",
    "weekday": "",
    "column": "成长故事",
    "title": "老师一句提醒，让我改了催作业的方式",
    "outline": [
      "老师在家长群里提醒了什么",
      "我意识到自己催作业的方式太硬",
      "第二天尝试了新的提问方法"
    ],
    "scene": "晚上看家长群消息时，老师提到孩子需要先复盘再改错。",
    "writing_tips": [
      "不要把老师写成标准答案",
      "重点写自己的反思"
    ],
    "is_spare": true
  }
]
```"""
        mock_path = self.workspace / "mock_response.txt"
        mock_path.write_text(mock_response, encoding="utf-8")

        md_path, json_path = generate_plan(
            self.config,
            self.output_dir / "analysis_report.json",
            self.output_dir,
            mock_response_path=mock_path,
        )

        plan_markdown = md_path.read_text(encoding="utf-8")
        plan_json = json.loads(json_path.read_text(encoding="utf-8"))

        self.assertIn("孩子第一次主动承认自己算错了", plan_markdown)
        self.assertEqual(len(plan_json), 3)
        self.assertEqual(sum(1 for item in plan_json if item["is_spare"]), 1)


if __name__ == "__main__":
    unittest.main()
