import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import SunziLessonVertical


class Lesson04VerticalScenes(SunziLessonVertical):
    """
    第4课：庙算 - 成功的预演魔法
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点 (引入) - 视觉逻辑：提出问题 -> 困境展示 -> 差一点点的遗憾
        
        口播稿关键词/短语：
        - "考试前一天才发现没复习" -> exam + clock 组合
        - "手忙脚乱" -> confused 图标
        - "漏洞百出" -> error 图标
        - "差一点点" -> 强调文字动画
        
        动态标题：「说干就干」的陷阱
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、问题文字、考试图标组、困惑图标组、漏洞图标组、底部强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题 (y=4.0) - 不使用 scene_type，根据口播内容生成
        title = Text(
            "「说干就干」的陷阱", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=YELLOW
        ).move_to(UP * 4.0)
        
        # 2. 引入问题 - 你有没有遇到过这种情况？
        question_text = Text(
            "你有没有遇到过……", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(UP * 2.5)
        
        # 3. 中部核心内容 - 考试前一天才发现没复习
        # 图标：exam.png (存在于 all_png_names.txt)
        exam_icon = self.load_png_icon("exam", height=1.8).shift(LEFT * 1.8 + UP * 0.8)
        exam_label = Text(
            "临时抱佛脚", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=GRAY
        ).next_to(exam_icon, DOWN, buff=0.2)
        exam_group = Group(exam_icon, exam_label)
        
        # 图标：confused.png (存在于 all_png_names.txt)
        confused_icon = self.load_png_icon("confused", height=1.8).shift(RIGHT * 1.8 + UP * 0.8)
        confused_label = Text(
            "手忙脚乱", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=GRAY
        ).next_to(confused_icon, DOWN, buff=0.2)
        confused_group = Group(confused_icon, confused_label)
        
        # 图标：error.png (存在于 all_png_names.txt) - 漏洞百出
        error_icon = self.load_png_icon("error", height=1.5).shift(DOWN * 1.5)
        error_label = Text(
            "漏洞百出", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=RED_C
        ).next_to(error_icon, DOWN, buff=0.2)
        error_group = Group(error_icon, error_label)

        # 4. 底部结论 - 差一点点
        bottom_text = Text(
            "明明很努力，却总是差一点点……", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(DOWN * 3.8)

        # 5. 动画序列 - 按口播节奏安排
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(question_text), run_time=step_time)
        self.play(FadeIn(exam_group, shift=UP), run_time=step_time)
        self.play(FadeIn(confused_group, shift=UP), run_time=step_time)
        self.play(FadeIn(error_group, scale=0.5), run_time=step_time)
        self.play(Write(bottom_text), Circumscribe(bottom_text, color=RED), run_time=step_time)
        
        # 6. 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识 (是什么) - 视觉逻辑：引言 -> 兵法原文(分行) -> 具象化解释
        
        口播稿关键词/短语：
        - "未战而庙算胜者，得算多也" -> 兵法原文，GOLD色，仪式感
        - "庙算" -> 核心概念
        - "脑子里演一遍" -> brain/brainstorm_skill 图标
        - "推演战争" -> critical_thinking 图标
        
        动态标题：孙武的「庙算」秘诀
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（引言、原文1、原文2、图标、解释、强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部：孙武说
        who_says = Text(
            "《孙子兵法》说：", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD_A
        ).move_to(UP * 4.2)
        
        # 2. 兵法原文（分行展示，使用「」避免语法错误）
        quote_line1 = Text(
            "「未战而庙算胜者，", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(who_says, DOWN, buff=0.5)
        
        quote_line2 = Text(
            "得算多也」", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(quote_line1, DOWN, buff=0.3)
        
        # 3. 中部图标 - brainstorm_skill.png (存在于 all_png_names.txt)
        # 表达"脑子里演一遍"的概念
        main_icon = self.load_png_icon("brainstorm_skill", height=2.5).move_to(DOWN * 0.3)
        
        # 4. 底部解释 - 一句话解释庙算
        explain_bg = RoundedRectangle(
            corner_radius=0.3, 
            color=ORANGE, 
            fill_opacity=0.15,
            width=7.5,
            height=1.2
        ).move_to(DOWN * 3.5)
        
        explain_text = Text(
            "庙算 = 动手前先在脑子里演一遍！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(DOWN * 3.5)

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
        场景3: 剖析 (为什么) - 视觉逻辑：下棋比喻 -> 高手vs盲棋对比 -> 结论
        
        口播稿关键词/短语：
        - "下棋" -> chessboard 图标
        - "高手下一步棋之前，脑子里已经想了后面五步十步" -> critical_thinking
        - "盲棋" -> 蒙眼/错误状态
        - "多算胜少算，不算必输" -> 核心结论
        
        动态标题：下棋高手的秘密
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、问题、左侧高手、右侧盲棋、VS、底部结论）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题
        title = Text(
            "下棋高手的秘密", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=YELLOW
        ).move_to(UP * 4.0)
        
        # 2. 引入问题
        question = Text(
            "为什么要先算呢？", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(UP * 2.8)
        
        # 3. 左侧 - 高手：想五步十步
        # 图标：critical_thinking.png (存在于 all_png_names.txt)
        master_icon = self.load_png_icon("critical_thinking", height=1.8).shift(LEFT * 2.0 + UP * 0.5)
        master_label = Text(
            "高手", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).next_to(master_icon, UP, buff=0.2)
        master_desc = Text(
            "想五步十步", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=GREEN_C
        ).next_to(master_icon, DOWN, buff=0.2)
        master_group = Group(master_icon, master_label, master_desc)
        
        # 4. 右侧 - 盲棋：不想就落子
        # 图标：confused.png 表示盲目状态
        blind_icon = self.load_png_icon("confused", height=1.8).shift(RIGHT * 2.0 + UP * 0.5)
        blind_label = Text(
            "盲棋", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).next_to(blind_icon, UP, buff=0.2)
        blind_desc = Text(
            "不想就落子", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=RED_C
        ).next_to(blind_icon, DOWN, buff=0.2)
        blind_group = Group(blind_icon, blind_label, blind_desc)
        
        # 5. 中间 VS
        vs_text = Text(
            "VS", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=YELLOW
        ).move_to(UP * 0.5)
        
        # 6. 底部结论
        conclusion_bg = RoundedRectangle(
            corner_radius=0.3, 
            color=GOLD, 
            fill_opacity=0.15,
            width=8.0,
            height=1.0
        ).move_to(DOWN * 3.5)
        
        conclusion = Text(
            "多算胜少算，不算必输！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(question), run_time=step_time)
        self.play(FadeIn(master_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(blind_group, shift=LEFT), run_time=step_time)
        self.play(FadeIn(vs_text, scale=0.5), run_time=step_time)
        self.play(FadeIn(conclusion_bg), Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 策略 (怎么做) - 视觉逻辑：三步预演魔法逐项弹出
        
        口播稿关键词/短语：
        - "三步预演魔法" -> 魔法主题
        - "第一步，画地图" -> map 图标
        - "第二步，找漏洞" -> checklist 图标
        - "第三步，准备B计划" -> planner 图标
        
        动态标题：三步预演魔法
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、步骤1、步骤2、步骤3、总结强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "🪄 三步预演魔法", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=YELLOW
        ).move_to(UP * 4.0)
        
        # 2. 步骤1：画地图 - map.png (存在于 all_png_names.txt)
        step1_icon = self.load_png_icon("map", height=1.5).shift(LEFT * 3 + UP * 1.5)
        step1_num = Text(
            "①", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).next_to(step1_icon, UP, buff=0.15)
        step1_title = Text(
            "画地图", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).next_to(step1_icon, DOWN, buff=0.15)
        step1_desc = Text(
            "把事情拆成小步骤", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=BLUE_C
        ).next_to(step1_title, DOWN, buff=0.1)
        step1_group = Group(step1_icon, step1_num, step1_title, step1_desc)
        
        # 3. 步骤2：找漏洞 - checklist.png (存在于 all_png_names.txt)
        step2_icon = self.load_png_icon("checklist", height=1.5).shift(UP * 1.5)
        step2_num = Text(
            "②", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).next_to(step2_icon, UP, buff=0.15)
        step2_title = Text(
            "找漏洞", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).next_to(step2_icon, DOWN, buff=0.15)
        step2_desc = Text(
            "想想哪里可能出错", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=ORANGE
        ).next_to(step2_title, DOWN, buff=0.1)
        step2_group = Group(step2_icon, step2_num, step2_title, step2_desc)
        
        # 4. 步骤3：准备B计划 - planner.png (存在于 all_png_names.txt)
        step3_icon = self.load_png_icon("planner", height=1.5).shift(RIGHT * 3 + UP * 1.5)
        step3_num = Text(
            "③", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).next_to(step3_icon, UP, buff=0.15)
        step3_title = Text(
            "准备B计划", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).next_to(step3_icon, DOWN, buff=0.15)
        step3_desc = Text(
            "万一出问题怎么办", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=GREEN_C
        ).next_to(step3_title, DOWN, buff=0.1)
        step3_group = Group(step3_icon, step3_num, step3_title, step3_desc)
        
        # 5. 底部总结
        summary_bg = RoundedRectangle(
            corner_radius=0.3, 
            color=PURPLE, 
            fill_opacity=0.15,
            width=7.0,
            height=1.0
        ).move_to(DOWN * 3.0)
        
        summary = Text(
            "画地图 → 找漏洞 → B计划", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=PURPLE
        ).move_to(DOWN * 3.0)

        # 动画序列 - 使用 LaggedStart 实现逐项弹出
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(step1_group, shift=UP), run_time=step_time)
        self.play(FadeIn(step2_group, shift=UP), run_time=step_time)
        self.play(FadeIn(step3_group, shift=UP), run_time=step_time)
        self.play(FadeIn(summary_bg), Write(summary), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 升华 (应用) - 视觉逻辑：金句展示 -> 应用场景 -> 愿景
        
        口播稿关键词/短语：
        - "多算胜少算，而况于无算乎" -> 核心金句，仪式感
        - "考试、比赛、演讲" -> 应用场景
        - "成功不是碰运气，是算出来的" -> 升华结论
        
        动态标题：成功是「算」出来的！
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、金句、应用场景、愿景、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "成功是「算」出来的！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 孙武金句 - 使用金句框强调
        quote_text = Text(
            "「多算胜少算，\n而况于无算乎！」", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD,
            line_spacing=1.2
        ).move_to(UP * 2.0)
        
        quote_bg = RoundedRectangle(
            corner_radius=0.4, 
            color=GOLD, 
            fill_opacity=0.1,
            stroke_width=2
        ).surround(quote_text, buff=0.5)
        
        quote_group = Group(quote_bg, quote_text)
        
        # 3. 应用场景 - 图标展示
        # 图标：exam.png, goal.png, speech.png (均存在于 all_png_names.txt)
        exam_icon = self.load_png_icon("exam", height=1.2).shift(LEFT * 2.5 + DOWN * 0.8)
        exam_label = Text("考试", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(exam_icon, DOWN, buff=0.1)
        
        goal_icon = self.load_png_icon("goal", height=1.2).shift(DOWN * 0.8)
        goal_label = Text("比赛", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(goal_icon, DOWN, buff=0.1)
        
        speech_icon = self.load_png_icon("speech", height=1.2).shift(RIGHT * 2.5 + DOWN * 0.8)
        speech_label = Text("演讲", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(speech_icon, DOWN, buff=0.1)
        
        scene_group = Group(exam_icon, exam_label, goal_icon, goal_label, speech_icon, speech_label)
        
        # 4. 底部愿景
        vision_bg = RoundedRectangle(
            corner_radius=0.3, 
            color=GREEN, 
            fill_opacity=0.2,
            width=7.5,
            height=1.2
        ).move_to(DOWN * 3.5)
        
        vision_text = Text(
            "动手前先在脑子里「演一遍」", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(quote_group, scale=0.8), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(exam_icon), FadeIn(exam_label),
                FadeIn(goal_icon), FadeIn(goal_label),
                FadeIn(speech_icon), FadeIn(speech_label),
                lag_ratio=0.2
            ), 
            run_time=step_time
        )
        self.play(FadeIn(vision_bg), Write(vision_text), run_time=step_time)
        self.play(Circumscribe(vision_text, color=GREEN), Circumscribe(quote_text, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 懿爸锦囊 - 视觉逻辑：问题 -> ABC选项展示
        
        口播稿关键词/短语：
        - "小美明天要参加演讲比赛" -> 场景设定
        - "A：临场发挥" -> 下策（红色）
        - "B：对着镜子练三遍" -> 智慧选项（绿色）
        - "C：模拟正式比赛" -> 智慧选项（绿色）
        
        动态标题：懿爸锦囊
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 15.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、问题、选项A、选项B、选项C、互动引导）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题
        title = Text(
            "🎒 懿爸锦囊", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=YELLOW
        ).move_to(UP * 4.0)
        
        # 2. 问题
        question = Text(
            "小美明天要参加演讲比赛，\n今晚她应该怎么做？", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 2.5)
        
        # 3. 选项A - 下策（红色）
        option_a_bg = RoundedRectangle(
            corner_radius=0.2, 
            color=RED, 
            fill_opacity=0.15,
            width=7.0,
            height=0.9
        ).move_to(UP * 0.8)
        
        option_a = Text(
            "A. 太累了，早点睡，明天临场发挥", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=RED
        ).move_to(UP * 0.8)
        option_a_group = Group(option_a_bg, option_a)
        
        # 4. 选项B - 智慧选项（绿色）
        option_b_bg = RoundedRectangle(
            corner_radius=0.2, 
            color=GREEN, 
            fill_opacity=0.15,
            width=7.0,
            height=0.9
        ).move_to(DOWN * 0.4)
        
        option_b = Text(
            "B. 对着镜子练三遍，想想可能的问题", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=GREEN
        ).move_to(DOWN * 0.4)
        option_b_group = Group(option_b_bg, option_b)
        
        # 5. 选项C - 智慧选项（绿色）
        option_c_bg = RoundedRectangle(
            corner_radius=0.2, 
            color=GREEN, 
            fill_opacity=0.15,
            width=7.0,
            height=0.9
        ).move_to(DOWN * 1.6)
        
        option_c = Text(
            "C. 让爸妈当观众，模拟正式比赛", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=GREEN
        ).move_to(DOWN * 1.6)
        option_c_group = Group(option_c_bg, option_c)
        
        # 6. 底部互动引导
        cta = Text(
            "评论区告诉懿爸，挑战小小谋略家！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(question), run_time=step_time)
        self.play(FadeIn(option_a_group, shift=LEFT), run_time=step_time)
        self.play(FadeIn(option_b_group, shift=LEFT), run_time=step_time)
        self.play(FadeIn(option_c_group, shift=LEFT), run_time=step_time)
        self.play(Write(cta), Circumscribe(cta, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def get_cover_decoration_icons(self):
        """
        根据 build_scene_1 到 build_scene_5 的动画内容中用到的 png 图片，
        选择封面装饰图标，不超过5个。
        所有图标名称必须在 all_png_names.txt 中存在：
        - brainstorm_skill: 庙算/脑子里演一遍 (场景2)
        - critical_thinking: 高手思考 (场景3)
        - map: 画地图 (场景4)
        - checklist: 找漏洞 (场景4)
        - goal: 成功目标 (场景5)
        """
        return ["brainstorm_skill", "critical_thinking", "map", "checklist", "goal"]
