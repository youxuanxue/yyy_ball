import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson030VerticalScenes(Zsxq100keLessonVertical):
    """
    第030课：见顶信号与购买时机
    主题：五个信号教你逃顶抄底
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)

        口播稿：你最怕什么？在股市最高点冲进去，然后眼睁睁看着一路跌。
                很多人买基金都是追涨杀跌，涨了跟风买，跌了慌忙卖。
                问题出在哪？就是不知道什么时候该停。
                今天教你五个判断大盘是否见顶的信号，学会了这些，你就不会当最后一个接盘的人。

        关键词/短语：
        - "最高点冲进去" -> decrease 图标，灰色恐惧
        - "追涨杀跌" -> 红色错误
        - "五个信号" -> 金色悬念
        - "不当接盘侠" -> 金色转折

        动态标题：「怎么判断大盘见顶？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "怎么判断大盘见顶？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 恐惧图标
        chart_icon = self.load_png_icon("decrease", height=2.0).move_to(UP * 1.5)
        fear_text = Text(
            "最高点冲进去，一路看着跌",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).next_to(chart_icon, DOWN, buff=0.3)
        fear_group = Group(chart_icon, fear_text)

        # 3. 错误做法
        wrong = Text(
            "追涨杀跌，不知道该何时停",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).shift(DOWN * 1.0)

        # 4. 底部悬念
        hook = Text(
            "五个信号帮你逃顶抄底",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(fear_group, shift=UP), run_time=step_time)
        self.play(Write(wrong), run_time=step_time)
        self.play(Write(hook), run_time=step_time)
        self.play(Circumscribe(hook, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)

        口播稿：大盘见顶不是看K线，那太后知后觉了。要看宏观指标。
                第一，融资余额突破三万亿，杠杆太高了。
                第二，公募基金月发行量超三千亿，热钱太多了。
                第三，大盘创新高但换手率没跟上，资金推不动了。
                这三个就是最关键的预警信号。

        关键词/短语：
        - "不是看K线" -> 认知纠正
        - "三个预警信号" -> 逐项展示 红色警示

        动态标题：「三大预警信号」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "三大预警信号",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(UP * 4.0)

        # 2. 认知纠正
        correct = Text(
            "别看K线，看宏观指标",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).move_to(UP * 2.5)

        # 3. 三个信号
        sig1_icon = self.load_png_icon("warning", height=0.8).shift(LEFT * 3.0 + UP * 1.0)
        sig1_text = Text("①融资余额突破3万亿", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(sig1_icon, RIGHT, buff=0.3)
        sig1 = Group(sig1_icon, sig1_text)

        sig2_icon = self.load_png_icon("high_importance", height=0.8).shift(LEFT * 3.0 + DOWN * 0.3)
        sig2_text = Text("②公募月发行超3000亿", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(sig2_icon, RIGHT, buff=0.3)
        sig2 = Group(sig2_icon, sig2_text)

        sig3_icon = self.load_png_icon("exclamation_mark", height=0.8).shift(LEFT * 3.0 + DOWN * 1.6)
        sig3_text = Text("③创新高但换手率不跟", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(sig3_icon, RIGHT, buff=0.3)
        sig3 = Group(sig3_icon, sig3_text)

        signals = [sig1, sig2, sig3]

        # 4. 底部总结
        summary = Text(
            "这三个是最关键的预警",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(correct), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(s, shift=RIGHT) for s in signals], lag_ratio=0.3),
            run_time=step_time
        )
        self.play(Write(summary), run_time=step_time)
        self.play(Circumscribe(summary, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)

        口播稿：还有两个民间信号也很准。
                第四，配资业务火爆，满大街借钱炒股，就是危险信号。
                第五，大妈朋友圈开始晒股票了，基本就是顶了。
                这五个信号像温度计，告诉你市场烧到什么程度。
                目前这些指标都没达到，说明还没见顶，指数跌了反而是上车机会。

        关键词/短语：
        - "配资火爆" -> 红色危险
        - "大妈晒股票" -> 民间信号
        - "温度计" -> 比喻
        - "目前没达到 = 还能上车" -> 绿色积极

        动态标题：「两个民间见顶信号」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "两个民间见顶信号",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(UP * 4.0)

        # 2. 信号四
        sig4_icon = self.load_png_icon("warning", height=1.0).shift(LEFT * 2.5 + UP * 1.5)
        sig4_label = Text("信号四", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(sig4_icon, DOWN, buff=0.2)
        sig4_text = Text("配资火爆，借钱炒股", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(sig4_label, DOWN, buff=0.1)
        sig4 = Group(sig4_icon, sig4_label, sig4_text)

        # 3. 信号五
        sig5_icon = self.load_png_icon("people", height=1.0).shift(RIGHT * 2.5 + UP * 1.5)
        sig5_label = Text("信号五", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(sig5_icon, DOWN, buff=0.2)
        sig5_text = Text("大妈朋友圈晒股票", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(sig5_label, DOWN, buff=0.1)
        sig5 = Group(sig5_icon, sig5_label, sig5_text)

        sigs = Group(sig4, sig5)

        # 4. 当前状态
        current = Text(
            "目前这些指标都没达到",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GREEN
        ).shift(DOWN * 1.0)

        # 5. 底部结论
        conclusion = Text(
            "还没见顶，跌了反而是机会",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GREEN
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(sigs, shift=UP), run_time=step_time)
        self.play(Write(current), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)
        self.play(Circumscribe(conclusion, color=GREEN), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)

        口播稿：什么时候该买？记住一句话：五个指标没达到，指数每次下跌都是机会。
                还有个小技巧，买基金下午三点前下单算当日价格，三点后算次日价格。
                想买低点，就盯着大盘跌的那天下午操作。

        关键词/短语：
        - "指数下跌 = 机会" -> 绿色
        - "下午三点" -> clock 图标，时间技巧
        - "盯着跌的那天" -> 金色策略

        动态标题：「什么时候该买？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "什么时候该买？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 核心规则
        rule = Text(
            "五个指标没达到 → 每次下跌都是机会",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GREEN
        ).move_to(UP * 2.0)
        rule_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=GREEN, fill_opacity=0.1)
        rule_box.surround(rule, buff=0.3)
        rule_group = VGroup(rule_box, rule)

        # 3. 时间技巧
        clock_icon = self.load_png_icon("clock", height=1.0).shift(LEFT * 2.5 + DOWN * 0.3)
        tip_text = Text("下午3点前下单", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(clock_icon, RIGHT, buff=0.3)
        tip_sub = Text("算当日价格", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(tip_text, DOWN, buff=0.1).align_to(tip_text, LEFT)
        tip_group = Group(clock_icon, tip_text, tip_sub)

        # 4. 底部策略
        strategy = Text(
            "盯着大盘跌的那天下午操作",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(rule_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(tip_group, shift=RIGHT), run_time=step_time)
        self.play(Write(strategy), Circumscribe(strategy, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)

        口播稿：给你一个操作清单。
                第一，关注融资余额数据，券商APP就能查。
                第二，每月看公募基金发行规模。
                第三，对比大盘新高和换手率，看是否背离。
                第四，感受身边氛围，人人都在聊股票就要警惕。
                只要这些信号没亮红灯，就大胆逢低买入。

        关键词/短语：
        - "四步操作清单" -> LaggedStart 逐项
        - "信号没亮红灯" -> 绿色积极
        - "大胆逢低买入" -> 金色鼓励

        动态标题：「逃顶抄底操作清单」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：6个动作
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text(
            "逃顶抄底操作清单",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 四步清单
        c1_icon = self.load_png_icon("analytics", height=0.8).shift(LEFT * 3.0 + UP * 2.2)
        c1_text = Text("①查融资余额数据", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(c1_icon, RIGHT, buff=0.3)
        c1 = Group(c1_icon, c1_text)

        c2_icon = self.load_png_icon("bar_chart", height=0.8).shift(LEFT * 3.0 + UP * 0.9)
        c2_text = Text("②看公募月发行规模", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(c2_icon, RIGHT, buff=0.3)
        c2 = Group(c2_icon, c2_text)

        c3_icon = self.load_png_icon("line_chart", height=0.8).shift(LEFT * 3.0 + DOWN * 0.4)
        c3_text = Text("③对比新高和换手率", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(c3_icon, RIGHT, buff=0.3)
        c3 = Group(c3_icon, c3_text)

        c4_icon = self.load_png_icon("people", height=0.8).shift(LEFT * 3.0 + DOWN * 1.7)
        c4_text = Text("④感受身边炒股氛围", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(c4_icon, RIGHT, buff=0.3)
        c4 = Group(c4_icon, c4_text)

        checklist = [c1, c2, c3, c4]

        # 3. 底部金句
        golden = Text(
            "信号没亮红灯，大胆逢低买入",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GREEN
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(c1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(c2, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(c3, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(c4, shift=RIGHT), run_time=step_time)
        self.play(Write(golden), Circumscribe(golden, color=GREEN), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action)

        口播稿：现在的市场就像弹簧被压着，还没到弹起来的时候。
                耐心等，信号来了再跑。点赞关注，咱们下期见。

        动态标题：「耐心等，信号来了再跑」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "耐心等，信号来了再跑",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心比喻
        takeaway = Text(
            "市场像弹簧被压着，还没弹起来",
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
