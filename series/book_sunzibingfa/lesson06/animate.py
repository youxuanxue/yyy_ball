import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import SunziLessonVertical


class Lesson06VerticalScenes(SunziLessonVertical):
    """
    第06课：不要添油战术 - 一次准备好，别反复补
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰 (Hook) - 视觉逻辑：引发共鸣 -> 提出问题 -> 抓住注意力
        
        口播稿关键词/短语：
        - "背单词记不住" -> 书本+问号图标
        - "补习班成绩没提高" -> 表示困惑的视觉
        - "努力了为什么不行" -> 灰色调表达困境
        
        动态标题：「越努力越累？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、困境图标、问题文字、强调文字、底部结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题 (y=4.0) - 灰色调表达困境感
        title = Text(
            "越努力越累？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 中部核心内容 - 使用 critical_thinking 表示学习困惑
        # "背单词记不住、补习班没效果" -> 困惑的学习场景
        center_icon = self.load_png_icon("critical_thinking", height=2.5).move_to(UP * 1.0)
        
        # 3. 关键短语：拼命背、没提高
        phrase1 = Text("拼命背", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(LEFT * 2.0 + DOWN * 0.5)
        phrase2 = Text("没提高", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(RIGHT * 2.0 + DOWN * 0.5)
        arrow = Arrow(phrase1.get_right(), phrase2.get_left(), color=GRAY, buff=0.3)
        effort_group = VGroup(phrase1, arrow, phrase2)
        
        # 4. 底部扎心结论 - 引发共鸣
        bottom_text = Text(
            "已经很努力了，为什么还是不行？", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(DOWN * 3.5)

        # 5. 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(center_icon, shift=UP), run_time=step_time)
        self.play(FadeIn(effort_group), run_time=step_time)
        self.play(Write(bottom_text), run_time=step_time)
        self.play(Circumscribe(bottom_text, color=RED), run_time=step_time)
        
        # 6. 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：《孙子兵法》说 -> 兵法原文 -> 白话解释
        
        口播稿关键词/短语：
        - "善用兵者，役不再籍，粮不三载" -> 兵法原文用金色
        - "一次就准备好" -> 核心要点
        - "反复补充越来越累" -> 错误做法
        
        动态标题：「孙武爷爷的智慧」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、原文第一行、原文第二行、图标、解释、强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部：《孙子兵法》说
        who_says = Text(
            "《孙子兵法》说：", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD_A
        ).move_to(UP * 4.2)
        
        # 2. 兵法原文（分行展示）
        quote_line1 = Text(
            "「善用兵者，役不再籍，」", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(who_says, DOWN, buff=0.5)
        
        quote_line2 = Text(
            "「粮不三载」", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(quote_line1, DOWN, buff=0.3)
        
        # 3. 中部图标 - 使用 supply_chain 表示物资运输
        main_icon = self.load_png_icon("supply_chain", height=2.0).move_to(DOWN * 0.3)
        
        # 4. 底部白话解释 - 核心要点
        explain_text = Text(
            "一次准备好，别反复补！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(DOWN * 3.5)
        
        # 金句背景框
        explain_bg = RoundedRectangle(
            height=1.2, 
            corner_radius=0.3, 
            color=ORANGE, 
            fill_opacity=0.15
        )
        explain_bg.surround(explain_text, buff=0.4)

        # 动画序列
        self.play(Write(who_says), run_time=step_time)
        self.play(Write(quote_line1), run_time=step_time)
        self.play(Write(quote_line2), run_time=step_time)
        self.play(FadeIn(main_icon, shift=UP), run_time=step_time)
        self.play(FadeIn(explain_bg), Write(explain_text), run_time=step_time)
        self.play(Circumscribe(explain_text, color=ORANGE), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/为什么重要 (Why) - 视觉逻辑：漏水桶比喻 -> 错误做法 vs 正确做法
        
        口播稿关键词/短语：
        - "漏水的水桶" -> waterbucket 图标
        - "不停加水，水还是漏光" -> 错误做法（红色）
        - "先把洞堵上" -> 正确做法（绿色）
        - "白费力气" -> 强调结论
        
        动态标题：「漏桶的秘密」
        使用左右对比布局
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、水桶图标、错误做法、正确做法、VS对比、底部结论）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text(
            "漏桶的秘密", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 中部核心 - 漏水桶图标
        bucket_icon = self.load_png_icon("waterbucket", height=2.5).move_to(UP * 1.5)
        
        # 3. 左右对比布局
        # 左侧：错误做法（红色）
        wrong_title = Text("❌ 不停加水", font=self.body_font, font_size=self.font_body_size, color=RED)
        wrong_desc = Text("水还是漏光", font=self.body_font, font_size=self.font_small_size, color=GRAY)
        wrong_group = VGroup(wrong_title, wrong_desc).arrange(DOWN, buff=0.2).move_to(LEFT * 2.2 + DOWN * 1.5)
        
        # 右侧：正确做法（绿色）
        right_title = Text("✅ 先堵洞", font=self.body_font, font_size=self.font_body_size, color=GREEN)
        right_desc = Text("然后再加水", font=self.body_font, font_size=self.font_small_size, color=GRAY)
        right_group = VGroup(right_title, right_desc).arrange(DOWN, buff=0.2).move_to(RIGHT * 2.2 + DOWN * 1.5)
        
        # VS 标志
        vs_text = Text("VS", font=self.title_font, font_size=self.font_body_size, color=YELLOW).move_to(DOWN * 1.5)
        
        # 4. 底部结论
        bottom_text = Text(
            "方法不对，补再多也是白费力气！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(bucket_icon, shift=UP), run_time=step_time)
        self.play(FadeIn(wrong_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(right_group, shift=LEFT), run_time=step_time)
        self.play(FadeIn(vs_text, scale=1.5), run_time=step_time)
        self.play(Write(bottom_text), Circumscribe(bottom_text, color=RED), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 策略/怎么做 (How) - 视觉逻辑：三步魔法咒语 -> 逐项弹出
        
        口播稿关键词/短语：
        - "魔法咒语" -> 蓝色调
        - "要不要？怎么做？该不该停？" -> 三个步骤
        - "想清楚、准备好、发现问题先停下来" -> 具体方法
        
        动态标题：「三步魔法咒语」
        使用 LaggedStart 实现逐项弹出
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、三个步骤一起弹出、步骤强调、底部结论、结论强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "三步魔法咒语", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 三个步骤 - 使用图标 + 文字
        # 步骤1：要不要？
        step1_icon = self.load_png_icon("target", height=1.2)
        step1_text = Text("① 要不要做？", font=self.body_font, font_size=self.font_body_size, color=BLUE)
        step1_desc = Text("想清楚再行动", font=self.body_font, font_size=self.font_small_size, color=GRAY)
        step1_content = VGroup(step1_text, step1_desc).arrange(DOWN, buff=0.1)
        step1_group = Group(step1_icon, step1_content).arrange(RIGHT, buff=0.3).move_to(UP * 2.0)
        
        # 步骤2：怎么做？
        step2_icon = self.load_png_icon("brainstorm_skill", height=1.2)
        step2_text = Text("② 怎么做？", font=self.body_font, font_size=self.font_body_size, color=BLUE)
        step2_desc = Text("一次准备好", font=self.body_font, font_size=self.font_small_size, color=GRAY)
        step2_content = VGroup(step2_text, step2_desc).arrange(DOWN, buff=0.1)
        step2_group = Group(step2_icon, step2_content).arrange(RIGHT, buff=0.3).move_to(UP * 0.0)
        
        # 步骤3：该不该停？
        step3_icon = self.load_png_icon("stop_gesture", height=1.2)
        step3_text = Text("③ 该不该停？", font=self.body_font, font_size=self.font_body_size, color=BLUE)
        step3_desc = Text("发现不对先暂停", font=self.body_font, font_size=self.font_small_size, color=GRAY)
        step3_content = VGroup(step3_text, step3_desc).arrange(DOWN, buff=0.1)
        step3_group = Group(step3_icon, step3_content).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.0)
        
        all_steps = Group(step1_group, step2_group, step3_group)
        
        # 3. 底部结论
        bottom_text = Text(
            "别傻傻地一直补！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(step1_group, shift=LEFT),
                FadeIn(step2_group, shift=LEFT),
                FadeIn(step3_group, shift=LEFT),
                lag_ratio=0.3
            ), 
            run_time=step_time * 2
        )
        self.play(Write(bottom_text), run_time=step_time)
        self.play(Circumscribe(bottom_text, color=ORANGE), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 升华/应用 (Apply) - 视觉逻辑：场景扩展 -> 金句总结
        
        口播稿关键词/短语：
        - "交朋友" -> 社交场景
        - "存零花钱" -> coins 图标
        - "真正的小谋略家，懂得在对的时候停下来" -> 金句
        
        动态标题：「小谋略家的智慧」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、场景1、场景2、思考图标、金句、强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text(
            "小谋略家的智慧", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 应用场景展示 - 左右布局
        # 场景1：交朋友
        scene1_icon = self.load_png_icon("handshake", height=1.5)
        scene1_text = Text("交朋友", font=self.body_font, font_size=self.font_body_size, color=BLUE)
        scene1_desc = Text("真心换真心", font=self.body_font, font_size=self.font_small_size, color=GRAY)
        scene1_content = VGroup(scene1_text, scene1_desc).arrange(DOWN, buff=0.1)
        scene1_group = Group(scene1_icon, scene1_content).arrange(DOWN, buff=0.2).move_to(LEFT * 2.2 + UP * 1.5)
        
        # 场景2：存零花钱
        scene2_icon = self.load_png_icon("coins", height=1.5)
        scene2_text = Text("存零花钱", font=self.body_font, font_size=self.font_body_size, color=BLUE)
        scene2_desc = Text("提前计划好", font=self.body_font, font_size=self.font_small_size, color=GRAY)
        scene2_content = VGroup(scene2_text, scene2_desc).arrange(DOWN, buff=0.1)
        scene2_group = Group(scene2_icon, scene2_content).arrange(DOWN, buff=0.2).move_to(RIGHT * 2.2 + UP * 1.5)
        
        # 3. 中部思考图标
        think_icon = self.load_png_icon("brain", height=2.0).move_to(DOWN * 0.5)
        
        # 4. 底部金句
        quote_text = Text(
            "懂得在对的时候停下来", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)
        
        # 金句背景框
        quote_bg = RoundedRectangle(
            height=1.2, 
            corner_radius=0.4, 
            color=GOLD, 
            fill_opacity=0.15
        )
        quote_bg.surround(quote_text, buff=0.5)
        quote_group = VGroup(quote_bg, quote_text)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(scene1_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(scene2_group, shift=LEFT), run_time=step_time)
        self.play(FadeIn(think_icon, scale=0.5), run_time=step_time)
        self.play(FadeIn(quote_group), run_time=step_time)
        self.play(Circumscribe(quote_text, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)
