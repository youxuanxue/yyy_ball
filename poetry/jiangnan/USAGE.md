# 📖 信息图生成器使用说明

## 🎯 快速开始

我们提供了两种自动化生成方案：

1. **Python + Pillow** - 纯代码生成，完全可控
2. **HTML + Playwright** - Web 技术渲染，易于调整

---

## 方案一：Pillow 生成器

### 安装依赖

```bash
cd /Users/xuejiao/Codes/yyy_ball
uv add pillow
```

### 运行生成器

```bash
uv run poetry/jiangnan/generator_pillow.py
```

### 输出文件

生成的图片位于：`poetry/jiangnan/jiangnan_infographic.png`

### 优点
- ✅ 无需浏览器，速度快
- ✅ 完全控制每个像素
- ✅ 适合批量生成
- ✅ 依赖少，部署简单

### 定制方法

编辑 `generator_pillow.py`：

```python
# 修改尺寸
generator = JiangnanInfographic(width=1080, height=1920)

# 修改颜色
self.colors = {
    'title': '#5D4037',      # 标题颜色
    'accent': '#4CAF50',     # 强调色
    # ...
}

# 修改字体大小
font_title = self.load_font(60)  # 调整数字
```

---

## 方案二：HTML + Playwright 生成器

### 安装依赖

```bash
cd /Users/xuejiao/Codes/yyy_ball
uv add playwright
uv run playwright install chromium
```

### 运行生成器

```bash
uv run poetry/jiangnan/generator_html.py
```

### 输出文件

- HTML 模板：`poetry/jiangnan/jiangnan_template.html`
- 生成图片：`poetry/jiangnan/jiangnan_infographic_html.png`

### 优点
- ✅ 使用熟悉的 HTML/CSS
- ✅ 易于调整布局和样式
- ✅ 可以在浏览器中预览
- ✅ 支持更丰富的 CSS 特效

### 定制方法

1. **直接编辑 HTML 模板**

运行一次生成器后，会创建 `jiangnan_template.html`，你可以：
- 用浏览器打开预览
- 修改 CSS 样式
- 调整布局和内容
- 再次运行脚本生成图片

2. **修改 Python 代码**

编辑 `generator_html.py` 中的 `HTML_TEMPLATE` 变量。

---

## 🎨 定制指南

### 修改颜色

#### Pillow 版本
```python
self.colors = {
    'title': '#你的颜色',
    'accent': '#你的颜色',
    # ...
}
```

#### HTML 版本
```css
.main-title {
    color: #你的颜色;
}
.accent {
    color: #你的颜色;
}
```

### 修改字体大小

#### Pillow 版本
```python
font_title = self.load_font(60)     # 标题 60pt
font_content = self.load_font(32)   # 正文 32pt
```

#### HTML 版本
```css
.main-title {
    font-size: 60px;  /* 标题 */
}
.bullet-list {
    font-size: 32px;  /* 正文 */
}
```

### 修改布局

#### Pillow 版本
调整 `y_start` 和间距参数

#### HTML 版本
修改 CSS 的 `margin`、`padding` 属性

---

## 🔧 高级用法

### 批量生成多首诗

创建数据文件 `poems.json`：

```json
[
  {
    "title": "江南",
    "author": "汉乐府",
    "content": ["江南可采莲，莲叶何田田。", "..."],
    "background": "...",
    "meaning": "..."
  },
  {
    "title": "咏鹅",
    "author": "骆宾王",
    "content": ["鹅鹅鹅，曲项向天歌。", "..."],
    "background": "...",
    "meaning": "..."
  }
]
```

然后修改生成器读取 JSON 数据。

### 添加插图

#### Pillow 版本

```python
from PIL import Image

# 加载插图
lotus_img = Image.open('lotus.png')
# 调整大小
lotus_img = lotus_img.resize((200, 200))
# 粘贴到画布
self.image.paste(lotus_img, (x, y), lotus_img)
```

#### HTML 版本

```html
<img src="lotus.png" class="illustration" />
```

```css
.illustration {
    width: 200px;
    height: 200px;
    margin: 20px auto;
    display: block;
}
```

### 添加水印

#### Pillow 版本

```python
font_watermark = self.load_font(20)
self.draw.text(
    (self.width - 200, self.height - 50),
    "© 2026 YYY Ball",
    fill='#CCCCCC',
    font=font_watermark
)
```

---

## 📊 性能对比

| 方案 | 生成时间 | 内存占用 | 输出质量 |
|------|---------|---------|---------|
| Pillow | ~1秒 | ~50MB | PNG 高清 |
| HTML + Playwright | ~3秒 | ~200MB | PNG 高清 |

---

## 🐛 常见问题

### Q: 中文字体显示不正常

**Pillow 版本**：
- macOS: 系统自带 PingFang.ttc
- Linux: 需要安装中文字体包
  ```bash
  sudo apt install fonts-wqy-microhei
  ```

**HTML 版本**：
- 浏览器会自动使用系统字体

### Q: 生成的图片太长/太短

修改画布高度：
```python
generator = JiangnanInfographic(width=1080, height=2400)  # 增加高度
```

### Q: Playwright 安装失败

尝试手动安装：
```bash
python -m playwright install chromium
```

### Q: 想要更精美的手绘效果

建议：
1. 使用 AI 生成手绘素材（参考 `ai_prompts.md`）
2. 用 Pillow 将素材拼接到画布上
3. 或者在 Figma/Canva 中手动设计

---

## 📚 扩展阅读

### Pillow 文档
- 官网：https://pillow.readthedocs.io/
- 中文教程：搜索"Python Pillow 教程"

### Playwright 文档
- 官网：https://playwright.dev/python/
- 截图功能：https://playwright.dev/python/docs/screenshots

### 其他工具推荐
- **Typst**：现代化排版系统 - https://typst.app/
- **ReportLab**：PDF 生成库 - https://www.reportlab.com/
- **CairoSVG**：SVG 转图片 - https://cairosvg.org/

---

## 💡 最佳实践

1. **先用 HTML 快速原型**
   - 在浏览器中调整样式
   - 确定最终布局

2. **再用 Pillow 精确实现**
   - 精确控制位置
   - 适合批量生成

3. **添加 AI 生成的插图**
   - 使用 `ai_prompts.md` 中的提示词
   - 将生成的图片嵌入信息图

4. **版本控制**
   - 将生成器代码纳入 git
   - 保留多个版本迭代
