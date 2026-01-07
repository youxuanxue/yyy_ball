#!/usr/bin/env python3
"""
Icons8 图标下载爬虫（支持多种风格）

下载指定分类的免费 PNG 图标（96x96 尺寸），按照分类目录结构保存。
支持风格：doodle, plasticine, stickers

从 assets/icons8/icons8_categories.json 读取分类信息，动态生成 URL 和路径。

使用方法:
    python src/crawlers/crawler_icons8.py
"""

import json
import time
import re
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from playwright.sync_api import sync_playwright, Page, TimeoutError as PlaywrightTimeoutError
import requests

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent.parent
CATEGORIES_FILE = PROJECT_ROOT / "assets" / "icons8" / "icons8_categories.json"
OUTPUT_BASE_DIR = PROJECT_ROOT / "assets"

# 配置
REQUEST_DELAY = 1  # 请求间隔


def generate_category_url(category_name: str, style: str) -> str:
    """
    根据分类名称和风格生成 Icons8 URL
    
    Args:
        category_name: 分类名称（如 "business", "food"）
        style: 图标风格（doodle, plasticine, stickers）
        
    Returns:
        Icons8 分类页面 URL
    """
    # 将分类名称转换为 URL 格式（小写，空格替换为连字符）
    url_name = category_name.lower().replace(' ', '-')
    return f"https://icons8.com/icons/set/{url_name}--style-{style}"


def generate_category_path(category_name: str, subcategory_name: str, style: str) -> str:
    """
    根据分类名称和风格生成本地路径
    
    Args:
        category_name: 主分类名称
        subcategory_name: 子分类名称
        style: 图标风格（doodle, plasticine, stickers）
        
    Returns:
        本地路径字符串（如 "icons8/doodle/Business/Business"）
    """
    # 将分类名称转换为路径格式（首字母大写，空格替换为下划线）
    def to_path_name(name: str) -> str:
        # 处理特殊字符，保留字母数字和空格
        name = re.sub(r'[^a-zA-Z0-9\s]', '', name)
        # 将空格替换为下划线
        name = name.replace(' ', '_')
        # 将每个单词首字母大写（Title Case）
        if name:
            parts = name.split('_')
            name = '_'.join(part.capitalize() for part in parts if part)
        return name
    
    category_path = to_path_name(category_name)
    subcategory_path = to_path_name(subcategory_name)
    
    return f"icons8/{style}/{category_path}/{subcategory_path}"


def normalize_filename(title: str) -> str:
    """
    规范化文件名
    
    Args:
        title: 图标标题
        
    Returns:
        规范化后的文件名（不含扩展名）
    """
    # 转换为小写
    filename = title.lower()
    # 替换空格为下划线
    filename = filename.replace(' ', '_')
    # 替换特殊字符，只保留字母、数字、下划线和连字符
    filename = re.sub(r'[^a-z0-9_-]', '', filename)
    # 移除连续的连字符和下划线
    filename = re.sub(r'[-_]+', '_', filename)
    # 移除首尾的连字符和下划线
    filename = filename.strip('-_')
    # 限制长度
    if len(filename) > 100:
        filename = filename[:100]
    return filename


def extract_icons_from_page(page: Page, category_url: str) -> List[Dict]:
    """
    从页面中提取图标信息
    
    Args:
        page: Playwright 页面对象
        category_url: 分类页面 URL
        
    Returns:
        图标列表，每个图标包含 title, url, icon_id 等信息
    """
    icons = []
    
    try:
        print(f"  访问页面: {category_url}")
        page.goto(category_url, wait_until="networkidle", timeout=60000)
        time.sleep(5)  # 等待页面完全加载
        
        # 尝试滚动页面以加载动态内容
        try:
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
            page.evaluate("window.scrollTo(0, 0)")
            time.sleep(1)
        except:
            pass
        
        # 尝试多种选择器来找到图标
        icon_selectors = [
            'a[href*="/icon/"]',
            '[class*="icon-card"]',
            '[class*="IconCard"]',
            '[data-icon-id]',
        ]
        
        icon_elements = []
        for selector in icon_selectors:
            try:
                elements = page.query_selector_all(selector)
                if elements:
                    print(f"  使用选择器 '{selector}' 找到 {len(elements)} 个元素")
                    icon_elements = elements
                    break
            except:
                continue
        
        if not icon_elements:
            # 尝试查找所有可能的图标容器
            print("  尝试查找所有可能的图标元素...")
            all_links = page.query_selector_all('a[href*="/icon/"]')
            icon_elements = all_links
            print(f"  找到 {len(icon_elements)} 个可能的图标链接")
        
        # 提取图标信息
        seen_urls = set()
        debug_count = 0
        for element in icon_elements:
            try:
                # 获取图标 URL
                icon_url = None
                href = element.get_attribute('href')
                
                # 调试：打印前几个元素的详细信息
                if debug_count < 3:
                    tag_name = element.evaluate("el => el.tagName")
                    outer_html = element.evaluate("el => el.outerHTML")[:200]  # 只取前200字符
                    print(f"    调试: 元素 {debug_count}")
                    print(f"      标签: {tag_name}, href = {href}")
                    print(f"      HTML: {outer_html}...")
                    debug_count += 1
                
                if href:
                    if href.startswith('/'):
                        icon_url = f"https://icons8.com{href}"
                    elif href.startswith('http'):
                        # 规范化不同语言版本的域名到 icons8.com
                        icon_url = re.sub(r'https?://[^/]+', 'https://icons8.com', href)
                
                if not icon_url:
                    continue
                    
                if icon_url in seen_urls:
                    continue
                seen_urls.add(icon_url)
                
                # 从 URL 中提取图标 ID
                # Icons8 的图标 ID 格式可能是：
                # 1. 纯数字: /icon/12345/icon-name
                # 2. 字母数字混合: /icon/bp1PJOFHVRiz/icon-name
                # 3. 集合链接: /icon/set/... (跳过)
                icon_id_match = re.search(r'/icon/([^/]+)/', icon_url)
                if not icon_id_match:
                    # 调试：打印无法匹配的 URL
                    if debug_count <= 3:
                        print(f"    调试: URL 无法匹配 icon ID: {icon_url}")
                    continue
                
                potential_id = icon_id_match.group(1)
                
                # 跳过集合链接（如 /icon/set/emoji/emoji）
                if potential_id == 'set':
                    continue
                
                icon_id = potential_id
                
                # 获取图标标题
                title = None
                title_attrs = ['title', 'aria-label', 'alt', 'data-title']
                for attr in title_attrs:
                    title = element.get_attribute(attr)
                    if title:
                        break
                
                if not title:
                    # 尝试从文本内容获取
                    try:
                        text = element.inner_text().strip()
                        if text and len(text) < 100 and text:
                            title = text
                    except:
                        pass
                
                if not title:
                    # 使用图标 ID 作为标题
                    title = f"icon_{icon_id}"
                
                icons.append({
                    'title': title,
                    'url': icon_url,
                    'icon_id': icon_id
                })
                    
            except Exception as e:
                # 调试：打印异常信息
                if debug_count <= 3:
                    print(f"    调试: 提取图标时出错: {e}")
                continue
        
        print(f"  提取到 {len(icons)} 个图标")
        
    except PlaywrightTimeoutError:
        print(f"  ⚠️ 页面加载超时")
    except Exception as e:
        print(f"  ✗ 提取图标时出错: {e}")
        import traceback
        traceback.print_exc()
    
    return icons


def get_icon_info_from_api(icon_id: str) -> Optional[Dict]:
    """
    从 API 获取图标信息
    
    Args:
        icon_id: 图标 ID
        
    Returns:
        图标信息字典，包含 commonName, free, platform 等
    """
    try:
        api_url = f"https://api-icons.icons8.com/siteApi/icons/icon?id={icon_id}"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        response = requests.get(api_url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('success') and 'icon' in data:
                return data['icon']
    except Exception as e:
        pass
    
    return None


def download_icon_png(icon_id: str, icon_name: str, common_name: str = None, size: int = 96, fallback_to_48: bool = True, style: str = 'doodle') -> Tuple[Optional[bytes], int]:
    """
    下载 PNG 格式图标（免费）
    
    Args:
        icon_id: 图标 ID
        icon_name: 图标名称（用于 URL）
        common_name: 图标的通用名称（如果提供）
        size: PNG 尺寸，默认 96（可选：48, 96, 128 等）
        fallback_to_48: 如果指定尺寸失败，是否退化为 48x48
        style: 图标风格（doodle, plasticine, stickers）
        
    Returns:
        (PNG 图片的字节数据, 实际下载的尺寸) 元组，如果失败返回 (None, 0)
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://icons8.com/',
    }
    
    # 优先尝试指定尺寸（默认 96x96）
    target_size = size
    result = _try_download_png(icon_id, icon_name, common_name, target_size, headers, style)
    
    if result is not None:
        return (result, target_size)
    
    # 如果失败且允许降级，尝试 48x48
    if fallback_to_48 and target_size != 48:
        print(f"    ⚠️  96x96 下载失败，尝试降级到 48x48...")
        result = _try_download_png(icon_id, icon_name, common_name, 48, headers, style)
        if result is not None:
            print(f"    ✓ 成功下载 48x48 尺寸")
            return (result, 48)
    
    return (None, 0)


def _try_download_png(icon_id: str, icon_name: str, common_name: str, size: int, headers: dict, style: str = 'doodle') -> Optional[bytes]:
    """
    尝试下载指定尺寸的 PNG
    
    Args:
        icon_id: 图标 ID
        icon_name: 图标名称
        common_name: 通用名称
        size: 目标尺寸
        headers: HTTP 请求头
        style: 图标风格（doodle, plasticine, stickers）
        
    Returns:
        PNG 字节数据，失败返回 None
    """
    try:
        # 方法1: 使用 img.icons8.com 直接下载
        if common_name:
            png_urls = [
                f"https://img.icons8.com/{style}/{size}/{common_name}.png",
            ]
        else:
            png_urls = [
                f"https://img.icons8.com/{style}/{size}/{icon_name}.png",
            ]
        
        # 尝试直接 URL 下载
        for png_url in png_urls:
            try:
                response = requests.get(png_url, headers=headers, timeout=10)
                if response.status_code == 200:
                    # 检查是否是有效的 PNG（PNG 文件以特定字节开头）
                    if response.content.startswith(b'\x89PNG\r\n\x1a\n'):
                        return response.content
            except Exception as e:
                continue
        
        # 方法2: 使用 API
        api_url = f"https://api-icons.icons8.com/api/icons/{icon_id}/png?size={size}"
        try:
            response = requests.get(api_url, headers=headers, timeout=10)
            if response.status_code == 200 and response.content.startswith(b'\x89PNG\r\n\x1a\n'):
                return response.content
        except:
            pass
        
    except Exception as e:
        pass
    
    return None


def save_png_content(png_data: bytes, output_path: Path, title: str) -> bool:
    """
    保存 PNG 数据到文件
    
    Args:
        png_data: PNG 图片的字节数据
        output_path: 保存路径
        title: 图标标题（用于错误提示）
        
    Returns:
        是否保存成功
    """
    try:
        # 确保目录存在
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 保存文件
        with open(output_path, 'wb') as f:
            f.write(png_data)
        
        return True
            
    except Exception as e:
        print(f"    ✗ 保存 PNG 失败: {title} - {e}")
        return False


def get_all_existing_png_files(icons_dir: Path) -> set:
    """
    扫描整个 icons8/{style} 目录，获取所有已存在的 PNG 文件名（不含扩展名）
    
    Args:
        icons_dir: icons8/{style} 目录路径
        
    Returns:
        已存在文件名的集合
    """
    existing_files = set()
    if icons_dir.exists():
        for png_file in icons_dir.rglob("*.png"):
            existing_files.add(png_file.stem)
    return existing_files


def get_png_resolution(png_file: Path) -> str:
    """
    获取 PNG 图片的分辨率（宽x高）
    
    Args:
        png_file: PNG 文件路径
        
    Returns:
        分辨率字符串，格式为 "宽x高"，如果失败返回 "unknown"
    """
    try:
        from PIL import Image
        with Image.open(png_file) as img:
            width, height = img.size
            return f"{width}x{height}"
    except Exception:
        # 如果 PIL 不可用，尝试从 PNG 文件头读取
        try:
            with open(png_file, 'rb') as f:
                # PNG 文件头：89 50 4E 47 0D 0A 1A 0A
                # IHDR chunk 包含宽高信息（偏移 16-23 字节）
                f.seek(16)
                width_bytes = f.read(4)
                height_bytes = f.read(4)
                if len(width_bytes) == 4 and len(height_bytes) == 4:
                    width = int.from_bytes(width_bytes, 'big')
                    height = int.from_bytes(height_bytes, 'big')
                    return f"{width}x{height}"
        except:
            pass
    return "unknown"




def generate_png_metadata(icons_dir: Path) -> Dict:
    """
    生成 PNG 文件的元信息清单
    
    Args:
        icons_dir: icons8 目录路径（如 icons8/doodle, icons8/plasticine 等）
        
    Returns:
        包含文件清单和统计信息的字典
    """
    import hashlib
    from collections import defaultdict
    from datetime import datetime
    
    metadata = {
        'version': '1.0',
        'generated_at': time.strftime('%Y-%m-%d %H:%M:%S'),
        'total_files': 0,
        'total_size_mb': 0,
        'by_category': defaultdict(int),
        'by_subcategory': defaultdict(int),
        'file_map': {}  # filename -> file_info 的映射，用于快速查找
    }
    
    if not icons_dir.exists():
        return metadata
    
    png_files = list(icons_dir.rglob("*.png"))
    metadata['total_files'] = len(png_files)
    
    total_size = 0
    
    for png_file in png_files:
        try:
            # 获取文件信息
            file_size = png_file.stat().st_size
            total_size += file_size
            
            # 计算文件哈希
            md5_hash = hashlib.md5()
            with open(png_file, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    md5_hash.update(chunk)
            file_hash = md5_hash.hexdigest()
            
            # 获取相对路径
            relative_path = png_file.relative_to(icons_dir)
            parts = relative_path.parts
            
            # 解析分类
            category = parts[0] if len(parts) >= 1 else "Unknown"
            subcategory = f"{parts[0]}/{parts[1]}" if len(parts) >= 2 else category
            
            # 获取修改时间（日期格式）
            mtime = png_file.stat().st_mtime
            modified_date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
            
            # 只保留 subcategory 信息
            file_info = {
                'subcategory': subcategory
            }
            
            metadata['file_map'][png_file.stem] = file_info
            metadata['by_category'][category] += 1
            metadata['by_subcategory'][subcategory] += 1
            
        except Exception as e:
            print(f"  ⚠️ 处理文件失败 {png_file}: {e}")
            continue
    
    metadata['total_size_mb'] = round(total_size / 1024 / 1024, 2)
    metadata['by_category'] = dict(metadata['by_category'])
    metadata['by_subcategory'] = dict(metadata['by_subcategory'])
    
    return metadata


def save_png_metadata(icons_dir: Path, metadata_file: Path = None, style: str = 'doodle'):
    """
    生成并保存 PNG 文件元信息
    
    Args:
        icons_dir: icons8 目录路径（如 assets/icons8/doodle）
        metadata_file: 元信息文件路径，如果为 None 则使用默认路径
        style: 图标风格（doodle, plasticine, stickers）
    """
    if metadata_file is None:
        # icons_dir 应该是 assets/icons8/{style}，所以 parent.parent 是 assets，parent 是 icons8
        metadata_file = icons_dir.parent / f"{style}_png_metadata.json"
    
    print(f"\n正在生成 PNG 文件元信息...")
    metadata = generate_png_metadata(icons_dir)
    
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"✓ 元信息已保存到: {metadata_file}")
    print(f"  总文件数: {metadata['total_files']}")
    print(f"  总大小: {metadata['total_size_mb']} MB")
    
    return metadata


def download_category_icons(category: Dict, output_base: Path, page: Page, global_existing_files: set = None, style: str = 'doodle') -> Dict:
    """
    下载单个分类的所有 PNG 图标
    
    Args:
        category: 分类信息字典（从 icons8_categories.json 读取，不包含 url 和 path）
        output_base: 输出基础目录
        page: Playwright 页面对象
        global_existing_files: 全局已存在文件集合
        style: 图标风格（doodle, plasticine, stickers）
        
    Returns:
        下载统计信息
    """
    category_name = category['name']
    
    # 动态生成路径和 URL
    print(f"\n{'='*60}")
    print(f"处理分类: {category_name} ({category['name_cn']})")
    print(f"{'='*60}")
    
    stats = {
        'category': category_name,
        'total_icons': 0,
        'downloaded': 0,
        'failed': 0,
        'skipped': 0
    }
    
    # 使用全局已存在文件集合
    if global_existing_files is not None:
        print(f"  全局已存在 {len(global_existing_files)} 个 PNG 文件，将跳过重复的")
    
    # 处理子分类
    if 'subcategories' in category and category['subcategories']:
        print(f"\n发现 {len(category['subcategories'])} 个子分类")
        
        for subcategory in category['subcategories']:
            subcategory_name = subcategory['name']
            
            # 动态生成 URL 和路径
            subcategory_url = generate_category_url(subcategory_name, style)
            subcategory_path = generate_category_path(category_name, subcategory_name, style)
            
            print(f"\n  └─ 子分类: {subcategory_name} ({subcategory['name_cn']})")
            print(f"     路径: {subcategory_path}")
            print(f"     URL: {subcategory_url}")
            
            # 下载图标
            output_dir = output_base / subcategory_path
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # 预先扫描当前子分类目录已存在的文件（用于统计显示）
            local_existing_files = set()
            for png_file in output_dir.glob("*.png"):
                local_existing_files.add(png_file.stem)
            
            if local_existing_files:
                print(f"     当前目录已存在 {len(local_existing_files)} 个文件")
            
            # 提取图标
            icons = extract_icons_from_page(page, subcategory_url)
            stats['total_icons'] += len(icons)
            
            for icon in icons:
                title = icon['title']
                filename = normalize_filename(title)
                icon_id = icon.get('icon_id', '')
                
                # 下载 PNG 格式（96x96）
                output_path = output_dir / f"{filename}.png"
                
                # 检查是否已存在（双重检查：全局集合 + 本地文件系统）
                if output_path.exists():
                    # 文件已存在，跳过
                    stats['skipped'] += 1
                    # 更新全局集合（如果提供）
                    if global_existing_files is not None:
                        global_existing_files.add(filename)
                    continue
                
                # 检查全局已存在文件集合（避免重复下载）
                if global_existing_files is not None and filename in global_existing_files:
                    stats['skipped'] += 1
                    continue
                
                # 获取图标信息以获取 common_name
                # 注意：PNG 格式（48x48, 96x96）通常是免费的，即使 API 返回 free=False
                icon_info = get_icon_info_from_api(icon_id)
                common_name = None
                
                if icon_info:
                    common_name = icon_info.get('commonName')
                    # PNG 格式通常是免费的，不检查 free 字段
                    # 如果下载失败，说明可能真的需要付费
                
                # 从 URL 中提取图标名称
                # Icons8 的 URL 格式：/icon/{icon_id}/{icon_name}
                # icon_id 可能是纯数字或字母数字混合
                icon_name_match = re.search(r'/icon/[^/]+/([^/?]+)', icon['url'])
                icon_name = icon_name_match.group(1) if icon_name_match else filename
                
                # 下载 PNG（优先 96x96，失败则降级到 48x48）
                png_data, actual_size = download_icon_png(icon_id, icon_name, common_name, size=96, fallback_to_48=True, style=style)
                
                if not png_data:
                    print(f"    ✗ 无法获取 PNG: {title} (ID: {icon_id})")
                    stats['failed'] += 1
                    continue
                
                # 记录实际下载的尺寸
                if actual_size == 48:
                    print(f"    ⚠️  {title}: 96x96 不可用，已下载 48x48 版本")
                
                # 保存 PNG
                if save_png_content(png_data, output_path, title):
                    stats['downloaded'] += 1
                    print(f"    ✓ {title} -> {filename}.png")
                    
                    # 下载成功后，更新全局已存在文件集合
                    if global_existing_files is not None:
                        global_existing_files.add(filename)
                else:
                    stats['failed'] += 1
                
                time.sleep(REQUEST_DELAY)
    
    print(f"\n分类 {category_name} 完成:")
    print(f"  总计: {stats['total_icons']}")
    print(f"  下载: {stats['downloaded']}")
    print(f"  跳过: {stats['skipped']}")
    print(f"  失败: {stats['failed']}")
    
    return stats


def download_style_icons(style: str, categories: List[Dict], output_base: Path):
    """
    下载指定风格的所有图标
    
    Args:
        style: 图标风格（doodle, plasticine, stickers）
        categories: 分类数据列表
        output_base: 输出基础目录
    """
    print("\n" + "="*60)
    print(f"Icons8 {style.capitalize()} 风格图标下载")
    print("="*60)
    print("下载格式: PNG (96x96)")
    
    # 直接使用分类数据（URL 和路径会动态生成）
    total_subcategories = sum(len(cat.get('subcategories', [])) for cat in categories)
    print(f"\n将下载所有 {len(categories)} 个主分类的图标（共 {total_subcategories} 个子分类）")
    
    # 测试模式：只下载第一个分类的第一个子分类的前 3 个图标
    TEST_MODE = False
    if TEST_MODE:
        print("\n⚠️ 测试模式：只下载少量图标")
        if categories and categories[0].get('subcategories'):
            test_category = categories[0].copy()
            test_category['subcategories'] = [test_category['subcategories'][0]]
            categories = [test_category]
    
    # 创建输出目录
    output_dir = output_base / "icons8" / style
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"输出目录: {output_dir}")
    
    # 预先扫描整个目录的已存在文件
    print("\n正在扫描已存在的 PNG 文件...")
    global_existing_files = get_all_existing_png_files(output_dir)
    print(f"发现 {len(global_existing_files)} 个已存在的 PNG 文件，将跳过重复的")
    
    # 生成/更新元信息文件
    metadata_file = output_base / "icons8" / f"{style}_png_metadata.json"
    if not metadata_file.exists() or len(global_existing_files) > 0:
        print("\n正在生成/更新 PNG 文件元信息...")
        save_png_metadata(output_dir, metadata_file, style)
    
    # 使用 Playwright 下载
    all_stats = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        try:
            for category in categories:
                stats = download_category_icons(category, output_base, page, global_existing_files=global_existing_files, style=style)
                all_stats.append(stats)
                time.sleep(2)  # 分类之间的延迟
                
        finally:
            browser.close()
    
    # 打印总结
    print("\n" + "="*60)
    print(f"{style.capitalize()} 风格下载完成")
    print("="*60)
    
    total_downloaded = sum(s['downloaded'] for s in all_stats)
    total_failed = sum(s['failed'] for s in all_stats)
    total_skipped = sum(s['skipped'] for s in all_stats)
    
    print(f"总计下载: {total_downloaded}")
    print(f"总计失败: {total_failed}")
    print(f"总计跳过: {total_skipped}")
    print(f"\n所有图标已保存到: {output_dir}")
    
    # 更新元信息
    if total_downloaded > 0:
        print("\n正在更新 PNG 文件元信息...")
        metadata = save_png_metadata(output_dir, metadata_file, style)
        if metadata:
            print(f"  元信息已更新: {metadata['total_files']} 个文件, {metadata['total_size_mb']} MB")
    
    return {
        'style': style,
        'downloaded': total_downloaded,
        'failed': total_failed,
        'skipped': total_skipped
    }


def main():
    """主函数"""
    print("="*60)
    print("Icons8 图标下载爬虫（支持多种风格）")
    print("="*60)
    print("下载格式: PNG (96x96)")
    print("支持风格: doodle, plasticine, stickers")
    
    # 读取分类文件
    if not CATEGORIES_FILE.exists():
        print(f"✗ 分类文件不存在: {CATEGORIES_FILE}")
        return
    
    with open(CATEGORIES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 获取基础分类数据
    categories = data['categories']
    print(f"总分类数: {len(categories)}")
    
    # 要下载的风格列表
    styles_to_download = ['color']
    
    # 下载所有风格的图标（支持断点续下载，自动跳过已存在的文件）
    all_results = []
    for style in styles_to_download:
        result = download_style_icons(style, categories, OUTPUT_BASE_DIR)
        all_results.append(result)
        print(f"\n{'='*60}")
        print(f"{style.capitalize()} 风格处理完成")
        print(f"{'='*60}\n")
    
    # 打印总体总结
    print("\n" + "="*60)
    print("所有风格下载完成")
    print("="*60)
    
    total_all_downloaded = sum(r['downloaded'] for r in all_results)
    total_all_failed = sum(r['failed'] for r in all_results)
    total_all_skipped = sum(r['skipped'] for r in all_results)
    
    print(f"\n总体统计:")
    print(f"  总计下载: {total_all_downloaded}")
    print(f"  总计失败: {total_all_failed}")
    print(f"  总计跳过: {total_all_skipped}")
    
    print(f"\n各风格统计:")
    for result in all_results:
        print(f"  {result['style'].capitalize()}: 下载 {result['downloaded']}, 失败 {result['failed']}, 跳过 {result['skipped']}")


if __name__ == "__main__":
    main()

