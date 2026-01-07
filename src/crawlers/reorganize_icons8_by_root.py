#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重新组织 Icons8 PNG 文件，按词根建立目录索引

从 assets/icons8/all_png_names.txt 读取所有文件名，
提取词根，创建按词根组织的目录结构，
并将对应的 PNG 文件复制到新目录中。
"""

import re
from pathlib import Path
from collections import defaultdict, Counter
from shutil import copy2
import json

PROJECT_ROOT = Path(__file__).parent.parent.parent
ALL_PNG_NAMES_FILE = PROJECT_ROOT / "assets" / "icons8" / "all_png_names.txt"
ICONS8_DIR = PROJECT_ROOT / "assets" / "icons8"
OUTPUT_DIR = PROJECT_ROOT / "assets" / "icons8png"


def extract_root_name(filename: str) -> str:
    """
    从文件名中提取词根
    
    策略：
    1. 如果包含下划线，取第一个下划线前的部分作为词根
    2. 如果是纯数字，直接返回
    3. 如果包含常见后缀模式（如 _skin_type_, _circled, _cute 等），取前缀
    4. 否则返回整个文件名
    
    Args:
        filename: 文件名（不含扩展名）
        
    Returns:
        词根名称
    """
    if not filename or filename == '.png':
        return 'special'
    
    # 纯数字或特殊字符开头的，直接返回
    if re.match(r'^[\d\.]+$', filename):
        return 'numbers'
    
    # 常见后缀模式，提取前缀
    suffix_patterns = [
        r'_skin_type_\d+$',
        r'_circled(_c)?$',
        r'_cute$',
        r'_v\d+$',
        r'_old$',
        r'_new$',
        r'_squared$',
        r'_circledv\d+$',
    ]
    
    for pattern in suffix_patterns:
        match = re.search(pattern, filename)
        if match:
            prefix = filename[:match.start()]
            if prefix:
                return prefix
    
    # 如果包含下划线，取第一个下划线前的部分
    if '_' in filename:
        parts = filename.split('_')
        # 如果第一部分是常见前缀（如数字），尝试取前两部分
        if len(parts) > 1:
            first_part = parts[0]
            # 如果第一部分很短（1-2个字符）且是数字或字母，可能不是词根
            if len(first_part) <= 2 and (first_part.isdigit() or first_part.isalpha()):
                # 尝试取前两部分
                if len(parts) > 2:
                    return '_'.join(parts[:2])
            return first_part
    
    # 如果包含连字符，取第一个连字符前的部分
    if '-' in filename:
        return filename.split('-')[0]
    
    # 否则返回整个文件名
    return filename


def find_png_file(filename: str, icons8_dir: Path) -> Path:
    """
    在 icons8 目录中查找对应的 PNG 文件
    
    Args:
        filename: 文件名（不含扩展名）
        icons8_dir: icons8 根目录
        
    Returns:
        PNG 文件路径，如果找不到返回 None
    """
    # 在所有风格目录中搜索
    for style in ['color', 'doodle', 'plasticine', 'stickers']:
        style_dir = icons8_dir / style
        if not style_dir.exists():
            continue
        
        # 递归搜索
        for png_file in style_dir.rglob(f"{filename}.png"):
            return png_file
    
    return None


def reorganize_icons():
    """
    重新组织 Icons8 PNG 文件
    """
    print("=" * 80)
    print("Icons8 PNG 文件重组工具")
    print("=" * 80)
    
    # 1. 读取所有文件名
    print("\n1. 读取文件名列表...")
    if not ALL_PNG_NAMES_FILE.exists():
        print(f"❌ 文件不存在: {ALL_PNG_NAMES_FILE}")
        return
    
    filenames = []
    with open(ALL_PNG_NAMES_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                # 去掉 .png 扩展名
                name = line.replace('.png', '') if line.endswith('.png') else line
                if name and name != '.':
                    filenames.append(name)
    
    print(f"   读取到 {len(filenames)} 个文件名")
    
    # 2. 提取词根并分组
    print("\n2. 提取词根并分组...")
    root_groups = defaultdict(list)
    root_stats = Counter()
    
    for filename in filenames:
        root = extract_root_name(filename)
        root_groups[root].append(filename)
        root_stats[root] += 1
    
    print(f"   提取到 {len(root_groups)} 个词根")
    print(f"   平均每个词根包含 {len(filenames) / len(root_groups):.1f} 个文件")
    
    # 显示最常见的词根
    print("\n   最常见的 20 个词根:")
    for root, count in root_stats.most_common(20):
        print(f"     {root:30s}: {count:4d} 个文件")
    
    # 3. 创建输出目录
    print("\n3. 创建输出目录...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"   输出目录: {OUTPUT_DIR}")
    
    # 4. 复制文件并建立索引
    print("\n4. 复制文件并建立目录结构...")
    copied_count = 0
    not_found_count = 0
    error_count = 0
    
    # 创建索引文件
    index_data = {
        'total_roots': len(root_groups),
        'total_files': len(filenames),
        'roots': {}
    }
    
    for root, files in sorted(root_groups.items()):
        root_dir = OUTPUT_DIR / root
        root_dir.mkdir(parents=True, exist_ok=True)
        
        root_info = {
            'file_count': len(files),
            'files': []
        }
        
        for filename in sorted(files):
            # 查找源文件
            source_file = find_png_file(filename, ICONS8_DIR)
            
            if source_file and source_file.exists():
                try:
                    # 复制文件
                    dest_file = root_dir / f"{filename}.png"
                    copy2(source_file, dest_file)
                    copied_count += 1
                    root_info['files'].append(filename)
                except Exception as e:
                    print(f"   ⚠️ 复制失败 {filename}: {e}")
                    error_count += 1
            else:
                not_found_count += 1
                # 只记录前10个未找到的文件
                if not_found_count <= 10:
                    print(f"   ⚠️ 未找到文件: {filename}")
        
        index_data['roots'][root] = root_info
        
        # 每处理 100 个词根显示进度
        if len(index_data['roots']) % 100 == 0:
            print(f"   已处理 {len(index_data['roots'])}/{len(root_groups)} 个词根...")
    
    # 5. 保存索引文件
    print("\n5. 保存索引文件...")
    index_file = OUTPUT_DIR / "index.json"
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    print(f"   索引文件已保存: {index_file}")
    
    # 6. 生成统计报告
    print("\n" + "=" * 80)
    print("重组完成！")
    print("=" * 80)
    print(f"\n统计信息:")
    print(f"  总词根数: {len(root_groups)}")
    print(f"  总文件数: {len(filenames)}")
    print(f"  成功复制: {copied_count}")
    print(f"  未找到文件: {not_found_count}")
    print(f"  复制错误: {error_count}")
    print(f"\n输出目录: {OUTPUT_DIR}")
    print(f"索引文件: {index_file}")


if __name__ == '__main__':
    reorganize_icons()



