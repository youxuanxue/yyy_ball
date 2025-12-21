import json
import os
from datetime import datetime

INPUT_FILE = "sunzi_bingfa_posts.json"
OUTPUT_MD = "孙子兵法_大王与你读兵法.md"

def parse_post(post):
    """
    Parse a single post dictionary into a structured object.
    """
    # Basic info
    created_time_str = post.get('create_time', '')
    try:
        # 2023-07-31T15:07:45.528+0800 -> Display format
        dt = datetime.strptime(created_time_str.split('.')[0], "%Y-%m-%dT%H:%M:%S")
        date_display = dt.strftime("%Y-%m-%d %H:%M")
    except:
        date_display = created_time_str

    author = post.get('talk', {}).get('owner', {}).get('name', 'Unknown')
    
    # Content
    content = ""
    images = []
    
    if 'talk' in post:
        content = post['talk'].get('text', '')
        images = post['talk'].get('images', [])
    elif 'show' in post:
        content = post['show'].get('text', '')
        images = post['show'].get('images', [])
        
    # Comments (if any in the list API, usually need detail API for full comments, 
    # but list sometimes has recent ones or show_comments)
    comments = []
    if 'show_comments' in post:
        for comment in post['show_comments']:
            c_author = comment.get('owner', {}).get('name', 'Unknown')
            c_text = comment.get('text', '')
            comments.append(f"{c_author}: {c_text}")
            
    return {
        'date': date_display,
        'author': author,
        'content': content,
        'images': [img.get('large', {}).get('url') for img in images if 'large' in img],
        'comments': comments,
        'likes': post.get('likes_count', 0),
        'comments_count': post.get('comments_count', 0)
    }

def generate_markdown(posts):
    md_content = "# 大王与你读兵法 - 孙子兵法系列\n\n"
    md_content += f"总计篇数：{len(posts)}\n\n---\n\n"
    
    # Sort by date (oldest first usually makes sense for reading a series, but let's stick to API order or reverse?)
    # API usually returns newest first. Let's reverse to read from beginning.
    posts.reverse()
    
    for i, post in enumerate(posts, 1):
        parsed = parse_post(post)
        
        md_content += f"## 第 {i} 篇\n\n"
        md_content += f"**时间**: {parsed['date']}  |  **作者**: {parsed['author']}  |  **点赞**: {parsed['likes']}\n\n"
        
        # Process content text to handle newlines
        content_text = parsed['content'].replace('\n', '  \n')
        md_content += f"{content_text}\n\n"
        
        if parsed['images']:
            md_content += "**图片**:\n\n"
            for img_url in parsed['images']:
                md_content += f"![]({img_url})\n\n"
                
        if parsed['comments']:
            md_content += "**精选评论**:\n\n"
            for c in parsed['comments']:
                md_content += f"> {c}  \n"
        
        md_content += "\n---\n\n"
        
    return md_content

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"File {INPUT_FILE} not found.")
        return
        
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        posts = json.load(f)
        
    print(f"Loaded {len(posts)} posts.")
    
    md_output = generate_markdown(posts)
    
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write(md_output)
        
    print(f"Generated Markdown file: {OUTPUT_MD}")

if __name__ == "__main__":
    main()

