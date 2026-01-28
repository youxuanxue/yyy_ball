"""
从B站动态爬取或解析本地古诗词内容
支持在线爬取和本地文件解析两种模式
"""
import requests
import json
import re
import sys
from pathlib import Path
from typing import List, Dict, Optional

# 输入输出目录
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR.parent.parent / "assets" / "data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 本地文件路径
RAW_TEXT_FILE = SCRIPT_DIR / "bilibili_poetry_raw.txt"
API_JSON_FILE = SCRIPT_DIR / "bilibili_poetry_api.json"

# 输出文件路径
OUTPUT_FILE = OUTPUT_DIR / "bilibili_poetry_94.json"
MARKDOWN_FILE = OUTPUT_DIR.parent / "books" / "小学生必备古诗词94首_完整版.md"

# 网络请求头
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Referer": "https://www.bilibili.com",
}


def fetch_bilibili_opus(opus_id: str) -> Optional[Dict]:
    """
    从B站动态API获取内容
    """
    try:
        # 先尝试API接口
        api_url = f"https://api.bilibili.com/x/polymer/web-dynamic/v1/opus/detail?id={opus_id}"
        
        response = requests.get(api_url, headers=HEADERS, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('code') == 0:
                return data.get('data')
        
        # 如果API失败，尝试直接获取网页
        web_url = f"https://www.bilibili.com/opus/{opus_id}"
        response = requests.get(web_url, headers=HEADERS, timeout=15)
        
        if response.status_code == 200:
            html = response.text
            # 尝试从网页中提取JSON数据
            match = re.search(r'window\.__INITIAL_STATE__\s*=\s*({.*?});', html, re.DOTALL)
            if match:
                json_data = json.loads(match.group(1))
                return json_data
            
            return {'html': html}
    
    except Exception as e:
        print(f"获取B站动态失败: {e}")
    
    return None


def parse_poetry_from_api_data(data: Dict) -> List[Dict]:
    """
    从API返回的数据中解析古诗词
    """
    poems = []
    
    if not data:
        return poems
    
    # 尝试从API返回的数据中提取文本
    text = ""
    
    # 格式1: 标准API响应
    if 'item' in data:
        item = data['item']
        if 'modules' in item:
            modules = item['modules']
            if 'module_content' in modules:
                content = modules['module_content']
                if 'desc' in content:
                    text = content['desc'].get('text', '')
    
    # 格式2: data字段包装
    elif 'data' in data:
        item = data['data'].get('item', {})
        modules = item.get('modules', {})
        module_content = modules.get('module_content', {})
        desc = module_content.get('desc', {})
        text = desc.get('text', '')
    
    # 格式3: HTML内容
    elif 'html' in data:
        html = data['html']
        # 提取文本内容
        text_match = re.search(r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL)
        if text_match:
            text = text_match.group(1)
            text = re.sub(r'<[^>]+>', '', text)
    
    if text:
        poems = parse_text_to_poems(text)
    
    return poems


def parse_text_to_poems(text: str) -> List[Dict]:
    """
    从文本中解析古诗词
    支持多种格式：
    1. 序号. 诗名 - 作者（朝代）
    2. 序号.《诗名》作者
    3. 序号、诗名
    """
    poems = []
    
    # 按行分割
    lines = text.split('\n')
    
    current_poem = None
    poem_content_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # 尝试匹配各种标题格式
        # 格式1: 1. 咏鹅 - 骆宾王（唐）
        title_match1 = re.match(r'^(\d+)[\.、]\s*《?([^》\-（—]+)》?\s*[-—]\s*([^（）]+)[（\(]([^）\)]+)[）\)]', line)
        # 格式2: 1.《咏鹅》骆宾王
        title_match2 = re.match(r'^(\d+)[\.、]\s*《([^》]+)》\s*([^\s]+)', line)
        # 格式3: 1. 咏鹅
        title_match3 = re.match(r'^(\d+)[\.、]\s*《?([^》0-9]+)》?$', line)
        
        if title_match1:
            # 保存上一首
            if current_poem and poem_content_lines:
                current_poem['content'] = '\n'.join(poem_content_lines)
                poems.append(current_poem)
                poem_content_lines = []
            
            index = int(title_match1.group(1))
            title = title_match1.group(2).strip()
            author = title_match1.group(3).strip()
            dynasty = title_match1.group(4).strip()
            
            current_poem = {
                'index': index,
                'title': title,
                'author': author,
                'dynasty': dynasty,
            }
        
        elif title_match2:
            if current_poem and poem_content_lines:
                current_poem['content'] = '\n'.join(poem_content_lines)
                poems.append(current_poem)
                poem_content_lines = []
            
            index = int(title_match2.group(1))
            title = title_match2.group(2).strip()
            author = title_match2.group(3).strip()
            
            current_poem = {
                'index': index,
                'title': title,
                'author': author,
                'dynasty': '',
            }
        
        elif title_match3:
            if current_poem and poem_content_lines:
                current_poem['content'] = '\n'.join(poem_content_lines)
                poems.append(current_poem)
                poem_content_lines = []
            
            index = int(title_match3.group(1))
            title = title_match3.group(2).strip()
            
            current_poem = {
                'index': index,
                'title': title,
                'author': '',
                'dynasty': '',
            }
        
        # 诗句内容（不是标题的行）
        elif current_poem and not re.match(r'^\d+[\.、]', line):
            poem_content_lines.append(line)
    
    # 添加最后一首
    if current_poem:
        if poem_content_lines:
            current_poem['content'] = '\n'.join(poem_content_lines)
        else:
            current_poem['content'] = ''
        poems.append(current_poem)
    
    return poems


def parse_api_json_file(json_file: Path) -> List[Dict]:
    """
    从本地API JSON文件解析古诗词
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return parse_poetry_from_api_data(data)
    
    except Exception as e:
        print(f"解析API JSON文件失败: {e}")
    
    return []


def save_to_json(poems: List[Dict]):
    """保存为JSON格式"""
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(poems, f, ensure_ascii=False, indent=2)
    print(f"✓ 已保存JSON数据到: {OUTPUT_FILE}")


def save_to_markdown(poems: List[Dict]):
    """保存为Markdown格式"""
    MARKDOWN_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    with open(MARKDOWN_FILE, 'w', encoding='utf-8') as f:
        f.write("# 小学生必备古诗词94首\n\n")
        f.write("> 来源: B站动态 https://www.bilibili.com/opus/711270159465054226\n\n")
        f.write("## 目录\n\n")
        
        for poem in poems:
            index = poem.get('index', 0)
            title = poem.get('title', '')
            f.write(f"{index}. {title}\n")
        
        f.write("\n---\n\n")
        
        for poem in poems:
            index = poem.get('index', 0)
            title = poem.get('title', '')
            content = poem.get('content', '')
            author = poem.get('author', '')
            dynasty = poem.get('dynasty', '')
            
            f.write(f"## {index}. {title}\n\n")
            
            if author or dynasty:
                if dynasty and author:
                    f.write(f"**{dynasty}** · {author}\n\n")
                elif author:
                    f.write(f"**作者**: {author}\n\n")
            
            if content:
                # 格式化内容
                lines = content.split('\n')
                for line in lines:
                    line = line.strip()
                    if line:
                        f.write(f"{line}  \n")
                f.write("\n")
            else:
                f.write("*(内容待补充)*\n\n")
            
            f.write("---\n\n")
    
    print(f"✓ 已保存Markdown文件到: {MARKDOWN_FILE}")


def crawl_from_bilibili(opus_id: str = "711270159465054226") -> List[Dict]:
    """
    从B站在线爬取古诗词
    """
    print(f"🌐 开始从B站动态爬取: {opus_id}")
    
    data = fetch_bilibili_opus(opus_id)
    
    if not data:
        print("❌ 无法获取B站动态内容")
        return []
    
    poems = parse_poetry_from_api_data(data)
    
    if poems:
        print(f"✓ 成功爬取并解析 {len(poems)} 首古诗词\n")
    
    return poems


def parse_from_local() -> List[Dict]:
    """
    从本地文件解析古诗词
    """
    print("📁 开始从本地文件解析...\n")
    
    poems = []
    
    # 优先尝试API JSON文件
    if API_JSON_FILE.exists():
        print(f"找到API JSON文件: {API_JSON_FILE}")
        poems = parse_api_json_file(API_JSON_FILE)
        if poems:
            print(f"✓ 从API JSON解析出 {len(poems)} 首古诗词\n")
            return poems
    
    # 尝试纯文本文件
    if RAW_TEXT_FILE.exists():
        print(f"找到文本文件: {RAW_TEXT_FILE}")
        with open(RAW_TEXT_FILE, 'r', encoding='utf-8') as f:
            text = f.read()
        poems = parse_text_to_poems(text)
        if poems:
            print(f"✓ 从文本文件解析出 {len(poems)} 首古诗词\n")
            return poems
    
    print("❌ 未找到本地文件")
    print("\n请先按照以下步骤操作：")
    print("1. 访问: https://www.bilibili.com/opus/711270159465054226")
    print("2. 将页面内容保存到以下任一文件：")
    print(f"   - {RAW_TEXT_FILE} (纯文本)")
    print(f"   - {API_JSON_FILE} (JSON格式)")
    
    return []


def main():
    """
    主函数
    支持两种模式：
    1. 默认/--crawl: 在线爬取（如果失败自动尝试本地文件）
    2. --local: 仅从本地文件解析
    """
    # 解析命令行参数
    mode = 'auto'  # auto, crawl, local
    
    if '--local' in sys.argv or '-l' in sys.argv:
        mode = 'local'
    elif '--crawl' in sys.argv or '-c' in sys.argv:
        mode = 'crawl'
    
    poems = []
    
    # 模式1: 仅本地解析
    if mode == 'local':
        poems = parse_from_local()
    
    # 模式2: 仅在线爬取
    elif mode == 'crawl':
        poems = crawl_from_bilibili()
    
    # 模式3: 自动模式（先爬取，失败则本地）
    else:
        print("🚀 自动模式: 先尝试在线爬取，失败则使用本地文件\n")
        poems = crawl_from_bilibili()
        
        if not poems:
            print("⚠️  在线爬取失败，尝试本地文件...\n")
            poems = parse_from_local()
    
    # 检查是否有数据
    if not poems:
        print("\n❌ 失败: 无法获取古诗词数据")
        print("\n💡 建议：")
        print("  1. 检查网络连接后重试")
        print("  2. 或手动保存文件后使用: python crawler_poetry_bilibili.py --local")
        return
    
    # 显示预览
    print("📖 预览前3首：")
    for poem in poems[:3]:
        print(f"  {poem['index']}. {poem['title']}", end='')
        if poem.get('author'):
            print(f" - {poem['author']}", end='')
        if poem.get('dynasty'):
            print(f"（{poem['dynasty']}）", end='')
        print()
    print()
    
    # 保存数据
    save_to_json(poems)
    save_to_markdown(poems)
    
    print(f"\n✅ 完成! 共获取 {len(poems)} 首古诗词")
    print(f"   JSON: {OUTPUT_FILE}")
    print(f"   Markdown: {MARKDOWN_FILE}")


if __name__ == "__main__":
    # 显示使用说明
    if '--help' in sys.argv or '-h' in sys.argv:
        print("""
小学生必备古诗词94首 - 爬虫和解析工具

用法:
  python crawler_poetry_bilibili.py           # 自动模式（推荐）
  python crawler_poetry_bilibili.py --crawl   # 仅在线爬取
  python crawler_poetry_bilibili.py --local   # 仅本地解析
  python crawler_poetry_bilibili.py --help    # 显示帮助

模式说明:
  自动模式: 先尝试在线爬取，如果失败则自动使用本地文件
  在线爬取: 从B站动态API获取数据
  本地解析: 从本地文件 (bilibili_poetry_raw.txt 或 bilibili_poetry_api.json) 读取

输出文件:
  - assets/data/bilibili_poetry_94.json
  - assets/books/小学生必备古诗词94首_完整版.md
        """)
    else:
        main()
