import json
import os
from datetime import datetime

INPUT_FILE = "yijing_details.json"
OUTPUT_MD = "易经_大王与你读兵法_完整版.md"

def parse_post(post):
    """
    Parse a single post dictionary into a structured object.
    """
    # Basic info
    created_time_str = post.get('create_time', '')
    try:
        dt = datetime.strptime(created_time_str.split('.')[0], "%Y-%m-%dT%H:%M:%S")
        date_display = dt.strftime("%Y-%m-%d %H:%M")
    except:
        date_display = created_time_str

    author = post.get('talk', {}).get('owner', {}).get('name', 'Unknown')
    if author == 'Unknown' and 'show' in post:
        author = post.get('show', {}).get('owner', {}).get('name', 'Unknown')
    
    # Content extraction logic for detail API structure
    content = ""
    images = []
    
    if 'talk' in post:
        content = post['talk'].get('text', '')
        images = post['talk'].get('images', [])
    elif 'show' in post:
        content = post['show'].get('text', '')
        images = post['show'].get('images', [])
    elif 'q_and_a' in post:
        content = post['q_and_a'].get('answer', {}).get('text', '')
        if not content:
             content = post['q_and_a'].get('question', {}).get('text', '')
    elif 'article' in post:
        content = post['article'].get('title', '') + "\n\n" + post['article'].get('text', '') 
        if not post['article'].get('text'):
             content += "(文章链接或富文本内容，此处仅展示标题)"
        images = post['article'].get('images', [])

    if not content:
        content = post.get('text', '')

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
        'comments_count': post.get('comments_count', 0),
        'title': post.get('title', '')
    }

def generate_markdown(posts):
    md_content = "# 《易经》系列 - 大王与你读兵法（完整版）\n\n"
    md_content += f"总计篇数：{len(posts)}\n\n---\n\n"
    
    # Sort by date
    posts.sort(key=lambda x: x.get('create_time', ''))
    
    for i, post in enumerate(posts, 1):
        parsed = parse_post(post)
        
        md_content += f"## 第 {i} 篇"
        if parsed['title']:
            md_content += f": {parsed['title']}"
        md_content += "\n\n"
        
        md_content += f"**时间**: {parsed['date']}  |  **作者**: {parsed['author']}  |  **点赞**: {parsed['likes']}\n\n"
        
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
        
    posts = [p for p in posts if p]
    
    print(f"Loaded {len(posts)} posts.")
    
    md_output = generate_markdown(posts)
    
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write(md_output)
        
    print(f"Generated Markdown file: {OUTPUT_MD}")

if __name__ == "__main__":
    main()

