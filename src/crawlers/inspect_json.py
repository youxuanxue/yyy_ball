import json

INPUT_FILE = "sunzi_bingfa_column_posts.json"

def inspect_json():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        posts = json.load(f)
    
    print(f"Total posts: {len(posts)}")
    if not posts:
        return
        
    # Check the keys of the first few posts to understand structure
    for i, post in enumerate(posts[:5]):
        print(f"\n--- Post {i+1} ---")
        print(f"Keys: {list(post.keys())}")
        print(f"Type: {post.get('type')}")
        
        # Check specific content fields based on type
        if 'talk' in post:
            print(f"Talk content length: {len(post['talk'].get('text', ''))}")
        if 'show' in post:
            print(f"Show content length: {len(post['show'].get('text', ''))}")
        if 'article' in post:
             print(f"Article title: {post['article'].get('title')}")
        
        # Print a small dump to see structure
        print(json.dumps(post, indent=2, ensure_ascii=False)[:500])

if __name__ == "__main__":
    inspect_json()

