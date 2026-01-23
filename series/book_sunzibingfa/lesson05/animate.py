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
    第5课：做事前先算账
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)

    核心主题：敬畏每一次大挑战，做事前要算清时间、精力、代价
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点 (引入) - 视觉逻辑：展示"虎头蛇尾"的困境

        口播稿关键词/短语：
        - "兴冲冲" -> 快速出现的多个活动图标
        - "三个兴趣班" -> 足球、画画、棋类图标
        - "累趴了" -> 低电量图标 + 灰色调
        - "做不下去" -> 失败图标

        动态标题：「为什么总是半途而废？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：6个动作（标题、三个活动、累趴、结论）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题 (y=4.0) - 根据口播"做不下去"生成
        title = Text(
            "为什么总是半途而废？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=YELLOW
        ).move_to(UP * 4.0)

        # 2. 中部核心内容：三个兴趣班图标（象征"贪多"）
        # 图标：soccer_ball, paint_palette, chessboard（均在 all_png_names.txt 中）
        soccer = self.load_png_icon("soccer_ball", height=1.8).shift(LEFT * 2.5 + UP * 1.5)
        paint = self.load_png_icon("paint_palette", height=1.8).shift(UP * 1.5)
        chess = self.load_png_icon("chessboard", height=1.8).shift(RIGHT * 2.5 + UP * 1.5)
        activities = Group(soccer, paint, chess)

        # 3. "兴冲冲"文字
        excited_text = Text("兴冲冲报了三个班...", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(activities, DOWN, buff=0.5)

        # 4. "累趴了"效果：低电量图标 + 文字（图标：nearly_empty_battery）
        tired_icon = self.load_png_icon("nearly_empty_battery", height=2.0).shift(DOWN * 1.0)
        tired_text = Text("结果累趴了...", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(tired_icon, DOWN, buff=0.3)
        tired_group = Group(tired_icon, tired_text)

        # 5. 底部结论：失败图标 + 问句
        # 图标：fail（在 all_png_names.txt 中）
        fail_icon = self.load_png_icon("fail", height=1.5).shift(DOWN * 3.5 + LEFT * 2.5)
        conclusion = Text("为什么做着做着就放弃了？", font=self.title_font, font_size=self.font_body_size, color=RED).shift(DOWN * 3.5 + RIGHT * 1.0)
        conclusion_group = Group(fail_icon, conclusion)

        # 6. 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        # 三个活动同时快速出现，象征"兴冲冲"
        self.play(
            LaggedStart(
                FadeIn(soccer, shift=DOWN),
                FadeIn(paint, shift=DOWN),
                FadeIn(chess, shift=DOWN),
                lag_ratio=0.2
            ),
            Write(excited_text),
            run_time=step_time
        )
        # 活动变灰，电量耗尽
        self.play(
            activities.animate.set_opacity(0.3),
            FadeOut(excited_text),
            run_time=step_time
        )
        self.play(FadeIn(tired_group, shift=UP), run_time=step_time)
        self.play(
            FadeIn(conclusion_group),
            Circumscribe(conclusion, color=RED),
            run_time=step_time
        )
        self.wait(step_time * 0.5)

        # 7. 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识 (是什么) - 视觉逻辑：兵法原文 + 金钱比喻

        口播稿关键词/短语：
        - "日费千金" -> 金币图标 + 金色文字
        - "十万之师" -> 军队象征
        - "久暴师则国用不足" -> 钱袋空了

        动态标题：「孙武爷爷的算账智慧」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：6个动作
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部：《孙子兵法》说
        who_says = Text("《孙子兵法》说：", font=self.title_font, font_size=self.font_body_size, color=GOLD_A).move_to(UP * 4.2)

        # 2. 兵法原文（分两行，使用「」）
        quote_line1 = Text(
            "「日费千金，",
            font=self.title_font,
            font_size=self.font_body_size,
            color=GOLD
        ).next_to(who_says, DOWN, buff=0.4)
        quote_line2 = Text(
            "然后十万之师举矣。」",
            font=self.title_font,
            font_size=self.font_body_size,
            color=GOLD
        ).next_to(quote_line1, DOWN, buff=0.2)

        # 3. 中部图标：金币堆（图标：stack_of_coins）
        coins_icon = self.load_png_icon("stack_of_coins", height=2.5).move_to(DOWN * 0.3)

        # 4. 第二句兵法
        quote_line3 = Text(
            "「久暴师则国用不足。」",
            font=self.title_font,
            font_size=self.font_body_size,
            color=ORANGE
        ).next_to(coins_icon, DOWN, buff=0.5)

        # 5. 底部解释
        explain_text = Text(
            "打仗太久，钱就不够用了！",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.8)
        explain_bg = RoundedRectangle(height=1.0, corner_radius=0.3, color=RED, fill_opacity=0.15).surround(explain_text, buff=0.3)

        # 动画序列
        self.play(Write(who_says), run_time=step_time)
        self.play(Write(quote_line1), run_time=step_time)
        self.play(Write(quote_line2), run_time=step_time)
        self.play(FadeIn(coins_icon, shift=UP), run_time=step_time)
        self.play(Write(quote_line3), run_time=step_time)
        self.play(
            FadeIn(explain_bg),
            Write(explain_text),
            Circumscribe(explain_text, color=RED),
            run_time=step_time
        )

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析 (为什么) - 视觉逻辑：存钱罐比喻

        口播稿关键词/短语：
        - "存钱罐里的硬币" -> 硬币图标
        - "掏硬币" -> 硬币飞出动画
        - "硬币掏光了" -> 空罐效果
        - "先数数自己有多少硬币" -> 计算器图标

        动态标题：「你的精力存钱罐」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：6个动作
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题
        title = Text(
            "你的精力存钱罐",
            font=self.title_font,
            font_size=self.font_title_size,
            color=YELLOW
        ).move_to(UP * 4.0)

        # 2. 比喻说明
        metaphor = Text(
            "时间和精力 = 存钱罐里的硬币",
            font=self.body_font,
            font_size=self.font_body_size,
            color=WHITE
        ).next_to(title, DOWN, buff=0.6)

        # 3. 存钱罐图标（使用 money_box 或自制）+ 硬币
        # 图标：money_box（在 all_png_names.txt 中）
        piggy = self.load_png_icon("money_box", height=2.5).move_to(LEFT * 1.5 + DOWN * 0.5)

        # 硬币群（图标：coins）
        coin1 = self.load_png_icon("coins", height=1.0).move_to(RIGHT * 1.5 + UP * 0.5)
        coin2 = self.load_png_icon("coins", height=1.0).move_to(RIGHT * 2.5 + DOWN * 0.3)
        coin3 = self.load_png_icon("coins", height=1.0).move_to(RIGHT * 1.8 + DOWN * 1.0)
        coins_group = Group(coin1, coin2, coin3)

        # 4. "做太多事"警告
        warning_text = Text(
            "做太多事 / 拖太久\n→ 硬币很快掏光！",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).move_to(DOWN * 2.5)

        # 5. 底部结论
        conclusion = Text(
            "做大事前，先数数硬币够不够！",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GREEN
        ).move_to(DOWN * 4.0)
        conclusion_bg = RoundedRectangle(height=1.0, corner_radius=0.3, color=GREEN, fill_opacity=0.15).surround(conclusion, buff=0.3)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(metaphor), run_time=step_time)
        self.play(
            FadeIn(piggy, shift=RIGHT),
            LaggedStart(
                FadeIn(coin1, shift=LEFT),
                FadeIn(coin2, shift=LEFT),
                FadeIn(coin3, shift=LEFT),
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        # 硬币飞走动画（象征"掏硬币"）
        self.play(
            coin1.animate.shift(RIGHT * 3 + UP * 2).set_opacity(0),
            coin2.animate.shift(RIGHT * 2 + DOWN * 2).set_opacity(0),
            coin3.animate.shift(RIGHT * 4).set_opacity(0),
            piggy.animate.set_opacity(0.4),
            run_time=step_time
        )
        self.play(Write(warning_text), run_time=step_time)
        self.play(
            FadeIn(conclusion_bg),
            Write(conclusion),
            run_time=step_time
        )

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 策略 (怎么做) - 视觉逻辑：三算法逐项弹出

        口播稿关键词/短语：
        - "三算法" -> 魔法咒语标题
        - "算时间" -> 时钟图标
        - "算精力" -> 电池/能量图标
        - "算代价" -> 天平/计算器图标

        动态标题：「魔法咒语：三算法」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：6个动作
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题
        title = Text(
            "魔法咒语：三算法",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 副标题
        subtitle = Text(
            "做事之前先问自己三个问题",
            font=self.body_font,
            font_size=self.font_body_size,
            color=WHITE
        ).next_to(title, DOWN, buff=0.4)

        # 3. 三个算法项目（图标 + 文字）
        # 图标：clock, battery, calculator（均在 all_png_names.txt 中）

        # 第一项：算时间
        time_icon = self.load_png_icon("clock", height=1.5)
        time_text = Text("算时间：我有多少时间？", font=self.body_font, font_size=self.font_body_size, color=BLUE)
        time_item = Group(time_icon, time_text).arrange(RIGHT, buff=0.3)

        # 第二项：算精力
        energy_icon = self.load_png_icon("battery", height=1.5)
        energy_text = Text("算精力：我能坚持多久？", font=self.body_font, font_size=self.font_body_size, color=GREEN)
        energy_item = Group(energy_icon, energy_text).arrange(RIGHT, buff=0.3)

        # 第三项：算代价
        cost_icon = self.load_png_icon("calculator", height=1.5)
        cost_text = Text("算代价：我要放弃什么？", font=self.body_font, font_size=self.font_body_size, color=ORANGE)
        cost_item = Group(cost_icon, cost_text).arrange(RIGHT, buff=0.3)

        # 排列三项
        items = Group(time_item, energy_item, cost_item).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(ORIGIN)

        # 4. 底部结论
        conclusion = Text(
            "算清楚再开始，不半途而废！",
            font=self.title_font,
            font_size=self.font_title_size,
            color=YELLOW
        ).move_to(DOWN * 3.8)
        conclusion_bg = RoundedRectangle(height=1.0, corner_radius=0.3, color=YELLOW, fill_opacity=0.15).surround(conclusion, buff=0.3)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(subtitle), run_time=step_time)
        # 使用 LaggedStart 逐项弹出
        self.play(
            LaggedStart(
                FadeIn(time_item, shift=RIGHT),
                FadeIn(energy_item, shift=RIGHT),
                FadeIn(cost_item, shift=RIGHT),
                lag_ratio=0.3
            ),
            run_time=step_time * 2
        )
        self.play(
            FadeIn(conclusion_bg),
            Write(conclusion),
            Circumscribe(conclusion, color=YELLOW),
            run_time=step_time
        )
        self.wait(step_time * 0.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 升华 (应用) - 视觉逻辑：高手思维 + 金句

        口播稿关键词/短语：
        - "真正的高手" -> 胜利者图标
        - "知道自己能要什么" -> 目标图标
        - "速战速决" -> 快速/闪电图标
        - "小小谋略家" -> 金牌图标

        动态标题：「高手的秘密」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "高手的秘密",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 对比：贪多 vs 专注
        # 左侧：贪多嚼不烂（使用 X 符号）
        wrong_text = Text("贪多嚼不烂", font=self.body_font, font_size=self.font_body_size, color=RED)
        wrong_cross = Text("✗", font_size=80, color=RED).next_to(wrong_text, LEFT, buff=0.3)
        wrong_group = VGroup(wrong_cross, wrong_text).move_to(LEFT * 2.0 + UP * 2.0)

        # 右侧：集中力量（使用目标图标）
        # 图标：target（在 all_png_names.txt 中）
        right_icon = self.load_png_icon("target", height=1.5)
        right_text = Text("集中力量", font=self.body_font, font_size=self.font_body_size, color=GREEN)
        right_group = Group(right_icon, right_text).arrange(RIGHT, buff=0.3).move_to(RIGHT * 2.0 + UP * 2.0)

        # 3. 中间金句
        quote1 = Text(
            "真正的高手",
            font=self.title_font,
            font_size=self.font_title_size,
            color=WHITE
        ).move_to(UP * 0.3)
        quote2 = Text(
            "知道自己能要什么",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).next_to(quote1, DOWN, buff=0.3)

        # 4. 底部：小小谋略家
        # 图标：gold_medal（在 all_png_names.txt 中）
        medal_icon = self.load_png_icon("gold_medal", height=2.0).move_to(DOWN * 2.5)
        final_text = Text(
            "先算账再行动",
            font=self.title_font,
            font_size=self.font_title_size,
            color=YELLOW
        ).move_to(DOWN * 4.2)
        final_bg = RoundedRectangle(height=1.0, corner_radius=0.4, color=GOLD, fill_opacity=0.2).surround(final_text, buff=0.4)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(
            FadeIn(wrong_group, shift=RIGHT),
            FadeIn(right_group, shift=LEFT),
            run_time=step_time
        )
        self.play(
            Write(quote1),
            Write(quote2),
            run_time=step_time
        )
        self.play(
            GrowFromCenter(medal_icon),
            run_time=step_time
        )
        self.play(
            FadeIn(final_bg),
            Write(final_text),
            Circumscribe(final_text, color=GOLD),
            run_time=step_time
        )

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def get_cover_decoration_icons(self):
        """
        根据 build_scene_1 到 build_scene_5 的动画内容中用到的 png 图片，
        选择封面装饰图标，不超过5个。
        所有图标名称在 all_png_names.txt 中已验证存在。
        """
        return [
            "calculator",      # 三算法核心
            "clock",           # 算时间
            "stack_of_coins",  # 存钱罐比喻
            "target",          # 专注目标
            "gold_medal"       # 小小谋略家
        ]
