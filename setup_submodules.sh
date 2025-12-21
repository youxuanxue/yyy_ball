#!/bin/bash
# 设置外部库为 git submodule 的脚本

set -e

echo "开始设置 git submodules..."

# 1. 添加 CosyVoice 为 submodule
echo ""
echo "添加 CosyVoice submodule..."
git submodule add https://github.com/FunAudioLLM/CosyVoice.git external/CosyVoice

# 2. 添加 SadTalker 为 submodule
echo ""
echo "添加 SadTalker submodule..."
git submodule add https://github.com/OpenTalker/SadTalker.git external/SadTalker

# 3. 切换到之前使用的特定版本
echo ""
echo "切换到之前使用的版本..."
cd external/CosyVoice
git checkout 055f64d0026601a092b942c69cf7f799ca6deecb
cd ../SadTalker
git checkout cd4c0465ae0b54a6f85af57f5c65fec9fe23e7f8
cd ../..

echo ""
echo "✓ Submodule 设置完成！"
echo ""
echo "下一步：提交更改"
echo "  git add .gitmodules external/"
echo "  git commit -m 'Add external libraries as git submodules'"

