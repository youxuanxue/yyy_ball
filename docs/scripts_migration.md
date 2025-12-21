# 脚本迁移说明

## 概述

`scripts` 目录下的 Python 脚本已整合到 `src` 目录中，以更好地组织代码结构。

## 迁移对照表

### 语音相关工具

| 旧脚本 | 新位置 | 使用方式 |
|--------|--------|----------|
| `scripts/gen_voice_clone.py` | `src/cli/voice_clone.py` | `python -m src.cli.voice_clone` |
| `scripts/regenerate_voice_with_prompt.py` | 已整合到 `src/cli/voice_clone.py` | 使用 `--auto-extract-text` 和 `--convert-to-mp3` 参数 |
| `scripts/list_edge_tts_voices.py` | 已整合到 `src/utils/voice.py` | 使用 `src.utils.voice.list_all_voices_sync()` |

### 说话头像工具

| 旧脚本 | 新位置 | 使用方式 |
|--------|--------|----------|
| `scripts/generate_talking_head.py` | `src/cli/talking_head.py` | `python -m src.cli.talking_head` |

### Icons8 图标管理工具

**注意**: PNG 文件重复检查和清理功能已删除。Icons8 图标下载和元数据整理功能保留在 `src/crawlers/crawler_icons8.py`。

## 使用示例

### 语音克隆

```bash
# 单个文本生成
python -m src.cli.voice_clone \
    --text "你好，这是测试语音" \
    --reference assets/voice/my_voice.wav \
    --output output.wav

# 从 JSON 脚本批量生成（自动优化和提取文字）
python -m src.cli.voice_clone \
    --script series/sunzi/lesson10/script.json \
    --reference assets/voice/my_voice.wav \
    --output-dir series/sunzi/lesson10/voice \
    --auto-extract-text \
    --convert-to-mp3
```

### 说话头像生成

```bash
# 生成单个视频
python -m src.cli.talking_head \
    --image assets/avatars/character_01.jpg \
    --audio series/sunzi/lesson10/voice/1.mp3 \
    --output series/sunzi/lesson10/talking_head/1.mp4

# 批量生成
python -m src.cli.talking_head \
    --image assets/avatars/character_01.jpg \
    --audio-dir series/sunzi/lesson10/voice \
    --output-dir series/sunzi/lesson10/talking_head
```

### Icons8 图标下载

```bash
# Icons8 图标下载和元数据整理
python src/crawlers/crawler_icons8.py
```

## 保留的脚本

以下脚本由于包含特定课程配置，暂时保留在 `scripts` 目录：

- `scripts/generate_lesson10_voice_and_talking_head.py` - lesson10 特定配置脚本

## 代码结构

```
src/
├── cli/                    # 命令行工具
│   ├── voice_clone.py     # 语音克隆 CLI
│   └── talking_head.py    # 说话头像 CLI
├── utils/                  # 工具函数
│   └── voice.py           # 语音相关工具（包含 Edge TTS 和 CosyVoice）
└── crawlers/              # 爬虫和下载工具
    └── crawler_icons8.py  # Icons8 图标下载和元数据整理
```

