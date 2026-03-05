import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson038VerticalScenes(Zsxq100keLessonVertical):
    """
    第038课：增资扩股与定向增发
    主题：本轮牛市的底色
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：定增是什么？

        口播稿关键词/短语：
        - "某公司定增了" -> stocks 图标
        - "股价就开始动" -> 关注焦点
        - "连股市为什么涨都看不明白" -> 焦虑感

        动态标题：「牛市到底怎么来的？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、定增新闻、股价动、牛市底色、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "牛市到底怎么来的？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 定增新闻
        stock_icon = self.load_png_icon("stocks", height=1.8).move_to(UP * 1.8)
        news = Text(
            "某公司定增了 股价开始动",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).next_to(stock_icon, DOWN, buff=0.3)
        news_group = Group(stock_icon, news)

        # 3. 疑问
        q_text = Text(
            "什么是定增？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 0.5)

        # 4. 牛市底色
        hint = Text(
            "定增新规 = 牛市底色",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).move_to(DOWN * 1.8)

        # 5. 底部
        bottom = Text(
            "搞不懂就看不明白股市",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(news_group, shift=UP), run_time=step_time)
        self.play(Write(q_text), run_time=step_time)
        self.play(Write(hint), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=RED), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：增资扩股 + 定增概念

        口播稿关键词/短语：
        - "增资扩股" -> company 图标
        - "定向增发 简称定增" -> 核心概念
        - "只卖给特定机构" -> 定向

        动态标题：「增资扩股是什么？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、增资、扩股、定增解释、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "增资扩股是什么？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 增资 + 扩股
        comp_icon = self.load_png_icon("company", height=1.5).move_to(UP * 2.0)
        add_text = Text(
            "增资 = 引进新股东 资本金增加",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(comp_icon, DOWN, buff=0.3)
        expand_text = Text(
            "扩股 = 总股本扩张",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(add_text, DOWN, buff=0.2)
        comp_group = Group(comp_icon, add_text, expand_text)

        # 3. 定增解释
        ding_text = Text(
            "上市后再融资 = 定向增发",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).move_to(DOWN * 0.8)
        ding_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=GOLD, fill_opacity=0.1)
        ding_box.surround(ding_text, buff=0.3)
        ding_group = VGroup(ding_box, ding_text)

        # 4. 特定对象
        target = Text(
            "只卖给特定的机构投资者",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GREEN
        ).move_to(DOWN * 2.2)

        # 5. 底部
        bottom = Text(
            "不是谁都能买",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(comp_group, shift=UP), run_time=step_time)
        self.play(FadeIn(ding_group, shift=UP), run_time=step_time)
        self.play(Write(target), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：过去定增的三个坑

        口播稿关键词/短语：
        - "名额少" -> 第一坑
        - "九折安全垫薄" -> 第二坑
        - "锁定期长" -> 第三坑

        动态标题：「过去定增有三个坑」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、三坑逐项展示、底部、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "过去定增有三个坑",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(UP * 4.0)

        # 2. 三个坑
        pit1 = Text("坑一  名额少 最多5个人买", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(UP * 2.0)
        pit1_desc = Text("一人分10亿 压力山大", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(pit1, DOWN, buff=0.15)

        pit2 = Text("坑二  只打九折 安全垫太薄", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(DOWN * 0.2)
        pit2_desc = Text("一不留神就亏", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(pit2, DOWN, buff=0.15)

        pit3 = Text("坑三  锁定12~36个月", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(DOWN * 2.0)
        pit3_desc = Text("黄花菜都凉了", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(pit3, DOWN, buff=0.15)

        # 3. 底部
        bottom = Text(
            "三条卡着 谁也赚不了钱",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(pit1), Write(pit1_desc), run_time=step_time)
        self.play(Write(pit2), Write(pit2_desc), run_time=step_time)
        self.play(Write(pit3), Write(pit3_desc), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=RED), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：定增信号解读

        口播稿关键词/短语：
        - "谁来买了" -> 机构看好
        - "价格打几折" -> 安全垫
        - "定增策略基金" -> 可观收益

        动态标题：「定增信号怎么看？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、两个关注点、策略基金、底部）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "定增信号怎么看？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 关注点
        s1_icon = self.load_png_icon("businessman", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        s1_text = Text("谁来买了？机构看好", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(s1_icon, RIGHT, buff=0.3)
        s1 = Group(s1_icon, s1_text)

        s2_icon = self.load_png_icon("percentage", height=0.8).shift(LEFT * 3.0 + UP * 0.5)
        s2_text = Text("打几折？折扣大更安全", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(s2_icon, RIGHT, buff=0.3)
        s2 = Group(s2_icon, s2_text)

        # 3. 策略基金
        fund_text = Text(
            "很多基金专做定增策略",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).move_to(DOWN * 1.2)
        fund_sub = Text(
            "收益相当可观",
            font=self.body_font,
            font_size=self.font_small_size,
            color=GRAY
        ).next_to(fund_text, DOWN, buff=0.2)

        # 4. 底部
        bottom = Text(
            "看定增公告就有信号",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(FadeIn(s1, shift=RIGHT), FadeIn(s2, shift=RIGHT), lag_ratio=0.3),
            run_time=step_time
        )
        self.play(Write(fund_text), Write(fund_sub), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：2020新规三大改变

        口播稿关键词/短语：
        - "5个→35个" -> 名额放宽
        - "9折→8折" -> 折扣加大
        - "12个月→6个月" -> 锁定缩短
        - "这就是牛市底色" -> 核心结论

        动态标题：「新规改了什么？」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、三个改变逐项、底部、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "2020新规改了什么？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三个改变 - 旧→新对比
        c1_old = Text("名额 5个", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(LEFT * 2.0 + UP * 2.0)
        c1_arrow = Text("→", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(c1_old, RIGHT, buff=0.2)
        c1_new = Text("35个", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(c1_arrow, RIGHT, buff=0.2)

        c2_old = Text("折扣 9折", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(LEFT * 2.0 + UP * 0.5)
        c2_arrow = Text("→", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(c2_old, RIGHT, buff=0.2)
        c2_new = Text("8折", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(c2_arrow, RIGHT, buff=0.2)

        c3_old = Text("锁定 12个月", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(LEFT * 2.0 + DOWN * 1.0)
        c3_arrow = Text("→", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(c3_old, RIGHT, buff=0.2)
        c3_new = Text("6个月", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(c3_arrow, RIGHT, buff=0.2)

        # 3. 总结
        summary = Text(
            "门槛降 折扣大 周期短",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).move_to(DOWN * 2.5)

        # 4. 底部核心
        bottom = Text(
            "这就是牛市的底色",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(c1_old), Write(c1_arrow), Write(c1_new), run_time=step_time)
        self.play(Write(c2_old), Write(c2_arrow), Write(c2_new),
                  Write(c3_old), Write(c3_arrow), Write(c3_new), run_time=step_time)
        self.play(Write(summary), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：看股市新闻更通透 -> 互动引导

        动态标题：「看股市更通透」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、核心收获、互动图标、口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "看股市更通透",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "搞懂定增 股市新闻就看明白了",
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
