import requests
import json
import time
import os
from urllib.parse import quote

# Configuration
GROUP_ID = "15284248885222"
COLUMN_ID = "481828511858" # 易经专栏ID

HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cookie": "zsxq_access_token=56E980AF-AB6F-4CC2-BEE6-EDFD10EFBA4B_07844E0DFEE29E1E; abtest_env=beta",
    "origin": "https://wx.zsxq.com",
    "priority": "u=1, i",
    "referer": "https://wx.zsxq.com/",
    "sec-ch-ua": '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "x-version": "2.85.0"
}

OUTPUT_FILE = "yijing_column_posts.json"

def fetch_topics(end_time=None):
    """
    Fetch topics from the API.
    :param end_time: The create_time of the last topic from the previous page, for pagination.
    """
    url = f"https://api.zsxq.com/v2/groups/{GROUP_ID}/columns/{COLUMN_ID}/topics?count=100&sort=default&direction=desc"
    
    if end_time:
        url += f"&end_time={quote(end_time)}"
    
    print(f"Fetching: {url}")
    
    try:
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
    
    # Check if we should disable SSL warnings
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
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
        new_end_time = last_topic.get('create_time')
        
        # Check against previous end_time to prevent infinite loop
        if new_end_time == end_time:
             print("Warning: end_time did not change, might be stuck loop. Breaking.")
             break
             
        end_time = new_end_time
        
        # With count=100, if we get fewer than 100, we are likely done.
        if len(topics) < 100:
            has_more = False
            
        # Be nice to the server
        time.sleep(2)

    print(f"Total topics fetched: {len(all_topics)}")
    
    # Save raw data
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_topics, f, ensure_ascii=False, indent=2)
    print(f"Saved raw data to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

