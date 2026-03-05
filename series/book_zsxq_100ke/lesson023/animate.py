import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson023VerticalScenes(Zsxq100keLessonVertical):
    """
    第023课：私募基金
    主题：巴菲特的赚钱方式跟你想的不一样
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)

        口播稿：你知道巴菲特和高瓴资本的张磊，他们靠什么身家百亿吗？
                不是炒股票，而是管私募基金。私募基金这个词听着高大上，
                很多人觉得跟自己没关系。但你必须搞懂它，因为未来你的钱可能会跟它打交道。

        关键词/短语：
        - "巴菲特/张磊" -> businessman 图标
        - "身家百亿" -> stack_of_money 图标
        - "私募基金" -> 金色悬念
        - "你的钱会跟它打交道" -> 灰色焦虑感

        动态标题：「巴菲特靠什么身家百亿？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "巴菲特靠什么身家百亿？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 大佬图标 + 财富
        boss_icon = self.load_png_icon("businessman", height=2.0).move_to(UP * 1.5)
        money_text = Text(
            "不是炒股票",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).next_to(boss_icon, DOWN, buff=0.3)
        boss_group = Group(boss_icon, money_text)

        # 3. 关键短语 - 管私募基金
        answer = Text(
            "而是管私募基金",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).shift(DOWN * 1.0)

        # 4. 底部悬念
        hook = Text(
            "你的钱迟早会跟它打交道",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(boss_group, shift=UP), run_time=step_time)
        self.play(Write(answer), run_time=step_time)
        self.play(Write(hook), run_time=step_time)
        self.play(Circumscribe(hook, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)

        口播稿：私募基金的私，不是私营企业，而是私下不公开。
                它不能像公募基金那样打广告，只能小范围募集。
                出钱的人叫LP，就是有限合伙人，最多只能有49个。
                管钱的人叫GP，就是普通合伙人。
                起投门槛一百万，直接把大多数人拦在外面了。

        关键词/短语：
        - "私下不公开" -> lock/privacy 图标
        - "LP/GP" -> 三方关系
        - "100万门槛" -> 红色强调

        动态标题：「私募 = 私下不公开」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "私募 = 私下不公开",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 核心定义
        definition = Text(
            "不能打广告，小范围募集",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).move_to(UP * 2.5)

        # 3. LP 和 GP 关系图
        lp_icon = self.load_png_icon("group", height=1.2).shift(LEFT * 2.5 + UP * 0.5)
        lp_label = Text("LP 出钱", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(lp_icon, DOWN, buff=0.15)
        lp_sub = Text("最多49人", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(lp_label, DOWN, buff=0.1)
        lp_group = Group(lp_icon, lp_label, lp_sub)

        arrow = Text("→", font=self.title_font, font_size=self.font_title_size, color=WHITE).shift(UP * 0.5)

        gp_icon = self.load_png_icon("manager", height=1.2).shift(RIGHT * 2.5 + UP * 0.5)
        gp_label = Text("GP 管钱", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(gp_icon, DOWN, buff=0.15)
        gp_sub = Text("专业操盘", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(gp_label, DOWN, buff=0.1)
        gp_group = Group(gp_icon, gp_label, gp_sub)

        flow_group = Group(lp_group, arrow, gp_group)

        # 4. 门槛强调
        threshold = Text(
            "起投门槛：100万",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(definition), run_time=step_time)
        self.play(FadeIn(flow_group, shift=UP), run_time=step_time)
        self.play(Write(threshold), run_time=step_time)
        self.play(Circumscribe(threshold, color=RED), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)

        口播稿：私募主要投两种标的。第一种是证券类，帮你炒股，找个专业的人替你操盘。
                第二种厉害了，叫股权投资基金，投的是没上市的企业。
                当年孙正义投阿里就是这种，年化回报几千倍。
                它赚的是两笔钱的乘法：企业利润增长乘以市盈率提高，翻倍再翻倍。

        关键词/短语：
        - "证券类 vs 股权类" -> 左右对比
        - "孙正义投阿里" -> 金色强调案例
        - "翻倍再翻倍" -> 绿色收益

        动态标题：「私募两大赚钱路径」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "私募两大赚钱路径",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 左右对比：证券类 vs 股权类
        # 左侧 - 证券类
        sec_icon = self.load_png_icon("stocks", height=1.2).shift(LEFT * 2.0 + UP * 2.0)
        sec_label = Text("证券类", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(sec_icon, DOWN, buff=0.2)
        sec_sub = Text("帮你炒股操盘", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(sec_label, DOWN, buff=0.1)
        sec_group = Group(sec_icon, sec_label, sec_sub)

        # 右侧 - 股权类
        eq_icon = self.load_png_icon("company", height=1.2).shift(RIGHT * 2.0 + UP * 2.0)
        eq_label = Text("股权类", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(eq_icon, DOWN, buff=0.2)
        eq_sub = Text("投未上市企业", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(eq_label, DOWN, buff=0.1)
        eq_group = Group(eq_icon, eq_label, eq_sub)

        vs_text = Text("VS", font=self.title_font, font_size=self.font_title_size, color=WHITE).shift(UP * 2.0)

        # 3. 案例 - 孙正义投阿里
        case_text = Text(
            "孙正义投阿里 → 回报几千倍",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GREEN
        ).shift(DOWN * 0.5)

        # 4. 底部公式
        formula = Text(
            "利润增长 × 市盈率提高 = 翻倍再翻倍",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(sec_group, shift=RIGHT), FadeIn(vs_text), FadeIn(eq_group, shift=LEFT), run_time=step_time)
        self.play(Write(case_text), run_time=step_time)
        self.play(Write(formula), run_time=step_time)
        self.play(Circumscribe(formula, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)

        口播稿：私募适合什么人呢？说实话，适合那些资产已经积累到一定程度、
                能承受高风险的人。你手里如果只有几十万存款，是你的养老钱救命钱，
                那真不建议碰。因为好项目难找，靠谱的基金管理人更难找。

        关键词/短语：
        - "资产积累到一定程度" -> safe 图标
        - "养老钱救命钱" -> warning 图标，红色
        - "好项目难找" -> 灰色

        动态标题：「私募适合你吗？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "私募适合你吗？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 适合的人
        ok_icon = self.load_png_icon("safe", height=1.2).shift(LEFT * 2.0 + UP * 1.5)
        ok_text = Text("资产积累到位", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(ok_icon, DOWN, buff=0.2)
        ok_sub = Text("能承受高风险", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(ok_text, DOWN, buff=0.1)
        ok_group = Group(ok_icon, ok_text, ok_sub)

        # 不适合的人
        no_icon = self.load_png_icon("warning", height=1.2).shift(RIGHT * 2.0 + UP * 1.5)
        no_text = Text("只有几十万", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(no_icon, DOWN, buff=0.2)
        no_sub = Text("养老钱救命钱别碰", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(no_text, DOWN, buff=0.1)
        no_group = Group(no_icon, no_text, no_sub)

        compare_group = Group(ok_group, no_group)

        # 3. 底部结论
        conclusion = Text(
            "好项目难找，靠谱管理人更难找",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(compare_group, shift=UP), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)
        self.wait(step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)

        口播稿：普通人该怎么做？
                第一，先把基本盘打好，公募基金、指数基金这些低门槛的工具用起来。
                第二，持续学习，看懂商业模式和投资逻辑。
                第三，等你资产到了一定规模，再拿出一小部分闲钱试水私募。
                记住，是闲钱，亏了不心疼的那种。千万别借钱投私募。

        关键词/短语：
        - "公募/指数基金" -> investment_portfolio 图标
        - "持续学习" -> education 图标
        - "闲钱试水" -> coins 图标
        - "千万别借钱" -> 红色警告

        动态标题：「普通人的三步走」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "普通人的三步走",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三步策略
        step1_icon = self.load_png_icon("investment_portfolio", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        step1_text = Text(
            "①先用公募和指数基金",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GREEN
        ).next_to(step1_icon, RIGHT, buff=0.3)
        step1_sub = Text("低门槛打好基本盘", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(step1_text, DOWN, buff=0.1).align_to(step1_text, LEFT)
        step1 = Group(step1_icon, step1_text, step1_sub)

        step2_icon = self.load_png_icon("education", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        step2_text = Text(
            "②持续学习投资逻辑",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(step2_icon, RIGHT, buff=0.3)
        step2_sub = Text("看懂商业模式", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(step2_text, DOWN, buff=0.1).align_to(step2_text, LEFT)
        step2 = Group(step2_icon, step2_text, step2_sub)

        step3_icon = self.load_png_icon("coins", height=0.8).shift(LEFT * 3.0 + DOWN * 1.4)
        step3_text = Text(
            "③闲钱试水私募",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).next_to(step3_icon, RIGHT, buff=0.3)
        step3_sub = Text("亏了不心疼的那种", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(step3_text, DOWN, buff=0.1).align_to(step3_text, LEFT)
        step3 = Group(step3_icon, step3_text, step3_sub)

        steps = [step1, step2, step3]

        # 3. 底部警告
        warning = Text(
            "千万别借钱投私募！",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(s, shift=RIGHT) for s in steps], lag_ratio=0.3),
            run_time=2 * step_time
        )
        self.play(Write(warning), run_time=step_time)
        self.play(Circumscribe(warning, color=RED), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action)

        口播稿：私募离普通人有点远，但理解它能帮你看清财富全貌。
                觉得有用就点个赞，关注我，下期见。

        动态标题：「看清财富全貌」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "看清财富全貌",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "理解私募，理解财富的上层建筑",
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
