import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson034VerticalScenes(Zsxq100keLessonVertical):
    """
    第034课：定位战略与心智模式
    主题：用营销思维经营你自己
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：你等于什么？ -> 定位缺失

        口播稿关键词/短语：
        - "海飞丝=去屑" -> 品牌案例
        - "你=？" -> question_mark 图标
        - "没有定位" -> 灰色焦虑

        动态标题：「你等于什么？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、品牌案例、你=？、底部警示、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "你等于什么？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 品牌案例
        brand1 = Text("海飞丝 = 去屑", font=self.body_font, font_size=self.font_body_size, color=BLUE).move_to(UP * 2.2)
        brand2 = Text("百度 = 搜索", font=self.body_font, font_size=self.font_body_size, color=BLUE).move_to(UP * 1.2)

        # 3. 你=？
        q_icon = self.load_png_icon("question_mark", height=1.5).move_to(DOWN * 0.2)
        q_text = Text(
            "你 = ？？？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).next_to(q_icon, DOWN, buff=0.3)
        q_group = Group(q_icon, q_text)

        # 4. 底部真相
        truth = Text(
            "说不清因为你没有定位",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(brand1), Write(brand2), run_time=step_time)
        self.play(FadeIn(q_group, shift=UP), run_time=step_time)
        self.play(Write(truth), run_time=step_time)
        self.play(Circumscribe(truth, color=RED), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：心智模式核心概念

        口播稿关键词/短语：
        - "心智" -> brain 图标
        - "品牌≠心智" -> 对比
        - "谁先抢占谁就赢" -> GOLD 强调

        动态标题：「什么是心智？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、核心定义、品牌案例、品牌≠心智、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "什么是心智？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 核心定义
        brain_icon = self.load_png_icon("brain", height=1.5).move_to(UP * 2.0)
        definition = Text(
            "心智 = 深入骨子里的印象",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(brain_icon, DOWN, buff=0.3)
        def_group = Group(brain_icon, definition)

        # 3. 案例
        case1 = Text("海飞丝 = 去屑", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(DOWN * 0.0)
        case2 = Text("加多宝 = 凉茶", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(case1, DOWN, buff=0.2)

        # 4. 核心观点
        point = Text(
            "品牌只是符号，心智才是地盘",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).move_to(DOWN * 1.8)

        # 5. 底部
        golden = Text(
            "谁先抢占心智谁就赢了",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(def_group, shift=DOWN), run_time=step_time)
        self.play(Write(case1), Write(case2), run_time=step_time)
        self.play(Write(point), run_time=step_time)
        self.play(Write(golden), Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：营销演变三阶段

        口播稿关键词/短语：
        - "广告为王" -> 旧时代 GRAY
        - "渠道为王" -> 中间 BLUE
        - "定位为王" -> 当下 GOLD
        - "占领脑子里的位置" -> 金色核心

        动态标题：「从嗓门大到占心智」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、三阶段、真相、底部、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "从嗓门大到占心智",
            font=self.title_font,
            font_size=self.font_title_size,
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 演变三阶段 - 递进展示
        stage1 = Text("广告为王", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(UP * 2.2 + LEFT * 2.5)
        arrow1 = Text("→", font=self.title_font, font_size=self.font_title_size, color=WHITE).move_to(UP * 2.2)
        stage2 = Text("渠道为王", font=self.body_font, font_size=self.font_body_size, color=BLUE).move_to(UP * 2.2 + RIGHT * 2.5)

        arrow2 = Text("→", font=self.title_font, font_size=self.font_title_size, color=WHITE).move_to(UP * 0.8)
        stage3 = Text("定位为王", font=self.title_font, font_size=self.font_title_size, color=GOLD).move_to(UP * 0.8 + RIGHT * 2.0)

        # 3. 真相
        reality = Text(
            "同质化时代，价格战补贴战都没用",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).move_to(DOWN * 0.8)
        reality2 = Text(
            "客户薅完羊毛就跑",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).next_to(reality, DOWN, buff=0.2)

        # 4. 底部核心
        golden = Text(
            "在客户脑子里占个位置",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(stage1), Write(arrow1), Write(stage2), run_time=step_time)
        self.play(Write(arrow2), Write(stage3), run_time=step_time)
        self.play(Write(reality), Write(reality2), run_time=step_time)
        self.play(Write(golden), Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：职场中的定位标签

        口播稿关键词/短语：
        - "小王教育口" -> 标签1
        - "小李北京人脉" -> 标签2
        - "小宋理财专家" -> 标签3
        - "没有标签轮不到你" -> RED 警示

        动态标题：「你在别人心里有标签吗？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、三个标签、底部警示、强调）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "你在别人心里有标签吗？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三个标签案例
        t1_icon = self.load_png_icon("person", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        t1_text = Text("小王 = 教育口关系到位", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(t1_icon, RIGHT, buff=0.3)
        t1 = Group(t1_icon, t1_text)

        t2_icon = self.load_png_icon("handshake", height=0.8).shift(LEFT * 3.0 + UP * 0.5)
        t2_text = Text("小李 = 北京人脉丰富", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(t2_icon, RIGHT, buff=0.3)
        t2 = Group(t2_icon, t2_text)

        t3_icon = self.load_png_icon("investment", height=0.8).shift(LEFT * 3.0 + DOWN * 1.0)
        t3_text = Text("小宋 = 理财专家", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(t3_icon, RIGHT, buff=0.3)
        t3 = Group(t3_icon, t3_text)

        items = [t1, t2, t3]

        # 3. 底部警示
        warning = Text(
            "没有标签，有机会也轮不到你",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(item, shift=RIGHT) for item in items], lag_ratio=0.3),
            run_time=step_time
        )
        self.play(Write(warning), run_time=step_time)
        self.play(Circumscribe(warning, color=RED), run_time=step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：三步打造个人定位

        口播稿关键词/短语：
        - "擅长什么" -> target 图标
        - "一句话说清楚" -> idea 图标
        - "反复强化印象" -> brain 图标

        动态标题：「三步打造你的定位」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、三步、彩蛋、金句、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "三步打造你的定位",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三步
        s1_icon = self.load_png_icon("target", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        s1_text = Text("①想清楚你擅长什么", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(s1_icon, RIGHT, buff=0.3)
        s1 = Group(s1_icon, s1_text)

        s2_icon = self.load_png_icon("idea", height=0.8).shift(LEFT * 3.0 + UP * 0.5)
        s2_text = Text("②一句话说清你是干嘛的", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(s2_icon, RIGHT, buff=0.3)
        s2 = Group(s2_icon, s2_text)

        s3_icon = self.load_png_icon("brain", height=0.8).shift(LEFT * 3.0 + DOWN * 1.0)
        s3_text = Text("③在圈子里反复强化印象", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(s3_icon, RIGHT, buff=0.3)
        s3 = Group(s3_icon, s3_text)

        items = [s1, s2, s3]

        # 3. 彩蛋提示
        tip = Text(
            "找不到定位？先给对手贴标签",
            font=self.body_font,
            font_size=self.font_small_size,
            color=ORANGE
        ).move_to(DOWN * 2.0)

        # 4. 底部金句
        golden = Text(
            "一句话说清楚你是谁",
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
        self.play(Write(tip), run_time=step_time)
        self.play(Write(golden), run_time=step_time)
        self.play(Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：定位自己 -> 互动引导

        动态标题：「定位你自己」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、核心收获、互动图标、口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "定位你自己",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "说清楚你是谁，你就赢了一半",
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
