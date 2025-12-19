import sys
import os
from manim import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from utils.anim_helper import get_audio_duration, combine_audio_clips, wait_until_audio_end

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
        TRANSITION_TIME = 0.2

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
        full_audio = combine_audio_clips(audio_clips, COMBINED_WAV, silence_duration=0.5)
        self.add_sound(full_audio)

        # =========================================================
        # 1. 封面：最好的胜利是不打架？
        # =========================================================
        audio_file = audio_clips[0]
        page_duration = get_audio_duration(audio_file)
        elapsed = 0
        
        title = Text("最好的胜利是不打架？", font=title_font, font_size=FONT_TITLE, weight=BOLD).shift(UP*2)
        subtitle = Text("—— 孙子兵法第三课：谋攻篇", font=title_font, font_size=FONT_BODY, color=BLUE)
        subtitle.next_to(title, DOWN, buff=1)
        
        # 图标：打架 vs 智慧 (使用纯文字避免渲染问题)
        icon_fight = Text("打架", font_size=60, color=RED, weight=BOLD)
        icon_brain = Text("智慧", font_size=60, color=BLUE, weight=BOLD)
        vs = Text("VS", font_size=48, color=GRAY, slant=ITALIC)
        icons = VGroup(icon_fight, vs, icon_brain).arrange(RIGHT, buff=0.8).next_to(subtitle, DOWN, buff=1.5)
        
        target = Text(
            "致：\n爱思考的你\n喜欢动脑筋的你\n",
            font=body_font, 
            font_size=FONT_SMALL, 
            color=GRAY,
            line_spacing=1.2
        ).to_edge(DOWN, buff=SAFE_BOTTOM_BUFF)

        t = 3.0; self.play(Write(title), run_time=t); elapsed += t
        t = 2.0; self.play(FadeIn(subtitle, shift=UP), run_time=t); elapsed += t
        t = 2.0; self.play(FadeIn(icons, shift=UP), run_time=t); elapsed += t
        t = 2.0; self.play(Write(target), run_time=t); elapsed += t
        
        wait_until_audio_end(self, page_duration, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)
        self.wait(0.3)

        # =========================================================
        # 2. 真正的赢家 (不战而屈人之兵)
        # =========================================================
        audio_file = audio_clips[1]
        page_duration = get_audio_duration(audio_file)
        elapsed = 0

        p2_title = Text("真正的赢家是谁？", font=title_font, font_size=FONT_TITLE, color=ORANGE).to_edge(UP, buff=2)
        
        quote = Text('“百战百胜，非善之善者也；\n不战而屈人之兵，善之善者也。”', font=body_font, font_size=FONT_BODY, slant=ITALIC, line_spacing=1.5).next_to(p2_title, DOWN, buff=1)
        
        # 对比框
        # 百战百胜
        box1 = RoundedRectangle(width=6, height=2, color=GRAY, fill_opacity=0.1)
        t1_text = Text("百战百胜 = 厉害", font_size=32, color=GRAY)
        t1_icon = Text("✔", font_size=32, color=GRAY, font="Arial") 
        txt1 = VGroup(t1_text, t1_icon).arrange(RIGHT).move_to(box1)
        group1 = VGroup(box1, txt1).next_to(quote, DOWN, buff=1)
        
        # 不战而屈人之兵
        box2 = RoundedRectangle(width=7, height=2.5, color=GOLD, fill_opacity=0.2)
        t2_text = Text("不战而胜 = 最棒", font_size=40, color=GOLD, weight=BOLD)
        t2_icon = Star(color=GOLD, fill_opacity=1).scale(0.3)
        txt2 = VGroup(t2_text, t2_icon).arrange(RIGHT).move_to(box2)
        group2 = VGroup(box2, txt2).next_to(group1, DOWN, buff=0.5)
        
        # 整体上移
        VGroup(p2_title, quote, group1, group2).move_to(ORIGIN).shift(UP * SAFE_CENTER_UP)

        t = 2.0; self.play(Write(p2_title), run_time=t); elapsed += t
        t = 6.0; self.play(Write(quote), run_time=t); elapsed += t
        t = 3.0; self.play(FadeIn(group1, shift=LEFT), run_time=t); elapsed += t
        t = 4.0; self.play(GrowFromCenter(group2), run_time=t); elapsed += t # 强调重点
        
        wait_until_audio_end(self, page_duration, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)
        self.wait(0.3)

        # =========================================================
        # 3. 解决问题的四个等级 (上兵伐谋...)
        # =========================================================
        audio_file = audio_clips[2]
        page_duration = get_audio_duration(audio_file)
        elapsed = 0

        p3_title = Text("解决问题的四个等级", font=title_font, font_size=FONT_TITLE, color=BLUE).to_edge(UP, buff=2)
        
        # 阶梯图数据 (从高到低)
        levels = [
            ("第一等：伐谋", "用脑子 (想办法)", GREEN),
            ("第二等：伐交", "动嘴巴 (找朋友)", TEAL),
            ("第三等：伐兵", "动手 (容易受伤)", ORANGE),
            ("最差等：攻城", "硬碰硬 (头破血流)", RED),
        ]
        
        level_group = VGroup()
        for i, (title_text, desc_text, color) in enumerate(levels):
            # 每一级稍微缩进一点，形成阶梯感
            indent = i * 0.5
            
            l_title = Text(title_text, font_size=32, color=color, weight=BOLD)
            l_desc = Text(desc_text, font_size=24, color=WHITE).next_to(l_title, DOWN, buff=0.2, aligned_edge=LEFT)
            
            # 装饰点
            dot = Dot(color=color).next_to(l_title, LEFT, buff=0.3)
            
            # 背景条
            bg = RoundedRectangle(width=6, height=1.8, color=color, fill_opacity=0.15)
            # 组合内容
            content = VGroup(dot, l_title, l_desc).move_to(bg)
            
            item = VGroup(bg, content).shift(RIGHT * indent)
            level_group.add(item)
            
        level_group.arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(p3_title, DOWN, buff=0.8)
        # 整体居中
        VGroup(p3_title, level_group).move_to(ORIGIN).shift(UP * SAFE_CENTER_UP)

        t = 2.0; self.play(Write(p3_title), run_time=t); elapsed += t
        
        # 逐个显示
        # 自动计算时间分配
        available_time = page_duration - elapsed - 2.0
        avg_time = available_time / 4
        
        for item in level_group:
            self.play(FadeIn(item, shift=DOWN * 0.5), run_time=0.8)
            # 剩余时间 wait
            self.wait(max(0.2, avg_time - 0.8))
            elapsed += avg_time

        wait_until_audio_end(self, page_duration, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)
        self.wait(0.3)

        # =========================================================
        # 4. 胜利的数学题 (知彼知己)
        # =========================================================
        audio_file = audio_clips[3]
        page_duration = get_audio_duration(audio_file)
        elapsed = 0

        p4_title = Text("胜利的数学题", font=title_font, font_size=FONT_TITLE, color=PURPLE).to_edge(UP, buff=2)
        
        # 金句
        golden_sentence = Text("“知彼知己，百战不殆”", font_size=48, color=YELLOW).next_to(p4_title, DOWN, buff=0.8)
        
        # 三种情况
        # 1. 赢 (全知)
        eq1 = VGroup(
            Text("知彼 + 知己", font_size=30, color=GREEN),
            Text("=", font_size=30),
            Text("百战不殆 (赢)", font_size=30, color=GREEN, weight=BOLD)
        ).arrange(RIGHT)
        
        # 2. 半赢 (不知彼)
        eq2 = VGroup(
            Text("不知彼 + 知己", font_size=30, color=YELLOW),
            Text("=", font_size=30),
            Text("一胜一负 (一半)", font_size=30, color=YELLOW)
        ).arrange(RIGHT)
        
        # 3. 输 (全不知)
        eq3 = VGroup(
            Text("不知彼 + 不知己", font_size=30, color=RED),
            Text("=", font_size=30),
            Text("每战必殆 (输)", font_size=30, color=RED, weight=BOLD)
        ).arrange(RIGHT)
        
        equations = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.8, aligned_edge=LEFT).next_to(golden_sentence, DOWN, buff=1.0)
        
        # 整体居中
        VGroup(p4_title, golden_sentence, equations).move_to(ORIGIN).shift(UP * SAFE_CENTER_UP)

        t = 3.0; self.play(Write(p4_title), run_time=t); elapsed += t
        t = 4.0; self.play(Write(golden_sentence), run_time=t); elapsed += t
        t = 3.0; self.play(Indicate(golden_sentence), run_time=t); elapsed += t # 解释意思
        
        # 三个公式逐个出
        t = 3.0; self.play(FadeIn(eq1, shift=RIGHT), run_time=t); elapsed += t
        t = 3.0; self.play(FadeIn(eq2, shift=RIGHT), run_time=t); elapsed += t
        t = 3.0; self.play(FadeIn(eq3, shift=RIGHT), run_time=t); elapsed += t

        wait_until_audio_end(self, page_duration, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)
        self.wait(0.3)

        # =========================================================
        # 5. 结尾互动：思考题
        # =========================================================
        audio_file = audio_clips[4]
        page_duration = get_audio_duration(audio_file)
        elapsed = 0

        # 视觉优化：带图标的标题
        # 大问号
        q_mark = Text("?", font_size=100, color=YELLOW, weight=BOLD)
        # 标题文字
        q_text = Text("小武思考时间", font=title_font, font_size=40, color=WHITE)
        # 背景框
        q_bg = RoundedRectangle(width=5, height=1.2, corner_radius=0.6, color=BLUE, fill_opacity=0.8)
        
        # 组合：问号在上面，标题在下面
        q_header = VGroup(q_mark, VGroup(q_bg, q_text)).arrange(DOWN, buff=0.3).to_edge(UP, buff=1.0)

        question = Text("如果同学给你起外号，怎么办？", font=body_font, font_size=36).next_to(q_header, DOWN, buff=0.8)

        # 选项
        options = [
            ("A. 骂回去，打一架！", RED),
            ("B. 生闷气，哭鼻子。", GRAY),
            ("C. 动脑筋，让他闭嘴。", GREEN),
        ]
        
        opt_group = VGroup()
        for text, color in options:
            box = RoundedRectangle(width=8, height=1.5, color=color, fill_opacity=0.1)
            txt = Text(text, font_size=32, color=WHITE).move_to(box)
            item = VGroup(box, txt)
            opt_group.add(item)
            
        opt_group.arrange(DOWN, buff=0.4).next_to(question, DOWN, buff=1.0)
        
        # 整体居中微调
        # 如果太靠下，整体上移
        if opt_group.get_bottom()[1] < -5:
             VGroup(q_header, question, opt_group).shift(UP * 0.5)

        # CTA: 文字 + 箭头
        cta_text = Text("在评论区告诉小武你的选择！", font_size=28, color=BLUE)
        cta_arrow = Triangle(color=BLUE, fill_opacity=1).scale(0.15).rotate(PI)
        cta = VGroup(cta_arrow, cta_text).arrange(RIGHT).to_edge(DOWN, buff=SAFE_BOTTOM_BUFF)

        # 动画 - 标题与问题 (压缩时长)
        # 并行播放：问号生长 + 背景/标题出现
        self.play(
            GrowFromCenter(q_mark),
            FadeIn(q_bg, shift=UP), 
            Write(q_text), 
            run_time=0.8
        )
        elapsed += 0.8
        
        # 问号摇摆 (缩短)
        self.play(Wiggle(q_mark, scale_value=1.2, rotation_angle=0.1 * TAU), run_time=0.5)
        elapsed += 0.5
        
        # 问题文字 (缩短)
        t = 1.2; self.play(Write(question), run_time=t); elapsed += t
        
        # 选项逐个出现 - 紧凑节奏
        # 不再平均分配剩余时间，防止因为剩余时间过长导致选项动画拖沓
        # 强制每个选项在 2.5s 内完成 (1.5s 动画 + 1.0s 等待)
        # 这样 3 个选项总共 7.5s
        
        fixed_anim_time = 1.5
        fixed_wait_time = 1.0
        
        for opt in opt_group:
            self.play(GrowFromCenter(opt), run_time=fixed_anim_time)
            self.wait(fixed_wait_time)
            elapsed += (fixed_anim_time + fixed_wait_time)

        # CTA
        # 剩下的时间全部留给 CTA
        remaining = max(1.0, page_duration - elapsed)
        # CTA 动画本身给 1.0s，剩下的时间 wait
        self.play(Write(cta), run_time=1.0)
        elapsed += 1.0
        
        wait_until_audio_end(self, page_duration, elapsed)
        self.wait(2.0)

