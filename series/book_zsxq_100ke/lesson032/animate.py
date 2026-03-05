import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson032VerticalScenes(Zsxq100keLessonVertical):
    """
    第032课：内循环与外循环
    主题：经济大棋局与你的钱袋子
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：TikTok被打压 -> 房价阴跌 -> 背后逻辑

        口播稿关键词/短语：
        - "TikTok被打压" -> globe 图标 + 灰色
        - "房价阴跌" -> house 图标 + RED
        - "内循环外循环" -> circular_arrows + 金色

        动态标题：「这些事背后的逻辑」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、TikTok现象、房价现象、核心逻辑、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "这些事背后的逻辑",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 现象一：TikTok被打压
        globe_icon = self.load_png_icon("globe", height=1.2).move_to(LEFT * 2.0 + UP * 2.0)
        tiktok_text = Text(
            "TikTok一打压就被动",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).next_to(globe_icon, RIGHT, buff=0.3)
        tiktok_group = Group(globe_icon, tiktok_text)

        # 3. 现象二：房价阴跌
        house_icon = self.load_png_icon("house", height=1.2).move_to(LEFT * 2.0 + UP * 0.3)
        house_text = Text(
            "有些城市房价一直阴跌",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).next_to(house_icon, RIGHT, buff=0.3)
        house_group = Group(house_icon, house_text)

        # 4. 核心逻辑
        core = Text(
            "同一个逻辑：内循环与外循环",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 1.5)

        # 5. 底部：大棋
        bottom = Text(
            "搞懂就看清了经济大棋",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(tiktok_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(house_group, shift=RIGHT), run_time=step_time)
        self.play(Write(core), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：外循环=替人打工 vs 内循环=自给自足

        口播稿关键词/短语：
        - "外循环" -> supply_chain 图标 + GRAY
        - "内循环" -> money_circulation 图标 + GOLD
        - "两个半" -> 数据强调

        动态标题：「什么是内外循环？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、外循环、内循环、两个半、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "什么是内外循环？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 外循环
        out_icon = self.load_png_icon("supply_chain", height=1.5).move_to(LEFT * 2.0 + UP * 2.0)
        out_label = Text("外循环", font=self.title_font, font_size=self.font_title_size, color=GRAY).next_to(out_icon, DOWN, buff=0.2)
        out_desc = Text("替人打工赚辛苦钱", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(out_label, DOWN, buff=0.2)
        out_group = Group(out_icon, out_label, out_desc)

        # 3. 内循环
        in_icon = self.load_png_icon("money_circulation", height=1.5).move_to(RIGHT * 2.0 + UP * 2.0)
        in_label = Text("内循环", font=self.title_font, font_size=self.font_title_size, color=GOLD).next_to(in_icon, DOWN, buff=0.2)
        in_desc = Text("中国人买中国货", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(in_label, DOWN, buff=0.2)
        in_group = Group(in_icon, in_label, in_desc)

        # 4. 数据强调
        data_text = Text(
            "全球能玩内循环的只有2.5个",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).move_to(DOWN * 1.0)
        data_sub = Text(
            "中国 + 美国 + 半个欧盟",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(data_text, DOWN, buff=0.2)

        # 5. 底部总结
        summary = Text(
            "有市场有工业就有底气",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(out_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(in_group, shift=DOWN), run_time=step_time)
        self.play(Write(data_text), Write(data_sub), run_time=step_time)
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：外循环三大致命伤

        口播稿关键词/短语：
        - "好东西全出口" -> logistics 图标
        - "被卡脖子" -> lock 图标
        - "金丝雀" -> warning 图标

        动态标题：「外循环的三大致命伤」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、三项、底部、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "外循环的三大致命伤",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(UP * 4.0)

        # 2. 三大问题
        p1_icon = self.load_png_icon("logistics", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        p1_text = Text("①好东西全出口自己用不上", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(p1_icon, RIGHT, buff=0.3)
        p1 = Group(p1_icon, p1_text)

        p2_icon = self.load_png_icon("lock", height=0.8).shift(LEFT * 3.0 + UP * 0.5)
        p2_text = Text("②高端技术被卡脖子", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(p2_icon, RIGHT, buff=0.3)
        p2 = Group(p2_icon, p2_text)

        p3_icon = self.load_png_icon("warning", height=0.8).shift(LEFT * 3.0 + DOWN * 1.0)
        p3_text = Text("③国际风吹草动就抖三抖", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(p3_icon, RIGHT, buff=0.3)
        p3 = Group(p3_icon, p3_text)

        items = [p1, p2, p3]

        # 3. 韩国案例
        case_text = Text(
            "韩国就是典型：经济金丝雀",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).move_to(DOWN * 2.0)

        # 4. 底部结论
        conclusion = Text(
            "中国不能走这条老路",
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
        self.play(Write(case_text), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)
        self.play(Circumscribe(conclusion, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：房价分化 + 股市慢牛

        口播稿关键词/短语：
        - "中西部房价阴跌" -> house + RED
        - "东部温和上涨" -> real_estate + GREEN
        - "股市慢牛" -> chart + GOLD

        动态标题：「跟你钱袋子的关系」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、房价分化左、房价分化右、股市、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "跟你钱袋子的关系",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 中西部房价：阴跌
        west_icon = self.load_png_icon("house", height=1.2).move_to(LEFT * 2.0 + UP * 2.0)
        west_label = Text("中西部房价", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(west_icon, DOWN, buff=0.2)
        west_trend = Text("长期阴跌", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(west_label, DOWN, buff=0.1)
        west_group = Group(west_icon, west_label, west_trend)

        # 3. 东部核心城市：温和上涨后横盘
        east_icon = self.load_png_icon("real_estate", height=1.2).move_to(RIGHT * 2.0 + UP * 2.0)
        east_label = Text("东部核心城市", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(east_icon, DOWN, buff=0.2)
        east_trend = Text("温和上涨后横盘", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(east_label, DOWN, buff=0.1)
        east_group = Group(east_icon, east_label, east_trend)

        # 4. 股市：慢牛
        stock_icon = self.load_png_icon("chart", height=1.2).move_to(DOWN * 0.8)
        stock_text = Text(
            "股市走慢牛，科技股涨得吓人",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).next_to(stock_icon, DOWN, buff=0.3)
        stock_group = Group(stock_icon, stock_text)

        # 5. 底部建议
        bottom = Text(
            "普通人买基金就够了",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(west_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(east_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(stock_group, shift=UP), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：三个方向逐项弹出

        口播稿关键词/短语：
        - "别赌三四线" -> house + RED
        - "国产替代" -> business_building + GREEN
        - "买基金跟慢牛" -> investment_portfolio + GOLD

        动态标题：「三个方向抓住红利」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、三项、金句、强调）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "三个方向抓住红利",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三个方向
        d1_icon = self.load_png_icon("house", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        d1_text = Text("①别在三四线赌房价反弹", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(d1_icon, RIGHT, buff=0.3)
        d1 = Group(d1_icon, d1_text)

        d2_icon = self.load_png_icon("business_building", height=0.8).shift(LEFT * 3.0 + UP * 0.5)
        d2_text = Text("②关注国产替代科技板块", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(d2_icon, RIGHT, buff=0.3)
        d2 = Group(d2_icon, d2_text)

        d3_icon = self.load_png_icon("investment_portfolio", height=0.8).shift(LEFT * 3.0 + DOWN * 1.0)
        d3_text = Text("③买基金跟着慢牛走", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(d3_icon, RIGHT, buff=0.3)
        d3 = Group(d3_icon, d3_text)

        items = [d1, d2, d3]

        # 3. 底部金句
        golden = Text(
            "细水长流才是真赢家",
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
        self.play(Write(golden), run_time=step_time)
        self.play(Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：看懂内循环 -> 互动引导

        动态标题：「看懂未来十年」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、核心收获、互动图标、口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "看懂未来十年",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "内循环就是未来十年的财富方向",
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
