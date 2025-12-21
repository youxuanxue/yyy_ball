#!/bin/bash
# 将 SadTalker 的 requirements.txt 转换为 uv add 命令

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REQUIREMENTS_FILE="$PROJECT_ROOT/external/SadTalker/requirements.txt"

if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "❌ 错误: requirements.txt 不存在: $REQUIREMENTS_FILE"
    echo "💡 请先克隆 SadTalker: git clone https://github.com/OpenTalker/SadTalker.git external/SadTalker"
    exit 1
fi

echo "=========================================="
echo "📦 添加 SadTalker 依赖到 pyproject.toml"
echo "=========================================="
echo ""

# 检查 uv 是否安装
if ! command -v uv &> /dev/null; then
    echo "❌ 错误: uv 未安装"
    echo "💡 请先安装 uv: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

echo "✅ 检测到 uv"
echo ""

# 读取 requirements.txt 并转换为 uv add 命令
cd "$PROJECT_ROOT"

echo "📥 正在添加依赖..."
echo ""

# 处理每个依赖
while IFS= read -r line || [ -n "$line" ]; do
    # 跳过空行和注释
    line=$(echo "$line" | sed 's/#.*$//' | xargs)
    if [ -z "$line" ]; then
        continue
    fi
    
    # 提取包名和版本
    if [[ "$line" == *"=="* ]]; then
        # 有版本号的情况: package==version
        package=$(echo "$line" | cut -d'=' -f1 | xargs)
        version=$(echo "$line" | cut -d'=' -f3 | xargs)
        echo "  ➕ 添加: $package==$version"
        uv add "$package==$version" || echo "    ⚠️  添加失败（可能已存在或版本冲突）"
    else
        # 无版本号的情况: package
        package=$(echo "$line" | xargs)
        echo "  ➕ 添加: $package"
        uv add "$package" || echo "    ⚠️  添加失败（可能已存在）"
    fi
done < "$REQUIREMENTS_FILE"

echo ""
echo "✅ 依赖添加完成！"
echo ""
echo "💡 提示:"
echo "   - 如果遇到版本冲突（如 scipy），uv 会尝试解决"
echo "   - 可以手动检查 pyproject.toml 查看添加的依赖"
echo "   - 使用 'uv sync' 同步环境"
echo ""

