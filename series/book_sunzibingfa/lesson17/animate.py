import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import SunziLessonVertical


class Lesson17VerticalScenes(SunziLessonVertical):
    """
    第17课: 功到自然成 - 攻守时机的智慧
    核心兵法: "不可胜者，守也；可胜者，攻也"
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点 (引入) - 急于求成导致失败
        口播关键词: 比赛、考试、急着上场、复习、交卷、搞砸、失败
        视觉逻辑: 困境感 -> 冷色调/灰色调 -> 失败后果
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 6个play动作
        step_time = (page_duration - t_trans) / 6

        # ========== 布局设计 ==========
        
        # 顶部标题 (y=4.0) - 动态标题，非直接使用 scene_type
        # 关键短语提取："急着上场"、"又搞砸了"
        title = Text(
            "别让急躁毁了努力", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=YELLOW
        ).move_to(UP * 4.0)
        
        # 中部：左右对比布局 - 急躁 vs 失败结果
        # 图标: student_male (学生) - 来自 all_png_names.txt
        student_icon = self.load_png_icon("student_male", height=2.0).shift(UP * 1.5 + LEFT * 1.8)
        
        # 关键短语动画: "急着上场"
        rush_text = Text(
            "急着上场", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).next_to(student_icon, DOWN, buff=0.3)
        
        # 图标: sad (失败情绪) - 来自 all_png_names.txt
        sad_icon = self.load_png_icon("sad", height=2.0).shift(UP * 1.5 + RIGHT * 1.8)
        
        # 关键短语动画: "又搞砸了"
        fail_text = Text(
            "又搞砸了！", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=RED
        ).next_to(sad_icon, DOWN, buff=0.3)
        
        # 箭头连接：急躁 -> 失败
        arrow = Arrow(
            student_icon.get_right() + DOWN * 0.5, 
            sad_icon.get_left() + DOWN * 0.5, 
            color=GRAY, 
            stroke_width=4
        )
        
        # 底部结论 (y=-3.5)
        bottom_question = Text(
            "明明很努力，为什么总是失败？", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(DOWN * 3.5)

        # ========== 动画序列 ==========
        # 动作1: 标题淡入
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        # 动作2: 学生图标 + 急着上场
        self.play(
            FadeIn(student_icon, shift=UP), 
            Write(rush_text), 
            run_time=step_time
        )
        # 动作3: 箭头
        self.play(GrowArrow(arrow), run_time=step_time)
        # 动作4: 失败图标 + 搞砸文字
        self.play(
            FadeIn(sad_icon, shift=UP), 
            Write(fail_text), 
            run_time=step_time
        )
        # 动作5: 底部问题
        self.play(Write(bottom_question), run_time=step_time)
        # 动作6: 强调问题
        self.play(Indicate(bottom_question, color=RED), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识 (是什么) - 孙武的攻守智慧
        口播关键词: 孙武、秘密、不可胜者守也、可胜者攻也、条件、防守、进攻
        视觉逻辑: 仪式感 -> GOLD色原文 -> 分行展示
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 6个play动作
        step_time = (page_duration - t_trans) / 6

        # ========== 布局设计 ==========
        
        # 顶部引言
        intro_text = Text(
            "《孙子兵法》说：", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD_A
        ).move_to(UP * 4.2)
        
        # 兵法原文 - 分行展示，增强仪式感
        # 图标: scroll (卷轴) - 来自 all_png_names.txt
        quote_line1 = Text(
            "「不可胜者，守也；」", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 2.5)
        
        quote_line2 = Text(
            "「可胜者，攻也。」", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).next_to(quote_line1, DOWN, buff=0.5)
        
        # 中部图标：shield (防守) 和 sword (进攻) 对比
        # 图标来源: shield, sword - all_png_names.txt
        shield_icon = self.load_png_icon("shield", height=1.8).shift(LEFT * 2.0 + DOWN * 0.5)
        shield_label = Text(
            "守", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).next_to(shield_icon, DOWN, buff=0.2)
        
        sword_icon = self.load_png_icon("sword", height=1.8).shift(RIGHT * 2.0 + DOWN * 0.5)
        sword_label = Text(
            "攻", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).next_to(sword_icon, DOWN, buff=0.2)
        
        # 底部解释
        explain_text = Text(
            "条件不成熟要防守，成熟了再进攻", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(DOWN * 3.5)
        
        # 强调框
        explain_box = SurroundingRectangle(
            explain_text, 
            color=ORANGE, 
            buff=0.3, 
            corner_radius=0.2
        )

        # ========== 动画序列 ==========
        # 动作1: 引言
        self.play(Write(intro_text), run_time=step_time)
        # 动作2: 兵法原文第一行
        self.play(Write(quote_line1), run_time=step_time)
        # 动作3: 兵法原文第二行
        self.play(Write(quote_line2), run_time=step_time)
        # 动作4: 防守和进攻图标同时出现
        self.play(
            FadeIn(shield_icon, shift=RIGHT), 
            Write(shield_label),
            FadeIn(sword_icon, shift=LEFT), 
            Write(sword_label),
            run_time=step_time
        )
        # 动作5: 解释文字
        self.play(Write(explain_text), run_time=step_time)
        # 动作6: 强调框
        self.play(Create(explain_box), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析 (为什么) - 充电宝比喻
        口播关键词: 能量、充电宝、电量、百分之二十、百分之百、没电、出发
        视觉逻辑: 对比布局 -> 低电量 vs 满电量 -> 因果关系
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 6个play动作
        step_time = (page_duration - t_trans) / 6

        # ========== 布局设计 ==========
        
        # 顶部标题
        title = Text(
            "像充电宝一样积蓄能量", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=YELLOW
        ).move_to(UP * 4.0)
        
        # 左侧：低电量场景
        # 图标: nearly_empty_battery - all_png_names.txt
        low_battery = self.load_png_icon("nearly_empty_battery", height=2.0).shift(LEFT * 2.0 + UP * 1.0)
        low_label = Text(
            "20%电量", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=RED
        ).next_to(low_battery, DOWN, buff=0.3)
        low_result = Text(
            "很快没电！", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=GRAY
        ).next_to(low_label, DOWN, buff=0.2)
        low_group = Group(low_battery, low_label, low_result)
        
        # 右侧：满电量场景
        # 图标: charged_battery - all_png_names.txt
        full_battery = self.load_png_icon("charged_battery", height=2.0).shift(RIGHT * 2.0 + UP * 1.0)
        full_label = Text(
            "100%电量", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).next_to(full_battery, DOWN, buff=0.3)
        full_result = Text(
            "能用很久！", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=GREEN
        ).next_to(full_label, DOWN, buff=0.2)
        full_group = Group(full_battery, full_label, full_result)
        
        # VS 文字
        vs_text = Text(
            "VS", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=WHITE
        ).move_to(UP * 1.0)
        
        # 底部结论
        conclusion = Text(
            "充满电再出发，才能走得更远！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)
        
        conclusion_box = RoundedRectangle(
            width=8, 
            height=1.2, 
            corner_radius=0.3, 
            color=GOLD, 
            fill_opacity=0.1
        ).move_to(conclusion)

        # ========== 动画序列 ==========
        # 动作1: 标题
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        # 动作2: 低电量场景
        self.play(
            FadeIn(low_battery, shift=UP), 
            Write(low_label), 
            run_time=step_time
        )
        # 动作3: VS + 低电量结果
        self.play(
            GrowFromCenter(vs_text), 
            FadeIn(low_result), 
            run_time=step_time
        )
        # 动作4: 满电量场景
        self.play(
            FadeIn(full_battery, shift=UP), 
            Write(full_label), 
            run_time=step_time
        )
        # 动作5: 满电量结果
        self.play(FadeIn(full_result), run_time=step_time)
        # 动作6: 底部结论 + 框
        self.play(
            Write(conclusion), 
            Create(conclusion_box), 
            run_time=step_time
        )
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 策略 (怎么做) - 三个魔法咒语
        口播关键词: 魔法咒语、问自己、准备好了吗、练功、小蚂蚁、存粮食、时机、全力出击
        视觉逻辑: LaggedStart 逐项弹出 -> 递进布局
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 5个play动作
        step_time = (page_duration - t_trans) / 5

        # ========== 布局设计 ==========
        
        # 顶部标题
        title = Text(
            "三个魔法咒语", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=YELLOW
        ).move_to(UP * 4.0)
        
        # 策略1: 问自己
        # 图标: ask_question - all_png_names.txt
        icon1 = self.load_png_icon("ask_question", height=1.2).shift(LEFT * 3.0 + UP * 1.8)
        text1 = Text(
            "①问自己：\n  准备好了吗？", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE,
            line_spacing=1.2
        ).next_to(icon1, RIGHT, buff=0.3)
        item1 = Group(icon1, text1)
        
        # 策略2: 安静练功
        # 图标: ant - all_png_names.txt (像小蚂蚁存粮食)
        icon2 = self.load_png_icon("ant", height=1.2).shift(LEFT * 3.0 + DOWN * 0.2)
        text2 = Text(
            "②没准备好，\n  像蚂蚁存粮食", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE,
            line_spacing=1.2
        ).next_to(icon2, RIGHT, buff=0.3)
        item2 = Group(icon2, text2)
        
        # 策略3: 全力出击
        # 图标: target - all_png_names.txt
        icon3 = self.load_png_icon("target", height=1.2).shift(LEFT * 3.0 + DOWN * 2.2)
        text3 = Text(
            "③时机到了，\n  全力出击！", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE,
            line_spacing=1.2
        ).next_to(icon3, RIGHT, buff=0.3)
        item3 = Group(icon3, text3)
        
        # 底部强调
        footer = Text(
            "功到自然成，急不得！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(DOWN * 4.0)

        # ========== 动画序列 ==========
        # 动作1: 标题
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        # 动作2-4: 三个策略使用 LaggedStart 逐项弹出
        self.play(
            LaggedStart(
                FadeIn(item1, shift=RIGHT),
                FadeIn(item2, shift=RIGHT),
                FadeIn(item3, shift=RIGHT),
                lag_ratio=0.3
            ),
            run_time=step_time * 2
        )
        # 动作5: 底部强调
        self.play(Write(footer), run_time=step_time)
        # 动作6: 闪烁强调
        self.play(Indicate(footer, color=GOLD), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 升华 (应用) - 善守善攻的智慧
        口播关键词: 孙武、智慧、善守者、九地之下、善攻者、九天之上、等待、胜利、功到自然成
        视觉逻辑: 愿景金句 -> 强调动画 (Circumscribe)
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 6个play动作
        step_time = (page_duration - t_trans) / 6

        # ========== 布局设计 ==========
        
        # 顶部标题
        title = Text(
            "孙武的终极智慧", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 兵法原文 - 分两行
        quote1 = Text(
            "「善守者藏于九地之下，」", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).move_to(UP * 2.2)
        
        quote2 = Text(
            "「善攻者动于九天之上。」", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).next_to(quote1, DOWN, buff=0.4)
        
        # 中部图标：winner (胜利者)
        # 图标: winner - all_png_names.txt
        winner_icon = self.load_png_icon("winner", height=2.5).move_to(DOWN * 0.5)
        
        # 底部金句框
        golden_text = Text(
            "会等待的人，才能赢得最大的胜利！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(DOWN * 3.2)
        
        golden_box = RoundedRectangle(
            width=8, 
            height=1.3, 
            corner_radius=0.3, 
            color=GOLD, 
            fill_opacity=0.15,
            stroke_width=3
        ).move_to(golden_text)
        
        # 最终口号
        slogan = Text(
            "功到自然成！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=YELLOW
        ).move_to(DOWN * 4.5)

        # ========== 动画序列 ==========
        # 动作1: 标题
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        # 动作2: 兵法原文第一行
        self.play(Write(quote1), run_time=step_time)
        # 动作3: 兵法原文第二行
        self.play(Write(quote2), run_time=step_time)
        # 动作4: 胜利者图标
        self.play(FadeIn(winner_icon, scale=0.5), run_time=step_time)
        # 动作5: 金句 + 框
        self.play(
            Write(golden_text), 
            Create(golden_box), 
            run_time=step_time
        )
        # 动作6: 最终口号 + 强调
        self.play(
            Write(slogan), 
            Circumscribe(golden_box, color=GOLD), 
            run_time=step_time
        )
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def get_cover_decoration_icons(self):
        """
        封面装饰图标 - 根据动画内容选择
        选用图标来源于 all_png_names.txt:
        - shield: 代表"守"
        - sword: 代表"攻"
        - charged_battery: 代表充电宝/积蓄力量
        - winner: 代表胜利
        - target: 代表目标
        """
        return ["shield", "sword", "charged_battery", "winner", "target"]
