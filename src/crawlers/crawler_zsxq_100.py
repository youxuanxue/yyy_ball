"""
爬取知识星球"精品100课"标签下的所有内容
链接：https://wx.zsxq.com/tags/%E7%B2%BE%E5%93%81100%E8%AF%BE/48848481815828
"""

import requests
import json
import time
import os
import random
from urllib.parse import quote
from pathlib import Path

# 标签ID
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
    "x-version": "2.87.0"
}

# Cookie 配置
COOKIES = {
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2248415142825128%22%2C%22first_id%22%3A%2219b2ca4f6608a5-0614dbf86a314dc-1c525631-1405320-19b2ca4f6612b4f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTliMmNhNGY2NjA4YTUtMDYxNGRiZjg2YTMxNGRjLTFjNTI1NjMxLTE0MDUzMjAtMTliMmNhNGY2NjEyYjRmIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiNDg0MTUxNDI4MjUxMjgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2248415142825128%22%7D%7D",
    "zsxq_access_token": "D5CAFEDB-51DE-41C2-BDB6-DB6A44AD327F_07844E0DFEE29E1E",
    "abtest_env": "product"
}

# 输出目录
OUTPUT_DIR = Path(__file__).parent.parent.parent / "assets" / "zsxq"
OUTPUT_FILE = OUTPUT_DIR / "jingpin_100ke_posts.json"


def fetch_topics(end_time=None):
    """
    获取标签下的话题列表
    :param end_time: 分页参数，上一页最后一条的 create_time
    """
    url = f"https://api.zsxq.com/v2/hashtags/{HASHTAG_ID}/topics?count=20"
    
    if end_time:
        url += f"&end_time={quote(end_time)}"
    
    print(f"正在获取: {url}")
    
    try:
        response = requests.get(url, headers=HEADERS, cookies=COOKIES, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"请求失败: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"请求出错: {e}")
        return None


def extract_content(topic):
    """
    提取话题的核心内容
    """
    result = {
        "topic_id": topic.get("topic_id"),
        "create_time": topic.get("create_time"),
        "type": topic.get("type"),
    }
    
    # 提取作者信息
    if "owner" in topic:
        result["author"] = {
            "name": topic["owner"].get("name"),
            "user_id": topic["owner"].get("user_id")
        }
    
    # 提取话题内容
    if "talk" in topic:
        talk = topic["talk"]
        result["text"] = talk.get("text", "")
        
        # 提取图片
        if "images" in talk:
            result["images"] = [
                {
                    "image_id": img.get("image_id"),
                    "url": img.get("large", {}).get("url") or img.get("original", {}).get("url")
                }
                for img in talk.get("images", [])
            ]
        
        # 提取文件
        if "files" in talk:
            result["files"] = [
                {
                    "file_id": f.get("file_id"),
                    "name": f.get("name"),
                    "size": f.get("size"),
                    "url": f.get("download_url")
                }
                for f in talk.get("files", [])
            ]
    
    # 提取互动数据
    result["likes_count"] = topic.get("likes_count", 0)
    result["comments_count"] = topic.get("comments_count", 0)
    result["rewards_count"] = topic.get("rewards_count", 0)
    result["reading_count"] = topic.get("reading_count", 0)
    
    return result


def load_existing_data():
    """
    加载已有数据，返回 (topics, topics_raw, seen_ids, last_end_time)
    """
    all_topics = []
    all_topics_raw = []
    seen_ids = set()
    last_end_time = None
    
    # 加载已有的提取数据
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            all_topics = json.load(f)
        for item in all_topics:
            seen_ids.add(item.get("topic_id"))
        # 获取最后一条的 create_time 作为续爬起点
        if all_topics:
            last_end_time = all_topics[-1].get("create_time")
    
    # 加载已有的原始数据
    raw_file = OUTPUT_DIR / "jingpin_100ke_posts_raw.json"
    if raw_file.exists():
        with open(raw_file, 'r', encoding='utf-8') as f:
            all_topics_raw = json.load(f)
    
    return all_topics, all_topics_raw, seen_ids, last_end_time


def main(start_end_time=None, continue_mode=False):
    """
    主函数
    :param start_end_time: 指定从某个时间点开始爬取
    :param continue_mode: 是否从已有数据继续爬取
    """
    # 禁用 SSL 警告
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    # 确保输出目录存在
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 初始化数据
    if continue_mode or start_end_time:
        # 加载已有数据
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
        
        # 提取核心内容（带去重）
        new_count = 0
        for topic in topics:
            topic_id = topic.get("topic_id")
            
            # 跳过已存在的话题
            if topic_id in seen_ids:
                duplicate_count += 1
                print(f"  [跳过重复] {topic_id}")
                continue
            
            seen_ids.add(topic_id)
            
            # 保存原始数据
            all_topics_raw.append(topic)
            
            # 提取并保存
            extracted = extract_content(topic)
            all_topics.append(extracted)
            new_count += 1
            print(f"  - {extracted.get('topic_id')}: {extracted.get('text', '')[:50]}...")
        
        print(f"  本页新增: {new_count}, 重复跳过: {len(topics) - new_count}")
        
        # 分页逻辑
        last_topic = topics[-1]
        new_end_time = last_topic.get("create_time")
        
        # 检查是否陷入循环
        if new_end_time == end_time:
            print("警告: end_time 未变化，可能陷入循环，退出")
            break
             
        end_time = new_end_time
        
        # 如果获取的数量少于请求数量，说明已到最后一页
        if len(topics) < 20:
            has_more = False
            
        # 随机延迟，模拟人工浏览行为，避免被封
        delay = random.uniform(2.0, 5.0)
        print(f"  等待 {delay:.1f} 秒后继续...")
        time.sleep(delay)

    print(f"\n总共获取 {len(all_topics)} 条话题（去重后）")
    print(f"跳过重复话题: {duplicate_count} 条")
    
    # 保存提取后的数据
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_topics, f, ensure_ascii=False, indent=2)
    print(f"已保存提取数据到 {OUTPUT_FILE}")
    
    # 保存原始数据
    raw_file = OUTPUT_DIR / "jingpin_100ke_posts_raw.json"
    with open(raw_file, 'w', encoding='utf-8') as f:
        json.dump(all_topics_raw, f, ensure_ascii=False, indent=2)
    print(f"已保存原始数据到 {raw_file}")


def deduplicate_existing():
    """
    对已保存的数据文件进行去重
    """
    # 处理提取后的数据
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        seen_ids = set()
        unique_data = []
        for item in data:
            topic_id = item.get("topic_id")
            if topic_id not in seen_ids:
                seen_ids.add(topic_id)
                unique_data.append(item)
        
        removed = len(data) - len(unique_data)
        print(f"提取数据: 原 {len(data)} 条，去重后 {len(unique_data)} 条，移除 {removed} 条重复")
        
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(unique_data, f, ensure_ascii=False, indent=2)
    
    # 处理原始数据
    raw_file = OUTPUT_DIR / "jingpin_100ke_posts_raw.json"
    if raw_file.exists():
        with open(raw_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        seen_ids = set()
        unique_data = []
        for item in data:
            topic_id = item.get("topic_id")
            if topic_id not in seen_ids:
                seen_ids.add(topic_id)
                unique_data.append(item)
        
        removed = len(data) - len(unique_data)
        print(f"原始数据: 原 {len(data)} 条，去重后 {len(unique_data)} 条，移除 {removed} 条重复")
        
        with open(raw_file, 'w', encoding='utf-8') as f:
            json.dump(unique_data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description="爬取知识星球精品100课")
    parser.add_argument("--dedupe", action="store_true", help="对已有数据进行去重")
    parser.add_argument("--continue", dest="continue_mode", action="store_true", 
                        help="从已有数据的最后一条继续爬取")
    parser.add_argument("--from", dest="start_from", type=str, 
                        help="从指定时间点继续爬取，如: 2022-12-31T17:25:41.134+0800")
    
    args = parser.parse_args()
    
    if args.dedupe:
        # 对已有数据去重
        deduplicate_existing()
    else:
        # 正常爬取
        main(start_end_time=args.start_from, continue_mode=args.continue_mode)
