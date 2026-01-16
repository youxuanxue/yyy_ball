import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import SunziLessonVertical


class Lesson03VerticalScenes(SunziLessonVertical):
    """
    第3课：聪明人不硬碰硬
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点 (引入) - 视觉逻辑：困境展示 -> 硬拼场景 -> 失败后果
        
        口播稿关键词/短语：
        - "考试/不会的题/死盯" -> confused 图标 + 灰色调
        - "比赛/硬拼/输得更惨" -> clenched_fist 图标 + 红色警示
        
        动态标题：「死磕≠努力」- 揭示硬碰硬的问题
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、困惑图标、死盯文字、拳头图标、输更惨文字、强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题 (y=4.0) - 揭示痛点
        title = Text(
            "死磕 ≠ 努力", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 左侧：考试困惑场景
        # 图标：confused 在 all_png_names.txt 第1493行
        confused_icon = self.load_png_icon("confused", height=2.0).move_to(LEFT * 1.8 + UP * 1.5)
        confused_text = Text(
            "死盯难题", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).next_to(confused_icon, DOWN, buff=0.3)
        confused_group = Group(confused_icon, confused_text)

        # 3. 右侧：比赛硬拼场景
        # 图标：clenched_fist 在 all_png_names.txt 第1304行
        fist_icon = self.load_png_icon("clenched_fist", height=2.0).move_to(RIGHT * 1.8 + UP * 1.5)
        fist_text = Text(
            "正面硬拼", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).next_to(fist_icon, DOWN, buff=0.3)
        fist_group = Group(fist_icon, fist_text)

        # 4. 底部结论 - 失败后果
        result_text = Text(
            "结果：输得更惨！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.5)

        # 5. 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(confused_group, shift=UP), run_time=step_time)
        self.play(Write(confused_text), run_time=step_time)
        self.play(FadeIn(fist_group, shift=UP), run_time=step_time)
        self.play(Write(result_text), run_time=step_time)
        self.play(Indicate(result_text, color=RED, scale_factor=1.2), run_time=step_time)
        
        # 6. 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识 (是什么) - 视觉逻辑：引言 -> 兵法原文 -> 核心解释
        
        口播稿关键词/短语：
        - "孙武爷爷说" -> scroll 卷轴图标
        - "「兵者，诡道也」" -> 金色原文，仪式感
        - "变化、灵活" -> change 图标
        - "「因利制权」" -> 制造有利形势
        
        动态标题：「兵法真谛」- 揭示诡道的真正含义
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（引言、原文1、原文2、图标、解释、强调）
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
            "「兵者，诡道也」", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).next_to(who_says, DOWN, buff=0.5)
        
        quote_line2 = Text(
            "「因利制权」", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).next_to(quote_line1, DOWN, buff=0.3)
        
        # 3. 中部图标 - 变化/灵活
        # 图标：change 在 all_png_names.txt 第1154行
        change_icon = self.load_png_icon("change", height=2.2).move_to(DOWN * 0.5)
        
        # 4. 底部解释 - 核心含义
        explain_text = Text(
            "诡 = 变化、灵活", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(DOWN * 3.0)
        
        explain_text2 = Text(
            "制造对自己有利的形势", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).next_to(explain_text, DOWN, buff=0.3)

        # 动画序列
        self.play(Write(who_says), run_time=step_time)
        self.play(Write(quote_line1), run_time=step_time)
        self.play(Write(quote_line2), run_time=step_time)
        self.play(FadeIn(change_icon, scale=0.5), run_time=step_time)
        self.play(Write(explain_text), run_time=step_time)
        self.play(Write(explain_text2), Circumscribe(explain_text, color=ORANGE), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析 (为什么) - 视觉逻辑：石头比喻 -> 硬推vs借势 -> 造势概念
        
        口播稿关键词/短语：
        - "推一块大石头/硬推推不动" -> 用几何形状表示石头（无合适图标）
        - "山坡上/滚下去" -> mountain 图标 + 箭头动画
        - "势不可挡" -> 强调动画
        - "造势" -> 核心金句
        
        动态标题：「借势的智慧」- 巧劲胜蛮力
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、石头硬推、山坡、石头滚动、结论、强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题
        title = Text(
            "借势的智慧", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 左侧：硬推场景（使用圆形代替石头，因为无合适图标）
        stone_left = Circle(radius=0.6, color=GRAY, fill_opacity=0.8).move_to(LEFT * 2.0 + UP * 1.5)
        push_text = Text(
            "硬推？", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).next_to(stone_left, DOWN, buff=0.3)
        cross_mark = Text(
            "✗", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).next_to(push_text, DOWN, buff=0.2)
        left_group = VGroup(stone_left, push_text, cross_mark)

        # 3. 右侧：借势场景 - 山坡 + 石头滚动
        # 图标：mountain 在 all_png_names.txt 第3981行
        mountain_icon = self.load_png_icon("mountain", height=2.5).move_to(RIGHT * 1.5 + UP * 0.5)
        
        # 石头在山顶
        stone_right = Circle(radius=0.4, color=GOLD, fill_opacity=0.9).move_to(RIGHT * 0.8 + UP * 2.0)
        
        # 箭头表示滚动方向
        roll_arrow = Arrow(
            start=RIGHT * 0.8 + UP * 1.5,
            end=RIGHT * 2.2 + DOWN * 0.5,
            color=GOLD,
            stroke_width=4
        )
        
        roll_text = Text(
            "轻轻一推", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).move_to(RIGHT * 1.8 + DOWN * 1.5)
        
        check_mark = Text(
            "✓", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GREEN
        ).next_to(roll_text, DOWN, buff=0.2)

        # 4. 底部金句
        conclusion = Text(
            "「造势」= 借助有利形势", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(left_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(mountain_icon, shift=UP), FadeIn(stone_right), run_time=step_time)
        # 石头滚动动画
        self.play(
            stone_right.animate.move_to(RIGHT * 2.2 + DOWN * 0.3),
            Create(roll_arrow),
            run_time=step_time
        )
        self.play(Write(roll_text), Write(check_mark), run_time=step_time)
        self.play(Write(conclusion), Indicate(conclusion, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 策略 (怎么做) - 视觉逻辑：三个魔法咒语逐项弹出
        
        口播稿关键词/短语：
        - "三个魔法咒语" -> sparkler 图标
        - "藏起实力" -> hide 图标
        - "找他的弱点" -> target 图标
        - "等最好的时机" -> clock 图标
        
        动态标题：「三个魔法咒语」- 行动指南
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、咒语1、咒语2、咒语3、总强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        # 图标：sparkler 在 all_png_names.txt 第5478行
        title_icon = self.load_png_icon("sparkler", height=1.0).move_to(UP * 4.5 + LEFT * 2.5)
        title = Text(
            "三个魔法咒语", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=PURPLE
        ).move_to(UP * 4.0)
        title_group = Group(title_icon, title)

        # 2. 咒语1：藏起实力
        # 图标：hide 在 all_png_names.txt 第2976行
        hide_icon = self.load_png_icon("hide", height=1.2).move_to(LEFT * 2.5 + UP * 1.8)
        spell1_num = Text(
            "①", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(hide_icon, LEFT, buff=0.3)
        spell1_text = Text(
            "藏起实力，不要炫耀", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).next_to(hide_icon, RIGHT, buff=0.3)
        spell1_group = Group(spell1_num, hide_icon, spell1_text)

        # 3. 咒语2：找弱点
        # 图标：target 在 all_png_names.txt 第5758行
        target_icon = self.load_png_icon("target", height=1.2).move_to(LEFT * 2.5 + UP * 0.0)
        spell2_num = Text(
            "②", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(target_icon, LEFT, buff=0.3)
        spell2_text = Text(
            "避开强处，找他弱点", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).next_to(target_icon, RIGHT, buff=0.3)
        spell2_group = Group(spell2_num, target_icon, spell2_text)

        # 4. 咒语3：等时机
        # 图标：clock 在 all_png_names.txt 第1320行
        clock_icon = self.load_png_icon("clock", height=1.2).move_to(LEFT * 2.5 + DOWN * 1.8)
        spell3_num = Text(
            "③", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(clock_icon, LEFT, buff=0.3)
        spell3_text = Text(
            "准备充分，等时机出手", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).next_to(clock_icon, RIGHT, buff=0.3)
        spell3_group = Group(spell3_num, clock_icon, spell3_text)

        # 5. 底部强调框
        all_spells = Group(spell1_group, spell2_group, spell3_group)
        
        # 动画序列 - 使用 LaggedStart 实现逐项弹出
        self.play(FadeIn(title_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(spell1_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(spell2_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(spell3_group, shift=RIGHT), run_time=step_time)
        # 整体闪烁强调
        self.play(
            Indicate(spell1_text, color=GOLD),
            Indicate(spell2_text, color=GOLD),
            Indicate(spell3_text, color=GOLD),
            run_time=step_time
        )

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 升华 (应用) - 视觉逻辑：兵法金句 -> 高手定义 -> 人生应用
        
        口播稿关键词/短语：
        - "「攻其无备，出其不意」" -> 兵法原文
        - "真正的高手/最会找机会的" -> winner 图标
        - "巧劲胜过蛮力，灵活胜过僵硬" -> 核心金句
        
        动态标题：「高手的秘密」- 升华主题
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（兵法原文、图标、高手定义、金句框、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部兵法原文
        quote = Text(
            "「攻其无备，出其不意」", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 中部图标 + 高手定义
        # 图标：winner 在 all_png_names.txt 第6411行
        winner_icon = self.load_png_icon("winner", height=2.5).move_to(UP * 1.0)
        
        definition = Text(
            "真正的高手 = 最会找机会的人", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).next_to(winner_icon, DOWN, buff=0.5)

        # 3. 底部金句框
        golden_line1 = Text(
            "巧劲胜过蛮力", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        )
        golden_line2 = Text(
            "灵活胜过僵硬", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).next_to(golden_line1, DOWN, buff=0.2)
        golden_group = VGroup(golden_line1, golden_line2).move_to(DOWN * 2.8)
        
        # 金句背景框
        quote_bg = RoundedRectangle(
            corner_radius=0.4, 
            color=GOLD, 
            fill_opacity=0.15,
            stroke_width=2
        ).surround(golden_group, buff=0.5)

        # 动画序列
        self.play(Write(quote), run_time=step_time)
        self.play(FadeIn(winner_icon, scale=0.5), run_time=step_time)
        self.play(Write(definition), run_time=step_time)
        self.play(
            FadeIn(quote_bg),
            Write(golden_line1),
            Write(golden_line2),
            run_time=step_time
        )
        self.play(
            Circumscribe(golden_group, color=GOLD, time_width=2),
            run_time=step_time
        )

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def get_cover_decoration_icons(self):
        """
        根据 build_scene_1 到 build_scene_5 的动画内容中用到的 png 图片，
        选择封面装饰图标，不超过5个。
        所有图标名称必须在 all_png_names.txt 中存在：
        - confused (第1493行)
        - change (第1154行)
        - mountain (第3981行)
        - target (第5758行)
        - winner (第6411行)
        """
        return ["confused", "change", "mountain", "target", "winner"]
