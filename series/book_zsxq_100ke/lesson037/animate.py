import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson037VerticalScenes(Zsxq100keLessonVertical):
    """
    第037课：债券市场全貌
    主题：理财和金融市场的基石
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：你的钱去哪了？

        口播稿关键词/短语：
        - "银行理财、余额宝" -> bank 图标
        - "你的钱买了债券" -> bonds 图标
        - "一百万亿" -> 震撼数字

        动态标题：「你的钱去哪了？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、银行理财、真相揭示、百万亿、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题 - 引发好奇
        title = Text(
            "你的钱去哪了？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 银行理财场景
        bank_icon = self.load_png_icon("bank", height=1.8).move_to(UP * 1.8)
        bank_text = Text(
            "银行理财  微信余额宝",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).next_to(bank_icon, DOWN, buff=0.3)
        bank_group = Group(bank_icon, bank_text)

        # 3. 真相揭示 - 债券
        bond_icon = self.load_png_icon("bonds", height=1.5).move_to(DOWN * 0.3)
        truth = Text(
            "底层全是债券！",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).next_to(bond_icon, DOWN, buff=0.3)
        truth_group = Group(bond_icon, truth)

        # 4. 震撼数字
        number = Text(
            "中国债券市场超108万亿",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).move_to(DOWN * 2.5)

        # 5. 底部
        bottom = Text(
            "金融市场的基石",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(bank_group, shift=UP), run_time=step_time)
        self.play(FadeIn(truth_group, shift=UP), run_time=step_time)
        self.play(Write(number), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：债券三级结构

        口播稿关键词/短语：
        - "标准化的借条" -> document 图标
        - "三级" -> 国债 > 金融债 > 企业债
        - "安全性依次递减" -> 递进布局

        动态标题：「债券就是标准化借条」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、借条比喻、三级逐项展示、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "债券就是标准化借条",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 借条比喻
        doc_icon = self.load_png_icon("finance_document", height=1.5).move_to(UP * 2.2)
        doc_text = Text(
            "约定利率、期限、抵押物",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(doc_icon, DOWN, buff=0.3)
        doc_group = Group(doc_icon, doc_text)

        # 3. 三级结构
        l1 = Text("第一级  国债 → 国家借钱 最安全", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(UP * 0.2)
        l2 = Text("第二级  金融债 → 银行保险借", font=self.body_font, font_size=self.font_body_size, color=BLUE).move_to(DOWN * 0.8)
        l3 = Text("第三级  企业债 → 公司借的", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(DOWN * 1.8)

        # 4. 底部总结
        bottom = Text(
            "安全性依次递减",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(doc_group, shift=UP), run_time=step_time)
        self.play(
            LaggedStart(Write(l1), Write(l2), Write(l3), lag_ratio=0.3),
            run_time=step_time
        )
        self.play(Write(bottom), run_time=step_time)
        self.play(Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：国债被低估

        口播稿关键词/短语：
        - "中国国债2.4%" -> 中国利率高
        - "美国0.2%" -> 对比悬殊
        - "外资抢着买" -> 全球视角
        - "银行保本靠国债" -> 真相

        动态标题：「国债被你小看了」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、中国利率、美国利率、外资、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "国债被你小看了",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(UP * 4.0)

        # 2. 中国国债利率 - 左侧
        cn_icon = self.load_png_icon("positive_dynamic", height=1.2).move_to(LEFT * 2.0 + UP * 2.0)
        cn_rate = Text("中国 2.4%", font=self.title_font, font_size=self.font_title_size, color=GREEN).next_to(cn_icon, DOWN, buff=0.2)
        cn_group = Group(cn_icon, cn_rate)

        # 3. 美国国债利率 - 右侧
        us_icon = self.load_png_icon("decrease", height=1.2).move_to(RIGHT * 2.0 + UP * 2.0)
        us_rate = Text("美国 0.2%", font=self.title_font, font_size=self.font_title_size, color=GRAY).next_to(us_icon, DOWN, buff=0.2)
        us_group = Group(us_icon, us_rate)

        # 4. 外资抢购
        foreign = Text(
            "外资持有中国国债10%",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).move_to(DOWN * 0.5)
        globe_icon = self.load_png_icon("globe", height=1.0).next_to(foreign, LEFT, buff=0.3)
        foreign_group = Group(globe_icon, foreign)

        # 5. 底部真相
        bottom = Text(
            "保本理财底层就是国债",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(cn_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(us_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(foreign_group, shift=UP), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：理财底层资产

        口播稿关键词/短语：
        - "年化2-3%底层是国债" -> safe 图标
        - "年化4-6%底层是AA+企业债" -> certificate 图标
        - "不被忽悠" -> 核心价值

        动态标题：「你的理财买了什么？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、低收益、高收益、底部）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "你的理财买了什么？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 低收益理财
        low_icon = self.load_png_icon("safe", height=1.2).move_to(UP * 1.8)
        low_text = Text("年化2~3%", font=self.title_font, font_size=self.font_title_size, color=GREEN).next_to(low_icon, RIGHT, buff=0.3)
        low_desc = Text("底层：国债", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(low_text, DOWN, buff=0.2)
        low_group = Group(low_icon, low_text, low_desc)

        # 3. 高收益理财
        high_icon = self.load_png_icon("certificate", height=1.2).move_to(DOWN * 0.5)
        high_text = Text("年化4~6%", font=self.title_font, font_size=self.font_title_size, color=GOLD).next_to(high_icon, RIGHT, buff=0.3)
        high_desc = Text("底层：AA+企业债", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(high_text, DOWN, buff=0.2)
        high_group = Group(high_icon, high_text, high_desc)

        # 4. 底部
        bottom = Text(
            "搞清楚就不会被忽悠",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(low_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(high_group, shift=RIGHT), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：三条原则

        口播稿关键词/短语：
        - "看评级" -> 第一条
        - "看发行方" -> 第二条
        - "看利率" -> 第三条
        - "安全第一收益第二" -> 核心

        动态标题：「选债三条原则」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、三条逐项、底部、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "选债三条原则",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三条原则
        r1_icon = self.load_png_icon("check_mark", height=0.8).shift(LEFT * 3.2 + UP * 2.0)
        r1_text = Text("看评级 AA+以上才靠谱", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(r1_icon, RIGHT, buff=0.3)
        r1 = Group(r1_icon, r1_text)

        r2_icon = self.load_png_icon("check_mark", height=0.8).shift(LEFT * 3.2 + UP * 0.5)
        r2_text = Text("看发行方 国企省会优先", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(r2_icon, RIGHT, buff=0.3)
        r2 = Group(r2_icon, r2_text)

        r3_icon = self.load_png_icon("warning", height=0.8).shift(LEFT * 3.2 + DOWN * 1.0)
        r3_text = Text("看利率 超6%要警惕", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(r3_icon, RIGHT, buff=0.3)
        r3 = Group(r3_icon, r3_text)

        items = [r1, r2, r3]

        # 3. 底部核心
        bottom = Text(
            "安全第一 收益第二",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(r1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(r2, shift=RIGHT), FadeIn(r3, shift=RIGHT), run_time=step_time)
        self.play(Write(bottom), run_time=step_time)
        self.play(Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：看透理财产品 -> 互动引导

        动态标题：「看透理财产品」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、核心收获、互动图标、口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "看透理财产品",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "搞懂债券 理财就看透了",
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
