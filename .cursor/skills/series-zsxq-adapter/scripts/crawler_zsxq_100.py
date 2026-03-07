"""
爬取知识星球“精品100课”标签下的内容。

该脚本属于 `series-zsxq-adapter` 的系列专属数据入口，用于刷新
`assets/zsxq/jingpin_100ke_posts.json` 与对应 raw 数据。

使用方法：
    uv run python .cursor/skills/series-zsxq-adapter/scripts/crawler_zsxq_100.py
"""

from __future__ import annotations

import argparse
import json
import os
import random
import time
from pathlib import Path
from urllib.parse import quote

import requests


# 标签 ID
HASHTAG_ID = "48848481815828"

# 请求头配置（从用户提供的 curl 命令提取）
HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "origin": "https://wx.zsxq.com",
    "priority": "u=1, i",
    "referer": "https://wx.zsxq.com/",
    "sec-ch-ua": '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "x-aduid": "5e7a2678e-e8d5-eb5c-08e4-af283659d53",
    "x-request-id": "dac8a5a34-e04d-c52e-4498-5b83cf4833d",
    "x-signature": "0ea2b2391d96882d838d78532f4bbc43a4fa8ab8",
    "x-timestamp": "1769435527",
    "x-version": "2.87.0",
}

WORKSPACE_ROOT = Path(__file__).resolve().parents[4]
OUTPUT_DIR = WORKSPACE_ROOT / "assets" / "zsxq"
OUTPUT_FILE = OUTPUT_DIR / "jingpin_100ke_posts.json"
RAW_OUTPUT_FILE = OUTPUT_DIR / "jingpin_100ke_posts_raw.json"


def build_cookies() -> dict[str, str]:
    token = os.getenv("ZSXQ_ACCESS_TOKEN")
    if not token:
        raise RuntimeError("Missing ZSXQ_ACCESS_TOKEN environment variable.")
    return {
        "zsxq_access_token": token,
        "abtest_env": "product",
    }


def fetch_topics(end_time: str | None = None):
    """
    获取标签下的话题列表。

    Args:
        end_time: 分页参数，上一页最后一条的 create_time。
    """
    url = f"https://api.zsxq.com/v2/hashtags/{HASHTAG_ID}/topics?count=20"

    if end_time:
        url += f"&end_time={quote(end_time)}"

    print(f"正在获取: {url}")

    try:
        response = requests.get(url, headers=HEADERS, cookies=build_cookies(), verify=False)
        if response.status_code == 200:
            return response.json()

        print(f"请求失败: {response.status_code} - {response.text}")
        return None
    except Exception as exc:
        print(f"请求出错: {exc}")
        return None


def extract_content(topic: dict) -> dict:
    """提取话题的核心内容。"""
    result = {
        "topic_id": topic.get("topic_id"),
        "create_time": topic.get("create_time"),
        "type": topic.get("type"),
    }

    if "owner" in topic:
        result["author"] = {
            "name": topic["owner"].get("name"),
            "user_id": topic["owner"].get("user_id"),
        }

    if "talk" in topic:
        talk = topic["talk"]
        result["text"] = talk.get("text", "")

        if "images" in talk:
            result["images"] = [
                {
                    "image_id": img.get("image_id"),
                    "url": img.get("large", {}).get("url") or img.get("original", {}).get("url"),
                }
                for img in talk.get("images", [])
            ]

        if "files" in talk:
            result["files"] = [
                {
                    "file_id": item.get("file_id"),
                    "name": item.get("name"),
                    "size": item.get("size"),
                    "url": item.get("download_url"),
                }
                for item in talk.get("files", [])
            ]

    result["likes_count"] = topic.get("likes_count", 0)
    result["comments_count"] = topic.get("comments_count", 0)
    result["rewards_count"] = topic.get("rewards_count", 0)
    result["reading_count"] = topic.get("reading_count", 0)

    return result


def load_existing_data():
    """
    加载已有数据，返回 (topics, topics_raw, seen_ids, last_end_time)。
    """
    all_topics = []
    all_topics_raw = []
    seen_ids = set()
    last_end_time = None

    if OUTPUT_FILE.exists():
        with OUTPUT_FILE.open("r", encoding="utf-8") as file:
            all_topics = json.load(file)
        for item in all_topics:
            seen_ids.add(item.get("topic_id"))
        if all_topics:
            last_end_time = all_topics[-1].get("create_time")

    if RAW_OUTPUT_FILE.exists():
        with RAW_OUTPUT_FILE.open("r", encoding="utf-8") as file:
            all_topics_raw = json.load(file)

    return all_topics, all_topics_raw, seen_ids, last_end_time


def main(start_end_time: str | None = None, continue_mode: bool = False) -> None:
    """
    主函数。

    Args:
        start_end_time: 指定从某个时间点开始爬取。
        continue_mode: 是否从已有数据继续爬取。
    """
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if continue_mode or start_end_time:
        all_topics, all_topics_raw, seen_ids, last_end_time = load_existing_data()
        print(f"已加载 {len(all_topics)} 条已有数据")

        if start_end_time:
            end_time = start_end_time
            print(f"从指定时间点继续: {end_time}")
        elif continue_mode and last_end_time:
            end_time = last_end_time
            print(f"从上次停止处继续: {end_time}")
        else:
            end_time = None
            print("没有找到续爬点，从头开始")
    else:
        all_topics = []
        all_topics_raw = []
        seen_ids = set()
        end_time = None

    has_more = True
    page = 0
    duplicate_count = 0

    while has_more:
        page += 1
        print(f"\n=== 第 {page} 页 ===")

        data = fetch_topics(end_time)

        if not data:
            print("未获取到数据")
            break

        if not data.get("succeeded"):
            print(f"API 返回失败: {data.get('code')} - {data.get('info')}")
            break

        resp_data = data.get("resp_data", {})
        topics = resp_data.get("topics", [])

        if not topics:
            print("没有更多话题了")
            break

        print(f"获取到 {len(topics)} 条话题")

        new_count = 0
        for topic in topics:
            topic_id = topic.get("topic_id")

            if topic_id in seen_ids:
                duplicate_count += 1
                print(f"  [跳过重复] {topic_id}")
                continue

            seen_ids.add(topic_id)
            all_topics_raw.append(topic)

            extracted = extract_content(topic)
            all_topics.append(extracted)
            new_count += 1
            print(f"  - {extracted.get('topic_id')}: {extracted.get('text', '')[:50]}...")

        print(f"  本页新增: {new_count}, 重复跳过: {len(topics) - new_count}")

        last_topic = topics[-1]
        new_end_time = last_topic.get("create_time")

        if new_end_time == end_time:
            print("警告: end_time 未变化，可能陷入循环，退出")
            break

        end_time = new_end_time

        if len(topics) < 20:
            has_more = False

        delay = random.uniform(2.0, 5.0)
        print(f"  等待 {delay:.1f} 秒后继续...")
        time.sleep(delay)

    print(f"\n总共获取 {len(all_topics)} 条话题（去重后）")
    print(f"跳过重复话题: {duplicate_count} 条")

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(all_topics, file, ensure_ascii=False, indent=2)
    print(f"已保存提取数据到 {OUTPUT_FILE}")

    with RAW_OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(all_topics_raw, file, ensure_ascii=False, indent=2)
    print(f"已保存原始数据到 {RAW_OUTPUT_FILE}")


def deduplicate_existing() -> None:
    """对已保存的数据文件进行去重。"""
    if OUTPUT_FILE.exists():
        with OUTPUT_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        seen_ids = set()
        unique_data = []
        for item in data:
            topic_id = item.get("topic_id")
            if topic_id not in seen_ids:
                seen_ids.add(topic_id)
                unique_data.append(item)

        removed = len(data) - len(unique_data)
        print(f"提取数据: 原 {len(data)} 条，去重后 {len(unique_data)} 条，移除 {removed} 条重复")

        with OUTPUT_FILE.open("w", encoding="utf-8") as file:
            json.dump(unique_data, file, ensure_ascii=False, indent=2)

    if RAW_OUTPUT_FILE.exists():
        with RAW_OUTPUT_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        seen_ids = set()
        unique_data = []
        for item in data:
            topic_id = item.get("topic_id")
            if topic_id not in seen_ids:
                seen_ids.add(topic_id)
                unique_data.append(item)

        removed = len(data) - len(unique_data)
        print(f"原始数据: 原 {len(data)} 条，去重后 {len(unique_data)} 条，移除 {removed} 条重复")

        with RAW_OUTPUT_FILE.open("w", encoding="utf-8") as file:
            json.dump(unique_data, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="爬取知识星球精品100课")
    parser.add_argument("--dedupe", action="store_true", help="对已有数据进行去重")
    parser.add_argument(
        "--continue",
        dest="continue_mode",
        action="store_true",
        help="从已有数据的最后一条继续爬取",
    )
    parser.add_argument(
        "--from",
        dest="start_from",
        type=str,
        help="从指定时间点继续爬取，如: 2022-12-31T17:25:41.134+0800",
    )

    args = parser.parse_args()

    if args.dedupe:
        deduplicate_existing()
    else:
        main(start_end_time=args.start_from, continue_mode=args.continue_mode)
