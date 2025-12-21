# 孙子兵法：小小谋略家 (Sunzi for Kids)

这是一个使用 Python 代码生成《孙子兵法》儿童教学视频的项目。结合了 **Manim**（数学/白板动画引擎）、**Edge TTS**（微软语音合成）和 **Playwright**（自动化发布），自动生成 9:16 竖屏短视频并自动发布到微信视频号。

## 🎥 项目成果

- **目标受众**：爱思考、喜欢动脑筋的你（4-12岁）
- **视频格式**：1080x1920 (9:16 竖屏)
- **核心技术**：
    - Stroke Animation (手绘/白板风格)
    - TTS (AI 语音解说)
    - **AI Music (AI 自动生成背景音乐)**
    - **Auto-Sync (音频画面自动对齐)**
    - **Safe-Zone (防视频号/抖音遮挡布局)**
    - **Auto-Publish (自动发布到微信视频号)**

## 📂 项目结构

```text
yyy_ball/
├── src/                    # 💻 源代码目录：所有源代码，包括爬虫、工具函数、发布模块
│   ├── crawlers/           # 🕷️ 爬虫层：数据抓取脚本，用于从知识星球等平台抓取内容
│   │   ├── __init__.py
│   │   ├── crawler.py      # 通用爬虫
│   │   ├── crawler_lunyu.py
│   │   ├── crawler_yijing.py
│   │   └── ...
│   ├── utils/              # 🔧 工具层：通用工具函数，包括动画辅助、语音合成、封面生成等
│   │   ├── __init__.py
│   │   ├── anim_helper.py  # ✨ 动画时间轴 & 音频混合核心
│   │   ├── animate.py      # 通用动画基类
│   │   ├── voice.py        # TTS 语音合成封装
│   │   ├── cover_generator.py # 🎨 封面生成器核心逻辑
│   │   └── gen_music_local.py # 🎵 本地 AI 音乐生成脚本
│   └── template/           # 📄 模板文件目录
│       └── sunzi/          # 孙子兵法系列模板
│           ├── cover_template.html  # HTML 封面模板
│           ├── animate_template.py  # 动画模板
│           └── script_template.json # 脚本模板
│   └── publish/            # 🚀 发布层：自动化发布模块，支持微信视频号发布
│       ├── __init__.py
│       ├── wx_channel.py   # 微信视频号发布核心逻辑
│       └── publish_lesson.py # 发布脚本入口
├── config/                 # ⚙️ 配置文件目录：配置文件，如认证信息等敏感数据
│   └── auth_wx.json        # 微信视频号认证信息
├── assets/                 # 📦 资源层：静态资源，包括音乐、书籍、数据、图片
│   ├── bgm/                # 🎵 背景音乐文件
│   ├── books/              # 📚 书籍 Markdown 文件
│   ├── data/               # 📊 爬取的数据 JSON 文件
│   └── images/             # 🖼️ 图片资源（课程配图等）
├── series/                 # 📚 内容层：课程内容源代码，每个课程目录包含脚本和生成的媒体文件
│   └── sunzi/              # 书籍：孙子兵法
│       ├── lesson01/       # 第一课源码
│       │   ├── animate.py  # 视频动画脚本
│       │   ├── script.md   # 课程脚本（Markdown 格式）
│       │   ├── script.json # 结构化脚本（JSON 格式）
│       │   ├── social_media.md # 社交媒体推广文案
│       │   └── media/       # 生成的媒体文件（视频、音频、图片）
│       ├── lesson02/       # 第二课源码
│       ├── lesson03/       # 第三课源码 (最新最佳实践模板)
│       │   ├── animate.py  # 视频动画脚本 (含 BGM 配置)
│       │   ├── gen_voice.py # 语音生成脚本（可选）
│       │   ├── gen_cover.py # 封面生成配置脚本（可选）
│       │   ├── script.md   # 课程脚本
│       │   ├── script.json # 结构化脚本
│       │   ├── social_media.md # 社交媒体推广文案
│       │   └── media/       # 生成的媒体文件
│       └── lessonXX/       # 其他课程...
├── docs/                   # 📖 文档目录：项目文档和使用指南
├── pyproject.toml          # Python 项目配置
├── uv.lock                 # 依赖锁定文件
└── README.md               # 项目说明文档
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

## 🚀 快速开始

### 制作新课程的基本流程

#### 1. 准备文案
编辑 `series/sunzi/lessonXX/script.md`，编写课程脚本内容。

#### 2. 生成结构化物料
根据 `script.md` 生成结构化 JSON 文件 `series/sunzi/lessonXX/script.json`。

#### 3. 设计并实现动画
根据 `script.json` 中的 `scenes` 和 `voiceover_script` 场景描述，设计并实现 Manim 动画代码。

**设计原则**：
- **定位**："小小谋略家"儿童财商/谋略课程
- **目标受众**：4-12 岁的孩子
- **核心策略**：将深刻的道理"降维"，用孩子熟悉的生活场景（学校、游戏、家庭）来重新演绎
- **实现方式**：使用 Manim 代码实现动画效果

**代码插入位置**：
将实现的 Manim 代码插入到 `series/sunzi/lessonXX/animate.py` 中的指定位置：

```python
# 主要的 manim 动画生成的代码，请放在这里。
###### start #######
        
###### end #######
```

#### 4. 生成视频
切换到对应的课程目录，运行 Manim 渲染动画视频（这样生成的 media 会自动保存在当前 lessonXX 目录中）：

```bash
cd series/sunzi/lessonXX
uv run manim -qh --disable_caching animate.py ClassName
```

#### 5. 发布到微信视频号
使用发布脚本自动发布：

```bash
uv run python src/publish/publish_lesson.py sunzi/lessonXX
```

### 完整示例（以 lesson05 为例）

```bash
# 1. 生成结构化物料（如果使用自动生成）
# 根据 script.md 生成 script.json

# 2. 生成语音（如果需要单独生成）
uv run python series/sunzi/lesson05/gen_voice.py

# 3. 生成封面（如果需要单独生成）
uv run python series/sunzi/lesson05/gen_cover.py

# 4. 渲染视频（高质量，1080x1920, 60fps）
# 切换到课程目录，生成的 media 会自动保存在当前目录
cd series/sunzi/lesson05
uv run manim -qh --disable_caching animate.py Lesson5Vertical

# 5. 发布到微信视频号
uv run python src/publish/publish_lesson.py sunzi/lesson05
```

> **提示**：步骤 2 和 3 通常会在 `animate.py` 中自动执行，无需单独运行。

## 📝 技术栈

- **Manim**: 数学动画引擎，用于生成手绘风格动画
- **Edge TTS**: 微软语音合成服务
- **Playwright**: 浏览器自动化，用于封面生成和发布
- **FFmpeg**: 音视频处理
- **Python 3.x**: 主要开发语言

## 📚 相关文档

- [图标使用指南](./docs/icon_quick_reference.md) - Manim 图标快速参考
- [CosyVoice 安装指南](./docs/cosyvoice_python313_guide.md) - 在 Python 3.13 环境下安装和使用 CosyVoice
- [说话头像指南](./docs/talking_head_guide.md) - 使用 SadTalker 生成说话头像

## 📄 许可证

本项目仅供学习和研究使用。
