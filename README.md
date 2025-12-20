# 孙子兵法：小小谋略家 (Sunzi for Kids)

这是一个使用 Python 代码生成《孙子兵法》儿童教学视频的项目。结合了 **Manim**（数学/白板动画引擎）、**Edge TTS**（微软语音合成）和 **Playwright**（自动化发布），自动生成 9:16 竖屏短视频并自动发布到微信视频号。

## 🎥 项目成果

- **目标受众**：爱思考、喜欢动脑筋的你（哪怕你是6岁的小学生）
- **视频格式**：1080x1920 (9:16 竖屏)
- **核心技术**：
    - Stroke Animation (手绘/白板风格)
    - TTS (AI 语音解说)
    - **AI Music (AI 自动生成背景音乐)**
    - **Auto-Sync (音频画面自动对齐)**
    - **Safe-Zone (防视频号/抖音遮挡布局)**
    - **Auto-Publish (自动发布到微信视频号)**

## 💎 最佳实践 (Best Practices)

### 1. 🚫 去 Emoji 化 (No-Emoji Policy)
**原则**：严禁在 `Text()` 中直接使用 Emoji（如 🥊, 🧠），因为渲染极不稳定。
**替代方案**：
*   使用 Manim 原生图形：`Circle`, `Square`, `Star`, `Triangle`, `CheckMark`。
*   使用带颜色的纯文字：`Text("VS", color=RED)`。
*   使用**简单符号**：
    *   **√** (绿色 `Text("√")`): 代表正确、掌控、自信。
    *   **?** (橙色 `Text("?")`): 代表未知、运气、不确定。
*   使用组合图形：`VGroup(Text("✔", font="Arial"), Text("描述"))`。

### 2. ⏱️ 自动化紧凑节奏 (Auto-Paced Timing)
**原则**：短视频节奏必须紧凑，画面要紧跟甚至略快于声音。
**核心机制**：
*   **并发拆解为串行**：避免使用 `(weight, [Anim1, Anim2])` 的并发形式，尽量拆分为两个独立的步骤 `(weight/2, Anim1), (weight/2, Anim2)`，获得更细腻的动画效果。
*   **转场时间扣除**：在计算每一页的停留时间时，**必须扣除转场动画（如 FadeOut）的耗时**。例如 `wait_until_audio_end(page_duration - TRANSITION_TIME)`，否则视频会越来越滞后于音频。

### 3. 📐 布局与排版 (Layout & Typography)
**原则**：大字号、宽行距、留足边距，打造高级感。
**标准参数**：
*   **两侧留白**：总内容宽度建议控制在 **7.5** 左右（屏幕宽9.0），给两侧各留出 **0.75** 的呼吸空间。
*   **文字大小**：
    *   标题：**48**
    *   正文列表：**36-40**
    *   说明小字：**30-32**
*   **行距**：使用 `line_spacing=1.4` 或 `1.5`，避免文字挤作一团。

### 4. 🎵 AI 智能配乐与音频管理 (Smart BGM & Audio)
**原则**：
1.  **文件命名**：严禁使用 `_v2`, `_new` 等后缀。文件名必须明确且固定，例如 `lesson5_full.wav`。
2.  **音量控制**：背景音乐音量推荐设置为 **-10dB** 到 **-15dB**。
3.  **音频修复**：在 Manim 渲染结束后的 `tear_down` 钩子中，必须调用音频检查函数（`utils.anim_helper.merge_audio_video_if_needed`），以防止生成的视频丢失音频。
4.  **时长精准**：依赖 `ffprobe` 等工具获取精确的音频时长，避免因元数据误差导致的音画不同步。

### 5. ⚡️ 极速转场 (Ultra-fast Transition)
**原则**：短视频切换必须干脆，不要拖泥带水。
**参数标准**：
*   建议在 `animate.py` 中统一设置 `TRANSITION_TIME = 0.5` 或更短。
*   `combine_audio_clips` 默认 `silence_duration=0`，由 `wait_until_audio_end` 精确控制页面停留，消除多余空白。

### 6. 🎮 互动结尾模板 (Interactive Ending)
**标准结构**：
1.  **"小武思考时间"** 标题（几何图形 + 摇摆动画）。
2.  **选择题**：A/B/C 三个选项，用颜色区分（红/灰/绿）。
3.  **CTA**：明确引导“在评论区告诉小武”。

### 7. 🎨 封面布局规范 (Cover Design Layout)
**原则**：封面是第一印象，必须精致且不与文字冲突。
**实现**：
*   **主视觉**：位置固定在屏幕中心略偏上，避免过大。
*   **致辞固化**：每一课的第一页（封面）底部必须包含统一的致辞。
*   **标题自适应**：封面生成脚本应包含根据标题字数自动缩放字号的逻辑，防止长标题溢出。

## 📂 项目结构

```text
yyy_ball/
├── assets/                 # 📦 资源层：原始素材 (书籍 Markdown, 数据 JSON)
│   └── music_candidates_local/ # 🎵 本地生成的 AI 音乐库
├── crawlers/               # 🕷️ 爬虫层：数据抓取脚本
├── publish/                # 🚀 发布层：自动化发布模块
│   ├── __init__.py         
│   └── wx_channel.py       # 微信视频号发布核心逻辑
├── utils/                  # 🔧 工具层：通用逻辑 (TTS 封装, Manim 辅助, 音乐生成)
│   ├── anim_helper.py      # ✨ 动画时间轴 & 音频混合核心
│   ├── gen_music_local.py  # 🎵 本地 AI 音乐生成脚本 (基于 Transformers)
│   ├── cover_generator.py  # 🎨 封面生成器核心逻辑
│   └── templates/          # 📄 HTML 封面模板
├── series/                 # 📚 内容层：按书籍和课时分类
│   └── sunzi/              # 书籍：孙子兵法
│       ├── run_publish.py  # 🚀 通用发布启动脚本
│       ├── lesson01/       # 第一课源码
│       ├── lesson02/       # 第二课源码
│       ├── lesson03/       # 第三课源码 (最新最佳实践模板)
│       │   ├── animate.py  # 视频动画脚本 (含 BGM 配置)
│       │   ├── gen_voice.py # 语音生成脚本
│       │   ├── gen_cover.py # 封面生成配置脚本
│       │   └── social_media.md # 社交媒体推广文案
│       └── lesson04/       # 第四课源码
└── media/                  # 🎬 产物层：生成的视频和音频
    └── sunzi/
        └── lesson03/
            ├── voice/      # 生成的 MP3
            ├── videos/     # 最终生成的 MP4 (请认准 1920p60 高清版)
            └── images/     # 生成的封面图
```

## 🛠️ 环境准备

推荐使用 `uv` 进行包管理。

### 1. 安装依赖

本项目使用 `pyproject.toml` 管理依赖。

```bash
# 1. 创建并同步环境
uv sync

# 2. 安装浏览器内核 (用于封面生成和自动化发布)
uv run playwright install chromium
```

**系统级依赖 (macOS):**
```bash
brew install ffmpeg pango scipy
```

## 🚀 制作流程

所有的运行命令都在**项目根目录**执行。

### 第一步：准备文案
1.  **Script**: 编辑 `series/sunzi/lessonXX/script.md`，确定 PPT 结构。
2.  **Social Copy**: 编写 `series/sunzi/lessonXX/social_media.md`，准备朋友圈/视频号推广文案（第一行为标题）。

### 第二步：生成语音
修改 `gen_voice.py` 中的台词字典，然后运行：
```bash
uv run python series/sunzi/lessonXX/gen_voice.py
```

### 第三步：生成/选择音乐 (新增)
1.  **生成音乐** (如需新音乐)：
    ```bash
    uv run utils/gen_music_local.py
    ```
    音乐会保存在 `assets/music_candidates_local/`。
2.  **挑选音乐**：试听并选择一首合适的，复制其路径。

### 第三步半（可选）：清理旧音频
如果之前生成过音频，建议手动清理 `media/sunzi/lessonXX/voice/` 下的旧文件，确保没有带有 `_v2` 等后缀的残留。

### 第四步：生成封面 (Cover)
配置 `gen_cover.py` 中的标题和标签，然后运行：
```bash
# 生成高清设计感封面 (HTML/CSS + Playwright)
uv run python series/sunzi/lessonXX/gen_cover.py
```

### 第五步：生成视频
1.  修改 `animate.py`：
    *   **插入封面首帧**：确保 `construct` 方法最开始包含了插入封面的逻辑。
    *   配置 `bgm_file` 为刚才挑选的音乐路径。
    *   确保 `bgm_volume` 设置为 `-15` (推荐值)。
    *   **音频文件名**：确保 `combine_audio_clips` 输出文件名为标准格式（如 `lessonX_full.wav`）。
    *   **自动修复音频**：确保实现了 `tear_down` 方法并调用了 `merge_audio_video_if_needed`。
2.  **渲染成品** (必须使用 `-qh` 高清模式以确保音质和画质)：
    ```bash
    # 高质量成品 (1080x1920, 60fps)
    # 建议加上 --disable_caching 以确保逻辑变更生效
    uv run manim -qh --disable_caching series/sunzi/lessonXX/animate.py ClassName
    ```

### 第六步：自动发布 (新增)
确保 `media/` 下生成了视频和封面，并且 `series/` 下有 `social_media.md` 文案。

```bash
# 自动发布指定课程 (需要扫码登录)
uv run python series/sunzi/run_publish.py lessonXX
```
*例如：`uv run python series/sunzi/run_publish.py lesson03`*

脚本会自动：
1.  截取标题（不超过16字）。
2.  读取文案描述。
3.  上传视频。
4.  保留浏览器窗口供人工确认封面和点击发布。

### 第七步：清理中间文件 (Cleanup)
发布完成后，删除 Manim 生成的庞大缓存文件，只保留最终的 MP4。

```bash
# 清理指定课程的中间文件 (Tex缓存, Partial movies)
rm -rf media/sunzi/lessonXX/videos/**/partial_movie_files
rm -rf media/sunzi/lessonXX/Tex
```

## 🌟 如何添加新课程

1.  **创建目录**：`mkdir -p series/sunzi/lesson04`
2.  **复制模板**：将 `series/sunzi/lesson03/` 下的所有 `.py` 和 `.md` 文件复制到新目录。**Lesson 03 是目前的最佳实践模板。**
3.  **修改配置**：更新 `gen_voice.py` 和 `animate.py` 中的路径配置 (`lesson03` -> `lesson04`)。
4.  **创作**：编写新一课的文案和动画代码。

## 📝 常用命令速查

- **只渲染最后一帧** (检查布局): `manim -ps series/.../animate.py ClassName`
- **清理缓存**: 删除 `media/` 下对应的子文件夹。
