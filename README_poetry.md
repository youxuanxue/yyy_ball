# 小学生必备古诗词94首

> 数据来源: [B站动态](https://www.bilibili.com/opus/711270159465054226)

## 📚 生成的文件

| 文件 | 位置 | 说明 |
|------|------|------|
| **Markdown完整版** | `assets/books/小学生必备古诗词94首_完整版.md` | 格式优美，适合阅读打印 |
| **JSON数据** | `assets/data/bilibili_poetry_94.json` | 结构化数据，方便程序调用 |
| **原始文本** | `src/crawlers/bilibili_poetry_raw.txt` | 纯文本格式 |

## 🚀 快速开始

### 使用现有数据
直接使用已生成的文件即可，包含完整的94首古诗词。

### 重新爬取数据

```bash
# 自动模式（推荐）：先在线爬取，失败则使用本地文件
python3 src/crawlers/crawler_poetry_bilibili.py

# 仅本地解析模式
python3 src/crawlers/crawler_poetry_bilibili.py --local

# 查看帮助
python3 src/crawlers/crawler_poetry_bilibili.py --help
```

## 📋 内容概览

**共94首古诗词**，涵盖从汉代到明清各个朝代：

### 按朝代分布
- **唐诗** (~60首): 李白、杜甫、王维、白居易等
- **宋诗词** (~25首): 苏轼、王安石、杨万里、陆游、辛弃疾等  
- **其他** (~9首): 汉乐府、曹植、陶渊明、王冕、于谦、郑燮等

### 经典作品示例
- 李白：静夜思、望庐山瀑布、赠汪伦、黄鹤楼送孟浩然之广陵...
- 杜甫：绝句、春夜喜雨、江畔独步寻花、望岳、春望...
- 苏轼：题西林壁、饮湖上初晴后雨、惠崇春江晚景...
- 其他：咏鹅、江南、敕勒歌、游子吟、石灰吟、竹石...

## 📖 数据格式

### JSON格式示例
```json
{
  "index": 1,
  "title": "咏鹅",
  "author": "骆宾王",
  "dynasty": "唐",
  "content": "鹅，鹅，鹅，曲项向天歌。\n白毛浮绿水，红掌拨清波。"
}
```

### 文本格式示例
```
1. 咏鹅 - 骆宾王（唐）
鹅，鹅，鹅，曲项向天歌。
白毛浮绿水，红掌拨清波。
```

## 🛠️ 工具说明

**主脚本**: `src/crawlers/crawler_poetry_bilibili.py`

**功能特性**:
- ✅ 在线爬取B站动态
- ✅ 本地文件解析  
- ✅ 自动智能切换
- ✅ 支持多种文本格式
- ✅ 输出JSON和Markdown

**本地文件**: 如需本地解析，准备以下任一文件
- `src/crawlers/bilibili_poetry_raw.txt` (纯文本)
- `src/crawlers/bilibili_poetry_api.json` (API JSON)

## 💡 适用场景

- 📚 学习背诵（教育部推荐篇目）
- 🖨️ 打印阅读（Markdown格式）
- 💻 程序开发（JSON格式）
- 📝 教学资料（完整元数据）

---

**创建时间**: 2026-01-13  
**数据来源**: 基于教育部《义务教育语文课程标准》推荐篇目
