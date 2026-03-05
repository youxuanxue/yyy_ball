#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
处理 jingpin_100ke_posts.json 文件：
1. 按 create_time 从小到大排序
2. 按顺序为每条添加 lesson 字段：第001课、第002课、…（x 为三位数字）
3. 去掉 text 开头以「第x课」「x课」「x 课」等开头的部分
"""

import json
import re
from datetime import datetime
from pathlib import Path


def strip_lesson_prefix(text):
    """
    去掉 text 开头以「第x课」「x课」「x 课」等开头的部分，只处理一次（仅文首）。
    """
    if not text or not isinstance(text, str):
        return text
    # 文首：第?数字 中间(空格、括号等) 课 及紧随其后的空格/标点
    mid = r"[\s\-\.\、]*(?:\([^)]*\))?[\s\-\.\、]*"
    prefix = re.match(r"^第?\s*\d+" + mid + r"课\s*", text)
    if prefix:
        return text[prefix.end() :].lstrip()
    return text


def process_posts(input_file, output_file=None):
    """
    按 create_time 升序排序，并按顺序写入 lesson：第001课、第002课、…
    """
    if output_file is None:
        output_file = input_file

    print(f"正在读取文件: {input_file}")
    with open(input_file, "r", encoding="utf-8") as f:
        posts = json.load(f)

    n = len(posts)
    print(f"共读取 {n} 条记录")

    # 按 create_time 从小到大排序
    def parse_time(time_str):
        try:
            return datetime.fromisoformat(
                (time_str or "").replace("+0800", "+08:00")
            )
        except Exception:
            return datetime.min

    posts.sort(key=lambda x: parse_time(x.get("create_time", "")))

    # 按顺序填写 lesson，并去掉 text 开头的「第x课」「x课」「x 课」等
    for i, post in enumerate(posts, start=1):
        post["lesson"] = f"第{i:03d}课"
        if "text" in post and post["text"]:
            post["text"] = strip_lesson_prefix(post["text"])

    print(f"正在保存到文件: {output_file}")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

    print(f"\n处理完成：共 {n} 条，lesson 为 第001课～第{n:03d}课")
    print("前 5 条示例:")
    for i, post in enumerate(posts[:5], 1):
        print(f"  {i}. {post.get('lesson')}  {post.get('create_time', '')[:10]}  {post.get('text', '')[:40]}...")


if __name__ == "__main__":
    input_file = (
        Path(__file__).parent / "assets" / "zsxq" / "jingpin_100ke_posts.json"
    )
    process_posts(input_file)
