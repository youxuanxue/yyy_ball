import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson017VerticalScenes(Zsxq100keLessonVertical):
    """
    第017课：底线思维与资产配置
    主题：不确定时代如何保护财富？
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)
        
        口播稿：世界变化太快了，今天这个政策，明天那个风险。
                很多人焦虑：我的钱放哪里才安全？
                今天告诉你一个思维方式：底线思维。先考虑最坏情况，再想怎么赚钱。
        
        动态标题：「钱放哪里才安全？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部动态标题
        title = Text(
            "钱放哪里才安全？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 焦虑场景
        worry_icon = self.load_png_icon("thinking", height=1.8).shift(UP * 1.5)
        worry_text = Text("世界变化太快了...", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(worry_icon, DOWN, buff=0.3)
        worry_group = Group(worry_icon, worry_text)

        # 3. 答案：底线思维
        answer = Text(
            "底线思维", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 1.0)
        answer_box = RoundedRectangle(height=1.2, corner_radius=0.3, color=GOLD, fill_opacity=0.15)
        answer_box.surround(answer, buff=0.4)
        answer_group = VGroup(answer_box, answer)

        # 4. 底部解释
        explain = Text(
            "先考虑最坏情况，再想怎么赚钱", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(worry_group, shift=UP), run_time=step_time)
        self.play(FadeIn(answer_group, shift=UP), run_time=step_time)
        self.play(Write(explain), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)
        
        口播稿：底线思维就是：假设最坏的情况发生，我还能保住什么？
                这不是悲观，而是理性。
                巴菲特说投资第一条规则是不要亏钱，第二条规则是记住第一条。
                这就是底线思维。
        
        动态标题：「什么是底线思维？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "什么是底线思维？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心定义
        definition = Text(
            "最坏情况下，我能保住什么？", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).move_to(UP * 2.2)

        # 3. 巴菲特名言
        quote_icon = self.load_png_icon("businessman", height=1.2).shift(LEFT * 3.0 + UP * 0.2)
        quote_text = VGroup(
            Text("巴菲特投资法则：", font=self.body_font, font_size=self.font_small_size, color=WHITE),
            Text("①不要亏钱", font=self.body_font, font_size=self.font_body_size, color=GREEN),
            Text("②记住第一条", font=self.body_font, font_size=self.font_body_size, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(quote_icon, RIGHT, buff=0.3)
        quote_group = Group(quote_icon, quote_text)

        # 4. 底部结论
        conclusion = Text(
            "这不是悲观，而是理性", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(definition), run_time=step_time)
        self.play(FadeIn(quote_group, shift=RIGHT), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)
        
        口播稿：普通人最大的误区是追求高收益，忽略了风险。
                你想着赚20%，结果亏了50%。
                问题的关键在于，保住本金比赚钱更重要。
                先活下来，才能等到翻盘的机会。
        
        动态标题：「为什么保本比赚钱重要？」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "为什么保本比赚钱重要？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 误区展示
        wrong_think = Text("想赚20%", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(LEFT * 1.8 + UP * 1.5)
        arrow = Text("→", font=self.title_font, font_size=self.font_title_size, color=GRAY).shift(UP * 1.5)
        reality = Text("结果亏50%", font=self.body_font, font_size=self.font_body_size, color=RED).shift(RIGHT * 1.8 + UP * 1.5)
        mistake_group = VGroup(wrong_think, arrow, reality)

        # 3. 核心道理
        key_icon = self.load_png_icon("shield", height=1.5).shift(DOWN * 0.3)
        key_text = Text("保住本金比赚钱更重要", font=self.title_font, font_size=self.font_title_size, color=GOLD).next_to(key_icon, DOWN, buff=0.3)
        key_group = Group(key_icon, key_text)

        # 4. 底部结论
        conclusion = Text(
            "先活下来，才能等翻盘", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(mistake_group), run_time=step_time)
        self.play(FadeIn(key_group, shift=UP), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)
        
        口播稿：什么时候最需要底线思维？
                就是市场特别不确定的时候。经济下行、政策变化、国际形势紧张，
                这些时候，别想着抄底捡便宜，先把自己的底线守住。
        
        动态标题：「什么时候最需要底线思维？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "什么时候最需要底线思维？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(UP * 4.0)

        # 2. 不确定场景
        scenarios = VGroup(
            Text("• 经济下行", font=self.body_font, font_size=self.font_body_size, color=ORANGE),
            Text("• 政策变化", font=self.body_font, font_size=self.font_body_size, color=ORANGE),
            Text("• 国际形势紧张", font=self.body_font, font_size=self.font_body_size, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(UP * 1.2)

        # 3. 警告
        warning_icon = self.load_png_icon("warning", height=1.5).shift(DOWN * 1.0)
        warning_text = Text("别想抄底捡便宜", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(warning_icon, DOWN, buff=0.2)
        warning_group = Group(warning_icon, warning_text)

        # 4. 底部结论
        conclusion = Text(
            "先守住底线", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(LaggedStart(*[FadeIn(s) for s in scenarios], lag_ratio=0.2), run_time=step_time)
        self.play(FadeIn(warning_group, shift=UP), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)
        
        口播稿：普通人的底线资产配置：
                第一，留够6个月生活费的现金或货币基金；
                第二，有套自住房，不是投资，是安身立命；
                第三，配置一份保险，防止大病返贫。
                这三样守住，再想别的。
        
        动态标题：「底线资产配置」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "底线资产配置", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三样底线资产
        tip1_icon = self.load_png_icon("piggy_bank", height=0.8).shift(LEFT * 3.0 + UP * 1.8)
        tip1_text = Text(
            "①6个月现金储备", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).next_to(tip1_icon, RIGHT, buff=0.3)
        tip1 = Group(tip1_icon, tip1_text)

        tip2_icon = self.load_png_icon("house", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        tip2_text = Text(
            "②一套自住房", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).next_to(tip2_icon, RIGHT, buff=0.3)
        tip2 = Group(tip2_icon, tip2_text)

        tip3_icon = self.load_png_icon("insurance", height=0.8).shift(LEFT * 3.0 + DOWN * 1.2)
        tip3_text = Text(
            "③一份保险", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).next_to(tip3_icon, RIGHT, buff=0.3)
        tip3 = Group(tip3_icon, tip3_text)

        tips = [tip1, tip2, tip3]

        # 3. 底部总结
        summary = Text(
            "这三样守住，再想别的", 
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
        
        口播稿：底线思维不是胆小，是智慧。
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
            "底线思维不是胆小，是智慧", 
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
