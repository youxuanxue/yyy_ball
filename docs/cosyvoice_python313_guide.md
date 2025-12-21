# 在 Python 3.13 环境下使用 CosyVoice（GitHub 版本）

## ✅ 可行性确认

**可以！** 在 Python 3.13 环境下使用 GitHub 版本的 CosyVoice 是可行的。

**状态**：✅ 已验证可以导入 CosyVoice 类

## 🚀 安装步骤

### 1. 克隆仓库

```bash
# 如果还没有克隆
git clone https://github.com/FunAudioLLM/CosyVoice.git external/CosyVoice
```

### 2. 安装必要的依赖

```bash
# 在项目根目录执行（使用 uv add，会自动添加到 pyproject.toml）
uv add HyperPyYAML modelscope onnxruntime openai-whisper torchaudio inflect soxr omegaconf

# 同步依赖
uv sync

# 验证安装
uv run python -c "import sys; sys.path.insert(0, 'external/CosyVoice'); from cosyvoice.cli.cosyvoice import CosyVoice; print('✅ 成功')"
```

**注意**：这些依赖已经添加到 `pyproject.toml`，运行 `uv sync` 即可安装。

**已安装的依赖**：
- ✅ `hyperpyyaml>=1.2.2`
- ✅ `modelscope>=1.33.0`
- ✅ `onnxruntime>=1.23.2`
- ✅ `openai-whisper>=20250625`
- ✅ `torchaudio>=2.9.1`
- ✅ `inflect>=7.5.0`
- ✅ `soxr>=1.0.0`
- ✅ `omegaconf>=2.3.0`

**状态**：✅ 已验证可以成功导入 CosyVoice

### 3. 使用方式

代码会自动检测并使用 GitHub 版本：

```python
from src.utils.voice_clone import clone_voice_cosyvoice

# 使用 CosyVoice 克隆语音
clone_voice_cosyvoice(
    text="你好，这是测试语音",
    reference_audio_path="assets/voice/frank.mp3",
    output_path="output.wav",
    language="zh"
)
```

## ⚠️ 注意事项

### 依赖冲突

CosyVoice 的 `requirements.txt` 中有一些依赖与项目冲突：
- `numpy==1.26.4` vs 项目要求 `numpy>=2.0`（通过 manim）
- `torch==2.3.1` vs 项目要求 `torch>=2.9.1`

**解决方案**：
- ✅ 不安装 CosyVoice 的所有依赖
- ✅ 只安装必要的、不冲突的依赖（如 `HyperPyYAML`, `modelscope`）
- ✅ 使用项目已有的依赖（如 `torch`, `numpy`）

### 功能限制

由于没有安装所有依赖，某些功能可能不可用：
- ⚠️ 某些音频处理功能可能需要 `librosa==0.10.2`（项目使用 `librosa==0.9.2`）
- ⚠️ 某些功能可能需要 `soundfile` 等额外依赖
- ✅ 核心的 zero-shot 语音克隆功能应该可以正常使用

### 模型下载

首次使用 CosyVoice 时，会自动从 ModelScope 下载模型（约 2-3GB）：
- 模型会下载到 `pretrained_models/` 目录
- 需要网络连接
- 下载时间取决于网络速度

## 📝 使用示例

### 基本用法

```python
import sys
sys.path.insert(0, 'external/CosyVoice')
from cosyvoice.cli.cosyvoice import CosyVoice
import torchaudio

# 初始化（首次使用会自动下载模型）
cosyvoice = CosyVoice(model_dir="pretrained_models/CosyVoice-300M")

# Zero-shot 语音克隆
# prompt_text: 参考音频对应的文字
# prompt_wav: 参考音频文件路径
for output in cosyvoice.inference_zero_shot(
    tts_text="你好，这是测试语音",
    prompt_text="希望你以后能够做的比我还好呦。",  # 参考音频对应的文字
    prompt_wav="assets/voice/frank.mp3",
    stream=False
):
    torchaudio.save("output.wav", output['tts_speech'], cosyvoice.sample_rate)
    break
```

### 通过工具函数使用

```bash
# 使用命令行工具
python scripts/gen_voice_clone.py \
    --text "你好，这是测试语音" \
    --reference assets/voice/frank.mp3 \
    --output output.wav \
    --engine cosyvoice
```

## 🔍 故障排除

### 问题：`ModuleNotFoundError: No module named 'hyperpyyaml'`

**解决**：
```bash
uv pip install HyperPyYAML
```

### 问题：`ModuleNotFoundError: No module named 'modelscope'`

**解决**：
```bash
uv pip install modelscope
```

### 问题：模型下载失败

**解决**：
- 检查网络连接
- 可能需要配置 ModelScope 镜像（如果在中国大陆）

## 📚 相关文档

- **CosyVoice GitHub**: https://github.com/FunAudioLLM/CosyVoice
- **CosyVoice 文档**: https://fun-audio-llm.github.io

