import sys
import os
from manim import *

# 将项目根目录加入 path，以便导入 utils
# 假设我们在项目根目录运行 manim，或者在脚本所在目录运行
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from utils.anim_helper import get_audio_duration, combine_audio_clips, wait_until_audio_end

# 配置竖屏 9:16
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

# 强制设置 Manim 输出目录
# 最终视频将生成在: media/sunzi/lesson02/videos/1920p60/Lesson2Vertical.mp4
config.media_dir = "media/sunzi/lesson02"

# 音频目录 (需与 gen_voice.py 对应)
VOICE_DIR = "media/sunzi/lesson02/voice"
COMBINED_WAV = os.path.join(VOICE_DIR, "lesson2_full.wav")

class Lesson2Vertical(Scene):
    def construct(self):
        # 字体配置
        title_font = "PingFang SC" 
        body_font = "PingFang SC"
        
        FONT_TITLE = 48
        FONT_BODY = 32
        FONT_SMALL = 24

        # 竖屏底部安全区
        SAFE_BOTTOM_BUFF = 4.0
        SAFE_CENTER_UP = 0.6
        
        # 页面停留缓冲（音频讲完后停留多久）
        PAGE_WAIT_BUFFER = 1.0 
        # 转场耗时
        TRANSITION_TIME = 0.2

        # ---------------------------------------------------------
        # 全局：只 add_sound 一次
        # ---------------------------------------------------------
        # 即使这里是 lesson02，我们也可以指定音频文件列表
        audio_clips = [
            os.path.join(VOICE_DIR, "01_cover.mp3"),
            os.path.join(VOICE_DIR, "02_formula.mp3"),
            os.path.join(VOICE_DIR, "03_five_gems.mp3"),
            os.path.join(VOICE_DIR, "04_seven_pk.mp3"),
            os.path.join(VOICE_DIR, "05_calculate.mp3"),
            os.path.join(VOICE_DIR, "06_ending.mp3"),
        ]
        
        full_audio = combine_audio_clips(audio_clips, COMBINED_WAV, silence_duration=0)
        self.add_sound(full_audio)

        # =========================================================
        # 1. 封面
        # =========================================================
        audio_file = audio_clips[0]
        page_duration = get_audio_duration(audio_file)
        elapsed = 0
        
        title = Text("谁是最后的赢家？", font=title_font, font_size=FONT_TITLE+10, weight=BOLD).shift(UP*2)
        subtitle = Text("—— 孙子兵法第二课：胜利大模型", font=title_font, font_size=FONT_BODY, color=BLUE)
        subtitle.next_to(title, DOWN, buff=1)
        
        icon = Star(color=YELLOW, fill_opacity=1).scale(1.0).next_to(subtitle, DOWN, buff=0.5)
        
        target = Text(
            "致：\n爱思考的你\n喜欢动脑筋的你\n",
            font=body_font, 
            font_size=FONT_SMALL, 
            color=GRAY,
            line_spacing=1.2
        ).to_edge(DOWN, buff=SAFE_BOTTOM_BUFF)

        # 动画编排 (精确卡点 + 自动计时)
        t = 3.0; self.play(Write(title), run_time=t); elapsed += t
        t = 2.0; self.play(FadeIn(subtitle, shift=UP), run_time=t); elapsed += t
        
        t = 2.0; self.play(GrowFromCenter(icon), run_time=t); elapsed += t
        t = 1.0; self.play(Indicate(icon, color=YELLOW), run_time=t); elapsed += t
        
        t = 2.0; self.play(Write(target), run_time=t); elapsed += t
        
        # 自动对齐：强制等到音频结束
        wait_until_audio_end(self, page_duration, elapsed)
        
        # 转场 (转场时间不计入上一页音频时间，而是算作间隔)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)

        # =========================================================
        # 2. 赢家是有公式的
        # =========================================================
        audio_file = audio_clips[1]
        page_duration = get_audio_duration(audio_file)
        elapsed = 0

        p2_title = Text("赢家是有公式的！", font=title_font, font_size=FONT_TITLE, color=ORANGE).to_edge(UP, buff=2)
        quote = Text('“经之以五事，校之以计...知之者胜。”', font=body_font, font_size=FONT_BODY, slant=ITALIC).next_to(p2_title, DOWN, buff=1)
        
        formula_text = Text("胜利公式：五事 + 七计", font=title_font, font_size=48, color=YELLOW)
        formula_box = RoundedRectangle(width=8.5, height=2.5, corner_radius=0.5, color=YELLOW, fill_opacity=0.2)
        formula_group = VGroup(formula_box, formula_text).next_to(quote, DOWN, buff=1.0)

        desc = Text("不用打仗，也能大概知道谁会赢！", font=body_font, font_size=FONT_BODY, color=BLUE).next_to(formula_group, DOWN, buff=0.8)
        exam = Text("就像考试前：复习得好，\n就能猜到自己能考100分！", font=body_font, font_size=FONT_SMALL, color=GRAY, line_spacing=1.2).next_to(desc, DOWN, buff=0.6)

        t = 3.0; self.play(Write(p2_title), run_time=t); elapsed += t
        t = 4.0; self.play(Write(quote), run_time=t); elapsed += t
        t = 1.0; self.wait(t); elapsed += t

        t = 3.0; self.play(FadeIn(formula_box), Write(formula_text), run_time=t); elapsed += t
        t = 2.0; self.play(Indicate(formula_text), run_time=t); elapsed += t
        
        t = 3.0; self.play(FadeIn(desc, shift=UP), run_time=t); elapsed += t
        t = 2.0; self.wait(t); elapsed += t

        t = 4.0; self.play(FadeIn(exam, shift=UP), run_time=t); elapsed += t
        
        wait_until_audio_end(self, page_duration, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)
        # =========================================================
        # 3. 胜利第一招：五颗宝石
        # =========================================================
        audio_file = audio_clips[2]
        page_duration = get_audio_duration(audio_file)
        elapsed = 0

        p3_title = Text("第一招：集齐“五颗宝石”", font=title_font, font_size=FONT_TITLE, color=PURPLE).to_edge(UP, buff=2)
        p3_tip = Text("看看自己手里有没有这五样宝贝：", font=body_font, font_size=FONT_SMALL, color=GRAY).next_to(p3_title, DOWN, buff=0.6)
        
        gems_data = [
            ("道", "大家一条心", RED),
            ("天", "时机对不对", ORANGE),
            ("地", "地盘熟不熟", GREEN),
            ("将", "队长牛不牛", BLUE),
            ("法", "纪律严不严", GOLD),
        ]
        
        gems_group = VGroup()
        for i, (char, text, color) in enumerate(gems_data):
            dot = Circle(radius=0.4, color=color, fill_opacity=0.8)
            char_text = Text(char, font_size=32, color=WHITE).move_to(dot)
            icon = VGroup(dot, char_text)
            desc = Text(text, font=body_font, font_size=28, color=color)
            row = VGroup(icon, desc).arrange(RIGHT, buff=0.4)
            bg = RoundedRectangle(width=7, height=1.0, corner_radius=0.5, color=color, fill_opacity=0.1, stroke_width=0)
            row_group = VGroup(bg, row)
            gems_group.add(row_group)
            
        gems_group.arrange(DOWN, buff=0.25).next_to(p3_tip, DOWN, buff=0.6)
        main_group = VGroup(p3_title, p3_tip, gems_group).move_to(ORIGIN).shift(UP * SAFE_CENTER_UP)

        t = 4.0; self.play(FadeIn(p3_title), run_time=t); elapsed += t
        t = 4.0; self.play(FadeIn(p3_tip), run_time=t); elapsed += t

        # 自动计算每颗宝石的展示时间
        available_time = page_duration - elapsed - 1.5 # 留1.5s缓冲
        # 确保每条至少有 3.0s (防止计算过短)
        if available_time < len(gems_data) * 3.0:
            available_time = len(gems_data) * 3.5
            
        avg_time = available_time / len(gems_data)

        for i, item in enumerate(gems_group):
            # 出现动作 0.8s
            t_anim = 1.5
            self.play(FadeIn(item, shift=LEFT), run_time=t_anim)
            
            # 强调动作 1.0s
            t_indicate = 1.0
            self.play(Indicate(item), run_time=t_indicate)
            
            # 剩余时间 wait
            t_wait = max(0.2, avg_time - t_anim - t_indicate)
            self.wait(t_wait)
            
            elapsed += (t_anim + t_indicate + t_wait)

        wait_until_audio_end(self, page_duration, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)
        self.wait(4.0)

        # =========================================================
        # 4. 胜利第二招：七个PK
        # =========================================================
        audio_file = audio_clips[3]
        page_duration = get_audio_duration(audio_file)
        elapsed = 0

        p4_title = Text("第二招：七个 PK 大战", font=title_font, font_size=FONT_TITLE, color=RED).to_edge(UP, buff=2)
        p4_tip = Text("光看自己还不够，还要和对手比一比！", font=body_font, font_size=FONT_SMALL, color=GRAY).next_to(p4_title, DOWN, buff=0.6)
        
        pk_texts = [
            ("PK 1", "谁更得人心？"),
            ("PK 2", "谁的队长更厉害？"),
            ("PK 3", "谁占了天时地利？"),
            ("PK 4", "谁的队伍更听话？"),
            ("PK 5", "谁的装备更好？"),
            ("PK 6", "谁训练得更棒？"),
            ("PK 7", "谁奖罚更公平？"),
        ]
        
        pk_group = VGroup()
        for label, content in pk_texts:
            l = Text(label, font=body_font, font_size=24, color=YELLOW, weight=BOLD)
            c = Text(content, font=body_font, font_size=24, color=WHITE)
            line = VGroup(l, c).arrange(RIGHT, buff=0.3)
            pk_group.add(line)
            
        pk_group.arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(p4_tip, DOWN, buff=0.8)
        VGroup(p4_title, p4_tip, pk_group).move_to(ORIGIN).shift(UP * SAFE_CENTER_UP)

        t = 4.0; self.play(Write(p4_title), run_time=t); elapsed += t
        t = 4.0; self.play(FadeIn(p4_tip), run_time=t); elapsed += t

        # 改为固定节奏，防止动画过快
        fixed_anim = 1.0
        fixed_wait = 3.5
        
        for i, pk in enumerate(pk_group):
            self.play(FadeIn(pk, shift=UP * 0.2), run_time=fixed_anim)
            self.wait(fixed_wait)
            elapsed += (fixed_anim + fixed_wait)

        wait_until_audio_end(self, page_duration, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)

        # =========================================================
        # 5. 算得准，才能赢
        # =========================================================
        audio_file = audio_clips[4]
        page_duration = get_audio_duration(audio_file)
        elapsed = 0

        p5_title = Text("算得准，才能赢！", font=title_font, font_size=FONT_TITLE).to_edge(UP, buff=2)
        quote2 = Text('“多算胜，少算不胜。”', font=body_font, font_size=FONT_BODY, slant=ITALIC, color=YELLOW).next_to(p5_title, DOWN, buff=0.8)
        
        # 左：胜 (减小高度，避免撞到底部)
        left_bg = RoundedRectangle(width=3.5, height=3.5, color=RED, fill_opacity=0.2)
        l_icon = Text("宝石 x5", font_size=36, color=RED).move_to(left_bg).shift(UP*0.5)
        l_txt = Text("多算\n(准备足)", font_size=24, color=RED).next_to(l_icon, DOWN)
        l_res = Text("胜！", font_size=48, color=RED, weight=BOLD).next_to(left_bg, UP)
        left_group = VGroup(left_bg, l_icon, l_txt, l_res)

        # 右：输 (减小高度)
        right_bg = RoundedRectangle(width=3.5, height=3.5, color=GRAY, fill_opacity=0.2)
        r_icon = Text("宝石 x0", font_size=36, color=GRAY).move_to(right_bg).shift(UP*0.5)
        r_txt = Text("少算\n(没准备)", font_size=24, color=GRAY).next_to(r_icon, DOWN)
        r_res = Text("输...", font_size=48, color=GRAY).next_to(right_bg, UP)
        right_group = VGroup(right_bg, r_icon, r_txt, r_res)
        
        # 重新编排位置：把 buff 从 1.5 减到 1.0，紧凑一点
        cards_group = VGroup(left_group, right_group).arrange(RIGHT, buff=1.0).next_to(quote2, DOWN, buff=1.0)
        
        # 整体居中偏上 (再往上提一点，UP * 0.5 -> UP * 1.0)
        main_group = VGroup(p5_title, quote2, cards_group).move_to(ORIGIN).shift(UP * 1.0)

        tips = Text("锦囊：算不赢，赶快去准备！", font=body_font, font_size=32, color=YELLOW).to_edge(DOWN, buff=SAFE_BOTTOM_BUFF)

        t = 3.0; self.play(FadeIn(p5_title), run_time=t); elapsed += t
        t = 4.0; self.play(Write(quote2), run_time=t); elapsed += t
        t = 2.0; self.wait(t); elapsed += t

        t = 3.0; self.play(FadeIn(left_group, shift=RIGHT), run_time=t); elapsed += t
        t = 3.0; self.play(FadeIn(right_group, shift=LEFT), run_time=t); elapsed += t
        
        t = 3.0; self.wait(t); elapsed += t
        t = 4.0; self.play(Write(tips), run_time=t); elapsed += t
        t = 2.0; self.play(Indicate(tips), run_time=t); elapsed += t

        wait_until_audio_end(self, page_duration, elapsed)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=TRANSITION_TIME)
        self.wait(4)

        # =========================================================
        # 6. 结尾互动：思考题
        # =========================================================
        audio_file = audio_clips[5]
        page_duration = get_audio_duration(audio_file)
        elapsed = 0

        # 视觉优化：带图标的标题
        q_mark = Text("?", font_size=100, color=YELLOW, weight=BOLD)
        q_text = Text("小武思考时间", font=title_font, font_size=40, color=WHITE)
        q_bg = RoundedRectangle(width=5, height=1.2, corner_radius=0.6, color=BLUE, fill_opacity=0.8)
        q_header = VGroup(q_mark, VGroup(q_bg, q_text)).arrange(DOWN, buff=0.3).to_edge(UP, buff=1.0)

        question = Text("跳绳比赛怎么赢？", font=body_font, font_size=36).next_to(q_header, DOWN, buff=0.8)

        # 选项
        options = [
            ("A. 不管三七二十一，拼命跳！", RED),
            ("B. 查绳子、看天气、多练习。", GREEN),
            ("C. 祈求老天保佑。", GRAY),
        ]
        
        opt_group = VGroup()
        for text, color in options:
            box = RoundedRectangle(width=8, height=1.5, color=color, fill_opacity=0.1)
            txt = Text(text, font_size=32, color=WHITE).move_to(box)
            item = VGroup(box, txt)
            opt_group.add(item)
            
        opt_group.arrange(DOWN, buff=0.4).next_to(question, DOWN, buff=1.0)
        
        # 整体居中微调
        if opt_group.get_bottom()[1] < -5:
             VGroup(q_header, question, opt_group).shift(UP * 0.5)

        # CTA: 文字 + 箭头
        cta_text = Text("在评论区告诉小武你的选择！", font_size=28, color=BLUE)
        cta_arrow = Triangle(color=BLUE, fill_opacity=1).scale(0.15).rotate(PI)
        cta = VGroup(cta_arrow, cta_text).arrange(RIGHT).to_edge(DOWN, buff=SAFE_BOTTOM_BUFF)

        # 动画 - 标题与问题 (压缩时长 2.5s)
        self.play(
            GrowFromCenter(q_mark),
            FadeIn(q_bg, shift=UP), 
            Write(q_text), 
            run_time=0.8
        )
        elapsed += 0.8
        
        self.play(Wiggle(q_mark, scale_value=1.2, rotation_angle=0.1 * TAU), run_time=0.5)
        elapsed += 0.5
        
        t = 4; self.play(Write(question), run_time=t); elapsed += t
        
        # 选项逐个出现 - 紧凑节奏 (2.5s per item)
        fixed_anim_time = 2.5
        fixed_wait_time = 1.0
        
        for opt in opt_group:
            self.play(GrowFromCenter(opt), run_time=fixed_anim_time)
            self.wait(fixed_wait_time)
            elapsed += (fixed_anim_time + fixed_wait_time)

        # CTA
        self.play(Write(cta), run_time=1.0)
        elapsed += 1.0
        
        wait_until_audio_end(self, page_duration, elapsed)
        self.wait(2.0)

