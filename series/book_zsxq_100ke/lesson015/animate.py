import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson015VerticalScenes(Zsxq100keLessonVertical):
    """
    第015课：征信是你的金融身份证
    主题：如何把自己变成银行想要的人？
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)
        
        口播稿：你有没有想过，为什么你的房贷利率比别人高？
                为什么信用卡额度才几千块？很可能不是你没钱，而是你的征信出了问题。
                征信这东西，看不见摸不着，却决定了你能借多少钱。
        
        动态标题：「为什么你借钱比别人贵？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部动态标题
        title = Text(
            "为什么你借钱比别人贵？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 两个问题
        q1 = Text("房贷利率比别人高？", font=self.body_font, font_size=self.font_body_size, color=RED).shift(UP * 2.0 + LEFT * 0.5)
        q1_icon = Text("？", font=self.title_font, font_size=self.font_title_size, color=RED).next_to(q1, RIGHT, buff=0.2)
        q1_group = VGroup(q1, q1_icon)

        q2 = Text("信用卡额度才几千？", font=self.body_font, font_size=self.font_body_size, color=RED).shift(UP * 0.8 + LEFT * 0.5)
        q2_icon = Text("？", font=self.title_font, font_size=self.font_title_size, color=RED).next_to(q2, RIGHT, buff=0.2)
        q2_group = VGroup(q2, q2_icon)

        # 3. 答案揭示
        answer_icon = self.load_png_icon("credit_card", height=1.8).shift(DOWN * 1.0)
        answer_text = Text("征信出了问题", font=self.title_font, font_size=self.font_title_size, color=ORANGE).next_to(answer_icon, DOWN, buff=0.3)
        answer_group = Group(answer_icon, answer_text)

        # 4. 底部结论
        conclusion = Text(
            "征信决定你能借多少钱", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(q1_group), FadeIn(q2_group), run_time=step_time)
        self.play(FadeIn(answer_group, shift=UP), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)
        
        口播稿：征信其实就是你和金融机构打交道的记录本。
                你在银行借过多少钱、还过多少钱、有没有逾期，全都记在上面。
                这个记录由中国人民银行统一管理，银行放款前必查。
        
        动态标题：「什么是征信？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "什么是征信？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 征信 = 记录本
        metaphor = Text(
            "征信 = 金融记录本", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 3.0)
        
        # 3. 记录内容
        record_icon = self.load_png_icon("document", height=1.5).shift(UP * 1.5)
        records = VGroup(
            Text("• 借过多少钱", font=self.body_font, font_size=self.font_body_size, color=WHITE),
            Text("• 还过多少钱", font=self.body_font, font_size=self.font_body_size, color=WHITE),
            Text("• 有没有逾期", font=self.body_font, font_size=self.font_body_size, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(record_icon, DOWN, buff=0.3)
        record_group = Group(record_icon, records)

        # 4. 底部：央行管理
        bank_text = Text(
            "中国人民银行统一管理", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(DOWN * 2.8)
        bank_note = Text("银行放款前必查", font=self.title_font, font_size=self.font_title_size, color=GOLD).next_to(bank_text, DOWN, buff=0.3)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(metaphor), run_time=step_time)
        self.play(FadeIn(record_group, shift=DOWN), run_time=step_time)
        self.play(Write(bank_text), Write(bank_note), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)
        
        口播稿：关键点来了：2年内连3累6，银行就不待见你了。
                什么意思？就是连续3次忘还款，或者累计6次逾期，
                你在银行眼里就成了高风险客户。贷款要么批不下来，要么利息高一截。
        
        动态标题：「连3累6是什么意思？」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "连3累6是什么意思？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(UP * 4.0)

        # 2. 核心概念
        key_concept = Text(
            "2年内「连3累6」", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 2.2)
        
        # 3. 解释
        explain1 = Text("连续3次忘还款", font=self.body_font, font_size=self.font_body_size, color=RED).shift(LEFT * 2.0 + UP * 0.5)
        explain2 = Text("或", font=self.body_font, font_size=self.font_body_size, color=WHITE).shift(UP * 0.5)
        explain3 = Text("累计6次逾期", font=self.body_font, font_size=self.font_body_size, color=RED).shift(RIGHT * 2.0 + UP * 0.5)
        explain_group = VGroup(explain1, explain2, explain3)

        # 4. 后果
        result_icon = self.load_png_icon("warning", height=1.2).shift(DOWN * 1.0)
        result_text = Text("银行眼中的高风险客户", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(result_icon, DOWN, buff=0.2)
        result_group = Group(result_icon, result_text)

        # 5. 底部结论
        conclusion = Text(
            "贷款难批或利息更高", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(key_concept), run_time=step_time)
        self.play(FadeIn(explain_group), run_time=step_time)
        self.play(FadeIn(result_group, shift=UP), Write(conclusion), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)
        
        口播稿：最容易踩坑的场景：网上那些让你查借款额度的广告，千万别点！
                输入身份证一查，就算你没借钱，也会在征信上留下一条查询记录。
                查多了，银行会觉得你很缺钱。
        
        动态标题：「最容易踩的坑」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "最容易踩的坑", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(UP * 4.0)

        # 2. 场景描述
        scenario = Text(
            "网上广告：查查你的借款额度", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(UP * 2.0)
        scenario_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=RED, fill_opacity=0.1)
        scenario_box.surround(scenario, buff=0.3)
        scenario_group = VGroup(scenario_box, scenario)

        # 3. 警告
        warning_icon = self.load_png_icon("warning", height=1.5).shift(DOWN * 0.2)
        warning_text = Text("千万别点！", font=self.title_font, font_size=self.font_title_size, color=RED).next_to(warning_icon, DOWN, buff=0.2)
        warning_group = Group(warning_icon, warning_text)

        # 4. 后果解释
        consequence = Text(
            "一查就在征信上留记录", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(DOWN * 2.5)
        consequence2 = Text(
            "查多了 = 银行觉得你缺钱", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).next_to(consequence, DOWN, buff=0.3)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(scenario_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(warning_group, shift=UP), run_time=step_time)
        self.play(Write(consequence), Write(consequence2), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)
        
        口播稿：保护征信记住三点：
                第一，借呗花呗少用，它们都上征信；
                第二，信用卡别逾期，实在还不上先还最低还款；
                第三，每年去央行网站免费查一次自己的征信，心里有数。
        
        动态标题：「保护征信三条建议」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "保护征信三条建议", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三条建议
        tip1_icon = self.load_png_icon("warning", height=0.8).shift(LEFT * 2.5 + UP * 1.8)
        tip1_text = Text(
            "①借呗花呗少用", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=RED
        ).next_to(tip1_icon, RIGHT, buff=0.3)
        tip1 = Group(tip1_icon, tip1_text)

        tip2_icon = self.load_png_icon("credit_card", height=0.8).shift(LEFT * 2.5 + UP * 0.3)
        tip2_text = Text(
            "②信用卡别逾期", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).next_to(tip2_icon, RIGHT, buff=0.3)
        tip2 = Group(tip2_icon, tip2_text)

        tip3_icon = self.load_png_icon("document", height=0.8).shift(LEFT * 2.5 + DOWN * 1.2)
        tip3_text = Text(
            "③每年免费查一次征信", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).next_to(tip3_icon, RIGHT, buff=0.3)
        tip3 = Group(tip3_icon, tip3_text)

        tips = [tip1, tip2, tip3]

        # 3. 底部总结
        summary = Text(
            "征信是金融身份证", 
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
        
        口播稿：征信就是你的金融身份证，好好保护它。
                觉得有用的话，点个赞，关注我，咱们下期继续聊理财那些事儿。
        
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
            "征信是你的金融身份证", 
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
