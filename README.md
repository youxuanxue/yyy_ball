# 孙子兵法：小小谋略家 (Sunzi for Kids)

这是一个使用 Python 代码生成《孙子兵法》儿童教学视频的项目。结合了 **Manim**（数学/白板动画引擎）和 **Edge TTS**（微软语音合成），自动生成 9:16 竖屏短视频。

## 🎥 项目成果

- **目标受众**：爱思考、喜欢动脑筋的你（哪怕你是6岁的小学生）
- **视频格式**：1080x1920 (9:16 竖屏)
- **核心技术**：
    - Stroke Animation (手绘/白板风格)
    - TTS (AI 语音解说)
    - **Auto-Sync (音频画面自动对齐)**
    - **Safe-Zone (防视频号/抖音遮挡布局)**

## 💎 最佳实践 (Best Practices)

### 1. 🚫 去 Emoji 化 (No-Emoji Policy)
**原则**：严禁在 `Text()` 中直接使用 Emoji（如 🥊, 🧠），因为渲染极不稳定。
**替代方案**：
*   使用 Manim 原生图形：`Circle`, `Square`, `Star`, `Triangle`, `CheckMark`。
*   使用带颜色的纯文字：`Text("VS", color=RED)`。
*   使用组合图形：`VGroup(Text("✔", font="Arial"), Text("描述"))`。

### 2. ⏱️ 紧凑节奏 (Compact Timing)
**原则**：短视频节奏必须紧凑，画面要紧跟甚至略快于声音。
**技巧**：
*   对于列表项（如选项 A/B/C），不要平均分配剩余时间。
*   推荐使用 **固定且紧凑的时长**（如每项 2.0s - 2.5s），确保节奏感。
*   将剩余的缓冲时间全部留给页面最后的 CTA 环节。

### 3. 🎮 互动结尾模板 (Interactive Ending)
**标准结构**：
1.  **"小武思考时间"** 标题（几何图形 + 摇摆动画）。
2.  **选择题**：A/B/C 三个选项，用颜色区分（红/灰/绿）。
3.  **CTA**：明确引导“在评论区告诉小武”。

## 📂 项目结构

```text
yyy_ball/
├── assets/                 # 📦 资源层：原始素材 (书籍 Markdown, 数据 JSON)
├── crawlers/               # 🕷️ 爬虫层：数据抓取脚本
├── utils/                  # 🔧 工具层：通用逻辑 (TTS 封装, Manim 辅助)
├── series/                 # 📚 内容层：按书籍和课时分类
│   └── sunzi/              # 书籍：孙子兵法
│       ├── lesson01/       # 第一课源码
│       ├── lesson02/       # 第二课源码
│       └── lesson03/       # 第三课源码 (最新最佳实践模板)
└── media/                  # 🎬 产物层：生成的视频和音频
    └── sunzi/
        └── lesson03/
            ├── voice/      # 生成的 MP3
            └── videos/     # 最终生成的 MP4
```

## 🛠️ 环境准备

推荐使用 `uv` 进行包管理。

### 1. 安装依赖

```bash
# 如果使用 uv (推荐)
uv venv
source .venv/bin/activate
uv pip install manim edge-tts mutagen

# 或者使用 pip
pip install manim edge-tts mutagen
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

### 第三步：生成视频
修改 `animate.py` 中的动画逻辑，然后渲染：
```bash
# 预览 (低质量, 速度快)
uv run manim -pql series/sunzi/lessonXX/animate.py ClassName

# 成品 (高质量 1080x1920, 60fps)
uv run manim -pqh series/sunzi/lessonXX/animate.py ClassName
```

### 第四步：清理中间文件 (Cleanup)
确认视频无误后，删除 Manim 生成的庞大缓存文件（partial_movie_files），只保留最终的 MP4。

```bash
# 清理指定课程的中间文件
rm -rf media/sunzi/lessonXX/videos/**/partial_movie_files
# 或者清理 Tex 缓存
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
