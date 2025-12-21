# 说话头像生成指南

## 🚀 快速开始

### 1. 安装 SadTalker

```bash
# 克隆仓库
git clone https://github.com/OpenTalker/SadTalker.git external/SadTalker

# 添加依赖到 pyproject.toml（推荐）
./scripts/add_sadtalker_deps.sh

# 或手动添加
cd external/SadTalker
uv add $(cat requirements.txt | grep -v '^#' | grep -v '^$' | tr '\n' ' ')
```

### 2. 下载模型

```bash
# 使用项目提供的脚本（兼容 macOS 和 Linux）
./scripts/download_sadtalker_models.sh

# 或使用官方脚本（需要 wget，macOS 可能需要安装）
cd external/SadTalker
bash scripts/download_models.sh
```

### 3. 生成说话头像

```bash
# 使用专用脚本（推荐）
uv run python scripts/generate_lesson10_talking_head.py

# 或使用通用脚本
uv run python scripts/generate_talking_head.py \
    --image series/sunzi/images/shane.jpg \
    --audio-dir series/sunzi/lesson10/voice \
    --output-dir series/sunzi/lesson10/talking_head
```

## 📦 所需素材

- ✅ **人物头像**: `series/sunzi/images/shane.jpg`
- ✅ **音频文件**: `series/sunzi/lesson10/voice/1-7.mp3`
- ✅ **文字脚本**: `series/sunzi/lesson10/script.json`

## 💻 Python API

```python
from src.utils.talking_head import batch_generate_talking_heads

batch_generate_talking_heads(
    image_path="series/sunzi/images/shane.jpg",
    audio_dir="series/sunzi/lesson10/voice",
    output_dir="series/sunzi/lesson10/talking_head"
)
```

## ⚙️ 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--face-enhance` | 启用面部增强 | 启用 |
| `--batch-size` | 批处理大小 | 1 |
| `--size` | 输出视频尺寸 | 512 |

## 🔍 检查状态

```bash
uv run python scripts/generate_lesson10_talking_head.py --check
```

## 📚 参考

- **SadTalker GitHub**: https://github.com/OpenTalker/SadTalker
- **工具函数**: `src/utils/talking_head.py`

