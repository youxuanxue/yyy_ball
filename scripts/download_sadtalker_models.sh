#!/bin/bash
# 下载 SadTalker 预训练模型（兼容 macOS 和 Linux）

set -e

SADTALKER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/external/SadTalker"
CHECKPOINTS_DIR="$SADTALKER_DIR/checkpoints"
GFPGAN_WEIGHTS_DIR="$SADTALKER_DIR/gfpgan/weights"

echo "=========================================="
echo "下载 SadTalker 预训练模型"
echo "=========================================="
echo "目标目录: $CHECKPOINTS_DIR"
echo ""

# 创建目录
mkdir -p "$CHECKPOINTS_DIR"
mkdir -p "$GFPGAN_WEIGHTS_DIR"

# 检测下载工具
if command -v wget &> /dev/null; then
    DOWNLOAD_CMD="wget -nc"
elif command -v curl &> /dev/null; then
    DOWNLOAD_CMD="curl -L -o"
else
    echo "❌ 错误: 未找到 wget 或 curl"
    exit 1
fi

# 下载函数
download_file() {
    local url=$1
    local output=$2
    local filename=$(basename "$output")
    
    if [ -f "$output" ]; then
        echo "✅ $filename 已存在，跳过下载"
        return 0
    fi
    
    echo "📥 下载 $filename..."
    if [ "$DOWNLOAD_CMD" = "wget -nc" ]; then
        wget -nc "$url" -O "$output"
    else
        # curl 方式
        curl -L "$url" -o "$output" || {
            echo "❌ 下载失败: $filename"
            return 1
        }
    fi
    echo "✅ $filename 下载完成"
}

cd "$SADTALKER_DIR"

# 下载新版本模型（推荐）
echo "📦 下载 SadTalker 核心模型..."
download_file "https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/mapping_00109-model.pth.tar" "$CHECKPOINTS_DIR/mapping_00109-model.pth.tar"
download_file "https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/mapping_00229-model.pth.tar" "$CHECKPOINTS_DIR/mapping_00229-model.pth.tar"
download_file "https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/SadTalker_V0.0.2_256.safetensors" "$CHECKPOINTS_DIR/SadTalker_V0.0.2_256.safetensors"
download_file "https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/SadTalker_V0.0.2_512.safetensors" "$CHECKPOINTS_DIR/SadTalker_V0.0.2_512.safetensors"

# 下载 GFPGAN 增强模型
echo ""
echo "📦 下载 GFPGAN 增强模型..."
download_file "https://github.com/xinntao/facexlib/releases/download/v0.1.0/alignment_WFLW_4HG.pth" "$GFPGAN_WEIGHTS_DIR/alignment_WFLW_4HG.pth"
download_file "https://github.com/xinntao/facexlib/releases/download/v0.1.0/detection_Resnet50_Final.pth" "$GFPGAN_WEIGHTS_DIR/detection_Resnet50_Final.pth"
download_file "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth" "$GFPGAN_WEIGHTS_DIR/GFPGANv1.4.pth"
download_file "https://github.com/xinntao/facexlib/releases/download/v0.2.2/parsing_parsenet.pth" "$GFPGAN_WEIGHTS_DIR/parsing_parsenet.pth"

echo ""
echo "=========================================="
echo "✅ 模型下载完成！"
echo "=========================================="
echo ""
echo "已下载的模型文件："
ls -lh "$CHECKPOINTS_DIR"/*.pth* "$CHECKPOINTS_DIR"/*.safetensors 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'
echo ""
echo "GFPGAN 模型文件："
ls -lh "$GFPGAN_WEIGHTS_DIR"/*.pth 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'

