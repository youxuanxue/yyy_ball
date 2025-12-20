import sys
import os
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from utils.anim_helper import get_audio_duration, combine_audio_clips, wait_until_audio_end, play_timeline

# 配置
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.media_dir = "media/sunzi/lesson04"

# 路径
VOICE_DIR = "media/sunzi/lesson04/voice"
COMBINED_WAV = os.path.join(VOICE_DIR, "lesson4_full.wav")

class Lesson4Vertical(Scene):
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
        # 0. 插入封面首帧 (Cover Frame)
        # ---------------------------------------------------------
        # 这一帧用于作为视频平台的默认封面
        cover_path = "media/sunzi/lesson04/images/cover_design.png"
        if os.path.exists(cover_path):
            cover_img = ImageMobject(cover_path)
            cover_img.height = config.frame_height # 铺满全屏
            self.add(cover_img)
            self.wait(0.1)
            self.remove(cover_img)

        # ---------------------------------------------------------
        # 全局音频 & BGM
        # ---------------------------------------------------------
        audio_clips = [
            os.path.join(VOICE_DIR, "01_cover.mp3"),
            os.path.join(VOICE_DIR, "02_invincible.mp3"),
            os.path.join(VOICE_DIR, "03_control.mp3"),
            os.path.join(VOICE_DIR, "04_winner_mindset.mp3"),
            os.path.join(VOICE_DIR, "05_ending.mp3"),
        ]
        
        # 假设我们已经挑选了一首 BGM
        bgm_file = "assets/bgm/smart_thinking.wav"
        
        full_audio = combine_audio_clips(
            audio_clips, 
            os.path.join(VOICE_DIR, "lesson4_full_v2.wav"), 
            silence_duration=0,
            bgm_file=bgm_file,
            bgm_volume=-15,
            bgm_loop=True
        )
        self.add_sound(full_audio)

        # =========================================================
        # 1. 封面：怎做常胜将军？
        # =========================================================
        audio_file = audio_clips[0]
        page_duration = get_audio_duration(audio_file)
        
        title = Text("怎做常胜将军？", font=title_font, font_size=FONT_TITLE, weight=BOLD).shift(UP*2)
        subtitle = Text("—— 孙子兵法第四课：军形篇", font=title_font, font_size=FONT_BODY, color=BLUE)
        subtitle.next_to(title, DOWN, buff=1)
        
        # 图标：奖杯 or 勋章
        # 再次缩小尺寸并上移位置，彻底解决重叠
        icon_medal = Star(color=GOLD, fill_opacity=1, outer_radius=1.2, inner_radius=0.6).move_to(ORIGIN)
        text_win = Text("永不输", font_size=28, color=BLACK).move_to(icon_medal)
        medal_group = VGroup(icon_medal, text_win).next_to(subtitle, DOWN, buff=0.8)
        
        target = Text(
            "致：\n爱思考的你\n喜欢动脑筋的你\n",
            font=body_font, 
            font_size=FONT_SMALL, 
            color=GRAY,
            line_spacing=1.2
        ).to_edge(DOWN, buff=SAFE_BOTTOM_BUFF)
        
        timeline_steps = [
            (5, Write(title)),
            (5, FadeIn(subtitle, shift=UP)),
            (8, GrowFromCenter(medal_group)),
            (5, Wiggle(medal_group)), # 强调“永远不输”
            (5, Write(target)),
        ]
        
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)

        # =========================================================
        # 2. 先为不可胜 (钢铁侠盔甲)
        # =========================================================
        audio_file = audio_clips[1]
        page_duration = get_audio_duration(audio_file)
        
        p2_title = Text("先为不可胜", font=title_font, font_size=FONT_TITLE, color=ORANGE).to_edge(UP, buff=2)
        quote = Text('“善战者，先为不可胜”', font=body_font, font_size=FONT_BODY, slant=ITALIC).next_to(p2_title, DOWN, buff=0.8)
        
        # 视觉：盾牌/防守
        shield = Circle(radius=2, color=BLUE, fill_opacity=0.3).set_stroke(width=10)
        shield_cross = VGroup(
            Line(start=LEFT*1.5, end=RIGHT*1.5, stroke_width=10, color=BLUE),
            Line(start=UP*1.5, end=DOWN*1.5, stroke_width=10, color=BLUE)
        ).move_to(shield)
        shield_group = VGroup(shield, shield_cross).move_to(ORIGIN)
        
        label_1 = Text("练好内功", font_size=32, color=YELLOW).next_to(shield_group, UP)
        label_2 = Text("立于不败", font_size=32, color=YELLOW).next_to(shield_group, DOWN)
        
        main_group = VGroup(label_1, shield_group, label_2).next_to(quote, DOWN, buff=1)
        
        timeline_steps = [
            (5, Write(p2_title)),
            (8, Write(quote)),
            (5, FadeIn(shield_group, shift=IN)),
            (5, FadeIn(label_1)),
            (5, FadeIn(label_2)),
            (5, Indicate(shield_group, color=WHITE)),
        ]
        
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)

        # =========================================================
        # 3. 在己 vs 在敌 (控制权)
        # =========================================================
        audio_file = audio_clips[2]
        page_duration = get_audio_duration(audio_file)
        
        p3_title = Text("赢的秘密：控制权", font=title_font, font_size=FONT_TITLE, color=GREEN).to_edge(UP, buff=2)
        
        # 左边：不可胜在己
        left_box = RoundedRectangle(width=3.5, height=5, color=BLUE, fill_opacity=0.1)
        l_title = Text("我不输", font_size=48, color=BLUE).next_to(left_box, UP)
        l_desc = Text("复习\n锻炼\n准备", font_size=36, color=WHITE, line_spacing=1.4).move_to(left_box).shift(UP*0.5)
        l_icon = Text("√", font_size=70, color=GREEN).next_to(l_desc, DOWN, buff=0.2) 
        l_tag = Text("归我管", font_size=32, color=YELLOW, background_stroke_color=BLACK).next_to(left_box, DOWN)
        left_group = VGroup(left_box, l_title, l_desc, l_icon, l_tag)
        
        # 右边：可胜在敌
        right_box = RoundedRectangle(width=3.5, height=5, color=RED, fill_opacity=0.1)
        r_title = Text("我不赢", font_size=48, color=RED).next_to(right_box, UP)
        r_desc = Text("对手犯错\n考卷简单\n运气好", font_size=36, color=WHITE, line_spacing=1.4).move_to(right_box).shift(UP*0.5)
        r_icon = Text("?", font_size=70, color=ORANGE).next_to(r_desc, DOWN, buff=0.2)
        r_tag = Text("看别人", font_size=32, color=GRAY, background_stroke_color=BLACK).next_to(right_box, DOWN)
        right_group = VGroup(right_box, r_title, r_desc, r_icon, r_tag)
        
        comp_group = VGroup(left_group, right_group).arrange(RIGHT, buff=0.6).next_to(p3_title, DOWN, buff=0.8)
        
        timeline_steps = [
            (5, Write(p3_title)),
            (10, FadeIn(left_group, shift=RIGHT)), # 讲“不可胜在己”
            (10, FadeIn(right_group, shift=LEFT)), # 讲“可胜在敌”
            (5, Indicate(l_tag)), # 强调“归我管”
        ]
        
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)

        # =========================================================
        # 4. 赢家心态 (胜兵先胜)
        # =========================================================
        audio_file = audio_clips[3]
        page_duration = get_audio_duration(audio_file)
        
        p4_title = Text("聪明人 vs 笨蛋", font=title_font, font_size=FONT_TITLE, color=PURPLE)
        
        # 聪明人流程
        arrow = Arrow(LEFT, RIGHT, color=YELLOW)
        step1 = Text("准备好了", color=GREEN, font_size=30)
        step2 = Text("去打仗", color=WHITE, font_size=30)
        smart_flow = VGroup(step1, arrow, step2).arrange(RIGHT)
        smart_label = Text("聪明人 (先胜)", color=GREEN, font_size=36)
        smart_block = VGroup(smart_label, smart_flow).arrange(DOWN, buff=0.5)
        
        # 笨蛋流程
        arrow2 = Arrow(LEFT, RIGHT, color=GRAY)
        step3 = Text("啥也没干", color=RED, font_size=30)
        step4 = Text("去打仗", color=WHITE, font_size=30)
        dumb_flow = VGroup(step3, arrow2, step4).arrange(RIGHT)
        dumb_label = Text("笨蛋 (碰运气)", color=RED, font_size=36)
        dumb_block = VGroup(dumb_label, dumb_flow).arrange(DOWN, buff=0.5)
        
        # 整体布局居中
        VGroup(p4_title, smart_block, dumb_block).arrange(DOWN, buff=1.5).move_to(ORIGIN)
        
        timeline_steps = [
            (5, Write(p4_title)),
            (8, FadeIn(smart_label)),
            (8, Write(smart_flow)),
            (8, FadeIn(dumb_label)),
            (8, Write(dumb_flow)),
            (5, Indicate(smart_label)),
        ]
        
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration, elapsed)
        self.wait(3.0)
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
        
        question = Text("明天要考试，怎么做才对？", font=body_font, font_size=36).next_to(q_header, DOWN, buff=0.8)
        
        options = [
            ("A. 偷看学霸答案", RED),
            ("B. 认真复习，弄懂错题", GREEN),
            ("C. 祈祷老师生病", GRAY),
        ]
        
        opt_group = VGroup()
        for text, color in options:
            box = RoundedRectangle(width=8, height=1.5, color=color, fill_opacity=0.1)
            txt = Text(text, font_size=32, color=WHITE).move_to(box)
            item = VGroup(box, txt)
            opt_group.add(item)
            
        opt_group.arrange(DOWN, buff=0.4).next_to(question, DOWN, buff=1.0)
        
        # 调整位置防溢出
        if opt_group.get_bottom()[1] < -SAFE_BOTTOM_BUFF:
             VGroup(q_header, question, opt_group).shift(UP * 0.5)

        cta_text = Text("评论区告诉我答案！", font_size=28, color=BLUE)
        cta = VGroup(Triangle(color=BLUE, fill_opacity=1).scale(0.15).rotate(PI), cta_text).arrange(RIGHT).to_edge(DOWN, buff=SAFE_BOTTOM_BUFF)
        
        timeline_steps = [
            (2, [GrowFromCenter(q_mark), FadeIn(q_bg, shift=UP), Write(q_text)]),
            (3, Write(question)),
            (5, GrowFromCenter(opt_group[0])),
            (5, GrowFromCenter(opt_group[1])),
            (5, GrowFromCenter(opt_group[2])),
            (5, Write(cta))
        ]
        
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration, elapsed)
        self.wait(2.0)

