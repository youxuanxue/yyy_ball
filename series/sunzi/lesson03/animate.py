import sys
import os
from manim import *

# 将项目根目录加入 path，以便导入 utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 更新：从 utils 导入 play_timeline
from utils.anim_helper import get_audio_duration, combine_audio_clips, wait_until_audio_end, play_timeline

# 配置
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.media_dir = "media/sunzi/lesson03"

# 路径
VOICE_DIR = "media/sunzi/lesson03/voice"
COMBINED_WAV = os.path.join(VOICE_DIR, "lesson3_full.wav")

class Lesson3Vertical(Scene):
    def construct(self):
        # 字体与样式
        title_font = "PingFang SC" 
        body_font = "PingFang SC"
        FONT_TITLE = 48
        FONT_BODY = 32
        FONT_SMALL = 24
        SAFE_BOTTOM_BUFF = 3.5
        SAFE_CENTER_UP = 0.6
        TRANSITION_TIME = 0.5

        # ---------------------------------------------------------
        # 全局音频
        # ---------------------------------------------------------
        audio_clips = [
            os.path.join(VOICE_DIR, "01_cover.mp3"),
            os.path.join(VOICE_DIR, "02_best_winner.mp3"),
            os.path.join(VOICE_DIR, "03_four_levels.mp3"),
            os.path.join(VOICE_DIR, "04_know_yourself.mp3"),
            os.path.join(VOICE_DIR, "05_ending.mp3"),
        ]
        
        # 合并音频（仅用于视频背景音，实际播放靠 wait 控制）
        full_audio = combine_audio_clips(audio_clips, COMBINED_WAV, silence_duration=0)
        self.add_sound(full_audio)

        # =========================================================
        # 1. 封面：最好的胜利是不打架？
        # =========================================================
        audio_file = audio_clips[0]
        page_duration = get_audio_duration(audio_file)
        
        # 元素定义
        title = Text("最好的胜利是不打架？", font=title_font, font_size=FONT_TITLE, weight=BOLD).shift(UP*2)
        subtitle = Text("—— 孙子兵法第三课：谋攻篇", font=title_font, font_size=FONT_BODY, color=BLUE)
        subtitle.next_to(title, DOWN, buff=1)
        
        icon_fight = Text("打架", font_size=60, color=RED, weight=BOLD)
        icon_brain = Text("智慧", font_size=60, color=BLUE, weight=BOLD)
        vs = Text("VS", font_size=48, color=GRAY, slant=ITALIC)
        # 先不 Group，分开定义位置以便独立动画
        vs.next_to(subtitle, DOWN, buff=2)
        icon_fight.next_to(vs, LEFT, buff=0.8)
        icon_brain.next_to(vs, RIGHT, buff=0.8)
        
        target = Text(
            "致：\n爱思考的你\n喜欢动脑筋的你\n",
            font=body_font, 
            font_size=FONT_SMALL, 
            color=GRAY,
            line_spacing=1.2
        ).to_edge(DOWN, buff=SAFE_BOTTOM_BUFF)

        # 编排与权重 (根据文本长度和重要性)
        # 标题(10) -> 副标题(8) -> VS(2) -> 打架(4) -> 智慧(4) -> 致辞(8)
        timeline_steps = [
            (10, Write(title)),
            (8,  FadeIn(subtitle, shift=UP)),
            (2,  FadeIn(vs)),
            (4,  FadeIn(icon_fight, shift=RIGHT)), # 撞击感
            (4,  FadeIn(icon_brain, shift=LEFT)),
            (8,  Write(target)),
        ]
        
        # 更新：传入 self
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration, elapsed)
        
        # 转场
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)

        # =========================================================
        # 2. 真正的赢家 (不战而屈人之兵)
        # =========================================================
        audio_file = audio_clips[1]
        page_duration = get_audio_duration(audio_file)
        
        p2_title = Text("真正的赢家是谁？", font=title_font, font_size=FONT_TITLE, color=ORANGE).to_edge(UP, buff=2)
        quote = Text('“百战百胜，非善之善者也；\n不战而屈人之兵，善之善者也。”', font=body_font, font_size=FONT_BODY, slant=ITALIC, line_spacing=1.5).next_to(p2_title, DOWN, buff=1)
        
        # Box 1
        box1 = RoundedRectangle(width=6, height=2, color=GRAY, fill_opacity=0.1)
        t1_text = Text("百战百胜 = 厉害", font_size=32, color=GRAY)
        t1_icon = Text("✔", font_size=32, color=GRAY, font="Arial") 
        txt1 = VGroup(t1_text, t1_icon).arrange(RIGHT).move_to(box1)
        group1 = VGroup(box1, txt1).next_to(quote, DOWN, buff=1)
        
        # Box 2
        box2 = RoundedRectangle(width=7, height=2.5, color=GOLD, fill_opacity=0.2)
        t2_text = Text("不战而胜 = 最棒", font_size=40, color=GOLD, weight=BOLD)
        t2_icon = Star(color=GOLD, fill_opacity=1).scale(0.3)
        txt2 = VGroup(t2_text, t2_icon).arrange(RIGHT).move_to(box2)
        group2 = VGroup(box2, txt2).next_to(group1, DOWN, buff=0.5)
        
        VGroup(p2_title, quote, group1, group2).move_to(ORIGIN).shift(UP * SAFE_CENTER_UP)
        
        # 权重
        # 标题(2) -> 引用(10, 很长) -> Box1(2) -> Box2(3, 重点)
        timeline_steps = [
            (2,  Write(p2_title)),
            (15, Write(quote)),
            (2,  FadeIn(group1, shift=LEFT)),
            (3, GrowFromCenter(group2)),
        ]
        
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration, elapsed)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)

        # =========================================================
        # 3. 解决问题的四个等级
        # =========================================================
        audio_file = audio_clips[2]
        page_duration = get_audio_duration(audio_file)
        
        p3_title = Text("解决问题的四个等级", font=title_font, font_size=FONT_TITLE, color=BLUE).to_edge(UP, buff=2)
        
        levels = [
            ("第一等：伐谋", "用脑子 (想办法)", GREEN),
            ("第二等：伐交", "动嘴巴 (找朋友)", TEAL),
            ("第三等：伐兵", "动手 (容易受伤)", ORANGE),
            ("最差等：攻城", "硬碰硬 (头破血流)", RED),
        ]
        
        level_items = []
        for i, (title_text, desc_text, color) in enumerate(levels):
            indent = i * 0.5
            l_title = Text(title_text, font_size=32, color=color, weight=BOLD)
            l_desc = Text(desc_text, font_size=24, color=WHITE).next_to(l_title, DOWN, buff=0.2, aligned_edge=LEFT)
            dot = Dot(color=color).next_to(l_title, LEFT, buff=0.3)
            bg = RoundedRectangle(width=6, height=1.8, color=color, fill_opacity=0.15)
            content = VGroup(dot, l_title, l_desc).move_to(bg)
            item = VGroup(bg, content).shift(RIGHT * indent)
            level_items.append(item)
            
        level_group = VGroup(*level_items)
        level_group.arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(p3_title, DOWN, buff=0.8)
        VGroup(p3_title, level_group).move_to(ORIGIN).shift(UP * SAFE_CENTER_UP)
        
        # 权重
        # 标题(3) -> 四个等级各(8)
        timeline_steps = [
            (4, Write(p3_title)),
            (8, FadeIn(level_items[0], shift=DOWN * 0.5)),
            (8, FadeIn(level_items[1], shift=DOWN * 0.5)),
            (8, FadeIn(level_items[2], shift=DOWN * 0.5)),
            (8, FadeIn(level_items[3], shift=DOWN * 0.5)),
        ]
        
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration, elapsed)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)

        # =========================================================
        # 4. 胜利的数学题
        # =========================================================
        audio_file = audio_clips[3]
        page_duration = get_audio_duration(audio_file)
        
        p4_title = Text("胜利的数学题", font=title_font, font_size=FONT_TITLE, color=PURPLE).to_edge(UP, buff=2)
        golden_sentence = Text("“知彼知己，百战不殆”", font_size=48, color=YELLOW).next_to(p4_title, DOWN, buff=0.8)
        
        eq1 = VGroup(Text("知彼 + 知己", font_size=30, color=GREEN), Text("=", font_size=30), Text("百战不殆 (赢)", font_size=30, color=GREEN, weight=BOLD)).arrange(RIGHT)
        eq2 = VGroup(Text("不知彼 + 知己", font_size=30, color=YELLOW), Text("=", font_size=30), Text("一胜一负 (一半)", font_size=30, color=YELLOW)).arrange(RIGHT)
        eq3 = VGroup(Text("不知彼 + 不知己", font_size=30, color=RED), Text("=", font_size=30), Text("每战必殆 (输)", font_size=30, color=RED, weight=BOLD)).arrange(RIGHT)
        
        equations = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.8, aligned_edge=LEFT).next_to(golden_sentence, DOWN, buff=1.0)
        VGroup(p4_title, golden_sentence, equations).move_to(ORIGIN).shift(UP * SAFE_CENTER_UP)
        
        # 权重
        # 标题(5) -> 金句(10) -> 解释金句(5, indicate) -> 公式1(8) -> 公式2(8) -> 公式3(8)
        timeline_steps = [
            (5,  Write(p4_title)),
            (10, Write(golden_sentence)),
            (5,  Indicate(golden_sentence)),
            (8,  FadeIn(eq1, shift=RIGHT)),
            (8,  FadeIn(eq2, shift=RIGHT)),
            (8,  FadeIn(eq3, shift=RIGHT)),
        ]
        
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration, elapsed)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)

        # =========================================================
        # 5. 结尾互动
        # =========================================================
        audio_file = audio_clips[4]
        page_duration = get_audio_duration(audio_file)
        
        q_mark = Text("?", font_size=100, color=YELLOW, weight=BOLD)
        q_text = Text("小武思考时间", font=title_font, font_size=40, color=WHITE)
        q_bg = RoundedRectangle(width=5, height=1.2, corner_radius=0.6, color=BLUE, fill_opacity=0.8)
        q_header = VGroup(q_mark, VGroup(q_bg, q_text)).arrange(DOWN, buff=0.3).to_edge(UP, buff=1.0)
        
        question = Text("如果同学给你起外号，怎么办？", font=body_font, font_size=36).next_to(q_header, DOWN, buff=0.8)
        
        options = [
            ("A. 骂回去，打一架！", RED),
            ("B. 生闷气，哭鼻子。", GRAY),
            ("C. 动脑筋，让他闭嘴。", GREEN),
        ]
        
        opt_items = []
        for text, color in options:
            box = RoundedRectangle(width=8, height=1.5, color=color, fill_opacity=0.1)
            txt = Text(text, font_size=32, color=WHITE).move_to(box)
            opt_items.append(VGroup(box, txt))
            
        opt_group = VGroup(*opt_items).arrange(DOWN, buff=0.4).next_to(question, DOWN, buff=1.0)
        
        if opt_group.get_bottom()[1] < -5:
             VGroup(q_header, question, opt_group).shift(UP * 0.5)

        cta_text = Text("在评论区告诉小武你的选择！", font_size=28, color=BLUE)
        cta_arrow = Triangle(color=BLUE, fill_opacity=1).scale(0.15).rotate(PI)
        cta = VGroup(cta_arrow, cta_text).arrange(RIGHT).to_edge(DOWN, buff=SAFE_BOTTOM_BUFF)
        
        # 权重
        # 头部(2) -> 问号动效(2) -> 问题(2) -> 选项A(6) -> 选项B(6) -> 选项C(6) -> CTA(5)
        timeline_steps = [
            (2, [GrowFromCenter(q_mark), FadeIn(q_bg, shift=UP), Write(q_text)]), # 组合动画作为一步
            (2, Wiggle(q_mark, scale_value=1.2)),
            (2, Write(question)),
            (6, GrowFromCenter(opt_items[0])),
            (6, GrowFromCenter(opt_items[1])),
            (6, GrowFromCenter(opt_items[2])),
            (5, Write(cta))
        ]
        
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration, elapsed)
        self.wait(2.0)
