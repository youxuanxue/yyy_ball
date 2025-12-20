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
config.media_dir = "media/sunzi/lesson05"

# 路径
VOICE_DIR = "media/sunzi/lesson05/voice"
COMBINED_WAV = os.path.join(VOICE_DIR, "lesson5_full.wav")

class Lesson5Vertical(Scene):
    def construct(self):
        # 字体与样式
        title_font = "PingFang SC" 
        body_font = "PingFang SC"
        FONT_TITLE = 48
        FONT_BODY = 32
        FONT_SMALL = 24
        SAFE_BOTTOM_BUFF = 3.5
        TRANSITION_TIME = 0.5

        # ---------------------------------------------------------
        # 0. 插入封面首帧 (Cover Frame)
        # ---------------------------------------------------------
        cover_path = "media/sunzi/lesson05/images/cover_design.png"
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
            os.path.join(VOICE_DIR, "02_orange.mp3"),
            os.path.join(VOICE_DIR, "03_quilts.mp3"),
            os.path.join(VOICE_DIR, "04_magic.mp3"),
            os.path.join(VOICE_DIR, "05_ending.mp3"),
        ]
        
        bgm_file = "assets/bgm/smart_thinking.wav"
        
        full_audio = combine_audio_clips(
            audio_clips, 
            os.path.join(VOICE_DIR, "lesson5_full.wav"), 
            silence_duration=0,
            bgm_file=bgm_file,
            bgm_volume=-15,
            bgm_loop=True
        )
        self.add_sound(full_audio)

        # =========================================================
        # 1. 封面：谁是战场魔术师？
        # =========================================================
        audio_file = audio_clips[0]
        page_duration = get_audio_duration(audio_file)
        
        title = Text("谁是战场魔术师？", font=title_font, font_size=FONT_TITLE, weight=BOLD).shift(UP*2)
        subtitle = Text("—— 孙子兵法第五课：兵势篇", font=title_font, font_size=FONT_BODY, color=BLUE)
        subtitle.next_to(title, DOWN, buff=1)
        
        # 图标：魔术帽/魔杖
        hat = Polygon(
            [-1, 0, 0], [1, 0, 0], [1, 1, 0], [0.8, 1, 0], [0.8, 2.5, 0], [-0.8, 2.5, 0], [-0.8, 1, 0], [-1, 1, 0],
            color=PURPLE, fill_opacity=1
        ).move_to(ORIGIN)
        wand = Line(start=[-1.5, -0.5, 0], end=[-0.5, 0.5, 0], color=WHITE, stroke_width=8)
        tip = Star(color=YELLOW, fill_opacity=1).scale(0.3).move_to(wand.get_end())
        magic_group = VGroup(hat, wand, tip).next_to(subtitle, DOWN, buff=0.8)
        
        timeline_steps = [
            (5, Write(title)),
            (5, FadeIn(subtitle, shift=UP)),
            (8, GrowFromCenter(magic_group)),
            (5, Wiggle(magic_group)), 
        ]
        
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration - TRANSITION_TIME, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)

        # =========================================================
        # 2. 橘子与橙汁 (形与势)
        # =========================================================
        audio_file = audio_clips[1]
        page_duration = get_audio_duration(audio_file)
        
        p2_title = Text("形 vs 势", font=title_font, font_size=FONT_TITLE, color=ORANGE).to_edge(UP, buff=2)
        
        # 左边：橘子 (形)
        orange = Circle(radius=1.2, color=ORANGE, fill_opacity=1)
        # 优化叶子：加个梗，叶子旋转一下
        stem = Line(start=orange.get_top(), end=orange.get_top() + UP*0.3, color=GREEN, stroke_width=8)
        leaf = Ellipse(width=0.8, height=0.4, color=GREEN, fill_opacity=1)
        leaf.move_to(stem.get_end() + RIGHT*0.2).rotate(-PI/6)
        orange_group = VGroup(orange, stem, leaf)
        orange_label = Text("形：橘子 (静止)", font_size=28).next_to(orange_group, DOWN)
        left_group = VGroup(orange_group, orange_label).shift(LEFT*2)

        # 右边：橙汁 (势)
        cup = VGroup(
            Line(start=[-0.8, 1.5, 0], end=[-0.6, -1.5, 0]),
            Line(start=[-0.6, -1.5, 0], end=[0.6, -1.5, 0]),
            Line(start=[0.6, -1.5, 0], end=[0.8, 1.5, 0])
        ).set_color(WHITE).set_z_index(1) # 提高层级

        juice = Polygon(
            [-0.75, 1.2, 0], [0.75, 1.2, 0], [0.6, -1.45, 0], [-0.6, -1.45, 0],
            color=ORANGE, fill_opacity=0.8
        )
        # 调整VGroup顺序虽然有效，但显示设置z_index更保险
        juice_group = VGroup(juice, cup)
        juice_label = Text("势：橙汁 (好喝)", font_size=28).next_to(juice_group, DOWN)
        right_group = VGroup(juice_group, juice_label).shift(RIGHT*2)

        arrow = CurvedArrow(
            start_point=left_group.get_right() + RIGHT*0.2, 
            end_point=right_group.get_left() + LEFT*0.2, 
            angle=-TAU/8, 
            color=YELLOW,
            stroke_width=6
        )
        action_text = Text("动脑筋", font_size=32, color=YELLOW).next_to(arrow, UP, buff=0.2)

        # all_group 只是用来定位吗？这里其实不需要把它们打组 move_to ORIGIN，因为已经是左右对称布局了
        # 如果非要打组，CurvedArrow 可能会影响包围盒计算，导致整体偏移
        # 保持原位即可，不需要 all_group.move_to(ORIGIN)

        timeline_steps = [
            (5, Write(p2_title)),
            (5, FadeIn(left_group, shift=RIGHT)),
            (8, Create(arrow)),
            (5, FadeIn(action_text, shift=UP)),
            (8, FadeIn(right_group, shift=LEFT)),
            (5, Wiggle(right_group)),
        ]
        
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration - TRANSITION_TIME, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)

        # =========================================================
        # 3. 叠被子的秘密 (治众如治寡)
        # =========================================================
        audio_file = audio_clips[2]
        page_duration = get_audio_duration(audio_file)
        
        p3_title = Text("治众如治寡", font=title_font, font_size=FONT_TITLE, color=BLUE).to_edge(UP, buff=2)
        quote = Text('“管很多人像管一个人”', font=body_font, font_size=FONT_BODY).next_to(p3_title, DOWN, buff=0.5)

        # 画面：方块阵列 (像豆腐块被子，也像士兵)
        squares = VGroup()
        for i in range(3):
            for j in range(3):
                sq = Square(side_length=1.5, color=BLUE, fill_opacity=0.5)
                sq.move_to([(i-1)*1.8, (j-1)*1.8, 0])
                squares.add(sq)
        
        squares.move_to(ORIGIN).shift(DOWN*0.5)
        
        label = Text("标准统一 = 好指挥", font_size=36, color=YELLOW).next_to(squares, UP, buff=0.5)

        timeline_steps = [
            (5, Write(p3_title)),
            (5, Write(quote)),
            (10, LaggedStart(*[GrowFromCenter(s) for s in squares], lag_ratio=0.1)),
            (5, Write(label)),
            (5, squares.animate.arrange_in_grid(rows=1, buff=0.2)), # 变换队形
        ]
        
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration - TRANSITION_TIME, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)

        # =========================================================
        # 4. 战场魔术师 (奇正相生)
        # =========================================================
        audio_file = audio_clips[3]
        page_duration = get_audio_duration(audio_file)
        
        p4_title = Text("奇正相生", font=title_font, font_size=FONT_TITLE, color=PURPLE).to_edge(UP, buff=2)

        # 正：方阵
        zheng_box = Square(side_length=3, color=BLUE, fill_opacity=0.5)
        zheng_text = Text("正 (正面迎战)", font_size=32).move_to(zheng_box)
        zheng_group = VGroup(zheng_box, zheng_text).move_to(ORIGIN)

        # 奇：箭头绕后
        qi_arrow = CurvedArrow(start_point=LEFT*3, end_point=UP*2, angle=-TAU/4, color=RED)
        qi_text = Text("奇 (出其不意)", font_size=32, color=RED).next_to(qi_arrow, UP)
        
        timeline_steps = [
            (5, Write(p4_title)),
            (8, FadeIn(zheng_group)),
            (8, Create(qi_arrow)),
            (5, Write(qi_text)),
            (5, Rotate(zheng_group, angle=PI/4)), # 变化
        ]
        
        elapsed = play_timeline(self, page_duration, timeline_steps)
        wait_until_audio_end(self, page_duration - TRANSITION_TIME, elapsed)
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
        
        question = Text("班长想让大家都听指挥，怎么做？", font=body_font, font_size=32).next_to(q_header, DOWN, buff=0.8)
        
        options = [
            ("A. 随心所欲，开心就好", RED),
            ("B. 制定规则，整齐划一", GREEN),
            ("C. 只管好朋友", GRAY),
        ]
        
        opt_group = VGroup()
        for text, color in options:
            box = RoundedRectangle(width=8, height=1.5, color=color, fill_opacity=0.1)
            txt = Text(text, font_size=28, color=WHITE).move_to(box)
            item = VGroup(box, txt)
            opt_group.add(item)
            
        opt_group.arrange(DOWN, buff=0.4).next_to(question, DOWN, buff=0.8)
        
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

    def tear_down(self):
        """
        Manim 的生命周期钩子：渲染结束后调用。
        检查生成的视频是否包含音频，如果缺失则自动合并。
        """
        super().tear_down()
        
        # 1. 获取 Manim 自动生成的视频路径
        # self.renderer.file_writer.movie_file_path 是绝对路径
        if self.renderer and self.renderer.file_writer:
            video_path = self.renderer.file_writer.movie_file_path
            
            # 2. 获取我们合成的完整音频路径
            # 注意：这里需要重新构建路径，或者从外部获取 COMBINED_WAV
            # 由于 COMBINED_WAV 是全局变量，这里直接使用
            audio_path = os.path.join(os.getcwd(), COMBINED_WAV)
            
            # 3. 尝试合并
            if video_path and os.path.exists(video_path):
                from utils.anim_helper import merge_audio_video_if_needed
                print(f"Checking audio for: {video_path}")
                merge_audio_video_if_needed(video_path, audio_path)

