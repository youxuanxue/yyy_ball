import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson016VerticalScenes(Zsxq100keLessonVertical):
    """
    第016课：房子还值得买吗
    主题：房地产市场的新逻辑
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)
        
        口播稿：很多人问我，房价会不会大跌？现在还能买房吗？
                我告诉你一个扎心的真相：上头既不希望大涨，也不准大跌，要的是慢牛。
                但接下来，买房的逻辑完全变了。
        
        动态标题：「房价会大跌吗？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部动态标题
        title = Text(
            "房价会大跌吗？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 常见疑问
        question_icon = self.load_png_icon("house", height=2.0).shift(UP * 1.5)
        question_text = Text("？", font=self.title_font, font_size=self.font_title_size * 1.5, color=GRAY).next_to(question_icon, RIGHT, buff=0.3)
        question_group = Group(question_icon, question_text)

        # 3. 真相揭示
        truth_line1 = Text("不希望大涨", font=self.body_font, font_size=self.font_body_size, color=RED).shift(LEFT * 1.5 + DOWN * 0.8)
        truth_line2 = Text("也不准大跌", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(RIGHT * 1.5 + DOWN * 0.8)
        truth_group = VGroup(truth_line1, truth_line2)

        # 4. 底部结论
        conclusion = Text(
            "要的是慢牛", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 2.5)
        
        key_point = Text(
            "但买房逻辑完全变了", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(question_group, shift=UP), run_time=step_time)
        self.play(FadeIn(truth_group), Write(conclusion), run_time=step_time)
        self.play(Write(key_point), Circumscribe(key_point, color=ORANGE), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)
        
        口播稿：新逻辑是什么？两个字：分化。
                从中央调控变成地方调控，各城市自己说了算。
                这意味着什么？好城市会更好，差城市会更差。
                闭眼买房躺赚的时代，一去不复返了。
        
        动态标题：「新逻辑：分化」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "新逻辑：分化", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心概念
        core_concept = Text(
            "地方调控，各城市自己说了算", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).move_to(UP * 2.2)

        # 3. 分化对比
        good_city = Text("好城市", font=self.title_font, font_size=self.font_title_size, color=GREEN).shift(LEFT * 2.0 + UP * 0.3)
        good_arrow = Text("↑ 更好", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(good_city, DOWN, buff=0.2)
        good_group = VGroup(good_city, good_arrow)

        bad_city = Text("差城市", font=self.title_font, font_size=self.font_title_size, color=RED).shift(RIGHT * 2.0 + UP * 0.3)
        bad_arrow = Text("↓ 更差", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(bad_city, DOWN, buff=0.2)
        bad_group = VGroup(bad_city, bad_arrow)

        # 4. 底部结论
        conclusion = Text(
            "闭眼买房躺赚的时代结束了", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(DOWN * 3.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(core_concept), run_time=step_time)
        self.play(FadeIn(good_group, shift=RIGHT), FadeIn(bad_group, shift=LEFT), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)
        
        口播稿：问题的关键在于，过去买房买的是学区、户口这些附加值。
                现在呢？要素在放开，人们开始就房论房。
                小区品质、物业管理、户型设计，这些才是影响房价的核心因素。
        
        动态标题：「买房买的是什么？」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "买房买的是什么？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 过去 vs 现在
        past_label = Text("过去", font=self.body_font, font_size=self.font_small_size, color=GRAY).shift(LEFT * 2.0 + UP * 2.0)
        past_content = Text("学区、户口等附加值", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(past_label, DOWN, buff=0.3)
        past_group = VGroup(past_label, past_content)

        now_label = Text("现在", font=self.body_font, font_size=self.font_small_size, color=GOLD).shift(RIGHT * 2.0 + UP * 2.0)
        now_content = Text("就房论房", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(now_label, DOWN, buff=0.3)
        now_group = VGroup(now_label, now_content)

        # 3. 新的核心因素
        factors = VGroup(
            Text("• 小区品质", font=self.body_font, font_size=self.font_body_size, color=GREEN),
            Text("• 物业管理", font=self.body_font, font_size=self.font_body_size, color=GREEN),
            Text("• 户型设计", font=self.body_font, font_size=self.font_body_size, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 1.0)

        # 4. 底部结论
        conclusion = Text(
            "品质决定房价", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(past_group, shift=RIGHT), FadeIn(now_group, shift=LEFT), run_time=step_time)
        self.play(LaggedStart(*[FadeIn(f) for f in factors], lag_ratio=0.2), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)
        
        口播稿：如果你要买房，重点关注两类城市：
                一是有抢人政策、落户容易、贷款宽松的；
                二是产业发展健康、人口持续流入的核心都市圈。
                这两条占一条，房子就有底气。
        
        动态标题：「该买哪里的房？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "该买哪里的房？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 第一类城市
        city1_icon = self.load_png_icon("building", height=1.2).shift(LEFT * 2.0 + UP * 1.5)
        city1_label = Text("抢人政策城市", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(city1_icon, DOWN, buff=0.2)
        city1_desc = Text("落户容易、贷款宽松", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(city1_label, DOWN, buff=0.1)
        city1_group = Group(city1_icon, city1_label, city1_desc)

        # 3. 第二类城市
        city2_icon = self.load_png_icon("real_estate", height=1.2).shift(RIGHT * 2.0 + UP * 1.5)
        city2_label = Text("核心都市圈", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(city2_icon, DOWN, buff=0.2)
        city2_desc = Text("产业健康、人口流入", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(city2_label, DOWN, buff=0.1)
        city2_group = Group(city2_icon, city2_label, city2_desc)

        # 4. 底部结论
        conclusion = Text(
            "占一条，房子就有底气", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 2.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(city1_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(city2_group, shift=DOWN), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)
        
        口播稿：记住三点：
                第一，选城市比选房子重要，先看产业和人口；
                第二，买品质房，好物业好户型，贬值慢；
                第三，关注各地人才政策，看落户条件和购房补贴，这是地方给你的红利。
        
        动态标题：「买房三条建议」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "买房三条建议", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三条建议
        tip1_icon = self.load_png_icon("building", height=0.8).shift(LEFT * 3.0 + UP * 1.8)
        tip1_text = Text(
            "①选城市比选房子重要", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).next_to(tip1_icon, RIGHT, buff=0.3)
        tip1 = Group(tip1_icon, tip1_text)

        tip2_icon = self.load_png_icon("house", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        tip2_text = Text(
            "②买品质房贬值慢", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).next_to(tip2_icon, RIGHT, buff=0.3)
        tip2 = Group(tip2_icon, tip2_text)

        tip3_icon = self.load_png_icon("document", height=0.8).shift(LEFT * 3.0 + DOWN * 1.2)
        tip3_text = Text(
            "③关注人才政策红利", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(tip3_icon, RIGHT, buff=0.3)
        tip3 = Group(tip3_icon, tip3_text)

        tips = [tip1, tip2, tip3]

        # 3. 底部总结
        summary = Text(
            "城市和品质是关键", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(tip, shift=RIGHT) for tip in tips], lag_ratio=0.3), 
            run_time=3*step_time
        )
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action)
        
        口播稿：买房这事儿，城市和品质是关键。
                觉得有收获的话，点个赞，关注我，咱们下期继续聊理财那些事儿。
        
        动态标题：「学到了吗？」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "学到了吗？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "城市和品质是关键", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(UP * 2.0)
        takeaway_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=GOLD, fill_opacity=0.1)
        takeaway_box.surround(takeaway, buff=0.3)
        takeaway_group = VGroup(takeaway_box, takeaway)

        # 3. 互动图标
        like_icon = self.load_png_icon("thumbs_up", height=1.8).move_to(LEFT * 2.0 + DOWN * 0.5)
        like_label = Text("点赞", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_label)
        
        follow_icon = self.load_png_icon("user", height=1.8).move_to(RIGHT * 2.0 + DOWN * 0.5)
        follow_label = Text("关注", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(follow_icon, DOWN, buff=0.2)
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

        # 结尾画面保持
        self.wait(t_trans)
