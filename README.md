# 孙子兵法：小小谋略家 (Sunzi for Kids)

这是一个使用 Python 代码生成《孙子兵法》儿童教学视频的项目。结合了 **Manim**（数学/白板动画引擎）和 **Edge TTS**（微软语音合成），自动生成 9:16 竖屏短视频。

## 🎥 项目成果

- **目标受众**：爱思考、喜欢动脑筋的你（哪怕你是6岁的小学生）
- **视频格式**：1080x1920 (9:16 竖屏)
- **核心技术**：
    - Stroke Animation (手绘/白板风格)
    - TTS (AI 语音解说)
    - **AI Music (AI 自动生成背景音乐)**
    - **Auto-Sync (音频画面自动对齐)**
    - **Safe-Zone (防视频号/抖音遮挡布局)**

## 💎 最佳实践 (Best Practices)

### 1. 🚫 去 Emoji 化 (No-Emoji Policy)
**原则**：严禁在 `Text()` 中直接使用 Emoji（如 🥊, 🧠），因为渲染极不稳定。
**替代方案**：
*   使用 Manim 原生图形：`Circle`, `Square`, `Star`, `Triangle`, `CheckMark`。
*   使用带颜色的纯文字：`Text("VS", color=RED)`。
*   使用组合图形：`VGroup(Text("✔", font="Arial"), Text("描述"))`。

### 2. ⏱️ 自动化紧凑节奏 (Auto-Paced Timing)
**原则**：短视频节奏必须紧凑，画面要紧跟甚至略快于声音。
**实现**：使用 `utils.anim_helper.play_timeline` 自动管理时间。
*   **机制**：只需定义每个动作的**权重 (Weight)**，函数会自动根据语音时长分配时间。
*   **智能限制**：函数内置了逻辑，确保单个动画时长不超过 2.5s（防止拖沓），并将剩余时间自动转换为停顿 (`wait`)。
*   **代码示例**：
    ```python
    # 权重: 标题(5) -> 内容(10) -> 结尾(5)
    timeline_steps = [
        (5, Write(title)),
        (10, FadeIn(content)),
        (5, GrowFromCenter(icon))
    ]
    elapsed = play_timeline(self, page_duration, timeline_steps)
    ```

### 3. 🎵 AI 智能配乐 (Smart BGM Mixing)
**原则**：背景音乐是灵魂，但不能喧宾夺主。
**实现**：使用 `utils.gen_music_local.py` 生成音乐，用 `utils.anim_helper.combine_audio_clips` 自动混合。
*   **音乐生成**：本地运行 MusicGen Small/Medium 模型，无需 API Key。
*   **自动混音**：
    *   自动循环 BGM 以填满视频时长。
    *   自动淡入淡出。
    *   **音量控制**：建议 BGM 设置为 **-15dB**，确保人声清晰。
    ```python
    # animate.py 配置示例
    full_audio = combine_audio_clips(
        audio_clips, 
        COMBINED_WAV, 
        bgm_file="assets/music_candidates_local/smart_thinking_0931.wav",
        bgm_volume=-15, 
        bgm_loop=True
    )
    ```

### 4. ⚡️ 极速转场 (Ultra-fast Transition)
**原则**：短视频切换必须干脆，不要拖泥带水。
**参数标准**：
*   建议在 `animate.py` 中统一设置 `TRANSITION_TIME = 0.5` 或更短。
*   `combine_audio_clips` 默认 `silence_duration=0`，由 `wait_until_audio_end` 精确控制页面停留，消除多余空白。

### 5. 🎮 互动结尾模板 (Interactive Ending)
**标准结构**：
1.  **"小武思考时间"** 标题（几何图形 + 摇摆动画）。
2.  **选择题**：A/B/C 三个选项，用颜色区分（红/灰/绿）。
3.  **CTA**：明确引导“在评论区告诉小武”。

## 📂 项目结构

```text
yyy_ball/
├── assets/                 # 📦 资源层：原始素材 (书籍 Markdown, 数据 JSON)
│   └── music_candidates_local/ # 🎵 本地生成的 AI 音乐库
├── crawlers/               # 🕷️ 爬虫层：数据抓取脚本
├── utils/                  # 🔧 工具层：通用逻辑 (TTS 封装, Manim 辅助, 音乐生成)
│   ├── anim_helper.py      # ✨ 动画时间轴 & 音频混合核心
│   ├── gen_music_local.py  # 🎵 本地 AI 音乐生成脚本 (基于 Transformers)
│   ├── cover_generator.py  # 🎨 封面生成器核心逻辑
│   └── templates/          # 📄 HTML 封面模板
├── series/                 # 📚 内容层：按书籍和课时分类
│   └── sunzi/              # 书籍：孙子兵法
│       ├── lesson01/       # 第一课源码
│       ├── lesson02/       # 第二课源码
│       └── lesson03/       # 第三课源码 (最新最佳实践模板)
│           ├── animate.py  # 视频动画脚本 (含 BGM 配置)
│           ├── gen_voice.py # 语音生成脚本
│           └── gen_cover.py # 封面生成配置脚本
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

# 2. 安装浏览器内核 (用于封面生成)
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
2.  **Social Copy**: 编写 `social_media.md`，准备朋友圈/视频号推广文案。

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

### 第四步：生成封面 (Cover)
配置 `gen_cover.py` 中的标题和标签，然后运行：
```bash
# 生成高清设计感封面 (HTML/CSS + Playwright)
uv run python series/sunzi/lessonXX/gen_cover.py
```

### 第五步：生成视频
1.  修改 `animate.py`：
    *   配置 `bgm_file` 为刚才挑选的音乐路径。
    *   确保 `bgm_volume` 设置为 `-15` (推荐值)。
2.  **渲染成品** (必须使用 `-qh` 高清模式以确保音质和画质)：
    ```bash
    # 高质量成品 (1080x1920, 60fps) - 推荐开启 --disable_caching 避免音频缓存问题
    uv run manim -qh series/sunzi/lessonXX/animate.py ClassName --disable_caching
    ```
    *注意：不要使用 `-pql` (低质量) 来预览音频混合效果，可能会有偏差。*

### 第六步：清理中间文件 (Cleanup)
确认视频无误后，删除 Manim 生成的庞大缓存文件，只保留最终的 MP4。

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
