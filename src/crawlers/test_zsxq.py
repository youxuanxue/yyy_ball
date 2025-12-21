import requests
import json

url = "https://api.zsxq.com/v2/hashtags/28888181858221/topics?count=20"

headers = {
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
    "x-aduid": "5e7a2678e-e8d5-eb5c-08e4-af283659d53",
    "x-request-id": "dd0f3b215-5f9a-a7cf-b805-8e6b20832dc",
    "x-signature": "16a747facd02e2f6e50554ca59a8dd517992798d",
    "x-timestamp": "1765957689",
    "x-version": "2.85.0"
}

try:
    response = requests.get(url, headers=headers, verify=False)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Keys in resp_data: {data.get('resp_data', {}).keys()}")
        topics = data.get('resp_data', {}).get('topics', [])
        print(f"Number of topics: {len(topics)}")
        if topics:
            last_topic = topics[-1]
            print(f"Last topic keys: {last_topic.keys()}")
            print(f"Last topic create_time: {last_topic.get('create_time')}")
            # Check for images and comments in the first topic to see structure
            first_topic = topics[0]
            print("First topic structure sample:")
            if 'talk' in first_topic:
                print(f"Talk text length: {len(first_topic['talk'].get('text', ''))}")
                print(f"Images: {first_topic['talk'].get('images')}")
            elif 'show' in first_topic: # sometimes it's show for essays
                print(f"Show text length: {len(first_topic['show'].get('text', ''))}")
    else:
        print(response.text)
except Exception as e:
    print(f"Error: {e}")

