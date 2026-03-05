import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson031VerticalScenes(Zsxq100keLessonVertical):
    """
    第031课：融资与融券
    主题：借钱炒股的真相
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：钱不够的焦虑 -> 借钱炒股诱惑 -> 水深警示

        口播稿关键词/短语：
        - "钱不够" -> cash_in_hand 图标 + 灰色焦虑
        - "借钱炒股" -> debt 图标
        - "水有多深" -> warning 图标 + 红色警示

        动态标题：「钱不够还想炒股？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、图标组、借钱文字、底部警示、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题 - 引发共鸣
        title = Text(
            "钱不够还想炒股？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 中部：钱不够的焦虑 - cash_in_hand 图标
        cash_icon = self.load_png_icon("cash_in_hand", height=2.0).move_to(UP * 1.5)
        cash_text = Text(
            "看好股票，兜里没钱",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).next_to(cash_icon, DOWN, buff=0.3)
        cash_group = Group(cash_icon, cash_text)

        # 3. 借钱诱惑
        borrow_text = Text(
            "还真能合法借钱炒股！",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).move_to(DOWN * 0.8)

        # 4. 底部警示 - 水有多深
        warning_text = Text(
            "但这水有多深你根本不知道",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(cash_group, shift=UP), run_time=step_time)
        self.play(Write(borrow_text), run_time=step_time)
        self.play(Write(warning_text), run_time=step_time)
        self.play(Circumscribe(warning_text, color=RED), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：融资=借钱买涨 vs 融券=借股卖跌

        口播稿关键词/短语：
        - "融资" -> 借钱买股（做多）-> GREEN
        - "融券" -> 借股来卖（做空）-> RED
        - "做多做空" -> 左右对比布局

        动态标题：「融资融券是什么？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、融资组、融券组、做多做空标签、底部总结）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "融资融券是什么？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 左侧：融资（做多）- 借钱买涨
        rz_icon = self.load_png_icon("cash_in_hand", height=1.5).move_to(LEFT * 2.0 + UP * 2.0)
        rz_label = Text("融资", font=self.title_font, font_size=self.font_title_size, color=GREEN).next_to(rz_icon, DOWN, buff=0.2)
        rz_desc = Text("借钱买股票", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(rz_label, DOWN, buff=0.2)
        rz_group = Group(rz_icon, rz_label, rz_desc)

        # 3. 右侧：融券（做空）- 借股来卖
        rq_icon = self.load_png_icon("stocks", height=1.5).move_to(RIGHT * 2.0 + UP * 2.0)
        rq_label = Text("融券", font=self.title_font, font_size=self.font_title_size, color=RED).next_to(rq_icon, DOWN, buff=0.2)
        rq_desc = Text("借股票来卖", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(rq_label, DOWN, buff=0.2)
        rq_group = Group(rq_icon, rq_label, rq_desc)

        # 4. 做多做空标签
        duo_text = Text("做多 = 看涨", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(LEFT * 2.0 + DOWN * 1.0)
        kong_text = Text("做空 = 看跌", font=self.body_font, font_size=self.font_body_size, color=RED).shift(RIGHT * 2.0 + DOWN * 1.0)

        # 5. 底部总结
        summary = Text(
            "借钱买涨·借股卖跌",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(rz_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(rq_group, shift=DOWN), run_time=step_time)
        self.play(Write(duo_text), Write(kong_text), run_time=step_time)
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：杠杆双刃剑 -> 赚一倍vs亏一倍

        口播稿关键词/短语：
        - "赚一倍" -> GREEN 正面
        - "亏双倍" -> RED 反面
        - "倾家荡产" -> 红色警示
        - 左右对比布局：赚 vs 亏

        动态标题：「杠杆是把双刃剑」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、赚的一面、亏的一面、底部警示、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "杠杆是把双刃剑",
            font=self.title_font,
            font_size=self.font_title_size,
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 左侧：赚的一面
        profit_icon = self.load_png_icon("profit", height=1.5).move_to(LEFT * 2.0 + UP * 1.8)
        profit_text = Text("借50万赚30万", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(profit_icon, DOWN, buff=0.2)
        profit_rate = Text("收益翻倍 59.4%", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(profit_text, DOWN, buff=0.2)
        profit_group = Group(profit_icon, profit_text, profit_rate)

        # 3. 右侧：亏的一面
        loss_icon = self.load_png_icon("loss", height=1.5).move_to(RIGHT * 2.0 + UP * 1.8)
        loss_text = Text("借50万亏30万", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(loss_icon, DOWN, buff=0.2)
        loss_rate = Text("亏损也翻倍！", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(loss_text, DOWN, buff=0.2)
        loss_group = Group(loss_icon, loss_text, loss_rate)

        # 4. VS 分隔
        vs_text = Text("VS", font=self.title_font, font_size=self.font_title_size, color=WHITE).move_to(UP * 1.8)

        # 5. 底部警示
        bottom_warn = Text(
            "多少人配资加杠杆倾家荡产",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(profit_group, shift=RIGHT), FadeIn(vs_text), run_time=step_time)
        self.play(FadeIn(loss_group, shift=LEFT), run_time=step_time)
        self.play(Write(bottom_warn), run_time=step_time)
        self.play(Circumscribe(bottom_warn, color=RED), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：三大门槛逐项展示

        口播稿关键词/短语：
        - "券商牌照" -> bank_building 图标
        - "带融字的股票" -> stocks 图标
        - "50万+6个月" -> shield 图标

        动态标题：「两融门槛有多高？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、三项门槛、底部结论、等待）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "两融门槛有多高？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三大门槛
        t1_icon = self.load_png_icon("bank_building", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        t1_text = Text("①券商需持有两融牌照", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(t1_icon, RIGHT, buff=0.3)
        t1_sub = Text("全国不到30家有资格", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(t1_text, DOWN, buff=0.1).align_to(t1_text, LEFT)
        t1 = Group(t1_icon, t1_text, t1_sub)

        t2_icon = self.load_png_icon("stocks", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        t2_text = Text("②只有带「融」字的股票", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(t2_icon, RIGHT, buff=0.3)
        t2_sub = Text("一半以上股票不能两融", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(t2_text, DOWN, buff=0.1).align_to(t2_text, LEFT)
        t2 = Group(t2_icon, t2_text, t2_sub)

        t3_icon = self.load_png_icon("shield", height=0.8).shift(LEFT * 3.0 + DOWN * 1.4)
        t3_text = Text("③6个月开户+50万资产", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(t3_icon, RIGHT, buff=0.3)
        t3_sub = Text("借款期限不超6个月", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(t3_text, DOWN, buff=0.1).align_to(t3_text, LEFT)
        t3 = Group(t3_icon, t3_text, t3_sub)

        items = [t1, t2, t3]

        # 3. 底部结论
        conclusion = Text(
            "门槛不低，不是谁都能玩",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(item, shift=RIGHT) for item in items], lag_ratio=0.3),
            run_time=step_time
        )
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        self.wait(step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：普通人别碰杠杆 -> 买基金才靠谱

        口播稿关键词/短语：
        - "别碰杠杆" -> warning 图标 + RED
        - "买公募基金" -> investment_portfolio 图标 + GREEN
        - "学霸替你打工" -> 金色金句

        动态标题：「普通人该怎么做？」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、警示、基金建议、金句、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "普通人该怎么做？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 警示：别碰杠杆
        warn_icon = self.load_png_icon("warning", height=1.5).move_to(UP * 2.0 + LEFT * 2.0)
        warn_text = Text(
            "别碰杠杆！",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).next_to(warn_icon, RIGHT, buff=0.3)
        warn_group = Group(warn_icon, warn_text)

        # 3. 正确做法：买基金
        fund_icon = self.load_png_icon("investment_portfolio", height=1.5).move_to(DOWN * 0.3 + LEFT * 2.0)
        fund_text = Text(
            "老实买公募基金",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GREEN
        ).next_to(fund_icon, RIGHT, buff=0.3)
        fund_sub = Text(
            "学霸替你盯盘，只收1.5%",
            font=self.body_font,
            font_size=self.font_small_size,
            color=GREEN
        ).next_to(fund_text, DOWN, buff=0.1).align_to(fund_text, LEFT)
        fund_group = Group(fund_icon, fund_text, fund_sub)

        # 4. 底部金句
        golden = Text(
            "省心又靠谱才是正道",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(warn_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(fund_group, shift=RIGHT), run_time=step_time)
        self.play(Write(golden), run_time=step_time)
        self.play(Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：双刃剑总结 -> 互动引导

        动态标题：「稳住心态·买基金」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、核心收获、互动图标、口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "稳住心态·买基金",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "杠杆是双刃剑，稳住才是正道",
            font=self.body_font,
            font_size=self.font_body_size,
            color=WHITE
        ).move_to(UP * 2.0)
        takeaway_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=GOLD, fill_opacity=0.1)
        takeaway_box.surround(takeaway, buff=0.3)
        takeaway_group = VGroup(takeaway_box, takeaway)

        # 3. 互动图标
        like_icon = self.load_png_icon("thumbs_up", height=1.5).move_to(LEFT * 2.5 + DOWN * 0.5)
        like_label = Text("点赞", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_label)

        follow_icon = self.load_png_icon("star", height=1.5).move_to(RIGHT * 2.5 + DOWN * 0.5)
        follow_label = Text("关注", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(follow_icon, DOWN, buff=0.2)
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

        self.save_scene_thumbnail(6)
        # 结尾画面保持
        self.wait(t_trans)
