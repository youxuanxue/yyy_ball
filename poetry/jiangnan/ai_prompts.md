# AI 生成信息图提示词

## 🎨 完整信息图生成提示词

### 中文提示词（适用于国内AI工具）

```
设计一张儿童古诗学习信息图，主题是汉乐府民歌《江南》。

风格要求：
- 手绘插画风格，水彩/蜡笔质感
- 卡通可爱，适合6-10岁小学生
- 配色清新：翠绿莲叶、粉红荷花、淡蓝水面

内容布局（从上到下）：
1. 标题：《江南》古诗趣味学
2. 古诗原文：江南可采莲，莲叶何田田...（配莲花背景）
3. 什么是汉乐府：2000年前收集民歌的机构
4. 场景描绘：江南水乡采莲的快乐场景
5. 诗歌含义：田田=茂盛，戏=嬉戏
6. 学习收获：感受自然之美，体会劳动快乐

插图元素：莲叶、荷花、可爱小鱼、采莲小女孩、小木船

尺寸：竖版1080×1920像素
```

### 英文提示词（适用于 Midjourney/DALL-E）

#### 完整信息图

```
Create a children's educational infographic about ancient Chinese poem "Jiangnan" (江南).

Style: Hand-drawn watercolor illustration, cute cartoon style, suitable for elementary school students aged 6-10.

Color palette: Fresh green lotus leaves, pink lotus flowers, light blue water, warm beige background.

Layout (vertical, 1080x1920):
- Title section: "Learning Ancient Poetry - Jiangnan"
- Poem section with lotus background
- Historical context section about Han Dynasty folk songs
- Scene illustration: lotus picking in water village
- Meaning explanation section
- Educational takeaways section

Elements to include:
- Cute chibi style characters
- Round green lotus leaves covering water
- Pink/white lotus flowers
- Golden fish swimming around
- Small wooden boat
- Cartoon girl picking lotus
- Decorative borders with plant motifs

Text should be in Chinese.
Warm, inviting, educational, kawaii aesthetic.
--ar 9:16 --style raw
```

---

## 🖼️ 分区域生成提示词

### 1. 主插图（采莲场景）

```
Cute hand-drawn illustration of lotus picking scene in ancient Chinese water village,
A cheerful cartoon girl sitting in a small wooden boat,
Surrounded by lush green lotus leaves and blooming pink lotus flowers,
Adorable golden and orange koi fish swimming playfully around the boat,
Dragonflies and butterflies in the air,
Watercolor painting style with soft brush strokes,
Warm summer sunlight filtering through,
Peaceful and joyful atmosphere,
Children's book illustration quality,
Soft pastel color palette,
White background for easy compositing,
--ar 4:3 --style cute --v 6
```

### 2. 鱼儿东西南北动态图

```
Four cute cartoon goldfish swimming in four different directions (east, west, south, north),
Arranged in a cross pattern with arrows showing direction,
Hand-drawn style with watercolor texture,
Each fish has a happy expression,
Orange and gold colors with subtle gradients,
Simple green lotus leaf silhouettes in background,
Clean educational diagram style,
Kawaii aesthetic,
White background,
--ar 1:1 --style cute
```

### 3. 汉乐府概念图

```
Cute illustrated diagram explaining Han Dynasty music bureau (汉乐府),
Ancient Chinese palace building in cartoon style,
Musical notes and scrolls floating around,
Cartoon villagers singing songs,
Officials collecting folk songs,
Warm sepia and gold color palette,
Hand-drawn educational illustration,
Simple and clear visual hierarchy,
Children's textbook style,
Chinese cultural elements,
--ar 16:9 --style illustration
```

### 4. 江南水乡背景

```
Panoramic view of ancient Chinese Jiangnan water village,
Hand-painted watercolor style,
Stone bridges over calm canals,
Traditional white-walled houses with black roof tiles,
Willow trees with flowing branches,
Lotus ponds in the foreground,
Soft misty mountains in the background,
Morning sunlight with golden hues,
Peaceful and dreamy atmosphere,
Studio Ghibli inspired aesthetic,
--ar 21:9 --style watercolor
```

### 5. 莲花特写装饰

```
Beautiful hand-drawn lotus flower collection,
Variety of pink and white lotus blooms,
Different stages: bud, half-open, fully bloomed,
Green lotus leaves with water droplets,
Lotus seed pods,
Watercolor painting technique,
Botanical illustration style but cute,
Soft pastel colors,
Isolated on white background,
Perfect for decorative borders,
--ar 3:2 --style botanical
```

---

## 🎯 Canva/Figma 设计建议

### 如果使用 Canva 制作

1. **选择模板**：搜索 "infographic" 或 "信息图"
2. **调整尺寸**：1080×1920 像素
3. **背景色**：设置为 #FFF8E1（暖米色）
4. **添加元素**：
   - 搜索 "lotus"、"fish"、"watercolor" 相关素材
   - 使用圆角矩形作为内容框
   - 添加手绘风格边框

### 素材关键词搜索

| 元素 | 英文关键词 | 中文关键词 |
|------|-----------|-----------|
| 莲花 | lotus, water lily | 荷花, 莲花 |
| 荷叶 | lotus leaf, lily pad | 荷叶, 莲叶 |
| 锦鲤 | koi fish, goldfish | 金鱼, 锦鲤 |
| 小船 | wooden boat | 小木船 |
| 水波 | water ripples | 水纹, 波纹 |
| 手绘 | hand-drawn, sketch | 手绘, 插画 |
| 水彩 | watercolor | 水彩 |

---

## 🔧 分步制作流程

### Step 1: 生成主要插图
使用 AI 工具生成采莲场景的主插图

### Step 2: 准备文字内容
从 `poem_info.md` 提取所需文案

### Step 3: 设计布局
在 Canva/Figma 中创建布局框架

### Step 4: 组合元素
将生成的插图和文字内容组合

### Step 5: 调整优化
统一字体、颜色，确保整体协调

### Step 6: 导出成品
导出 PNG/PDF 格式
