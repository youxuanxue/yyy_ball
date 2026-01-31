import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson020VerticalScenes(Zsxq100keLessonVertical):
    """
    第020课：大投资人与公募基金
    主题：普通人如何借力大资本
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)
        
        口播稿：你有没有想过，为什么好项目总是轮不到普通人？
                比亚迪、京东这种好公司，你想投也投不进去。
                因为大户有议价权，95%的优质项目和你我无缘。
        
        动态标题：「好项目为啥轮不到你？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部动态标题
        title = Text(
            "好项目为啥轮不到你？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 好公司示例
        examples = Text(
            "比亚迪、京东...", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(UP * 2.0)
        examples_sub = Text("你想投也投不进去", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(examples, DOWN, buff=0.2)

        # 3. 大户 vs 散户
        big_icon = self.load_png_icon("businessman", height=1.5).shift(LEFT * 2.0 + DOWN * 0.5)
        big_label = Text("大户", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(big_icon, DOWN, buff=0.2)
        big_value = Text("有议价权", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(big_label, DOWN, buff=0.1)
        big_group = Group(big_icon, big_label, big_value)

        small_icon = self.load_png_icon("user", height=1.5).shift(RIGHT * 2.0 + DOWN * 0.5)
        small_label = Text("散户", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(small_icon, DOWN, buff=0.2)
        small_value = Text("没机会", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(small_label, DOWN, buff=0.1)
        small_group = Group(small_icon, small_label, small_value)

        # 4. 底部结论
        conclusion = Text(
            "95%优质项目和你无缘", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(examples), FadeIn(examples_sub), run_time=step_time)
        self.play(FadeIn(big_group, shift=UP), FadeIn(small_group, shift=UP), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=RED), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)
        
        口播稿：公募基金就是把大家的钱凑在一起，交给专业的基金经理来投资。
                100块就能起买，门槛极低。
                它让普通人也能参与大资本的游戏，借力专业机构赚钱。
        
        动态标题：「什么是公募基金？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "什么是公募基金？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心定义
        definition = Text(
            "大家的钱凑一起，专业经理投资", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).move_to(UP * 2.2)

        # 3. 图示
        people_icon = self.load_png_icon("group", height=1.2).shift(LEFT * 2.5 + UP * 0.2)
        arrow1 = Text("→", font=self.title_font, font_size=self.font_title_size, color=WHITE).shift(LEFT * 0.8 + UP * 0.2)
        fund_icon = self.load_png_icon("money_bag_with_coins", height=1.2).shift(UP * 0.2)
        arrow2 = Text("→", font=self.title_font, font_size=self.font_title_size, color=WHITE).shift(RIGHT * 0.8 + UP * 0.2)
        manager_icon = self.load_png_icon("businessman", height=1.2).shift(RIGHT * 2.5 + UP * 0.2)
        flow_group = Group(people_icon, arrow1, fund_icon, arrow2, manager_icon)

        # 4. 优势
        advantage1 = Text("100块起买", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(LEFT * 1.5 + DOWN * 1.5)
        advantage2 = Text("门槛极低", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(RIGHT * 1.5 + DOWN * 1.5)
        
        # 5. 底部总结
        summary = Text(
            "借力专业机构赚钱", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(definition), run_time=step_time)
        self.play(FadeIn(flow_group, shift=UP), run_time=step_time)
        self.play(Write(advantage1), Write(advantage2), Write(summary), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)
        
        口播稿：大户为什么赚钱？
                第一，沟通成本低，项目方愿意对接；
                第二，除了钱还能带资源。
                普通人单打独斗没有优势，但通过基金抱团，就能享受大资本的待遇。
        
        动态标题：「大户为什么赚钱？」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "大户为什么赚钱？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 两个原因
        reason1 = Text("① 沟通成本低", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(UP * 2.0)
        reason1_sub = Text("项目方愿意对接", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(reason1, DOWN, buff=0.15)
        
        reason2 = Text("② 除了钱还能带资源", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(UP * 0.5)
        reason2_sub = Text("品牌、人脉、渠道", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(reason2, DOWN, buff=0.15)

        # 3. 解决方案
        solution_icon = self.load_png_icon("group", height=1.2).shift(DOWN * 1.5)
        solution_text = Text("通过基金抱团", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(solution_icon, DOWN, buff=0.2)
        solution_group = Group(solution_icon, solution_text)

        # 4. 底部结论
        conclusion = Text(
            "享受大资本待遇", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(reason1), FadeIn(reason1_sub), Write(reason2), FadeIn(reason2_sub), run_time=step_time)
        self.play(FadeIn(solution_group, shift=UP), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)
        
        口播稿：什么人适合买公募基金？
                没时间研究个股的上班族；不想承担太大风险的保守派；
                想长期定投的年轻人。
                总之，不想花精力但想参与股市的，都可以选基金。
        
        动态标题：「谁适合买基金？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "谁适合买基金？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 三类人群
        group1 = Text("• 没时间研究的上班族", font=self.body_font, font_size=self.font_body_size, color=WHITE).shift(UP * 1.8)
        group2 = Text("• 不想承担大风险的保守派", font=self.body_font, font_size=self.font_body_size, color=WHITE).shift(UP * 0.8)
        group3 = Text("• 想长期定投的年轻人", font=self.body_font, font_size=self.font_body_size, color=WHITE).shift(DOWN * 0.2)
        groups = VGroup(group1, group2, group3)

        # 3. 总结
        summary_icon = self.load_png_icon("investment_portfolio", height=1.2).shift(DOWN * 1.8)
        summary_text = Text("不想花精力但想参与股市", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(summary_icon, DOWN, buff=0.2)
        summary_group = Group(summary_icon, summary_text)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(LaggedStart(*[FadeIn(g) for g in groups], lag_ratio=0.2), run_time=step_time)
        self.play(FadeIn(summary_group, shift=UP), run_time=step_time)
        self.wait(step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)
        
        口播稿：记住三点：
                第一，选择正规渠道买基金，银行、支付宝、天天基金都行；
                第二，看基金经理的历史业绩，至少管理3年以上；
                第三，定投比一次性买入更稳，分散风险。
        
        动态标题：「买基金三条建议」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "买基金三条建议", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三条建议
        tip1_icon = self.load_png_icon("bank", height=0.8).shift(LEFT * 3.0 + UP * 1.8)
        tip1_text = Text(
            "①正规渠道买", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).next_to(tip1_icon, RIGHT, buff=0.3)
        tip1 = Group(tip1_icon, tip1_text)

        tip2_icon = self.load_png_icon("businessman", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        tip2_text = Text(
            "②看经理历史业绩", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).next_to(tip2_icon, RIGHT, buff=0.3)
        tip2 = Group(tip2_icon, tip2_text)

        tip3_icon = self.load_png_icon("growing_money", height=0.8).shift(LEFT * 3.0 + DOWN * 1.2)
        tip3_text = Text(
            "③定投分散风险", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(tip3_icon, RIGHT, buff=0.3)
        tip3 = Group(tip3_icon, tip3_text)

        tips = [tip1, tip2, tip3]

        # 3. 底部总结
        summary = Text(
            "基金是普通人最佳选择", 
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
        
        口播稿：公募基金是普通人参与资本市场的最佳方式。
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
            "基金是普通人参与资本市场的最佳方式", 
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
