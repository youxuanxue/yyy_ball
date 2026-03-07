---
name: content-creator
description: 内容研究与规划工具：抓取竞品公众号数据、分析内容特征、LLM 辅助生成选题规划。
---

# Content Creator

本 Skill 提供内容研究与规划能力，从竞品分析到选题生成形成闭环。

核心能力从 [yyy_monkey/creator](https://github.com/youxuanxue/yyy_monkey/tree/main/creator) 迁移而来，适配 yyy_ball 的视频生产流水线。

具体脚本资产、配置格式和 LLM 要求见 `REFERENCE.md`。

## 何时使用

- 需要批量研究竞品公众号的内容风格与互动数据
- 需要基于数据驱动做系列选题规划（而非逐课规划）
- 需要用 LLM 辅助生成结构化的内容日历

## 与 lesson-content-planning 的关系

本 Skill 工作在**系列级别**，输出选题方向和内容日历；
`lesson-content-planning` 工作在**课程级别**，输出具体的 `script.json`。

典型链路：`content-creator`（选题）→ `lesson-content-planning`（脚本）→ `lesson-animation-authoring`（动画+渲染）

## 三阶段流水线

### 1. Scrape — 数据抓取

通过 Playwright 登录 `mp.weixin.qq.com`，利用内部 AJAX 接口抓取公众号文章列表和互动数据。

- 目标账号：深度抓取（全部文章 + 正文 + 阅读/点赞量）
- 参考账号：列表抓取（标题 + 采样互动数据）

```bash
uv run python .cursor/skills/content-creator/scripts/cli.py scrape
```

### 2. Analyze — 内容分析

离线分析抓取数据，生成：
- 主题分布与关键词聚类
- 标题风格画像
- 写作风格指纹（人称、表达、段落结构）
- 互动数据排名
- 参考账号交叉对标

```bash
uv run python .cursor/skills/content-creator/scripts/cli.py analyze
```

### 3. Plan — LLM 选题规划

基于分析报告 + 配置中的栏目体系，调用 LLM 生成结构化的日更规划。

```bash
uv run python .cursor/skills/content-creator/scripts/cli.py plan
```

## 前置条件

- Playwright Chromium 已安装
- 抓取阶段需要能访问 `mp.weixin.qq.com` 并扫码登录
- 规划阶段需要 LLM API，通过环境变量配置：
  - `OPENAI_API_KEY`
  - `OPENAI_BASE_URL`（如使用 DeepSeek/Qwen 等兼容 API）
  - `OPENAI_MODEL`（默认 `gpt-4o`）

## 配置

编辑 `.cursor/skills/content-creator/config/target.json` 设置目标账号、参考账号和栏目体系。
参考样例：`.cursor/skills/content-creator/config/target_sample.json`

## 依赖

运行时需要 `openai` 和 `rich` 包：

```bash
uv add openai rich
```
