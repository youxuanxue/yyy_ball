# CPU 优化指南（无 GPU）

## 🚀 快速优化（推荐）

使用 `--fast-mode` 参数，一键启用所有 CPU 优化：

```bash
uv run python scripts/generate_lesson10_voice_and_talking_head.py \
    --talking-head-only \
    --fast-mode
```

**优化效果：**
- ⚡ 速度提升：**5-8 倍**
- 📉 质量损失：轻微（仅唇形动画，头部不移动）
- ⏱️ 预计时间：10 秒音频约 1-2 分钟（vs 5-10 分钟）

## ⚙️ 优化参数说明

### 1. 快速模式 (`--fast-mode`)

自动应用以下优化：
- ❌ 禁用面部增强（节省 20-30% 时间）
- 📐 分辨率降至 256x256（比 512x512 快 2-3 倍）
- ✂️ 使用 `crop` 预处理模式（比 `full` 快 30-50%）
- 🎭 启用 `still` 模式（仅唇形动画，头部不移动，节省 30-40% 时间）

### 2. 手动优化参数

如果快速模式质量不够，可以手动调整：

```bash
# 禁用面部增强（节省 20-30% 时间）
--no-face-enhance

# 降低分辨率（256 比 512 快 2-3 倍）
--size 256

# 使用更快的预处理模式
--preprocess crop  # 最快，但可能裁剪部分画面
--preprocess resize  # 较快，保持完整画面

# 启用 still 模式（仅唇形动画，头部不移动，节省 30-40% 时间）
# 注意：still 模式在快速模式中自动启用
```

### 3. 组合优化示例

```bash
# 平衡模式（速度和质量平衡）
uv run python scripts/generate_lesson10_voice_and_talking_head.py \
    --talking-head-only \
    --no-face-enhance \
    --size 256 \
    --preprocess resize

# 极速模式（最快速度）
uv run python scripts/generate_lesson10_voice_and_talking_head.py \
    --talking-head-only \
    --fast-mode
```

## 📊 性能对比

| 配置 | 10秒音频耗时 | 速度提升 | 质量 |
|------|------------|---------|------|
| **默认（512, full, 增强）** | 5-10 分钟 | 1x | ⭐⭐⭐⭐⭐ |
| **优化（256, crop, 无增强）** | 1-2 分钟 | **3-5x** | ⭐⭐⭐⭐ |
| **极速（256, crop, 无增强）** | 1-2 分钟 | **3-5x** | ⭐⭐⭐ |

## 💡 其他优化建议

### 1. 系统优化

```bash
# macOS: 关闭其他占用 CPU 的应用
# 确保有足够的 RAM（建议 8GB+）

# 使用多核处理（PyTorch 会自动使用）
export OMP_NUM_THREADS=4  # 根据 CPU 核心数调整
```

### 2. 批量处理优化

- 一次处理多个文件时，脚本会自动顺序处理
- 建议在夜间或空闲时间运行批量任务
- 可以分批处理，避免一次性处理太多文件

### 3. 音频优化

- 较短的音频文件处理更快
- 如果音频很长，考虑分段处理

## 🔍 检查当前配置

```bash
# 查看帮助信息
uv run python scripts/generate_lesson10_voice_and_talking_head.py --help

# 检查安装状态
uv run python scripts/generate_lesson10_voice_and_talking_head.py --check
```

## 📝 使用示例

### 示例 1: 快速生成（推荐）

```bash
uv run python scripts/generate_lesson10_voice_and_talking_head.py \
    --talking-head-only \
    --fast-mode
```

### 示例 2: 自定义优化

```bash
uv run python scripts/generate_lesson10_voice_and_talking_head.py \
    --talking-head-only \
    --no-face-enhance \
    --size 256 \
    --preprocess resize
```

### 示例 3: 质量优先（较慢）

```bash
uv run python scripts/generate_lesson10_voice_and_talking_head.py \
    --talking-head-only \
    --size 512 \
    --preprocess full
```

## ⚠️ 注意事项

1. **分辨率选择**
   - `256`: 适合预览、测试、快速迭代
   - `512`: 适合最终输出、高质量需求

2. **预处理模式**
   - `crop`: 最快，但可能裁剪部分画面
   - `resize`: 较快，保持完整画面
   - `full`: 最慢，但质量最好

3. **Still 模式**
   - 启用：仅唇形动画，头部不移动，速度更快（节省 30-40% 时间）
   - 禁用：头部会随音频移动，更自然但更慢
   - 快速模式中自动启用

4. **面部增强**
   - 禁用可节省 20-30% 时间
   - 质量损失通常不明显
   - 建议在快速迭代时禁用

## 🎯 推荐配置

**对于无 GPU 环境，推荐使用：**

```bash
--fast-mode
```

或者手动配置：

```bash
--no-face-enhance --size 256 --preprocess resize
```

这样可以获得最佳的速度/质量平衡。

