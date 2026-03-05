"""
使用 HTML + CSS + Playwright 生成《江南》古诗信息图

依赖：
    uv add playwright
    playwright install chromium

使用：
    uv run poetry/jiangnan/generator_html.py
"""

from pathlib import Path


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>《江南》古诗趣味学</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
            background: linear-gradient(to bottom, #FFF8E1, #FFFDE7);
            padding: 50px;
            width: 1080px;
            min-height: 1920px;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
        }
        
        /* 标题区 */
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .main-title {
            font-size: 60px;
            color: #5D4037;
            margin-bottom: 20px;
            font-weight: bold;
        }
        
        .subtitle {
            font-size: 30px;
            color: #4CAF50;
        }
        
        /* 卡片样式 */
        .card {
            background: #FFFDE7;
            border: 3px solid #4CAF50;
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        /* 古诗区 */
        .poem {
            text-align: center;
            font-size: 40px;
            line-height: 70px;
            color: #424242;
        }
        
        /* 内容区标题 */
        .section-title {
            font-size: 38px;
            color: #5D4037;
            margin-bottom: 25px;
            font-weight: bold;
        }
        
        .emoji {
            font-size: 42px;
            margin-right: 10px;
        }
        
        /* 列表 */
        .bullet-list {
            list-style: none;
            font-size: 32px;
            line-height: 50px;
            color: #424242;
        }
        
        .bullet-list li {
            margin-bottom: 15px;
            padding-left: 10px;
        }
        
        .accent {
            color: #4CAF50;
        }
        
        /* 装饰元素 */
        .decoration {
            text-align: center;
            font-size: 50px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- 标题区 -->
        <div class="header">
            <h1 class="main-title">🌸 《江南》古诗趣味学 🌸</h1>
            <p class="subtitle">汉乐府民歌 | 适合小学生</p>
        </div>
        
        <!-- 古诗原文 -->
        <div class="card poem">
            <div>江南可采莲，莲叶何田田。</div>
            <div>鱼戏莲叶间。</div>
            <div>鱼戏莲叶东，鱼戏莲叶西，</div>
            <div>鱼戏莲叶南，鱼戏莲叶北。</div>
        </div>
        
        <div class="decoration">🌿 🐟 🌸 🐟 🌿</div>
        
        <!-- 什么是汉乐府 -->
        <div class="card">
            <h2 class="section-title">
                <span class="emoji">📚</span>什么是汉乐府？
            </h2>
            <ul class="bullet-list">
                <li>🏛️ 2000年前皇帝的音乐机构</li>
                <li>🎵 专门收集民间歌谣</li>
                <li>👨‍👩‍👧‍👦 老百姓集体创作的民歌</li>
            </ul>
        </div>
        
        <!-- 创作背景 -->
        <div class="card">
            <h2 class="section-title">
                <span class="emoji">🏞️</span>古诗的故事背景
            </h2>
            <ul class="bullet-list">
                <li>📍 江南 = 长江以南的水乡</li>
                <li>🌿 那里湖泊多、莲花多</li>
                <li>☀️ 夏天人们划船采莲</li>
                <li>🎶 边采莲边唱歌，好快乐！</li>
            </ul>
        </div>
        
        <div class="decoration">～～ 🚣 ～～</div>
        
        <!-- 含义解读 -->
        <div class="card">
            <h2 class="section-title">
                <span class="emoji">📖</span>古诗是什么意思？
            </h2>
            <ul class="bullet-list">
                <li>🌿 <strong>田田</strong> = 莲叶茂盛整齐</li>
                <li>🐟 <strong>戏</strong> = 开心地嬉戏玩耍</li>
                <li>🔄 <strong>东西南北</strong> = 小鱼游遍每个角落</li>
            </ul>
        </div>
        
        <!-- 价值意义 -->
        <div class="card">
            <h2 class="section-title">
                <span class="emoji">✨</span>这首诗教会我们
            </h2>
            <ul class="bullet-list">
                <li>🌈 感受大自然的美丽</li>
                <li>😊 体会劳动的快乐</li>
                <li>🤝 人与自然和谐相处</li>
                <li>📜 了解古人的生活</li>
            </ul>
        </div>
        
        <!-- 趣味知识 -->
        <div class="card">
            <h2 class="section-title">
                <span class="emoji">🎯</span>你知道吗？
            </h2>
            <p class="bullet-list" style="margin-bottom: 20px;">莲花全身都是宝！</p>
            <ul class="bullet-list">
                <li>🌸 荷花 → 观赏</li>
                <li>🫛 莲子 → 营养美食</li>
                <li>🥢 莲藕 → 清甜可口</li>
            </ul>
        </div>
        
        <div class="decoration">🌸 🌿 感谢学习 🌿 🌸</div>
    </div>
</body>
</html>
"""


async def generate_infographic_from_html():
    """使用 Playwright 从 HTML 生成图片"""
    from playwright.async_api import async_playwright
    
    print("开始生成《江南》信息图（HTML方式）...")
    
    # 保存 HTML 文件
    html_path = Path(__file__).parent / "jiangnan_template.html"
    html_path.write_text(HTML_TEMPLATE, encoding='utf-8')
    print(f"✅ HTML模板已生成：{html_path}")
    
    # 使用 Playwright 渲染为图片
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1080, 'height': 1920})
        
        # 加载 HTML
        await page.goto(f'file://{html_path.absolute()}')
        
        # 等待渲染完成
        await page.wait_for_timeout(1000)
        
        # 截图
        output_path = Path(__file__).parent / "jiangnan_infographic_html.png"
        await page.screenshot(path=str(output_path), full_page=True)
        
        await browser.close()
        
        print(f"✅ 信息图已生成：{output_path}")
        return output_path


def main():
    """主函数"""
    import asyncio
    output_path = asyncio.run(generate_infographic_from_html())
    print(f"\n🎉 完成！请查看生成的图片：{output_path}")


if __name__ == '__main__':
    main()
