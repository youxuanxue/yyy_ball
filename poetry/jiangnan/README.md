# 🌸 《江南》古诗信息图项目

## 📁 文件说明

| 文件 | 说明 |
|------|------|
| `poem_info.md` | 古诗的完整信息，包含原文、背景、含义、意义等 |
| `infographic_design.md` | 信息图设计方案，包含布局、配色、元素清单 |
| `ai_prompts.md` | AI 生成图片的提示词，可用于 Midjourney/DALL-E 等 |
| `tools_comparison.md` | 开源工具对比，推荐最适合的方案 |
| `generator_pillow.py` | Python + Pillow 自动生成器（推荐） |
| `generator_html.py` | HTML + Playwright 自动生成器 |
| `USAGE.md` | 详细使用说明和定制指南 |

---

## 📜 古诗原文

**《江南》** — 汉乐府民歌

> 江南可采莲，莲叶何田田。
> 鱼戏莲叶间。
> 鱼戏莲叶东，鱼戏莲叶西，
> 鱼戏莲叶南，鱼戏莲叶北。

---

## 🎯 设计目标

- **目标受众**：6-10岁小学生
- **设计风格**：手绘风格、卡通可爱
- **核心内容**：
  - ✅ 古诗原文与注音
  - ✅ 什么是"汉乐府"（创作背景）
  - ✅ 诗歌描绘的场景（江南水乡采莲）
  - ✅ 重要词语解释（田田、戏）
  - ✅ 诗歌的意义与价值

---

## 🎨 视觉元素

### 主色调
- 🌿 翠绿色（莲叶）
- 🌸 粉红色（荷花）
- 💧 淡蓝色（水面）
- 🐟 金橙色（鱼儿）

### 核心插图元素
1. 密密层层的莲叶
2. 盛开的粉色荷花
3. 活泼可爱的小鱼
4. 采莲的卡通小女孩
5. 小木船

---

## 🚀 快速开始

### 方式一：一键生成（推荐）

```bash
cd /Users/xuejiao/Codes/yyy_ball
./poetry/jiangnan/quickstart.sh
```

按提示选择生成方式即可！

### 方式二：手动运行

#### 使用 Pillow 生成（推荐）
```bash
uv add pillow
uv run poetry/jiangnan/generator_pillow.py
```

#### 使用 HTML + Playwright 生成
```bash
uv add playwright
uv run playwright install chromium
uv run poetry/jiangnan/generator_html.py
```

详细说明请查看 `USAGE.md`

---

## 🛠️ 其他制作方式

### 方式三：AI 生成插图素材
1. 打开 `ai_prompts.md`
2. 复制提示词到 Midjourney / DALL-E / Stable Diffusion
3. 生成插图素材
4. 在设计软件中组合

### 方式四：设计软件制作
1. 打开 Canva / Figma / Procreate
2. 参考 `infographic_design.md` 中的布局
3. 使用素材库搜索相关元素
4. 添加 `poem_info.md` 中的文案

---

## 📚 知识要点速览

| 项目 | 内容 |
|------|------|
| 诗歌来源 | 汉乐府民歌（约2000年前） |
| 作者 | 无具体作者，老百姓集体创作 |
| 江南 | 长江以南的水乡地区 |
| 田田 | 形容莲叶茂盛整齐 |
| 戏 | 嬉戏、玩耍 |
| 主题 | 采莲的快乐场景、人与自然和谐 |

---

## 🌟 制作完成后

可将成品保存为：
- `jiangnan_infographic.png` - 高清图片
- `jiangnan_infographic.pdf` - 可打印版本
