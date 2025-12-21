# Manim 图标快速参考指南

## 快速开始

### 1. 导入图标工具
```python
from src.utils.icon_helper import emoji_icon, svg_icon, create_icon
```

### 2. 使用 Emoji 图标（推荐）
```python
# 基本用法
handshake = emoji_icon("handshake", font_size=72)
fist = emoji_icon("fist", font_size=72, color=RED)

# 在动画中使用
self.play(GrowFromCenter(handshake))
```

### 3. 使用 SVG 图标
```python
# 需要先下载 SVG 文件到 assets/icons/ 目录
custom_icon = svg_icon("my_icon", scale=2, color=BLUE)
```

## 常用图标列表

### 手势图标
| 图标名称 | Emoji | 说明 |
|---------|-------|------|
| `handshake` | 🤝 | 握手/合作 |
| `fist` | ✊ | 拳头 |
| `punch` | 👊 | 出拳 |
| `thumbs_up` | 👍 | 点赞 |
| `thumbs_down` | 👎 | 点踩 |
| `wave` | 👋 | 挥手 |
| `stop` | ✋ | 停止 |
| `point` | 👉 | 指向 |

### 人物图标
| 图标名称 | Emoji | 说明 |
|---------|-------|------|
| `person` | 👤 | 单人 |
| `people` | 👥 | 多人 |
| `man` | 👨 | 男人 |
| `woman` | 👩 | 女人 |
| `child` | 👶 | 小孩 |
| `boy` | 👦 | 男孩 |
| `girl` | 👧 | 女孩 |

### 表情图标
| 图标名称 | Emoji | 说明 |
|---------|-------|------|
| `happy` | 😊 | 开心 |
| `sad` | 😢 | 难过 |
| `angry` | 😡 | 生气 |
| `surprised` | 😱 | 惊讶 |
| `cool` | 😎 | 酷 |
| `thinking` | 🤔 | 思考 |

### 物品图标
| 图标名称 | Emoji | 说明 |
|---------|-------|------|
| `gift` | 🎁 | 礼物 |
| `trophy` | 🏆 | 奖杯 |
| `money` | 💰 | 金钱 |
| `coin` | 🪙 | 硬币 |
| `sword` | ⚔️ | 剑 |
| `shield` | 🛡️ | 盾牌 |
| `crown` | 👑 | 皇冠 |
| `star` | ⭐ | 星星 |
| `medal` | 🏅 | 奖牌 |

### 动作图标
| 图标名称 | Emoji | 说明 |
|---------|-------|------|
| `running` | 🏃 | 跑步 |
| `strength` | 💪 | 力量 |
| `game` | 🎮 | 游戏 |
| `art` | 🎨 | 艺术 |
| `book` | 📚 | 书籍 |
| `lightbulb` | 💡 | 灯泡/想法 |

### 其他图标
| 图标名称 | Emoji | 说明 |
|---------|-------|------|
| `fire` | 🔥 | 火 |
| `lightning` | ⚡ | 闪电 |
| `check` | ✅ | 对勾 |
| `cross` | ❌ | 叉号 |
| `question` | ❓ | 问号 |
| `exclamation` | ❗ | 感叹号 |
| `heart` | ❤️ | 爱心 |

## 实际替换示例

### 示例 1：替换握手图标

**旧代码（手动绘制）：**
```python
handshake = VGroup(
    Circle(radius=0.3, color=GREEN, fill_opacity=0.5).shift(LEFT*0.4),
    Circle(radius=0.3, color=GREEN, fill_opacity=0.5).shift(RIGHT*0.4),
    Line(LEFT*0.1, RIGHT*0.1, color=GREEN, stroke_width=4).shift(UP*0.1)
)
```

**新代码（使用 emoji）：**
```python
handshake = emoji_icon("handshake", font_size=72)
```

### 示例 2：替换拳头图标

**旧代码：**
```python
fist_icon = VGroup(
    Circle(radius=0.3, color=RED, fill_opacity=0.5),
    Text("拳头", font_size=24, color=RED, weight=BOLD)
)
```

**新代码：**
```python
fist_icon = emoji_icon("fist", font_size=72, color=RED)
```

### 示例 3：替换胜利图标

**旧代码：**
```python
win_icon = VGroup(
    Star(color=GOLD, fill_opacity=0.8).scale(0.4),
    Text("WIN", font_size=24, color=GOLD, weight=BOLD)
)
```

**新代码：**
```python
win_icon = emoji_icon("trophy", font_size=72)
```

## 高级用法

### 组合图标和文字
```python
# 图标 + 文字标签
icon_with_label = VGroup(
    emoji_icon("handshake", font_size=72),
    Text("合作", font_size=24).next_to(emoji_icon("handshake", font_size=72), DOWN, buff=0.2)
)
```

### 图标动画
```python
handshake = emoji_icon("handshake", font_size=72)

# 常用动画
self.play(GrowFromCenter(handshake))  # 从中心生长
self.play(FadeIn(handshake))          # 淡入
self.play(Indicate(handshake, color=YELLOW))  # 高亮指示
self.play(handshake.animate.scale(1.5))  # 缩放动画
```

### 图标颜色背景
```python
# 添加彩色背景（emoji 本身颜色不可改）
handshake = emoji_icon("handshake", font_size=72, color=GREEN)
# 这会添加一个半透明的绿色背景圆
```

## SVG 图标资源

### 推荐网站
1. **Flaticon** - https://www.flaticon.com/
   - 超过 500 万免费图标
   - 支持 SVG 格式下载
   - 需要注册（免费）

2. **Icons8** - https://icons8.com/
   - 高质量图标库
   - 多种风格可选
   - 部分免费

3. **Font Awesome** - https://fontawesome.com/
   - 可下载 SVG 版本
   - 图标风格统一

4. **Material Icons** - https://fonts.google.com/icons
   - Google 官方图标
   - 简洁现代风格

### 使用 SVG 图标
1. 下载 SVG 文件
2. 保存到 `assets/icons/` 目录
3. 使用 `svg_icon("文件名", scale=1, color=BLUE)` 加载

```python
# 示例：使用自定义 SVG 图标
custom_icon = svg_icon("my_custom_icon", scale=2, color=RED)
```

## 常见问题

### Q: emoji 颜色无法修改怎么办？
A: emoji 本身的颜色是固定的，但可以通过 `color` 参数添加半透明背景。如果需要完全自定义颜色，建议使用 SVG 图标。

### Q: 找不到需要的图标怎么办？
A: 
1. 查看完整的图标列表（见上方表格）
2. 使用相近的图标替代
3. 从图标网站下载 SVG 版本
4. 对于特殊需求，可以手动绘制

### Q: 如何批量替换现有代码中的图标？
A: 
1. 先识别所有手动绘制的图标
2. 找到对应的 emoji 或下载 SVG
3. 逐个替换，测试效果
4. 建议一次替换一个场景，确保效果满意

## 最佳实践

1. **优先使用 emoji**：简单、高效、零成本
2. **复杂图标用 SVG**：需要特定风格时
3. **保持一致性**：同一类型的图标使用相同的风格
4. **适当大小**：根据场景调整图标大小（通常 48-96）
5. **添加动画**：让图标更有生命力

## 相关文档

- 图标工具源码：`src/utils/icon_helper.py`

