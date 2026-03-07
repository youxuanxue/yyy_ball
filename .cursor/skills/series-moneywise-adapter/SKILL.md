---
name: series-moneywise-adapter
description: MoneyWise Global 系列适配层，提供英文内容源、prompt、站点内容派生和发布约束。
---

# Series Adapter: MoneyWise

配套 prompt 资产、taxonomy fallback 和 site 依赖说明见 `REFERENCE.md`。

## 系列配置

- `series`: `moneywise`
- 目录：`series/moneywise_global`
- lesson 编号：3 位数，如 `001`
- script prompt：`series/prompts/moneywise_script.prompt`
- animate prompt：`series/prompts/moneywise_annimate.prompt`
- 数据源：`assets/zsxq/jingpin_100ke_posts.json`

## 特异规则

- 输出为英文 audience 的脚本与动画
- `lesson-content-planning` 在拿到发布元数据后可生成 website MDX
- 站点内容依赖 `MONEYWISE_SITE_DIR`

## 与其他 skill 的关系

- 由本 Skill 暴露英文系列的输入输出约束
- 具体的生成、渲染、发布分别交给内容规划、动画编排和执行校验层
