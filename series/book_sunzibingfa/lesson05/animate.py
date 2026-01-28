import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import SunziLessonVertical


class Lesson05VerticalScenes(SunziLessonVertical):
    """
    第05课：敬畏的力量 - 为什么聪明人做事前要算账
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰 (Hook) - 视觉逻辑：引发共鸣 -> 提出问题 -> 抓住注意力
        
        口播稿关键词/短语：
        - "搭乐高城堡" -> 使用积木相关图标
        - "零件不够" -> 显示缺失、不完整的视觉
        - "放弃" -> 灰色调，困境感
        
        动态标题：「半途而废的秘密」（引发共鸣）
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、图标组、问号、底部文字、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题 (y=4.0) - 引发共鸣
        title = Text(
            "半途而废的秘密", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 中部核心内容 - 乐高场景 (使用 budget 图标代表计划不足)
        # 关键词：搭乐高、零件不够、放弃
        main_icon = self.load_png_icon("budget", height=2.5).move_to(UP * 1.0)
        
        # 关键短语浮现
        phrase1 = Text("零件不够了...", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(main_icon, DOWN, buff=0.5)
        phrase2 = Text("手都酸了...", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(phrase1, DOWN, buff=0.3)
        
        center_group = Group(main_icon, phrase1, phrase2)

        # 3. 问号元素 - 表示困惑
        question_mark = Text("?", font=self.title_font, font_size=72, color=RED).move_to(DOWN * 1.5)

        # 4. 底部扎心结论
        bottom_text = Text("是不是特别可惜？", font=self.title_font, font_size=self.font_title_size, color=RED).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(main_icon, shift=UP), run_time=step_time)
        self.play(Write(phrase1), Write(phrase2), run_time=step_time)
        self.play(GrowFromCenter(question_mark), run_time=step_time)
        self.play(Write(bottom_text), Circumscribe(bottom_text, color=RED), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：《孙子兵法》说 -> 兵法原文 -> 白话解释
        
        口播稿关键词/短语：
        - 「日费千金，然后十万之师举矣」 -> 金色原文，仪式感
        - "每天要花好多钱" -> 金币图标
        - "准备好了，大军才能出发" -> 强调准备的重要性
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（引言、原文第一行、原文第二行、图标、解释、强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部：孙武爷爷说
        who_says = Text("孙武爷爷说：", font=self.title_font, font_size=self.font_body_size, color=GOLD_A).move_to(UP * 4.2)
        
        # 2. 兵法原文（分行展示，使用「」）
        quote_line1 = Text("「日费千金，", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(who_says, DOWN, buff=0.5)
        quote_line2 = Text("然后十万之师举矣」", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(quote_line1, DOWN, buff=0.2)
        
        # 3. 中部金币图标 - 代表花钱
        coin_icon = self.load_png_icon("coins", height=2.0).move_to(DOWN * 0.3)
        
        # 4. 底部白话解释
        explain_text = Text("准备好了，大军才能出发！", font=self.title_font, font_size=self.font_title_size, color=ORANGE).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(who_says), run_time=step_time)
        self.play(Write(quote_line1), run_time=step_time)
        self.play(Write(quote_line2), run_time=step_time)
        self.play(FadeIn(coin_icon, scale=0.5), run_time=step_time)
        self.play(Write(explain_text), run_time=step_time)
        self.play(Circumscribe(explain_text, color=ORANGE), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/为什么重要 (Why) - 视觉逻辑：类比解释 -> 对比布局
        
        口播稿关键词/短语：
        - "装满一个超级大的水桶" -> 水桶比喻
        - "水龙头流得有多快" -> 时间/速度
        - "聪明人做事前，算一算要花多少本钱" -> 大脑/思考图标
        
        使用上下布局：上方比喻场景，下方结论
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、比喻图标、比喻文字、思考图标、结论、强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text("为什么要算账？", font=self.title_font, font_size=self.font_title_size, color=BLUE).move_to(UP * 4.0)
        
        # 2. 比喻场景 - 水桶 + 时钟
        # 使用 time 图标代表时间消耗
        bucket_icon = self.load_png_icon("time", height=2.0).move_to(UP * 1.5 + LEFT * 1.5)
        clock_icon = self.load_png_icon("clock", height=1.5).move_to(UP * 1.5 + RIGHT * 1.5)
        
        metaphor_group = Group(bucket_icon, clock_icon)
        
        # 3. 比喻文字
        metaphor_text = Text("不知道要花多少时间和精力...", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(DOWN * 0.5)
        
        # 4. 思考图标 - 聪明人会先算账
        brain_icon = self.load_png_icon("brain", height=1.8).move_to(DOWN * 2.0)
        
        # 5. 底部结论
        conclusion = Text("聪明人先算本钱！", font=self.title_font, font_size=self.font_title_size, color=GREEN).move_to(DOWN * 4.0)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(bucket_icon, shift=RIGHT), FadeIn(clock_icon, shift=LEFT), run_time=step_time)
        self.play(Write(metaphor_text), run_time=step_time)
        self.play(FadeIn(brain_icon, scale=0.5), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)
        self.play(Circumscribe(conclusion, color=GREEN), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 策略/怎么做 (How) - 视觉逻辑：魔法咒语 -> 逐项弹出
        
        口播稿关键词/短语：
        - "快、准、狠" -> 三字口诀，逐个弹出
        - "快：做好准备后快速行动"
        - "准：目标清楚，一次只做一件事"
        - "狠：做完马上收工"
        
        使用 LaggedStart 实现逐项弹出效果
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、快、准、狠、金句、强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题 - 魔法咒语
        title = Text("记住这个魔法咒语", font=self.title_font, font_size=self.font_title_size, color=GOLD).move_to(UP * 4.0)
        
        # 2. 三字口诀 - 快准狠
        fast_char = Text("快", font=self.title_font, font_size=72, color=BLUE)
        fast_desc = Text("做好准备，快速行动", font=self.body_font, font_size=self.font_small_size, color=WHITE)
        fast_group = VGroup(fast_char, fast_desc).arrange(DOWN, buff=0.2).move_to(UP * 2.0)
        
        precise_char = Text("准", font=self.title_font, font_size=72, color=GREEN)
        precise_desc = Text("目标清楚，一次一件", font=self.body_font, font_size=self.font_small_size, color=WHITE)
        precise_group = VGroup(precise_char, precise_desc).arrange(DOWN, buff=0.2).move_to(UP * 0.0)
        
        decisive_char = Text("狠", font=self.title_font, font_size=72, color=ORANGE)
        decisive_desc = Text("做完收工，不要拖拉", font=self.body_font, font_size=self.font_small_size, color=WHITE)
        decisive_group = VGroup(decisive_char, decisive_desc).arrange(DOWN, buff=0.2).move_to(DOWN * 2.0)
        
        # 3. 底部金句
        golden_rule = Text("最厉害的仗，打完就回家！", font=self.title_font, font_size=self.font_title_size, color=GOLD).move_to(DOWN * 4.0)
        
        # 金句框
        rule_bg = RoundedRectangle(height=1.2, corner_radius=0.3, color=GOLD, fill_opacity=0.15)
        rule_bg.surround(golden_rule, buff=0.3)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(GrowFromCenter(fast_char), Write(fast_desc), run_time=step_time)
        self.play(GrowFromCenter(precise_char), Write(precise_desc), run_time=step_time)
        self.play(GrowFromCenter(decisive_char), Write(decisive_desc), run_time=step_time)
        self.play(FadeIn(rule_bg), Write(golden_rule), run_time=step_time)
        self.play(Circumscribe(golden_rule, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 升华/应用 (Apply) - 视觉逻辑：愿景展示 -> 金句总结
        
        口播稿关键词/短语：
        - "写作业、交朋友、管理零花钱" -> 多场景应用
        - "敬畏" -> 核心概念，重点强调
        - "认真对待每一件大事" -> 金句
        
        使用 Circumscribe 强调动画（严禁使用 Indicate）
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、应用场景图标、场景文字、敬畏大字、金句、强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text("敬畏的力量", font=self.title_font, font_size=self.font_title_size, color=GOLD).move_to(UP * 4.0)
        
        # 2. 应用场景图标组（横向排列）
        icon1 = self.load_png_icon("thinking_bubble", height=1.5)  # 思考/写作业
        icon2 = self.load_png_icon("shield", height=1.5)  # 保护/交朋友
        icon3 = self.load_png_icon("money", height=1.5)  # 金钱/零花钱
        
        icons_group = Group(icon1, icon2, icon3).arrange(RIGHT, buff=1.0).move_to(UP * 1.5)
        
        # 3. 场景文字
        scene_labels = VGroup(
            Text("写作业", font=self.body_font, font_size=self.font_small_size, color=WHITE),
            Text("交朋友", font=self.body_font, font_size=self.font_small_size, color=WHITE),
            Text("管零花钱", font=self.body_font, font_size=self.font_small_size, color=WHITE)
        )
        scene_labels[0].next_to(icon1, DOWN, buff=0.3)
        scene_labels[1].next_to(icon2, DOWN, buff=0.3)
        scene_labels[2].next_to(icon3, DOWN, buff=0.3)
        
        # 4. 核心概念 - 敬畏
        respect_text = Text("敬 畏", font=self.title_font, font_size=72, color=GOLD).move_to(DOWN * 1.0)
        
        # 5. 底部金句
        golden_quote = Text("认真对待每一件大事", font=self.title_font, font_size=self.font_title_size, color=ORANGE).move_to(DOWN * 3.5)
        
        # 金句框
        quote_bg = RoundedRectangle(height=1.2, corner_radius=0.4, color=GOLD, fill_opacity=0.15)
        quote_bg.surround(golden_quote, buff=0.4)
        quote_group = VGroup(quote_bg, golden_quote)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(icon1, shift=UP),
                FadeIn(icon2, shift=UP),
                FadeIn(icon3, shift=UP),
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        self.play(
            LaggedStart(
                Write(scene_labels[0]),
                Write(scene_labels[1]),
                Write(scene_labels[2]),
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        self.play(GrowFromCenter(respect_text), run_time=step_time)
        self.play(FadeIn(quote_bg), Write(golden_quote), run_time=step_time)
        self.play(Circumscribe(respect_text, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)
