import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson035VerticalScenes(Zsxq100keLessonVertical):
    """
    第035课：从种子到上市
    主题：一家公司的融资全景
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：A轮B轮你知道啥意思吗？

        口播稿关键词/短语：
        - "招聘网站A轮B轮" -> briefcase 图标
        - "搞不清楚" -> question_mark 图标
        - "一次讲明白" -> GOLD 吸引

        动态标题：「A轮B轮啥意思？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、招聘现象、搞不清楚、今天讲明白、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "A轮B轮啥意思？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 招聘现象
        brief_icon = self.load_png_icon("briefcase", height=1.5).move_to(UP * 1.8)
        job_text = Text(
            "招聘网站写着A轮、B轮、C轮",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).next_to(brief_icon, DOWN, buff=0.3)
        job_group = Group(brief_icon, job_text)

        # 3. 搞不清楚
        q_icon = self.load_png_icon("question_mark", height=1.2).move_to(DOWN * 0.5)
        confused = Text(
            "大多数人完全搞不清楚",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).next_to(q_icon, DOWN, buff=0.3)
        confused_group = Group(q_icon, confused)

        # 4. 底部承诺
        promise = Text(
            "今天一次给你讲明白",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(job_group, shift=UP), run_time=step_time)
        self.play(FadeIn(confused_group, shift=UP), run_time=step_time)
        self.play(Write(promise), run_time=step_time)
        self.play(Circumscribe(promise, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：三阶段融资路径

        口播稿关键词/短语：
        - "早期：种子/天使/A轮" -> small_business 图标
        - "中期：B轮/C轮" -> company 图标
        - "后期：IPO" -> business_building 图标

        动态标题：「融资三大阶段」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、早期、中期、后期、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "融资三大阶段",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 早期
        early_icon = self.load_png_icon("small_business", height=1.0).move_to(LEFT * 2.5 + UP * 2.0)
        early_label = Text("早期", font=self.title_font, font_size=self.font_title_size, color=BLUE).next_to(early_icon, DOWN, buff=0.2)
        early_desc = Text("种子·天使·A轮", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(early_label, DOWN, buff=0.1)
        early_amount = Text("几万~1亿", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(early_desc, DOWN, buff=0.1)
        early_group = Group(early_icon, early_label, early_desc, early_amount)

        # 3. 中期
        mid_icon = self.load_png_icon("company", height=1.0).move_to(UP * 2.0)
        mid_label = Text("中期", font=self.title_font, font_size=self.font_title_size, color=GREEN).next_to(mid_icon, DOWN, buff=0.2)
        mid_desc = Text("B轮·C轮", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(mid_label, DOWN, buff=0.1)
        mid_amount = Text("1亿~10亿", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(mid_desc, DOWN, buff=0.1)
        mid_group = Group(mid_icon, mid_label, mid_desc, mid_amount)

        # 4. 后期
        late_icon = self.load_png_icon("business_building", height=1.0).move_to(RIGHT * 2.5 + UP * 2.0)
        late_label = Text("后期", font=self.title_font, font_size=self.font_title_size, color=GOLD).next_to(late_icon, DOWN, buff=0.2)
        late_desc = Text("IPO上市", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(late_label, DOWN, buff=0.1)
        late_amount = Text("20亿起", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(late_desc, DOWN, buff=0.1)
        late_group = Group(late_icon, late_label, late_desc, late_amount)

        # 5. 底部
        summary = Text(
            "从想法到敲钟的全过程",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(early_group, shift=UP), run_time=step_time)
        self.play(FadeIn(mid_group, shift=UP), run_time=step_time)
        self.play(FadeIn(late_group, shift=UP), run_time=step_time)
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：每轮都是生死考验

        口播稿关键词/短语：
        - "十个活一个" -> 种子轮高风险
        - "钱不是白给的" -> 投资人要回报
        - "每轮都是考验" -> 递进展示

        动态标题：「拿到融资就成功了？」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、误区、真相列表、底部警示、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "拿到融资就成功了？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(UP * 4.0)

        # 2. 误区
        wrong = Text(
            "大错特错！",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(UP * 2.5)

        # 3. 每轮的考验
        r1 = Text("种子轮 → 靠运气，十个活一个", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(UP * 1.2)
        r2 = Text("A 轮 → 靠产品，验证模式", font=self.body_font, font_size=self.font_body_size, color=BLUE).move_to(UP * 0.2)
        r3 = Text("B 轮 → 靠数据，复制扩张", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 0.8)
        r4 = Text("C 轮 → 靠利润，冲刺上市", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(DOWN * 1.8)

        # 4. 底部警示
        bottom = Text(
            "钱不是白给的，要几十倍回报",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(wrong), run_time=step_time)
        self.play(
            LaggedStart(Write(r1), Write(r2), Write(r3), Write(r4), lag_ratio=0.3),
            run_time=step_time
        )
        self.play(Write(bottom), run_time=step_time)
        self.play(Circumscribe(bottom, color=RED), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：搞清楚融资阶段的实用价值

        口播稿关键词/短语：
        - "找工作" -> briefcase 图标
        - "做投资" -> investment 图标
        - "聊天不露怯" -> handshake 图标

        动态标题：「搞清楚有什么用？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、三项用途、底部、强调）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "搞清楚有什么用？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三个用途
        u1_icon = self.load_png_icon("briefcase", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        u1_text = Text("找工作：A轮风险大但股权值钱", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(u1_icon, RIGHT, buff=0.3)
        u1 = Group(u1_icon, u1_text)

        u2_icon = self.load_png_icon("investment", height=0.8).shift(LEFT * 3.0 + UP * 0.5)
        u2_text = Text("做投资：pre-IPO是抢手货", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(u2_icon, RIGHT, buff=0.3)
        u2 = Group(u2_icon, u2_text)

        u3_icon = self.load_png_icon("handshake", height=0.8).shift(LEFT * 3.0 + DOWN * 1.0)
        u3_text = Text("聊天：场面上不会露怯", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(u3_icon, RIGHT, buff=0.3)
        u3 = Group(u3_icon, u3_text)

        items = [u1, u2, u3]

        # 3. 底部
        bottom = Text(
            "搞懂融资逻辑看公司更清楚",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(item, shift=RIGHT) for item in items], lag_ratio=0.3),
            run_time=step_time
        )
        self.play(Write(bottom), run_time=step_time)
        self.play(Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：融资口诀

        口播稿关键词/短语：
        - "种子看运气" -> 口诀逐项展示
        - "天使看人品 A轮看产品" -> 递进
        - "B轮看数据 C轮看利润 上市看行情" -> 递进

        动态标题：「记住这个口诀」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、口诀上半、口诀下半、底部、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "记住这个口诀",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 口诀
        m1 = Text("种子看运气", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(UP * 2.5)
        m2 = Text("天使看人品", font=self.body_font, font_size=self.font_body_size, color=BLUE).move_to(UP * 1.5)
        m3 = Text("A轮看产品", font=self.body_font, font_size=self.font_body_size, color=BLUE).move_to(UP * 0.5)
        m4 = Text("B轮看数据", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 0.5)
        m5 = Text("C轮看利润", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 1.5)
        m6 = Text("上市看行情", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(DOWN * 2.5)

        # 3. 底部
        bottom = Text(
            "记住框架比90%的人看得清",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(Write(m1), Write(m2), Write(m3), lag_ratio=0.3),
            run_time=step_time
        )
        self.play(
            LaggedStart(Write(m4), Write(m5), Write(m6), lag_ratio=0.3),
            run_time=step_time
        )
        self.play(Write(bottom), run_time=step_time)
        self.play(Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：融资全景总结 -> 互动引导

        动态标题：「从想法到敲钟」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、核心收获、互动图标、口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "从想法到敲钟",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "每一步都是真金白银的考验",
            font=self.body_font,
            font_size=self.font_body_size,
            color=WHITE
        ).move_to(UP * 2.0)
        takeaway_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=GOLD, fill_opacity=0.1)
        takeaway_box.surround(takeaway, buff=0.3)
        takeaway_group = VGroup(takeaway_box, takeaway)

        # 3. 互动图标
        like_icon = self.load_png_icon("thumbs_up", height=1.5).move_to(LEFT * 2.5 + DOWN * 0.5)
        like_label = Text("点赞", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_label)

        follow_icon = self.load_png_icon("star", height=1.5).move_to(RIGHT * 2.5 + DOWN * 0.5)
        follow_label = Text("关注", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(follow_icon, DOWN, buff=0.2)
        follow_group = Group(follow_icon, follow_label)

        icons_group = Group(like_group, follow_group)

        # 4. 底部口号
        slogan = Text(
            "每天一课，日日生金！",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(takeaway_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(icons_group, shift=UP), run_time=step_time)
        self.play(Write(slogan), Circumscribe(slogan, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(6)
        # 结尾画面保持
        self.wait(t_trans)
