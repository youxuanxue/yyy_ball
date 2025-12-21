# 语音克隆优化指南

## 🎯 问题：音色相似度低

如果生成的语音文件音色与参考音频相差很大，可以通过以下方法优化：

## 🔧 优化方案

### 1. 提供 prompt_text（最重要）⭐

**问题**：CosyVoice 的 zero-shot 模式如果提供参考音频对应的文字，音色相似度会显著提高。

**解决方案**：

#### 方式一：手动提供（推荐）
```bash
uv run python scripts/generate_lesson10_voice_and_talking_head.py \
    --voice-only \
    --prompt-text "这是参考音频 frank.mp3 对应的准确文字内容"
```

#### 方式二：自动提取（使用 Whisper）
```bash
# 默认会自动提取，也可以显式启用
uv run python scripts/generate_lesson10_voice_and_talking_head.py \
    --voice-only
```

**注意**：自动提取可能不够准确，建议手动提供准确的文字。

### 2. 优化参考音频质量

脚本会自动优化参考音频：
- ✅ 转换为单声道（CosyVoice 推荐）
- ✅ 标准化采样率到 16kHz
- ✅ 裁剪到 10 秒（最佳时长）

优化后的音频保存在：`series/sunzi/lesson10/voice/optimized_reference.wav`

### 3. 参考音频要求

**最佳实践**：
- **时长**：5-15 秒（建议 10 秒）
- **格式**：WAV 格式，单声道，16kHz 采样率
- **质量**：清晰，无背景噪音
- **内容**：包含多种音调和情感，语速适中

## 📝 使用示例

### 完整优化流程

```bash
# 1. 查看优化指南
uv run python scripts/generate_lesson10_voice_and_talking_head.py --optimization-guide

# 2. 手动提供 prompt_text 重新生成（推荐）
uv run python scripts/generate_lesson10_voice_and_talking_head.py \
    --voice-only \
    --prompt-text "frank.mp3 对应的准确文字内容"

# 3. 如果不想自动优化参考音频
uv run python scripts/generate_lesson10_voice_and_talking_head.py \
    --voice-only \
    --no-optimize-reference \
    --prompt-text "文字内容"

# 4. 如果不想自动提取文字
uv run python scripts/generate_lesson10_voice_and_talking_head.py \
    --voice-only \
    --no-auto-extract \
    --prompt-text "文字内容"
```

## 🔍 如何获取 prompt_text

### 方法一：手动转录（最准确）
1. 播放 `assets/voice/frank.mp3`
2. 准确记录音频中的文字内容
3. 使用 `--prompt-text` 参数提供

### 方法二：使用 Whisper 自动提取
```python
from src.utils.voice_clone_optimizer import extract_text_from_audio

text = extract_text_from_audio("assets/voice/frank.mp3")
print(f"提取的文字: {text}")
```

### 方法三：使用其他 ASR 工具
可以使用任何语音识别工具提取文字。

## 💡 优化效果对比

| 方案 | prompt_text | 参考音频优化 | 音色相似度 |
|------|-------------|--------------|------------|
| 基础 | ❌ 无 | ❌ 无 | ⭐⭐ (低) |
| 优化1 | ✅ 自动提取 | ✅ 是 | ⭐⭐⭐ (中) |
| 优化2 | ✅ 手动提供 | ✅ 是 | ⭐⭐⭐⭐⭐ (高) |

## 🎯 最佳实践

1. **录制高质量参考音频**
   - 10 秒左右
   - 清晰，无背景噪音
   - 包含多种音调

2. **提供准确的 prompt_text**
   - 手动转录最准确
   - 与参考音频内容完全一致

3. **使用优化功能**
   - 自动优化参考音频格式
   - 自动提取或手动提供文字

## 📚 相关文档

- `src/utils/voice_clone_optimizer.py` - 优化工具函数
- `scripts/generate_lesson10_voice_and_talking_head.py` - 生成脚本
- `docs/voice_cloning_guide.md` - 语音克隆基础指南

