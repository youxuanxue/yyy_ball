import requests
import json
import time
import os

# Configuration
INPUT_FILE = "yijing_column_posts.json"
OUTPUT_FILE = "yijing_details.json"

HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cookie": "zsxq_access_token=56E980AF-AB6F-4CC2-BEE6-EDFD10EFBA4B_07844E0DFEE29E1E; abtest_env=beta",
    "origin": "https://wx.zsxq.com",
    "referer": "https://wx.zsxq.com/",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "x-version": "2.85.0"
}

def fetch_topic_detail(topic_id):
    url = f"https://api.zsxq.com/v2/topics/{topic_id}/info"
    print(f"Fetching detail for: {topic_id}")
    
    try:
        response = requests.get(url, headers=HEADERS, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"{INPUT_FILE} not found!")
        return
        
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        simple_posts = json.load(f)
        
    print(f"Found {len(simple_posts)} posts to fetch details for.")
    
    full_posts = []
    
    # Check if we already have some fetched (resume capability)
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
                existing = json.load(f)
                full_posts = existing
                print(f"Loaded {len(full_posts)} existing details.")
        except:
            pass
            
    existing_ids = {p.get('topic_id') for p in full_posts if 'topic_id' in p}
    
    # Suppress SSL warnings
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    for i, post in enumerate(simple_posts):
        topic_id = post.get('topic_id')
        if not topic_id:
            continue
            
        if topic_id in existing_ids:
            continue
            
        detail = fetch_topic_detail(topic_id)
        
        if detail and 'resp_data' in detail:
            topic_data = detail['resp_data'].get('topic')
            if topic_data:
                full_posts.append(topic_data)
                
        # Save every 5 requests just in case
        if i % 5 == 0:
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                json.dump(full_posts, f, ensure_ascii=False, indent=2)
                
        time.sleep(1.5) # Be nice
        
    # Final save
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(full_posts, f, ensure_ascii=False, indent=2)
        
    print(f"Done. Saved {len(full_posts)} details to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

