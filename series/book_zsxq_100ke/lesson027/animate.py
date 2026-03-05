import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson027VerticalScenes(Zsxq100keLessonVertical):
    """
    第027课：客户分级与买入建议
    主题：找到属于你的投资风格
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)

        口播稿：你是不是经常看到别人推荐基金就跟着买，结果别人赚了你亏了？
                原因很简单，每个人的风险承受能力不一样。
                就好比吃辣，有人无辣不欢，有人一口就上火。投资也是一样，适合别人的不一定适合你。
                今天咱们聊聊，怎么找到属于你的投资风格。

        关键词/短语：
        - "别人推荐就买" -> group 图标，灰色
        - "别人赚你亏" -> 红色扎心
        - "吃辣比喻" -> 生活化比喻
        - "找到你的投资风格" -> 金色悬念

        动态标题：「为啥别人赚你却亏？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "为啥别人赚你却亏？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 跟风买基金 -> 亏损
        group_icon = self.load_png_icon("group", height=1.5).move_to(UP * 1.8)
        follow_text = Text(
            "别人推荐就跟着买",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).next_to(group_icon, DOWN, buff=0.3)
        result_text = Text(
            "结果别人赚了你亏了",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).next_to(follow_text, DOWN, buff=0.3)

        top_group = Group(group_icon, follow_text, result_text)

        # 3. 比喻 - 吃辣
        analogy = Text(
            "吃辣有人无辣不欢，有人一口上火",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).shift(DOWN * 1.0)

        # 4. 底部悬念
        hook = Text(
            "找到属于你的投资风格",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(top_group, shift=UP), run_time=step_time)
        self.play(Write(analogy), run_time=step_time)
        self.play(Write(hook), run_time=step_time)
        self.play(Circumscribe(hook, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)

        口播稿：我把投资者分成三类。
                第一类稳健型，希望年赚百分之三十左右，亏损不超百分之二十。
                第二类进取型，追求百分之五十以上回报，能扛百分之三十亏损。
                第三类激进型，就想翻倍，赔了也认。
                你是哪一类？先搞清楚再谈买什么。

        关键词/短语：
        - "三类投资者" -> 颜色递进 绿/蓝/金
        - "收益/亏损比" -> 数据展示
        - "先搞清楚" -> 金色强调

        动态标题：「你是哪类投资人？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "你是哪类投资人？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三类投资者
        type1_icon = self.load_png_icon("safe", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        type1_text = Text("①稳健型", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(type1_icon, RIGHT, buff=0.3)
        type1_sub = Text("年赚30%·最多亏20%", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(type1_text, DOWN, buff=0.1).align_to(type1_text, LEFT)
        type1 = Group(type1_icon, type1_text, type1_sub)

        type2_icon = self.load_png_icon("positive_dynamic", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        type2_text = Text("②进取型", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(type2_icon, RIGHT, buff=0.3)
        type2_sub = Text("年赚50%+·能扛30%亏损", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(type2_text, DOWN, buff=0.1).align_to(type2_text, LEFT)
        type2 = Group(type2_icon, type2_text, type2_sub)

        type3_icon = self.load_png_icon("increase", height=0.8).shift(LEFT * 3.0 + DOWN * 1.4)
        type3_text = Text("③激进型", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(type3_icon, RIGHT, buff=0.3)
        type3_sub = Text("就想翻倍·赔了也认", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(type3_text, DOWN, buff=0.1).align_to(type3_text, LEFT)
        type3 = Group(type3_icon, type3_text, type3_sub)

        types = [type1, type2, type3]

        # 3. 底部结论
        conclusion = Text(
            "先搞清楚自己再谈买什么",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(t, shift=RIGHT) for t in types], lag_ratio=0.3),
            run_time=2 * step_time
        )
        self.play(Write(conclusion), run_time=step_time)
        self.play(Circumscribe(conclusion, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)

        口播稿：为什么分类这么重要？因为买错了类型的基金，你根本拿不住。
                稳健的人买了激进基金，一跌百分之二十就慌了割肉；
                激进的人买了稳健基金，嫌赚得少半途而废。
                结果两头不讨好，什么都是就什么都不是。认清自己，才是投资的第一课。

        关键词/短语：
        - "买错了拿不住" -> 红色错误
        - "稳健买激进 -> 割肉" -> 左侧错误案例
        - "激进买稳健 -> 放弃" -> 右侧错误案例
        - "认清自己" -> 金色核心

        动态标题：「买错基金你根本拿不住」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "买错基金你根本拿不住",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(UP * 4.0)

        # 2. 左右对比：两种错误
        # 左侧 - 稳健买激进
        err1_icon = self.load_png_icon("decrease", height=1.2).shift(LEFT * 2.0 + UP * 1.5)
        err1_text = Text("稳健型买激进基金", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(err1_icon, DOWN, buff=0.2)
        err1_result = Text("跌20%就割肉", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(err1_text, DOWN, buff=0.1)
        err1 = Group(err1_icon, err1_text, err1_result)

        # 右侧 - 激进买稳健
        err2_icon = self.load_png_icon("thumbs_down", height=1.2).shift(RIGHT * 2.0 + UP * 1.5)
        err2_text = Text("激进型买稳健基金", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(err2_icon, DOWN, buff=0.2)
        err2_result = Text("嫌赚少就放弃", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(err2_text, DOWN, buff=0.1)
        err2 = Group(err2_icon, err2_text, err2_result)

        # 3. 结果
        result = Text(
            "两头不讨好",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).shift(DOWN * 1.0)

        # 4. 底部金句
        golden = Text(
            "认清自己，才是投资第一课",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(err1, shift=RIGHT), FadeIn(err2, shift=LEFT), run_time=step_time)
        self.play(Write(result), run_time=step_time)
        self.play(Write(golden), run_time=step_time)
        self.play(Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)

        口播稿：那三类人分别买什么？
                稳健型买沪深三百指数增强基金，大盘跌时分两三次买进。
                进取型买证券全指数基金，等券商板块普跌时入场。
                激进型就选一个最看好的行业，5G、芯片、科技，挑一个就够了。

        关键词/短语：
        - "三类人三种买法" -> 对应关系

        动态标题：「三类人分别买什么」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "三类人分别买什么",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 稳健型
        buy1_icon = self.load_png_icon("bar_chart", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        buy1_text = Text("稳健型 → 沪深300增强", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(buy1_icon, RIGHT, buff=0.3)
        buy1_sub = Text("大盘跌时分批买", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(buy1_text, DOWN, buff=0.1).align_to(buy1_text, LEFT)
        buy1 = Group(buy1_icon, buy1_text, buy1_sub)

        # 3. 进取型
        buy2_icon = self.load_png_icon("stocks", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        buy2_text = Text("进取型 → 证券全指数", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(buy2_icon, RIGHT, buff=0.3)
        buy2_sub = Text("券商普跌时入场", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(buy2_text, DOWN, buff=0.1).align_to(buy2_text, LEFT)
        buy2 = Group(buy2_icon, buy2_text, buy2_sub)

        # 4. 激进型
        buy3_icon = self.load_png_icon("light_bulb", height=0.8).shift(LEFT * 3.0 + DOWN * 1.4)
        buy3_text = Text("激进型 → 重仓一个行业", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(buy3_icon, RIGHT, buff=0.3)
        buy3_sub = Text("5G·芯片·科技选一个", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(buy3_text, DOWN, buff=0.1).align_to(buy3_text, LEFT)
        buy3 = Group(buy3_icon, buy3_text, buy3_sub)

        buys = [buy1, buy2, buy3]

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(buy1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(buy2, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(buy3, shift=RIGHT), run_time=step_time)
        self.wait(step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)

        口播稿：具体怎么操作？稳健型等大盘跌时分批买入，不追高。
                进取型等券商板块普跌时一把买进，买完拿着别动。
                激进型就重仓一个行业，信就信到底，别今天追5G明天追芯片，来回切换只会两头挨打。
                记住：认清自己，只做一类人该做的事。

        关键词/短语：
        - "分批买入" -> 稳健策略
        - "一把买进" -> 进取策略
        - "信就信到底" -> 激进策略
        - "来回切换两头挨打" -> 红色警告

        动态标题：「只做一类人该做的事」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "只做一类人该做的事",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三种操作
        op1 = Text("稳健型：分批买入不追高", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(UP * 2.0)
        op2 = Text("进取型：一把买进拿着别动", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(op1, DOWN, buff=0.5)
        op3 = Text("激进型：重仓一个信到底", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(op2, DOWN, buff=0.5)

        # 3. 警告
        warning = Text(
            "来回切换只会两头挨打",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).shift(DOWN * 1.5)

        # 4. 底部金句
        golden = Text(
            "认清自己，专注一种风格",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(Write(op1), Write(op2), Write(op3), lag_ratio=0.3),
            run_time=2 * step_time
        )
        self.play(Write(warning), run_time=step_time)
        self.play(Write(golden), Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action)

        口播稿：投资没有万能策略，只有适合你的策略。
                点赞关注，下期咱们聊聊怎么把零钱变成真正的财富。

        动态标题：「只有适合你的策略」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "没有万能策略",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "只有适合你的策略",
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

        follow_icon = self.load_png_icon("add_user", height=1.5).move_to(RIGHT * 2.5 + DOWN * 0.5)
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
