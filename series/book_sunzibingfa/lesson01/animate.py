import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import SunziLessonVertical


class Lesson01VerticalScenes(SunziLessonVertical):
    """
    第1课：国之大事 - 做决定前，先问自己四个问题
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点 (引入) - 冲动后悔症
        
        口播稿关键词/短语：
        - "冲动" -> 快速动作 + 红色
        - "零花钱全花了" -> 硬币图标 + 消失动画
        - "和好朋友吵架" -> 愤怒图标
        - "后悔" -> 灰色调 + 缩小动画
        - "冲动后悔症" -> 核心短语，突出显示
        
        动态标题：别让冲动害了你（而非直接使用"痛点"）
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题 + 场景1 + 场景2 + 后悔文字 + 解决方案提示 + 强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题 (y=4.0) - 根据口播内容设计，不是简单的"痛点"
        title = Text(
            "别让冲动害了你", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=YELLOW
        ).move_to(UP * 4.0)
        
        # 2. 中部核心内容：两个场景对比
        # 场景A：冲动花钱 - 使用 coins 图标（all_png_names.txt 中存在）
        coins_icon = self.load_png_icon("coins", height=1.8).shift(LEFT * 2 + UP * 1.5)
        spend_text = Text("零花钱花光", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(coins_icon, DOWN, buff=0.3)
        scene_a = Group(coins_icon, spend_text)
        
        # 场景B：冲动吵架 - 使用 angry 图标（all_png_names.txt 中存在）
        angry_icon = self.load_png_icon("angry", height=1.8).shift(RIGHT * 2 + UP * 1.5)
        fight_text = Text("朋友吵架", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(angry_icon, DOWN, buff=0.3)
        scene_b = Group(angry_icon, fight_text)
        
        # 3. 中间分隔符：VS
        vs_text = Text("VS", font=self.title_font, font_size=self.font_title_size, color=RED).move_to(UP * 1.5)
        
        # 4. 底部：后悔的结果 + 解决方案暗示
        regret_text = Text(
            "冷静下来...后悔了", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(DOWN * 1.0)
        
        # 核心短语突出："冲动后悔症"
        syndrome_text = Text(
            "「冲动后悔症」", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 2.5)
        
        # 底部：解决方案提示
        solution_hint = Text(
            "今天懿爸教你一个古人的智慧", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).move_to(DOWN * 4.0)

        # 5. 动画序列：按口播节奏编排
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(scene_a, shift=RIGHT), FadeIn(vs_text), run_time=step_time)
        self.play(FadeIn(scene_b, shift=LEFT), run_time=step_time)
        self.play(Write(regret_text), run_time=step_time)
        self.play(Write(syndrome_text), Indicate(syndrome_text, color=RED), run_time=step_time)
        self.play(FadeIn(solution_hint, shift=UP), run_time=step_time)
        
        # 6. 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识 (是什么) - 孙子兵法原文
        
        口播稿关键词/短语：
        - "两千多年前" -> 古籍感
        - "孙武" -> 军事大师形象
        - "兵者，国之大事，死生之地，存亡之道，不可不察也" -> 核心原文，GOLD色+仪式感
        - "先想清楚再行动" -> 核心解释
        
        动态标题：古人的智慧（强调历史传承）
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题 + 出处 + 原文第一行 + 原文第二行 + 图标 + 解释）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部：动态标题
        title = Text(
            "古人的智慧", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.2)
        
        # 2. 出处说明
        who_says = Text(
            "《孙子兵法》说：", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD_A
        ).next_to(title, DOWN, buff=0.5)
        
        # 3. 兵法原文（分两行展示，更有仪式感）
        # 原文："兵者，国之大事，死生之地，存亡之道，不可不察也"
        quote_line1 = Text(
            "「兵者，国之大事，", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(who_says, DOWN, buff=0.4)
        
        quote_line2 = Text(
            "死生之地，存亡之道，", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(quote_line1, DOWN, buff=0.2)
        
        quote_line3 = Text(
            "不可不察也。」", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(quote_line2, DOWN, buff=0.2)
        
        # 4. 中部图标：使用 scroll 图标表示古籍（graduation_scroll 在 all_png_names.txt 中存在）
        scroll_icon = self.load_png_icon("graduation_scroll", height=2.5).move_to(DOWN * 0.8)
        
        # 5. 底部解释
        explain_bg = RoundedRectangle(
            corner_radius=0.3, 
            color=ORANGE, 
            fill_opacity=0.2,
            width=8, 
            height=1.2
        ).move_to(DOWN * 3.5)
        
        explain_text = Text(
            "先想清楚，再行动！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(explain_bg.get_center())
        
        explain_group = VGroup(explain_bg, explain_text)

        # 6. 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(who_says), run_time=step_time)
        self.play(Write(quote_line1), run_time=step_time * 0.8)
        self.play(Write(quote_line2), Write(quote_line3), run_time=step_time * 1.2)
        self.play(FadeIn(scroll_icon, shift=UP), run_time=step_time)
        self.play(FadeIn(explain_group), Circumscribe(explain_text, color=ORANGE), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析 (为什么) - 下棋比喻
        
        口播稿关键词/短语：
        - "下棋" -> 棋盘图标
        - "高手" -> 金色/王冠
        - "想好后面几步" -> 前瞻性思维
        - "一步错、步步错" -> 红色警告
        - "满盘皆输" -> 失败结果
        
        动态标题：像高手一样思考
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 1. 顶部动态标题
        title = Text(
            "像高手一样思考", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 中部：棋盘图标（chessboard 在 all_png_names.txt 中存在）
        chess_icon = self.load_png_icon("chessboard", height=3.0).move_to(UP * 1.0)
        
        # 3. 左右对比：新手 vs 高手
        # 左侧：新手思维
        novice_label = Text("新手", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(LEFT * 2.5 + DOWN * 1.5)
        novice_desc = Text("不想就落子", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(novice_label, DOWN, buff=0.2)
        novice_group = VGroup(novice_label, novice_desc)
        
        # 右侧：高手思维
        master_label = Text("高手", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(RIGHT * 2.5 + DOWN * 1.5)
        master_desc = Text("想好再落子", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(master_label, DOWN, buff=0.2)
        master_group = VGroup(master_label, master_desc)
        
        # 4. 底部：核心短语 "一步错、步步错"
        warning_text = Text(
            "一步错、步步错", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.0)
        
        # 5. 底部结论
        conclusion = Text(
            "做决定也是一样的道理", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(DOWN * 4.2)

        # 6. 动画序列
        # 时间管理：6个动作（修正：Write和Wiggle需要分开执行）
        step_time = (page_duration - t_trans) / 6
        
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(chess_icon, scale=0.5), run_time=step_time)
        self.play(FadeIn(novice_group, shift=RIGHT), FadeIn(master_group, shift=LEFT), run_time=step_time)
        # 注意：Write 和 Wiggle 不能同时应用于同一对象，需分开执行
        self.play(Write(warning_text), run_time=step_time)
        self.play(Wiggle(warning_text), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 策略 (怎么做) - 四问魔法
        
        口播稿关键词/短语：
        - "四问魔法" -> 核心策略名
        - "必须做吗？" -> 问题1
        - "有把握吗？" -> 问题2
        - "代价是什么？" -> 问题3
        - "如果失败了怎么办？" -> 问题4
        - "不容易后悔" -> 正向结果
        
        动态标题：四问魔法咒语
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：7个动作（标题 + 4个问题逐个弹出 + 问号图标 + 结论）
        step_time = (page_duration - t_trans) / 7

        # 1. 顶部动态标题
        title = Text(
            "四问魔法咒语", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 问号图标（ask_question 在 all_png_names.txt 中存在）
        question_icon = self.load_png_icon("ask_question", height=2.0).move_to(UP * 2.0)
        
        # 3. 四个问题（使用 LaggedStart 实现逐项弹出）
        questions = [
            ("1️⃣", "必须做吗？"),
            ("2️⃣", "有把握吗？"),
            ("3️⃣", "代价是什么？"),
            ("4️⃣", "失败了怎么办？"),
        ]
        
        question_group = VGroup()
        colors = [BLUE, GREEN, ORANGE, RED]
        
        for i, (num, q_text) in enumerate(questions):
            num_text = Text(num, font_size=self.font_body_size)
            q = Text(q_text, font=self.body_font, font_size=self.font_body_size, color=colors[i])
            item = VGroup(num_text, q).arrange(RIGHT, buff=0.3)
            question_group.add(item)
        
        question_group.arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(DOWN * 0.5)
        
        # 4. 底部结论
        conclusion_bg = RoundedRectangle(
            corner_radius=0.3,
            color=GREEN,
            fill_opacity=0.2,
            width=8,
            height=1.0
        ).move_to(DOWN * 3.8)
        
        conclusion_text = Text(
            "问完再行动，不容易后悔！", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).move_to(conclusion_bg.get_center())
        
        conclusion_group = VGroup(conclusion_bg, conclusion_text)

        # 5. 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(question_icon, scale=0.5), run_time=step_time)
        
        # 使用 LaggedStart 逐个弹出问题，lag_ratio=0.3
        self.play(
            LaggedStart(
                *[FadeIn(q, shift=LEFT) for q in question_group],
                lag_ratio=0.3
            ),
            run_time=step_time * 3
        )
        
        self.play(FadeIn(conclusion_group), run_time=step_time)
        self.play(Indicate(conclusion_text, color=GREEN), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 升华 (应用) - 智慧金句
        
        口播稿关键词/短语：
        - "真正聪明的人" -> 智慧形象
        - "不是冲在最前面的人" -> 反面
        - "想在最前面的人" -> 正面核心
        - "花钱、交朋友、做选择" -> 应用场景
        - "先想后做" -> 核心方法
        - "更有智慧" -> 目标愿景
        
        动态标题：做一个「想在最前面」的人
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "做「想在最前面」的人", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 中部：灯泡图标代表智慧（light_bulb 在 all_png_names.txt 中存在）
        bulb_icon = self.load_png_icon("light_bulb", height=2.5).move_to(UP * 1.5)
        
        # 3. 对比展示
        # 左侧：错误方式
        wrong_text = Text("冲在最前面", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(LEFT * 2 + DOWN * 0.5)
        wrong_cross = Text("✗", font_size=60, color=RED).next_to(wrong_text, LEFT, buff=0.2)
        wrong_group = VGroup(wrong_cross, wrong_text)
        
        # 右侧：正确方式
        right_text = Text("想在最前面", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(RIGHT * 2 + DOWN * 0.5)
        right_check = Text("✓", font_size=60, color=GREEN).next_to(right_text, LEFT, buff=0.2)
        right_group = VGroup(right_check, right_text)
        
        # 4. 应用场景
        scenarios = Text(
            "花钱 · 交朋友 · 做选择", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(DOWN * 2.0)
        
        # 5. 底部金句框
        golden_quote = Text(
            "先想后做，更有智慧", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        )
        
        quote_bg = RoundedRectangle(
            corner_radius=0.4,
            color=GOLD,
            fill_opacity=0.15
        ).surround(golden_quote, buff=0.5)
        
        quote_group = VGroup(quote_bg, golden_quote).move_to(DOWN * 4.2)

        # 6. 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(bulb_icon, scale=0.5), run_time=step_time)
        self.play(FadeIn(wrong_group, shift=RIGHT), FadeIn(right_group, shift=LEFT), run_time=step_time)
        self.play(Write(scenarios), run_time=step_time)
        self.play(
            FadeIn(quote_group), 
            Circumscribe(golden_quote, color=GOLD, buff=0.3),
            run_time=step_time
        )

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def get_cover_decoration_icons(self):
        """
        封面装饰图标：根据课程主题选择
        - brain: 代表思考
        - light_bulb: 代表智慧
        - chessboard: 代表策略
        - crown: 代表"国之大事"
        - graduation_scroll: 代表兵法古籍
        
        所有图标均在 all_png_names.txt 中验证存在
        """
        return ["brain", "light_bulb", "chessboard", "crown", "graduation_scroll"]
