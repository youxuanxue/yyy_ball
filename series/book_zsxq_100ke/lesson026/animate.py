import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson026VerticalScenes(Zsxq100keLessonVertical):
    """
    第026课：基金买入时机
    主题：指数基金和股票基金什么时候该出手
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)

        口播稿：很多朋友问我，基金我都选好了，到底什么时候买呢？
                上周一买就跌，是不是我运气太差？别急，买基金这件事，时机比选品更重要。
                买对了时间，躺着就赚钱；买错了时间，神仙也救不了。
                今天咱们就聊聊指数基金和股票基金，到底什么时候该出手。

        关键词/短语：
        - "什么时候买" -> clock/calendar 图标
        - "买就跌" -> decrease 图标，灰色焦虑
        - "时机比选品更重要" -> 金色核心
        - "躺着赚钱 vs 神仙也救不了" -> 对比

        动态标题：「基金到底啥时候买？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "基金到底啥时候买？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 时钟图标 + 焦虑
        clock_icon = self.load_png_icon("clock", height=2.0).move_to(UP * 1.5)
        pain_text = Text(
            "一买就跌，运气太差？",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).next_to(clock_icon, DOWN, buff=0.3)
        clock_group = Group(clock_icon, pain_text)

        # 3. 核心观点
        core = Text(
            "时机比选品更重要",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).shift(DOWN * 1.0)

        # 4. 底部对比
        hook = Text(
            "买对躺赚，买错神仙也救不了",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(clock_group, shift=UP), run_time=step_time)
        self.play(Write(core), run_time=step_time)
        self.play(Write(hook), run_time=step_time)
        self.play(Circumscribe(hook, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)

        口播稿：先说指数基金，分两种。沪深三百、中证五百叫宽基指数，跟着大盘涨跌走。
                还有窄基指数，像5G、医药，跟着某个行业走。
                股票型基金不一样，基金经理主动选股换股，哪里有风口追哪里。
                三种基金性格不同，买入时机自然也不一样。

        关键词/短语：
        - "宽基/窄基/股票型" -> 三分类展示
        - "跟大盘走/跟行业走/追风口" -> 区分逻辑

        动态标题：「三种基金三种性格」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "三种基金三种性格",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三种基金分类
        wide_icon = self.load_png_icon("bar_chart", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        wide_text = Text("宽基指数", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(wide_icon, RIGHT, buff=0.3)
        wide_sub = Text("沪深300·跟大盘走", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(wide_text, DOWN, buff=0.1).align_to(wide_text, LEFT)
        wide = Group(wide_icon, wide_text, wide_sub)

        narrow_icon = self.load_png_icon("line_chart", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        narrow_text = Text("窄基指数", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(narrow_icon, RIGHT, buff=0.3)
        narrow_sub = Text("5G·医药·跟行业走", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(narrow_text, DOWN, buff=0.1).align_to(narrow_text, LEFT)
        narrow = Group(narrow_icon, narrow_text, narrow_sub)

        stock_icon = self.load_png_icon("stocks", height=0.8).shift(LEFT * 3.0 + DOWN * 1.4)
        stock_text = Text("股票型基金", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(stock_icon, RIGHT, buff=0.3)
        stock_sub = Text("基金经理追风口", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(stock_text, DOWN, buff=0.1).align_to(stock_text, LEFT)
        stock = Group(stock_icon, stock_text, stock_sub)

        funds = [wide, narrow, stock]

        # 3. 底部结论
        conclusion = Text(
            "性格不同，时机自然不同",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(f, shift=RIGHT) for f in funds], lag_ratio=0.3),
            run_time=2 * step_time
        )
        self.play(Write(conclusion), run_time=step_time)
        self.play(Circumscribe(conclusion, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)

        口播稿：眼下来看，外盘受贸易摩擦和各种不确定因素影响，宽基指数短期机会不大。
                行业指数也在轮动，像电风扇一样转，没有明确方向。
                但股票型基金反而有机会，因为基金经理能不断追踪热点、灵活换股。
                看清大环境再出手，才不会当接盘侠。

        关键词/短语：
        - "贸易摩擦/不确定" -> warning 图标
        - "电风扇一样转" -> 灰色轮动
        - "基金经理灵活换股" -> 金色优势
        - "接盘侠" -> 红色警示

        动态标题：「当前谁有机会？」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "当前谁有机会？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 宽基 - 机会不大
        wide_label = Text("宽基指数", font=self.body_font, font_size=self.font_body_size, color=GRAY).shift(LEFT * 2.0 + UP * 2.0)
        wide_status = Text("短期机会不大", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(wide_label, DOWN, buff=0.1)
        wide_group = VGroup(wide_label, wide_status)

        # 3. 窄基 - 轮动无方向
        narrow_label = Text("窄基指数", font=self.body_font, font_size=self.font_body_size, color=GRAY).shift(RIGHT * 2.0 + UP * 2.0)
        narrow_status = Text("像电风扇在转", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(narrow_label, DOWN, buff=0.1)
        narrow_group = VGroup(narrow_label, narrow_status)

        # 4. 股票型 - 有机会
        stock_icon = self.load_png_icon("positive_dynamic", height=1.5).shift(DOWN * 0.5)
        stock_label = Text("股票型基金", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(stock_icon, DOWN, buff=0.2)
        stock_status = Text("基金经理灵活换股", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(stock_label, DOWN, buff=0.1)
        stock_group = Group(stock_icon, stock_label, stock_status)

        # 5. 底部结论
        conclusion = Text(
            "看清大环境，别当接盘侠",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(wide_group, shift=DOWN), FadeIn(narrow_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(stock_group, shift=UP), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)
        self.play(Circumscribe(conclusion, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)

        口播稿：什么时候买宽基？大盘要涨之前，得提前一两个月埋伏。
                窄基指数呢？等某个行业有持续利好再下手。
                股票型基金随时可以关注，因为总有个股在涨。
                关键是别等到人人都喊牛市时才冲进去。

        关键词/短语：
        - "宽基等大势" -> calendar 图标
        - "窄基看行业" -> search 图标
        - "股票基金随时盯" -> target 图标

        动态标题：「三种基金三种时机」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "三种基金三种时机",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三种时机
        t1_icon = self.load_png_icon("calendar", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        t1_text = Text("宽基：提前埋伏", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(t1_icon, RIGHT, buff=0.3)
        t1_sub = Text("大盘要涨前一两个月", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(t1_text, DOWN, buff=0.1).align_to(t1_text, LEFT)
        t1 = Group(t1_icon, t1_text, t1_sub)

        t2_icon = self.load_png_icon("search", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        t2_text = Text("窄基：等行业利好", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(t2_icon, RIGHT, buff=0.3)
        t2_sub = Text("持续利好再下手", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(t2_text, DOWN, buff=0.1).align_to(t2_text, LEFT)
        t2 = Group(t2_icon, t2_text, t2_sub)

        t3_icon = self.load_png_icon("target", height=0.8).shift(LEFT * 3.0 + DOWN * 1.4)
        t3_text = Text("股票型：随时盯", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(t3_icon, RIGHT, buff=0.3)
        t3_sub = Text("总有个股在涨", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(t3_text, DOWN, buff=0.1).align_to(t3_text, LEFT)
        t3 = Group(t3_icon, t3_text, t3_sub)

        timings = [t1, t2, t3]

        # 3. 底部警告
        warning = Text(
            "别等人人喊牛市才冲进去",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(t, shift=RIGHT) for t in timings], lag_ratio=0.3),
            run_time=2 * step_time
        )
        self.play(Write(warning), run_time=step_time)
        self.play(Circumscribe(warning, color=RED), run_time=step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)

        口播稿：给你一个实操策略。选一只长期业绩靠前的成长价值型基金，
                每当大盘跌的时候就买进一千块。注意别一把梭哈，控制总仓位在可投资额度的百分之二十左右。
                越跌越买，等市场回暖你就赢了。定投加逢低买入，这是普通人最靠谱的打法。

        关键词/短语：
        - "成长价值型基金" -> investment 图标
        - "大盘跌就买1000" -> 绿色策略
        - "别梭哈" -> 红色警告
        - "定投+逢低买入" -> 金色总结

        动态标题：「最靠谱的实操策略」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "最靠谱的实操策略",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 选基金
        fund_icon = self.load_png_icon("investment", height=1.2).move_to(UP * 2.0)
        fund_text = Text(
            "选一只长期业绩靠前的基金",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(fund_icon, DOWN, buff=0.3)
        fund_group = Group(fund_icon, fund_text)

        # 3. 操作方式
        op1 = Text("大盘跌就买1000块", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(UP * 0.0)
        op2 = Text("控制仓位20%左右", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(op1, DOWN, buff=0.3)
        op3 = Text("越跌越买，等回暖", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(op2, DOWN, buff=0.3)

        # 4. 底部金句
        summary = Text(
            "定投 + 逢低买入 = 最靠谱打法",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(fund_group, shift=DOWN), run_time=step_time)
        self.play(Write(op1), Write(op2), Write(op3), run_time=step_time)
        self.play(Write(summary), run_time=step_time)
        self.play(Circumscribe(summary, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action)

        口播稿：记住，宽基等大势，窄基看行业，股票基金随时盯。
                觉得有用就点个赞，关注我，咱们下期继续聊买基金的门道。

        动态标题：「宽基等大势·窄基看行业」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "记住这三句话",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 三句话总结
        line1 = Text("宽基等大势", font=self.body_font, font_size=self.font_body_size, color=BLUE).move_to(UP * 2.0)
        line2 = Text("窄基看行业", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(line1, DOWN, buff=0.4)
        line3 = Text("股票基金随时盯", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(line2, DOWN, buff=0.4)
        lines = VGroup(line1, line2, line3)

        # 3. 互动图标
        like_icon = self.load_png_icon("thumbs_up", height=1.5).move_to(LEFT * 2.5 + DOWN * 1.5)
        like_label = Text("点赞", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_label)

        follow_icon = self.load_png_icon("add_user", height=1.5).move_to(RIGHT * 2.5 + DOWN * 1.5)
        follow_label = Text("关注", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(follow_icon, DOWN, buff=0.2)
        follow_group = Group(follow_icon, follow_label)

        icons_group = Group(like_group, follow_group)

        # 4. 底部口号
        slogan = Text(
            "每天一课，日日生金！",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[Write(l) for l in [line1, line2, line3]], lag_ratio=0.3),
            run_time=step_time
        )
        self.play(FadeIn(icons_group, shift=UP), run_time=step_time)
        self.play(Write(slogan), Circumscribe(slogan, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(6)
        # 结尾画面保持
        self.wait(t_trans)
