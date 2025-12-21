#!/bin/bash
# SadTalker 模型下载脚本（兼容 macOS 和 Linux）

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SADTALKER_DIR="$PROJECT_ROOT/external/SadTalker"
CHECKPOINTS_DIR="$SADTALKER_DIR/checkpoints"

# 检测下载工具
if command -v wget &> /dev/null; then
    DOWNLOAD_CMD="wget"
    DOWNLOAD_FLAGS="-nc"
elif command -v curl &> /dev/null; then
    DOWNLOAD_CMD="curl"
    DOWNLOAD_FLAGS="-L -C -"
else
    echo "❌ 错误: 未找到 wget 或 curl"
    exit 1
fi

echo "=========================================="
echo "📥 SadTalker 模型下载脚本"
echo "=========================================="
echo ""
echo "使用工具: $DOWNLOAD_CMD"
echo ""

# 创建目录
mkdir -p "$CHECKPOINTS_DIR"
cd "$SADTALKER_DIR"

# 下载函数（带完整性检查）
download_file() {
    local url=$1
    local output=$2
    local filename=$(basename "$output")
    
    # 如果文件存在，检查是否损坏（对于 .tar 文件）
    if [ -f "$output" ]; then
        if [[ "$filename" == *.tar ]] || [[ "$filename" == *.zip ]]; then
            if unzip -t "$output" >/dev/null 2>&1 || tar -tzf "$output" >/dev/null 2>&1; then
                echo "  ✅ 已存在且完整: $filename"
                return 0
            else
                echo "  ⚠️  文件损坏，重新下载: $filename"
                rm -f "$output"
            fi
        else
            echo "  ⏭️  已存在: $filename"
            return 0
        fi
    fi
    
    echo "  📥 下载中: $filename"
    if [ "$DOWNLOAD_CMD" = "wget" ]; then
        wget --progress=bar:force "$url" -O "$output" 2>&1 | grep -E "(saved|100%)" || true
    else
        curl -L --progress-bar "$url" -o "$output"
    fi
    
    # 验证下载的文件
    if [[ "$filename" == *.tar ]] || [[ "$filename" == *.zip ]]; then
        if unzip -t "$output" >/dev/null 2>&1 || tar -tzf "$output" >/dev/null 2>&1; then
            echo "  ✅ 下载完成并验证: $filename"
        else
            echo "  ❌ 下载的文件可能损坏: $filename"
            echo "  💡 请重新运行脚本或手动下载"
            return 1
        fi
    else
        echo "  ✅ 下载完成: $filename"
    fi
}

echo "📦 下载核心模型..."
echo ""

# 核心模型
download_file \
    "https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/mapping_00109-model.pth.tar" \
    "$CHECKPOINTS_DIR/mapping_00109-model.pth.tar"

download_file \
    "https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/mapping_00229-model.pth.tar" \
    "$CHECKPOINTS_DIR/mapping_00229-model.pth.tar"

download_file \
    "https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/SadTalker_V0.0.2_256.safetensors" \
    "$CHECKPOINTS_DIR/SadTalker_V0.0.2_256.safetensors"

download_file \
    "https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/SadTalker_V0.0.2_512.safetensors" \
    "$CHECKPOINTS_DIR/SadTalker_V0.0.2_512.safetensors"

echo ""
echo "📦 下载 GFPGAN 增强模型..."
echo ""

# GFPGAN 增强模型
mkdir -p "$SADTALKER_DIR/gfpgan/weights"

download_file \
    "https://github.com/xinntao/facexlib/releases/download/v0.1.0/alignment_WFLW_4HG.pth" \
    "$SADTALKER_DIR/gfpgan/weights/alignment_WFLW_4HG.pth"

download_file \
    "https://github.com/xinntao/facexlib/releases/download/v0.1.0/detection_Resnet50_Final.pth" \
    "$SADTALKER_DIR/gfpgan/weights/detection_Resnet50_Final.pth"

download_file \
    "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth" \
    "$SADTALKER_DIR/gfpgan/weights/GFPGANv1.4.pth"

download_file \
    "https://github.com/xinntao/facexlib/releases/download/v0.2.2/parsing_parsenet.pth" \
    "$SADTALKER_DIR/gfpgan/weights/parsing_parsenet.pth"

echo ""
echo "✅ 模型下载完成！"
echo ""
echo "📁 模型位置: $CHECKPOINTS_DIR"
echo ""

