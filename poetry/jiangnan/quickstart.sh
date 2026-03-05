#!/bin/bash
# 快速开始脚本 - 自动生成《江南》信息图

set -e

echo "🌸 《江南》古诗信息图生成器"
echo "======================================"
echo ""

# 检查是否在正确的目录
if [ ! -f "pyproject.toml" ]; then
    echo "❌ 错误：请在项目根目录运行此脚本"
    echo "   cd /Users/xuejiao/Codes/yyy_ball"
    exit 1
fi

echo "📦 检查依赖..."

# 选项菜单
echo ""
echo "请选择生成方式："
echo "  1. Python + Pillow (推荐，速度快)"
echo "  2. HTML + Playwright (需要安装浏览器)"
echo ""
read -p "请输入选项 [1/2]: " choice

case $choice in
    1)
        echo ""
        echo "📥 安装 Pillow..."
        uv add pillow
        
        echo ""
        echo "🎨 生成信息图..."
        uv run poetry/jiangnan/generator_pillow.py
        
        echo ""
        echo "✅ 完成！"
        echo "📁 生成的文件：poetry/jiangnan/jiangnan_infographic.png"
        ;;
    2)
        echo ""
        echo "📥 安装 Playwright..."
        uv add playwright
        
        echo ""
        echo "🌐 安装 Chromium 浏览器..."
        uv run playwright install chromium
        
        echo ""
        echo "🎨 生成信息图..."
        uv run poetry/jiangnan/generator_html.py
        
        echo ""
        echo "✅ 完成！"
        echo "📁 生成的文件："
        echo "   - poetry/jiangnan/jiangnan_template.html (可在浏览器中预览)"
        echo "   - poetry/jiangnan/jiangnan_infographic_html.png"
        ;;
    *)
        echo "❌ 无效选项"
        exit 1
        ;;
esac

echo ""
echo "🎉 大功告成！"
