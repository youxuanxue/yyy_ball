import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson036VerticalScenes(Zsxq100keLessonVertical):
    """
    第036课：企业估值的秘密
    主题：市盈率、市梦率与几倍退出
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：公司值多少钱？你搞不清楚

        口播稿关键词/短语：
        - "估值十亿百亿" -> money_bag_with_coins 图标
        - "锅碗瓢盆容易定价" -> shopping_cart 图标
        - "水可就深了" -> 灰色调焦虑感

        动态标题：「公司到底值多少钱？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、估值新闻、定价容易、公司定价难、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题 - 引发好奇
        title = Text(
            "公司到底值多少钱？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 估值新闻场景 - "估值十亿百亿"
        news_icon = self.load_png_icon("money_bag_with_coins", height=2.0).move_to(UP * 1.8)
        news_text = Text(
            "某公司估值十亿、百亿",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).next_to(news_icon, DOWN, buff=0.3)
        news_group = Group(news_icon, news_text)

        # 3. 锅碗瓢盆容易定价 vs 公司定价难 - 对比
        easy_text = Text(
            "锅碗瓢盆好定价",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GREEN
        ).move_to(LEFT * 2.0 + DOWN * 0.8)
        hard_text = Text(
            "公司定价水很深",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).move_to(RIGHT * 2.0 + DOWN * 0.8)

        # 4. 底部扎心文案
        bottom = Text(
            "你真能搞清楚吗？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(news_group, shift=UP), run_time=step_time)
        self.play(FadeIn(easy_text, shift=RIGHT), FadeIn(hard_text, shift=LEFT), run_time=step_time)
        self.play(Write(bottom), run_time=step_time)
        self.play(Circumscribe(bottom, color=RED), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：PE市盈率核心概念

        口播稿关键词/短语：
        - "PE市盈率" -> chart 图标
        - "多少年能回本" -> 核心比喻
        - "净利润乘以市盈率" -> 公式展示

        动态标题：「PE估值一算就懂」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、PE解释、回本比喻、公式、底部总结）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "PE估值一算就懂",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. PE核心概念 - 图标 + 文字
        pe_icon = self.load_png_icon("chart", height=1.8).move_to(UP * 2.0)
        pe_text = Text(
            "PE = 市盈率",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(pe_icon, DOWN, buff=0.3)
        pe_group = Group(pe_icon, pe_text)

        # 3. 回本比喻 - 白话解释
        metaphor = Text(
            "「多少年能回本」",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).move_to(DOWN * 0.3)
        example = Text(
            "5倍 = 5年回本  30倍 = 30年回本",
            font=self.body_font,
            font_size=self.font_small_size,
            color=GRAY
        ).next_to(metaphor, DOWN, buff=0.3)

        # 4. 公式
        formula = Text(
            "市值 = 净利润 × 市盈率",
            font=self.title_font,
            font_size=self.font_body_size,
            color=GOLD
        ).move_to(DOWN * 2.0)
        formula_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=GOLD, fill_opacity=0.1)
        formula_box.surround(formula, buff=0.3)
        formula_group = VGroup(formula_box, formula)

        # 5. 底部
        summary = Text(
            "一算就出来了",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(pe_group, shift=UP), run_time=step_time)
        self.play(Write(metaphor), Write(example), run_time=step_time)
        self.play(FadeIn(formula_group, shift=UP), run_time=step_time)
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：科技股vs银行股

        口播稿关键词/短语：
        - "80倍科技股有人抢" -> 左侧绿色
        - "5倍银行股没人碰" -> 右侧灰色
        - "两个乘数同时涨" -> 核心洞察

        动态标题：「科技股凭啥比银行贵？」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、科技股、银行股、原因揭示、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "科技股凭啥比银行贵？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 左侧：科技股 80倍
        tech_icon = self.load_png_icon("positive_dynamic", height=1.5).move_to(LEFT * 2.0 + UP * 2.0)
        tech_label = Text("科技股", font=self.title_font, font_size=self.font_title_size, color=GREEN).next_to(tech_icon, DOWN, buff=0.2)
        tech_pe = Text("80倍PE 有人抢", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(tech_label, DOWN, buff=0.1)
        tech_group = Group(tech_icon, tech_label, tech_pe)

        # 3. 右侧：银行股 5倍
        bank_icon = self.load_png_icon("bank_building", height=1.5).move_to(RIGHT * 2.0 + UP * 2.0)
        bank_label = Text("银行股", font=self.title_font, font_size=self.font_title_size, color=GRAY).next_to(bank_icon, DOWN, buff=0.2)
        bank_pe = Text("5倍PE 没人碰", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(bank_label, DOWN, buff=0.1)
        bank_group = Group(bank_icon, bank_label, bank_pe)

        # 4. 原因揭示
        reason = Text(
            "利润增长快 + 容忍度高",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).move_to(DOWN * 1.0)
        reason2 = Text(
            "两个乘数同时涨，涨幅恐怖",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).next_to(reason, DOWN, buff=0.3)

        # 5. 底部结论
        bottom = Text(
            "银行两个都不涨 当然没人爱",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(tech_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(bank_group, shift=DOWN), run_time=step_time)
        self.play(Write(reason), Write(reason2), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GRAY), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：估值是你的标尺

        口播稿关键词/短语：
        - "创业融资" -> investment 图标
        - "股票价格" -> stocks 图标
        - "PE法还是PS法" -> 装逼利器

        动态标题：「估值是你的标尺」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、三个场景、金句、强调）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "估值是你的标尺",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三个适用场景
        s1_icon = self.load_png_icon("investment", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        s1_text = Text("看创业公司融资", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(s1_icon, RIGHT, buff=0.3)
        s1 = Group(s1_icon, s1_text)

        s2_icon = self.load_png_icon("stocks", height=0.8).shift(LEFT * 3.0 + UP * 0.5)
        s2_text = Text("理解股票价格", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(s2_icon, RIGHT, buff=0.3)
        s2 = Group(s2_icon, s2_text)

        s3_icon = self.load_png_icon("handshake", height=0.8).shift(LEFT * 3.0 + DOWN * 1.0)
        s3_text = Text("评估项目值不值得投", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(s3_icon, RIGHT, buff=0.3)
        s3 = Group(s3_icon, s3_text)

        items = [s1, s2, s3]

        # 3. 底部金句
        quote = Text(
            "「PE法还是PS法？」",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.0)
        quote_sub = Text(
            "一句话立马显专业",
            font=self.body_font,
            font_size=self.font_small_size,
            color=GRAY
        ).next_to(quote, DOWN, buff=0.2)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(item, shift=RIGHT) for item in items], lag_ratio=0.3),
            run_time=step_time
        )
        self.play(Write(quote), Write(quote_sub), run_time=step_time)
        self.play(Circumscribe(quote, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：四把尺子

        口播稿关键词/短语：
        - "PE看利润" -> profit 图标
        - "PB看净资产" -> safe 图标
        - "PS看流水" -> money_circulation 图标
        - "DCF折现金流" -> calculator 图标

        动态标题：「记住四把尺子」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、PE+PB、PS+DCF、底部警示、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "记住四把尺子",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. PE和PB
        pe_icon = self.load_png_icon("profit", height=1.0).move_to(LEFT * 2.0 + UP * 2.0)
        pe_label = Text("PE 看利润", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(pe_icon, DOWN, buff=0.2)
        pe_desc = Text("赚钱的公司用", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(pe_label, DOWN, buff=0.1)
        pe_group = Group(pe_icon, pe_label, pe_desc)

        pb_icon = self.load_png_icon("safe", height=1.0).move_to(RIGHT * 2.0 + UP * 2.0)
        pb_label = Text("PB 看资产", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(pb_icon, DOWN, buff=0.2)
        pb_desc = Text("有家底的用", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(pb_label, DOWN, buff=0.1)
        pb_group = Group(pb_icon, pb_label, pb_desc)

        # 3. PS和DCF
        ps_icon = self.load_png_icon("money_circulation", height=1.0).move_to(LEFT * 2.0 + DOWN * 0.8)
        ps_label = Text("PS 看流水", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(ps_icon, DOWN, buff=0.2)
        ps_desc = Text("烧钱的互联网用", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(ps_label, DOWN, buff=0.1)
        ps_group = Group(ps_icon, ps_label, ps_desc)

        dcf_icon = self.load_png_icon("calculator", height=1.0).move_to(RIGHT * 2.0 + DOWN * 0.8)
        dcf_label = Text("DCF 折现金流", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(dcf_icon, DOWN, buff=0.2)
        dcf_desc = Text("看长远的用", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(dcf_label, DOWN, buff=0.1)
        dcf_group = Group(dcf_icon, dcf_label, dcf_desc)

        # 4. 底部警示
        bottom = Text(
            "别被一个数字忽悠了",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(pe_group, shift=UP), FadeIn(pb_group, shift=UP), run_time=step_time)
        self.play(FadeIn(ps_group, shift=UP), FadeIn(dcf_group, shift=UP), run_time=step_time)
        self.play(Write(bottom), run_time=step_time)
        self.play(Circumscribe(bottom, color=RED), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：估值不是玄学 -> 互动引导

        动态标题：「估值不是玄学」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、核心收获、互动图标、口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "估值不是玄学",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "四个方法看懂大部分公司",
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
