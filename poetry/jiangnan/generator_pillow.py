"""
使用 Pillow 生成《江南》古诗信息图

依赖：
    uv add pillow

使用：
    uv run poetry/jiangnan/generator_pillow.py
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import textwrap


class JiangnanInfographic:
    """《江南》古诗信息图生成器"""
    
    def __init__(self, width=1080, height=1920):
        """初始化画布"""
        self.width = width
        self.height = height
        # 创建画布（暖米色背景）
        self.image = Image.new('RGB', (width, height), color='#FFF8E1')
        self.draw = ImageDraw.Draw(self.image)
        
        # 字体路径（需要根据实际系统调整）
        self.font_paths = self._get_font_paths()
        
        # 颜色配置
        self.colors = {
            'title': '#5D4037',      # 深棕色
            'text': '#424242',       # 深灰色
            'accent': '#4CAF50',     # 翠绿色
            'lotus': '#F48FB1',      # 粉红色
            'water': '#81D4FA',      # 淡蓝色
            'bg_card': '#FFFDE7',    # 浅黄色卡片
        }
    
    def _get_font_paths(self):
        """获取系统字体路径"""
        # macOS 字体路径
        possible_fonts = [
            '/System/Library/Fonts/PingFang.ttc',
            '/System/Library/Fonts/Supplemental/Arial Unicode.ttf',
            '/Library/Fonts/Arial Unicode.ttf',
            # Linux 字体路径
            '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
            '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
        ]
        
        for font_path in possible_fonts:
            if Path(font_path).exists():
                return font_path
        
        # 如果找不到，返回默认
        return None
    
    def load_font(self, size):
        """加载字体"""
        try:
            if self.font_paths:
                return ImageFont.truetype(self.font_paths, size)
            else:
                return ImageFont.load_default()
        except:
            return ImageFont.load_default()
    
    def draw_title_section(self, y_start=50):
        """绘制标题区域"""
        # 主标题
        font_title = self.load_font(60)
        title = "《江南》古诗趣味学"
        
        # 计算居中位置
        bbox = self.draw.textbbox((0, 0), title, font=font_title)
        text_width = bbox[2] - bbox[0]
        x = (self.width - text_width) // 2
        
        # 绘制标题
        self.draw.text((x, y_start), title, fill=self.colors['title'], font=font_title)
        
        # 副标题
        font_subtitle = self.load_font(30)
        subtitle = "汉乐府民歌 | 适合小学生"
        bbox = self.draw.textbbox((0, 0), subtitle, font=font_subtitle)
        text_width = bbox[2] - bbox[0]
        x = (self.width - text_width) // 2
        
        self.draw.text((x, y_start + 80), subtitle, fill=self.colors['accent'], font=font_subtitle)
        
        return y_start + 150
    
    def draw_card(self, x, y, width, height, color='#FFFDE7', radius=20):
        """绘制圆角卡片背景"""
        # 创建圆角矩形
        self.draw.rounded_rectangle(
            [(x, y), (x + width, y + height)],
            radius=radius,
            fill=color,
            outline=self.colors['accent'],
            width=3
        )
    
    def draw_poem_section(self, y_start):
        """绘制古诗原文区域"""
        card_width = self.width - 120
        card_height = 350
        x = 60
        
        # 绘制卡片背景
        self.draw_card(x, y_start, card_width, card_height, color=self.colors['bg_card'])
        
        # 古诗内容
        font_poem = self.load_font(40)
        poem_lines = [
            "江南可采莲，莲叶何田田。",
            "鱼戏莲叶间。",
            "鱼戏莲叶东，鱼戏莲叶西，",
            "鱼戏莲叶南，鱼戏莲叶北。"
        ]
        
        y_offset = y_start + 60
        for line in poem_lines:
            bbox = self.draw.textbbox((0, 0), line, font=font_poem)
            text_width = bbox[2] - bbox[0]
            text_x = (self.width - text_width) // 2
            self.draw.text((text_x, y_offset), line, fill=self.colors['text'], font=font_poem)
            y_offset += 70
        
        return y_start + card_height + 40
    
    def draw_section_with_emoji(self, y_start, emoji, title, content_lines, bullet_points=None):
        """绘制带 emoji 标题的内容区域"""
        card_width = self.width - 120
        # 计算卡片高度
        base_height = 100 + len(content_lines) * 50
        if bullet_points:
            base_height += len(bullet_points) * 50
        
        x = 60
        
        # 绘制卡片
        self.draw_card(x, y_start, card_width, base_height, color=self.colors['bg_card'])
        
        # 标题
        font_title = self.load_font(38)
        title_text = f"{emoji} {title}"
        self.draw.text((x + 40, y_start + 30), title_text, fill=self.colors['title'], font=font_title)
        
        # 内容
        font_content = self.load_font(32)
        y_offset = y_start + 90
        
        for line in content_lines:
            self.draw.text((x + 40, y_offset), line, fill=self.colors['text'], font=font_content)
            y_offset += 50
        
        # 子弹点列表
        if bullet_points:
            for point in bullet_points:
                self.draw.text((x + 40, y_offset), point, fill=self.colors['accent'], font=font_content)
                y_offset += 50
        
        return y_start + base_height + 30
    
    def draw_author_section(self, y_start):
        """绘制作者来源区域"""
        content_lines = []
        bullet_points = [
            "🏛️ 2000年前皇帝的音乐机构",
            "🎵 专门收集民间歌谣",
            "👨‍👩‍👧‍👦 老百姓集体创作的民歌"
        ]
        
        return self.draw_section_with_emoji(
            y_start, "📚", "什么是汉乐府？",
            content_lines, bullet_points
        )
    
    def draw_background_section(self, y_start):
        """绘制创作背景区域"""
        content_lines = []
        bullet_points = [
            "📍 江南 = 长江以南的水乡",
            "🌿 那里湖泊多、莲花多",
            "☀️ 夏天人们划船采莲",
            "🎶 边采莲边唱歌，好快乐！"
        ]
        
        return self.draw_section_with_emoji(
            y_start, "🏞️", "古诗的故事背景",
            content_lines, bullet_points
        )
    
    def draw_meaning_section(self, y_start):
        """绘制含义解读区域"""
        content_lines = []
        bullet_points = [
            "🌿 田田 = 莲叶茂盛整齐",
            "🐟 戏 = 开心地嬉戏玩耍",
            "🔄 东西南北 = 小鱼游遍每个角落"
        ]
        
        return self.draw_section_with_emoji(
            y_start, "📖", "古诗是什么意思？",
            content_lines, bullet_points
        )
    
    def draw_value_section(self, y_start):
        """绘制价值意义区域"""
        content_lines = []
        bullet_points = [
            "🌈 感受大自然的美丽",
            "😊 体会劳动的快乐",
            "🤝 人与自然和谐相处",
            "📜 了解古人的生活"
        ]
        
        return self.draw_section_with_emoji(
            y_start, "✨", "这首诗教会我们",
            content_lines, bullet_points
        )
    
    def draw_knowledge_section(self, y_start):
        """绘制趣味知识区域"""
        content_lines = [
            "莲花全身都是宝！"
        ]
        bullet_points = [
            "🌸 荷花 → 观赏",
            "🫛 莲子 → 营养美食",
            "🥢 莲藕 → 清甜可口"
        ]
        
        return self.draw_section_with_emoji(
            y_start, "🎯", "你知道吗？",
            content_lines, bullet_points
        )
    
    def generate(self, output_path='jiangnan_infographic.png'):
        """生成完整信息图"""
        print("开始生成《江南》信息图...")
        
        # 1. 标题区
        y_pos = self.draw_title_section(50)
        
        # 2. 古诗原文区
        y_pos = self.draw_poem_section(y_pos)
        
        # 3. 作者来源区
        y_pos = self.draw_author_section(y_pos)
        
        # 4. 创作背景区
        y_pos = self.draw_background_section(y_pos)
        
        # 5. 含义解读区
        y_pos = self.draw_meaning_section(y_pos)
        
        # 6. 价值意义区
        y_pos = self.draw_value_section(y_pos)
        
        # 7. 趣味知识区
        y_pos = self.draw_knowledge_section(y_pos)
        
        # 保存图片
        output_file = Path(__file__).parent / output_path
        self.image.save(output_file, quality=95)
        print(f"✅ 信息图已生成：{output_file}")
        print(f"📏 尺寸：{self.width} x {self.height}")
        
        return output_file


def main():
    """主函数"""
    generator = JiangnanInfographic(width=1080, height=1920)
    output_path = generator.generate()
    print(f"\n🎉 完成！请查看生成的图片：{output_path}")


if __name__ == '__main__':
    main()
