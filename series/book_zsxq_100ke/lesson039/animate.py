import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson039VerticalScenes(Zsxq100keLessonVertical):
    """
    第039课：汇率的秘密
    主题：人民币升值对我们的影响
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：人民币升值是好是坏？

        口播稿关键词/短语：
        - "人民币涨了好几千个基点" -> currency_exchange 图标
        - "升值是好事还是坏事" -> 困惑感
        - "一头雾水" -> 灰色调

        动态标题：「升值到底好不好？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、汇率新闻、升值问题、大白话、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "升值到底好不好？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 汇率新闻
        fx_icon = self.load_png_icon("currency_exchange", height=1.8).move_to(UP * 1.8)
        fx_text = Text(
            "人民币涨了好几千个基点",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GREEN
        ).next_to(fx_icon, DOWN, buff=0.3)
        fx_group = Group(fx_icon, fx_text)

        # 3. 困惑
        q_text = Text(
            "是好事还是坏事？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 0.5)

        # 4. 承诺
        promise = Text(
            "其实没那么复杂",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).move_to(DOWN * 1.8)

        # 5. 底部
        bottom = Text(
            "用大白话给你讲清楚",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(fx_group, shift=UP), run_time=step_time)
        self.play(Write(q_text), run_time=step_time)
        self.play(Write(promise), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：汇率的本质

        口播稿关键词/短语：
        - "两种货币兑换比例" -> currency 图标
        - "1美元换7块人民币" -> 具象例子
        - "升值" vs "贬值" -> 对比

        动态标题：「汇率就是你的钱值多少」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、定义、例子、升值贬值、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "汇率就是钱的价格",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 定义
        currency_icon = self.load_png_icon("currency", height=1.5).move_to(UP * 2.2)
        definition = Text(
            "两种货币之间的兑换比例",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(currency_icon, DOWN, buff=0.3)
        def_group = Group(currency_icon, definition)

        # 3. 例子
        example = Text(
            "1美元 = 7元人民币",
            font=self.title_font,
            font_size=self.font_title_size,
            color=WHITE
        ).move_to(UP * 0.0)
        ex_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=BLUE, fill_opacity=0.1)
        ex_box.surround(example, buff=0.3)
        ex_group = VGroup(ex_box, example)

        # 4. 升值 vs 贬值
        up_text = Text("换的外币多 = 升值", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 1.5)
        down_text = Text("换的外币少 = 贬值", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(DOWN * 2.5)

        # 5. 底部
        bottom = Text(
            "你的钱在别人那值多少",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(def_group, shift=UP), run_time=step_time)
        self.play(FadeIn(ex_group, shift=UP), run_time=step_time)
        self.play(Write(up_text), Write(down_text), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：升值不全是好事

        口播稿关键词/短语：
        - "贬值利出口" -> 出口箭头
        - "升值出口压力大" -> 对比
        - "世界工厂靠贬值" -> 历史选择

        动态标题：「升值不全是好事」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、贬值利出口、升值反效果、世界工厂、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "升值不全是好事",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(UP * 4.0)

        # 2. 贬值利出口 - 左侧
        devalue_icon = self.load_png_icon("decrease", height=1.2).move_to(LEFT * 2.0 + UP * 2.0)
        devalue_label = Text("贬值", font=self.title_font, font_size=self.font_title_size, color=GREEN).next_to(devalue_icon, DOWN, buff=0.2)
        devalue_effect = Text("出口好做 赚外汇", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(devalue_label, DOWN, buff=0.1)
        devalue_group = Group(devalue_icon, devalue_label, devalue_effect)

        # 3. 升值出口承压 - 右侧
        apprec_icon = self.load_png_icon("increase", height=1.2).move_to(RIGHT * 2.0 + UP * 2.0)
        apprec_label = Text("升值", font=self.title_font, font_size=self.font_title_size, color=RED).next_to(apprec_icon, DOWN, buff=0.2)
        apprec_effect = Text("出口压力大", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(apprec_label, DOWN, buff=0.1)
        apprec_group = Group(apprec_icon, apprec_label, apprec_effect)

        # 4. 世界工厂
        factory = Text(
            "中国靠贬值成了世界工厂",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).move_to(DOWN * 1.0)
        globe_icon = self.load_png_icon("world_markets", height=1.0).next_to(factory, LEFT, buff=0.3)
        factory_group = Group(globe_icon, factory)

        # 5. 底部
        bottom = Text(
            "这是历史的选择",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(devalue_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(apprec_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(factory_group, shift=UP), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：汇率影响你的钱包

        口播稿关键词/短语：
        - "外贸、海外投资" -> globe 图标
        - "留学、旅游" -> airplane 图标
        - "利润被汇率吃掉" -> 风险警示

        动态标题：「汇率影响你的钱包」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、受影响人群、升值好处/坏处、底部）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "汇率影响你的钱包",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 受影响的人群
        p1_icon = self.load_png_icon("globe", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        p1_text = Text("做外贸 海外投资", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(p1_icon, RIGHT, buff=0.3)
        p1 = Group(p1_icon, p1_text)

        p2_icon = self.load_png_icon("airplane", height=0.8).shift(LEFT * 3.0 + UP * 0.5)
        p2_text = Text("留学 出国旅游", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(p2_icon, RIGHT, buff=0.3)
        p2 = Group(p2_icon, p2_text)

        # 3. 好处和坏处
        good = Text("升值：出国消费更便宜", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 1.0)
        bad = Text("外贸：利润可能被吃掉", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(DOWN * 2.0)

        # 4. 底部
        bottom = Text(
            "汇率直接影响你的钱包",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(FadeIn(p1, shift=RIGHT), FadeIn(p2, shift=RIGHT), lag_ratio=0.3),
            run_time=step_time
        )
        self.play(Write(good), Write(bad), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：升值时代三件事

        口播稿关键词/短语：
        - "外资涌入推高股市" -> 第一件
        - "房住不炒" -> 第二件
        - "降息利好房贷族" -> 第三件
        - "顺势而为" -> 核心

        动态标题：「升值时代关注三件事」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、三件事逐项、底部、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "升值时代关注三件事",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三件事
        e1_icon = self.load_png_icon("positive_dynamic", height=0.8).shift(LEFT * 3.2 + UP * 2.0)
        e1_text = Text("外资涌入 推高股市", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(e1_icon, RIGHT, buff=0.3)
        e1 = Group(e1_icon, e1_text)

        e2_icon = self.load_png_icon("house", height=0.8).shift(LEFT * 3.2 + UP * 0.5)
        e2_text = Text("房住不炒 热钱不进房市", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(e2_icon, RIGHT, buff=0.3)
        e2 = Group(e2_icon, e2_text)

        e3_icon = self.load_png_icon("bank", height=0.8).shift(LEFT * 3.2 + DOWN * 1.0)
        e3_text = Text("降息预期 房贷族受益", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(e3_icon, RIGHT, buff=0.3)
        e3 = Group(e3_icon, e3_text)

        items = [e1, e2, e3]

        # 3. 底部
        bottom = Text(
            "顺势而为才是正道",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(e1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(e2, shift=RIGHT), FadeIn(e3, shift=RIGHT), run_time=step_time)
        self.play(Write(bottom), run_time=step_time)
        self.play(Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：汇率值得了解 -> 互动引导

        动态标题：「值得每个人了解」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、核心收获、互动图标、口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "值得每个人了解",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "汇率影响钱包 股市 经济大盘",
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
