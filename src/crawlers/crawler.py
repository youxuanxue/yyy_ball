import requests
import json
import time
import os
from urllib.parse import quote

# Configuration
GROUP_ID = "28888181858221" # 话题ID (Hashtag ID)
TAG_NAME = "大王与你读兵法"
HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cookie": "zsxq_access_token=56E980AF-AB6F-4CC2-BEE6-EDFD10EFBA4B_07844E0DFEE29E1E; abtest_env=beta",
    "origin": "https://wx.zsxq.com",
    "referer": "https://wx.zsxq.com/",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "x-timestamp": "1765957689", # Try adding static timestamp from curl
    "x-signature": "16a747facd02e2f6e50554ca59a8dd517992798d", # Try adding signature
    "x-request-id": "dd0f3b215-5f9a-a7cf-b805-8e6b20832dc",
    "x-version": "2.85.0"
}

OUTPUT_FILE = "sunzi_bingfa_posts.json"

def fetch_topics(end_time=None):
    """
    Fetch topics from the API.
    :param end_time: The create_time of the last topic from the previous page, for pagination.
    """
    url = f"https://api.zsxq.com/v2/hashtags/{GROUP_ID}/topics?count=20"
    if end_time:
        # URL encode only the necessary part, but keep the format clean
        # The API seems to accept the raw ISO string or URL encoded. 
        # Let's try NOT encoding it first as requests might handle it, or encode it manually.
        # However, looking at the previous output, the URL printed was:
        # ...&end_time=2023-07-31T15%3A07%3A45.528%2B0800
        # This means quote() was working.
        
        # KEY FIX: The 'create_time' from the API includes milliseconds +0800.
        # Sometimes using the EXACT same time as end_time excludes it (good), 
        # sometimes it includes it (bad loop).
        # We need to make sure we are paginating correctly.
        # Let's subtract 1 millisecond just to be safe if we get stuck?
        # Or rely on the fact that we got 16 results last time, meaning it worked.
        
        # If the last result was empty, it means we are done or blocked.
        url += f"&end_time={quote(end_time)}"
    
    print(f"Fetching: {url}")
    
    try:
        # We need to update headers dynamic values if possible, but for now reuse.
        # If curl works, python should work.
        response = requests.get(url, headers=HEADERS, verify=False) 
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    all_topics = []
    end_time = None
    has_more = True
    
    while has_more:
        data = fetch_topics(end_time)
        
        if not data or 'resp_data' not in data:
            print("No valid data received or error occurred.")
            break
            
        topics = data['resp_data'].get('topics', [])
        
        if not topics:
            print("No more topics found.")
            break
            
        print(f"Retrieved {len(topics)} topics.")
        all_topics.extend(topics)
        
        # Pagination logic
        last_topic = topics[-1]
        
        # 知识星球翻页逻辑修正：
        # create_time 格式如 2023-07-31T15:07:45.528+0800
        # 实际 API 请求中，create_time 中的 + 号会被 requests 自动编码或不编码，但 API 可能需要严格的 URL 编码。
        # 另外，最后一条数据的 create_time 作为下一页的 end_time 时，需要毫秒级减 1 毫秒或者直接使用，
        # 但有些接口使用 exact time，有些是 exclusive。
        # 观察之前的输出，第二次请求只拿到了 16 条，说明翻页是生效了的。
        # 为什么只抓了 36 条？可能是因为第二次请求后 len(topics) < 20 导致退出。
        # 如果总数真的只有 36 条，那就是对的。如果不仅如此，那可能是 end_time 处理有问题。
        
        new_end_time = last_topic.get('create_time')
        
        # Check against previous end_time to prevent infinite loop
        if new_end_time == end_time:
             print("Warning: end_time did not change, might be stuck loop. Breaking.")
             break
             
        end_time = new_end_time
        
        # API often returns fewer than 20 if filtered or at end.
        if len(topics) == 0:
            has_more = False
            
        # Be nice to the server
        time.sleep(1)

    print(f"Total topics fetched: {len(all_topics)}")
    
    # Save raw data first
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_topics, f, ensure_ascii=False, indent=2)
    print(f"Saved raw data to {OUTPUT_FILE}")

if __name__ == "__main__":
    # Suppress SSL warnings
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()

