import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson018VerticalScenes(Zsxq100keLessonVertical):
    """
    第018课：需求决定经济
    主题：为什么到处都在逼你花钱？
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)
        
        口播稿：你有没有发现，到处都在逼你花钱？
                降息、发优惠券、搞消费补贴。这不是巧合，而是有深层原因的。
                今天告诉你，经济的本质只有两个字：需求。
        
        动态标题：「为什么到处逼你花钱？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部动态标题
        title = Text(
            "为什么到处逼你花钱？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 4.0)
        
        # 2. 刺激消费场景
        stimuli = VGroup(
            Text("降息", font=self.body_font, font_size=self.font_body_size, color=GREEN),
            Text("发优惠券", font=self.body_font, font_size=self.font_body_size, color=GOLD),
            Text("消费补贴", font=self.body_font, font_size=self.font_body_size, color=BLUE),
        ).arrange(RIGHT, buff=0.8).move_to(UP * 1.8)

        # 3. 疑问
        question = Text("这不是巧合...", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(UP * 0.3)

        # 4. 答案揭示
        answer_icon = self.load_png_icon("shopping_cart", height=1.5).shift(DOWN * 1.2)
        answer_text = Text("经济的本质：需求", font=self.title_font, font_size=self.font_title_size, color=GOLD).next_to(answer_icon, DOWN, buff=0.3)
        answer_group = Group(answer_icon, answer_text)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(LaggedStart(*[FadeIn(s, shift=UP) for s in stimuli], lag_ratio=0.2), run_time=step_time)
        self.play(Write(question), run_time=step_time)
        self.play(FadeIn(answer_group, shift=UP), Circumscribe(answer_text, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)
        
        口播稿：两百多年来，经济学说到底就两件事：供给和需求。
                有需求才有供给，东西卖得出去，工厂才会生产，工人才有工资。
                需求一萎缩，整个链条就断了。
        
        动态标题：「供给与需求」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "供给与需求", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心概念
        core = Text(
            "经济学的本质就两件事", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(UP * 2.2)

        # 3. 供给需求循环
        demand = Text("需求", font=self.title_font, font_size=self.font_title_size, color=GREEN).shift(LEFT * 2.0 + UP * 0.3)
        arrow1 = Text("→", font=self.title_font, font_size=self.font_title_size, color=WHITE).shift(UP * 0.3)
        supply = Text("供给", font=self.title_font, font_size=self.font_title_size, color=BLUE).shift(RIGHT * 2.0 + UP * 0.3)
        cycle_group = VGroup(demand, arrow1, supply)

        # 4. 链条说明
        chain = VGroup(
            Text("东西卖得出去", font=self.body_font, font_size=self.font_small_size, color=WHITE),
            Text("→ 工厂生产", font=self.body_font, font_size=self.font_small_size, color=WHITE),
            Text("→ 工人有工资", font=self.body_font, font_size=self.font_small_size, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.5)

        # 5. 底部警告
        warning = Text(
            "需求萎缩，链条就断了", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(core), run_time=step_time)
        self.play(FadeIn(cycle_group), FadeIn(chain), run_time=step_time)
        self.play(Write(warning), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)
        
        口播稿：问题的关键在于，现代社会普遍面临需求萎缩。
                老百姓债务压顶，不敢花钱；政府搞基建，也不能无限借债。
                需求创造不出来，只能刺激，所以才到处逼你花钱。
        
        动态标题：「为什么需求萎缩？」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "为什么需求萎缩？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(UP * 4.0)

        # 2. 两个原因
        reason1 = Text("老百姓债务压顶", font=self.body_font, font_size=self.font_body_size, color=GRAY).shift(LEFT * 2.0 + UP * 1.5)
        reason1_sub = Text("不敢花钱", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(reason1, DOWN, buff=0.15)
        reason1_group = VGroup(reason1, reason1_sub)

        reason2 = Text("政府搞基建", font=self.body_font, font_size=self.font_body_size, color=GRAY).shift(RIGHT * 2.0 + UP * 1.5)
        reason2_sub = Text("不能无限借债", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(reason2, DOWN, buff=0.15)
        reason2_group = VGroup(reason2, reason2_sub)

        # 3. 结论
        conclusion_icon = self.load_png_icon("coupon", height=1.2).shift(DOWN * 1.0)
        conclusion_text = Text("需求创造不出来，只能刺激", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(conclusion_icon, DOWN, buff=0.2)
        conclusion_group = Group(conclusion_icon, conclusion_text)

        # 4. 底部
        final = Text(
            "所以到处逼你花钱", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(reason1_group, shift=RIGHT), FadeIn(reason2_group, shift=LEFT), run_time=step_time)
        self.play(FadeIn(conclusion_group, shift=UP), run_time=step_time)
        self.play(Write(final), Circumscribe(final, color=ORANGE), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)
        
        口播稿：当你看到降息、发消费券、搞促销的时候，说明经济需要刺激了。
                这时候反而是理性消费的好时机：
                政府给补贴的东西，该买就买；但别冲动消费，被营销牵着走。
        
        动态标题：「刺激消费时该怎么办？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "刺激消费时该怎么办？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 信号识别
        signal = Text(
            "看到降息、消费券、促销", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(UP * 2.2)
        signal_meaning = Text("= 经济需要刺激", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(signal, DOWN, buff=0.2)

        # 3. 两种做法
        do_icon = self.load_png_icon("check_mark", height=1.0).shift(LEFT * 2.0 + DOWN * 0.5)
        do_text = Text("有补贴的该买就买", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(do_icon, DOWN, buff=0.2)
        do_group = Group(do_icon, do_text)

        dont_icon = self.load_png_icon("warning", height=1.0).shift(RIGHT * 2.0 + DOWN * 0.5)
        dont_text = Text("别被营销牵着走", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(dont_icon, DOWN, buff=0.2)
        dont_group = Group(dont_icon, dont_text)

        # 4. 底部总结
        summary = Text(
            "理性消费的好时机", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(signal), Write(signal_meaning), run_time=step_time)
        self.play(FadeIn(do_group, shift=UP), FadeIn(dont_group, shift=UP), run_time=step_time)
        self.play(Write(summary), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)
        
        口播稿：记住三点：
                第一，大件消费等政策，有补贴再出手；
                第二，别被促销冲昏头，需要的才买；
                第三，理解经济周期，需求低迷时现金为王，复苏时再入场。
        
        动态标题：「理性消费三条建议」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "理性消费三条建议", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三条建议
        tip1_icon = self.load_png_icon("coupon", height=0.8).shift(LEFT * 3.0 + UP * 1.8)
        tip1_text = Text(
            "①大件消费等补贴", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).next_to(tip1_icon, RIGHT, buff=0.3)
        tip1 = Group(tip1_icon, tip1_text)

        tip2_icon = self.load_png_icon("warning", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        tip2_text = Text(
            "②需要的才买", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=RED
        ).next_to(tip2_icon, RIGHT, buff=0.3)
        tip2 = Group(tip2_icon, tip2_text)

        tip3_icon = self.load_png_icon("money", height=0.8).shift(LEFT * 3.0 + DOWN * 1.2)
        tip3_text = Text(
            "③低迷时现金为王", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(tip3_icon, RIGHT, buff=0.3)
        tip3 = Group(tip3_icon, tip3_text)

        tips = [tip1, tip2, tip3]

        # 3. 底部总结
        summary = Text(
            "懂需求，才能看懂经济", 
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
        
        口播稿：懂需求，才能看懂经济。
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
            "懂需求，才能看懂经济", 
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
