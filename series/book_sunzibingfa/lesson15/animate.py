import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import SunziLessonVertical

class Lesson15VerticalScenes(SunziLessonVertical):
    """
    第15课：优势在我 - 准备充分，才能稳操胜券
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """场景1: 痛点 (引入) - 视觉逻辑：临时抱佛脚的困境 -> 考试失败 -> 反思提问"""
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、学生图标、翻书动作、失败结果、提问）
        step_time = (page_duration - t_trans) / 5

        # 动态标题：根据口播核心内容"临时抱佛脚"生成，而非直接使用scene_type
        # 口播关键词："临时抱佛脚"、"考得一塌糊涂" -> 标题："别让努力白费"
        title = Text("别让努力白费", font=self.title_font, font_size=self.font_title_size, color=RED).move_to(UP * 4.0)
        
        # 中部核心：学生晚上翻书的场景
        # 使用 student_male 图标（合法图标，存在于 all_png_names.txt）
        student_icon = self.load_png_icon("student_male", height=2.0).shift(LEFT * 1.5 + UP * 1.0)
        # 使用 book 图标表示翻书（合法图标）
        book_icon = self.load_png_icon("book", height=1.5).next_to(student_icon, RIGHT, buff=0.3)
        # 使用 night 图标表示晚上（合法图标）
        night_icon = self.load_png_icon("night", height=1.2).move_to(UP * 2.5)
        
        # 失败结果：使用 fail 图标（合法图标）
        fail_icon = self.load_png_icon("fail", height=1.8).shift(DOWN * 1.5)
        fail_text = Text("考得一塌糊涂", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(fail_icon, DOWN, buff=0.3)
        
        # 底部提问：强化痛点
        bottom_text = Text("你是不是也这样临时抱佛脚过？", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(DOWN * 4.5)

        # 动画序列：严格按照口播节奏
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(student_icon, shift=UP), FadeIn(night_icon, shift=DOWN), run_time=step_time)
        self.play(FadeIn(book_icon, shift=LEFT), Wiggle(book_icon), run_time=step_time)
        self.play(FadeIn(fail_icon, shift=RIGHT), Write(fail_text), run_time=step_time)
        self.play(Write(bottom_text), Circumscribe(bottom_text), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """场景2: 知识 (是什么) - 视觉逻辑：引言 -> 兵法原文(分行) -> 具象化解释"""
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（引言、原文第一行、原文第二行、解释、图标、强调）
        step_time = (page_duration - t_trans) / 6

        # 顶部：《孙子兵法》说
        who_says = Text("《孙子兵法》说：", font=self.title_font, font_size=self.font_title_size, color=GOLD_A).move_to(UP * 4.2)
        
        # 兵法原文：分行展示，每行独立动画，使用 GOLD 色增强仪式感
        # 口播关键词："以虞待不虞者胜" -> 分行展示
        quote_line1 = Text("'以虞待不虞者胜'", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(UP * 3.0)
        quote_line2 = Text("（虞：准备）", font=self.body_font, font_size=self.font_small_size, color=GOLD_E).next_to(quote_line1, DOWN, buff=0.3)
        
        # 中部：具象化图标 - 使用 planner 图标表示"准备"（合法图标）
        main_icon = self.load_png_icon("planner", height=2.5).shift(DOWN * 0.5)
        
        # 底部：解析文字 - 提取口播关键短语"准备充分的军队，能战胜仓促应战的对手"
        explain_text1 = Text("准备充分的军队", font=self.body_font, font_size=self.font_body_size, color=ORANGE).move_to(DOWN * 3.5)
        explain_text2 = Text("能战胜仓促应战的对手", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(explain_text1, DOWN)

        self.play(Write(who_says), run_time=step_time)
        self.play(Write(quote_line1), run_time=step_time)
        self.play(Write(quote_line2), run_time=step_time)
        self.play(FadeIn(main_icon, shift=UP), run_time=step_time)
        self.play(Write(explain_text1), Write(explain_text2), run_time=step_time)
        self.play(Circumscribe(quote_line1, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """场景3: 剖析 (为什么) - 视觉逻辑：对比布局 -> 提前搭桥 vs 临时找路 -> 结果对比"""
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、左侧蚂蚁搭桥、右侧蚂蚁找路、左侧成功、右侧失败、底部结论）
        step_time = (page_duration - t_trans) / 6

        # 动态标题：根据口播核心比喻"蚂蚁过河搭桥"生成
        title = Text("提前搭桥 vs 临时找路", font=self.title_font, font_size=self.font_title_size, color=YELLOW).move_to(UP * 4.0)
        
        # 左侧：提前搭桥的蚂蚁（成功）
        # 使用 ant 图标（合法图标）
        ant_left = self.load_png_icon("ant", height=1.5).move_to(LEFT * 2.0 + UP * 1.5)
        # 使用几何形状表示桥（因为图标库可能没有桥的图标，用 Rectangle 表示）
        bridge_left = Rectangle(width=2.5, height=1.0, color=GREEN, fill_opacity=0.6).next_to(ant_left, DOWN, buff=0.2)
        success_icon = self.load_png_icon("win", height=1.2).next_to(bridge_left, DOWN, buff=0.3)
        success_text = Text("顺利过河", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(success_icon, DOWN, buff=0.2)
        left_group = Group(ant_left, bridge_left, success_icon, success_text)
        
        # 右侧：临时找路的蚂蚁（失败）
        ant_right = self.load_png_icon("ant", height=1.5).move_to(RIGHT * 2.0 + UP * 1.5)
        # 使用波浪线表示河流（用 Arc 表示）
        river = Arc(radius=1.0, angle=PI, color=BLUE, fill_opacity=0.3).next_to(ant_right, DOWN, buff=0.2)
        fail_icon = self.load_png_icon("fail", height=1.2).next_to(river, DOWN, buff=0.3)
        fail_text = Text("被冲走", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(fail_icon, DOWN, buff=0.2)
        right_group = Group(ant_right, river, fail_icon, fail_text)
        
        # 底部结论：提取口播关键短语"准备充分，就像提前搭好了桥"
        bottom_text1 = Text("准备充分", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(DOWN * 3.5)
        bottom_text2 = Text("提前搭好了桥，让你有路可走", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(bottom_text1, DOWN)
        bottom_box = RoundedRectangle(width=8.5, height=2.0, corner_radius=0.3, color=GOLD, fill_opacity=0.1).surround(Group(bottom_text1, bottom_text2), buff=0.2)
        bottom_group = Group(bottom_box, bottom_text1, bottom_text2)

        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(left_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(right_group, shift=LEFT), run_time=step_time)
        self.play(Indicate(success_icon), Indicate(success_text), run_time=step_time)
        self.play(Indicate(fail_icon), Indicate(fail_text), run_time=step_time)
        self.play(FadeIn(bottom_group, shift=UP), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """场景4: 策略 (怎么做) - 视觉逻辑：三个魔法咒语 -> 逐项弹出 -> 强调效果"""
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：7个动作（标题、咒语1、咒语2、咒语3、强调、总结、整体强调）
        step_time = (page_duration - t_trans) / 7

        # 动态标题：根据口播核心"三个魔法咒语"生成
        title = Text("三个魔法咒语", font=self.title_font, font_size=self.font_title_size, color=PURPLE).move_to(UP * 4.0)
        
        # 使用 magic_lamp 图标作为装饰（合法图标）
        magic_icon = self.load_png_icon("magic_lamp", height=1.5).next_to(title, RIGHT, buff=0.5)
        title_group = Group(title, magic_icon)
        
        # 三个魔法咒语：使用 LaggedStart 实现逐项弹出
        # 咒语1：先停下3秒，问问自己"我要准备什么"
        # 提取口播关键短语："先停下3秒"、"我要准备什么"
        icon1 = self.load_png_icon("stop_gesture", height=1.2).move_to(LEFT * 3 + UP * 2.5)
        text1 = Text("第一：先停下三秒钟", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(icon1, RIGHT, buff=0.3)
        text11 = Text("问问自己'我要准备什么'", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(text1, DOWN, buff=0.3)

        # 注意：icon1 是 ImageMobject，必须使用 Group 而不是 VGroup
        content1 = Group(text1, text11)
        box1 = RoundedRectangle(width=6.0, height=1.5, corner_radius=0.3, color=BLUE, fill_opacity=0.2).move_to(content1.get_center())
        spell1 = Group(icon1, box1, content1)
        
        # 咒语2：把大任务拆成小任务，每天完成一点
        # 提取口播关键短语："把大任务拆成小任务"、"每天完成一点"
        icon2 = self.load_png_icon("split_vertical", height=1.2).move_to(LEFT * 3)
        text2 = Text("第二：把大任务拆小", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(icon2, RIGHT, buff=0.3)
        text22 = Text("每天完成一点", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(text2, DOWN, buff=0.3)
        # 注意：icon2 是 ImageMobject，必须使用 Group 而不是 VGroup
        content2 = Group(text2, text22)
        box2 = RoundedRectangle(width=6.0, height=1.5, corner_radius=0.3, color=GREEN, fill_opacity=0.2).move_to(content2.get_center())
        spell2 = Group(icon2, box2, content2)
        
        # 咒语3：提前一周开始，每天15分钟，比临时熬夜3小时更有效
        # 提取口播关键短语："提前一周开始"、"每天15分钟"、"比临时熬夜3小时更有效"
        icon3 = self.load_png_icon("calendar", height=1.2).move_to(LEFT * 3 + DOWN * 2.5)
        text3 = Text("第三：提前一周开始", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(icon3, RIGHT, buff=0.3)
        text33 = Text("每天15分钟，比临时熬夜更有效", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(text3, DOWN, buff=0.3)
        # 注意：icon3 是 ImageMobject，必须使用 Group 而不是 VGroup
        content3 = Group(text3, text33)
        box3 = RoundedRectangle(width=6.0, height=1.5, corner_radius=0.3, color=ORANGE, fill_opacity=0.2).move_to(content3.get_center())
        spell3 = Group(icon3, box3, content3)
        
        # 底部总结
        bottom_text = Text("提前准备，才是真正的优势", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(DOWN * 4.5)

        self.play(FadeIn(title_group, shift=DOWN), run_time=step_time)
        # 使用 LaggedStart 实现逐项弹出，lag_ratio=0.3
        self.play(LaggedStart(
            GrowFromCenter(spell1),
            GrowFromCenter(spell2),
            GrowFromCenter(spell3),
            lag_ratio=0.3
        ), run_time=step_time * 2)
        self.play(Indicate(spell1), run_time=step_time)
        self.play(Indicate(spell2), run_time=step_time)
        self.play(Indicate(spell3), run_time=step_time)
        self.play(Write(bottom_text), Circumscribe(bottom_text, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """场景5: 升华 (应用) - 视觉逻辑：错误 vs 正确对比 -> 愿景金句"""
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、错误方式、正确方式、对比强调、金句、最终强调）
        step_time = (page_duration - t_trans) / 6

        # 动态标题：根据口播核心"真正的优势"生成
        title = Text("真正的优势", font=self.title_font, font_size=self.font_title_size, color=GOLD).move_to(UP * 4.0)
        
        # 左侧：错误方式 - 临时抱佛脚
        # 提取口播关键短语："临时抱佛脚"
        wrong_icon = self.load_png_icon("night", height=1.8).move_to(LEFT * 2.0 + UP * 1.5)
        wrong_text = Text("临时抱佛脚", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(wrong_icon, DOWN, buff=0.3)
        wrong_cross = Text("✗", font_size=60, color=RED).next_to(wrong_text, DOWN, buff=0.2)
        wrong_group = Group(wrong_icon, wrong_text, wrong_cross)
        
        # 右侧：正确方式 - 提前准备
        right_icon = self.load_png_icon("planner", height=1.8).move_to(RIGHT * 2.0 + UP * 1.5)
        right_text = Text("提前准备", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(right_icon, DOWN, buff=0.3)
        right_check = Text("✓", font_size=60, color=GREEN).next_to(right_text, DOWN, buff=0.2)
        right_group = Group(right_icon, right_text, right_check)
        
        # 中部：应用场景图标
        # 提取口播关键短语："学习、比赛、工作"
        study_icon = self.load_png_icon("book", height=1.0).move_to(LEFT * 1.5 + DOWN * 2.2)
        game_icon = self.load_png_icon("win", height=1.0).move_to(ORIGIN + DOWN * 2.2)
        work_icon = self.load_png_icon("task", height=1.0).move_to(RIGHT * 1.5 + DOWN * 2.2)
        scene_text = Text("学习 · 比赛 · 工作", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(game_icon, DOWN, buff=0.5)
        scene_group = Group(study_icon, game_icon, work_icon, scene_text)
        
        # 底部金句：使用 RoundedRectangle 强调
        # 提取口播关键短语："准备充分的人，才能稳操胜券"
        golden_text = Text("准备充分，稳操胜券", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(DOWN * 4.5)
        golden_box = RoundedRectangle(width=9.0, height=1.5, corner_radius=0.4, color=GOLD, fill_opacity=0.15).surround(golden_text, buff=0.3)
        golden_group = Group(golden_box, golden_text)

        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(wrong_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(right_group, shift=LEFT), run_time=step_time)
        self.play(FadeIn(scene_group, shift=UP), run_time=step_time)
        self.play(FadeIn(golden_group, shift=UP), run_time=step_time)
        # 使用强烈的强调动画
        self.play(Indicate(golden_text, color=GOLD), Circumscribe(golden_box, color=GOLD), run_time=step_time * 2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def get_cover_decoration_icons(self):
        """
        根据 build_scene_1 到 build_scene_5 的动画内容中用到的png图片，选择封面装饰图标，不超过5个
        选择的图标：
        1. planner - 代表"准备"主题
        2. student_male - 代表"学生/学习"场景
        3. calendar - 代表"时间规划"
        4. magic_lamp - 代表"魔法咒语"
        5. win - 代表"成功/优势"
        """
        return ["planner", "student_male", "calendar", "magic_lamp", "win"]

