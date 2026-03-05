import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson025VerticalScenes(Zsxq100keLessonVertical):
    """
    第025课：区块链与数字货币
    主题：大白话讲透区块链和数字人民币
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)

        口播稿：比特币暴涨暴跌，各种数字货币满天飞。你是不是也被人拉进过什么区块链投资群？
                大佬们天天喊你上车，搞得你心里痒痒的。
                但区块链到底是个什么东西？数字货币靠不靠谱？今天咱们用大白话把它讲透。

        关键词/短语：
        - "比特币暴涨暴跌" -> bitcoin 图标
        - "区块链投资群" -> 灰色焦虑
        - "大佬喊你上车" -> 红色警示
        - "今天讲透" -> 金色转折

        动态标题：「区块链是啥玩意？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "区块链是啥玩意？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 比特币图标 + 暴涨暴跌
        btc_icon = self.load_png_icon("bitcoin", height=2.0).move_to(UP * 1.5)
        chaos_text = Text(
            "暴涨暴跌，各种币满天飞",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).next_to(btc_icon, DOWN, buff=0.3)
        btc_group = Group(btc_icon, chaos_text)

        # 3. 关键短语
        pull_text = Text(
            "大佬天天喊你上车",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).shift(DOWN * 1.0)

        # 4. 底部转折
        hook = Text(
            "今天用大白话讲透",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(btc_group, shift=UP), run_time=step_time)
        self.play(Write(pull_text), run_time=step_time)
        self.play(Write(hook), run_time=step_time)
        self.play(Circumscribe(hook, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)

        口播稿：区块链说白了就是一个共享数据库。以前的数据库是中心化的，
                一个单位收集整理存在自己电脑里，想改就能改。
                区块链恰恰相反，数据存在好多素不相识的人的电脑里，不归任何一家管。
                五个特征：不可伪造、全程留痕、可以追溯、公开透明、集体维护。

        关键词/短语：
        - "共享数据库" -> data_backup/cloud_storage 图标
        - "五个特征" -> 逐项展示
        - "不归任何一家管" -> 蓝色去中心化

        动态标题：「区块链 = 共享数据库」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "区块链 = 共享数据库",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 核心定义 + 图标
        db_icon = self.load_png_icon("cloud_storage", height=1.5).move_to(UP * 2.0)
        definition = Text(
            "数据存在很多人的电脑里",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(db_icon, DOWN, buff=0.3)
        db_group = Group(db_icon, definition)

        # 3. 五个特征 - 分两行排列
        feat1 = Text("不可伪造", font=self.body_font, font_size=self.font_small_size, color=GREEN)
        feat2 = Text("全程留痕", font=self.body_font, font_size=self.font_small_size, color=GREEN)
        feat3 = Text("可以追溯", font=self.body_font, font_size=self.font_small_size, color=GREEN)
        feat4 = Text("公开透明", font=self.body_font, font_size=self.font_small_size, color=GREEN)
        feat5 = Text("集体维护", font=self.body_font, font_size=self.font_small_size, color=GREEN)

        row1 = VGroup(feat1, feat2, feat3).arrange(RIGHT, buff=0.5).shift(DOWN * 0.5)
        row2 = VGroup(feat4, feat5).arrange(RIGHT, buff=0.5).shift(DOWN * 1.3)
        feats = VGroup(row1, row2)

        # 4. 底部总结
        summary = Text(
            "不归任何一家管",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(db_group, shift=DOWN), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(f, shift=UP) for f in [feat1, feat2, feat3, feat4, feat5]], lag_ratio=0.3),
            run_time=step_time
        )
        self.play(Write(summary), run_time=step_time)
        self.play(Circumscribe(summary, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)

        口播稿：为什么国家要搞数字货币？两个大目的。
                第一，防洗钱、方便征税。每一笔钱去了哪儿都记录在案，想逃税？门都没有。
                第二，国际贸易结算。现在跨国转账都得走美国的SWIFT系统，
                人家随时能卡你脖子。数字货币能帮咱们绕开这个限制，这是大国博弈的金融武器。

        关键词/短语：
        - "防洗钱/征税" -> security_shield 图标
        - "SWIFT系统" -> network 图标
        - "大国博弈" -> 红色紧迫感
        - "金融武器" -> 金色强调

        动态标题：「国家为啥搞数字货币」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "国家为啥搞数字货币",
            font=self.title_font,
            font_size=self.font_title_size,
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 目的一：防洗钱征税
        shield_icon = self.load_png_icon("security_shield", height=1.2).shift(LEFT * 2.0 + UP * 1.5)
        purpose1_label = Text("目的一", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(shield_icon, DOWN, buff=0.2)
        purpose1_text = Text("防洗钱·方便征税", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(purpose1_label, DOWN, buff=0.1)
        purpose1 = Group(shield_icon, purpose1_label, purpose1_text)

        # 3. 目的二：绕开 SWIFT
        net_icon = self.load_png_icon("globe", height=1.2).shift(RIGHT * 2.0 + UP * 1.5)
        purpose2_label = Text("目的二", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(net_icon, DOWN, buff=0.2)
        purpose2_text = Text("绕开SWIFT·国际结算", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(purpose2_label, DOWN, buff=0.1)
        purpose2 = Group(net_icon, purpose2_label, purpose2_text)

        purposes = Group(purpose1, purpose2)

        # 4. 关键短语
        key_phrase = Text(
            "随时能卡你脖子",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).shift(DOWN * 1.0)

        # 5. 底部结论
        conclusion = Text(
            "大国博弈的金融武器",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(purposes, shift=UP), run_time=step_time)
        self.play(Write(key_phrase), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)
        self.play(Circumscribe(conclusion, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)

        口播稿：注意了，人民银行的数字货币并不是基于区块链发行的。
                它本质上是把造币技术数字化了，只是在流通和监管环节用了区块链技术。
                这跟市面上那些山寨币完全是两码事，千万别搞混了。

        关键词/短语：
        - "数字人民币 ≠ 区块链" -> 对比布局
        - "造币技术数字化" -> 蓝色知识
        - "山寨币两码事" -> 红色警告

        动态标题：「数字人民币 ≠ 比特币」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "数字人民币 ≠ 比特币",
            font=self.title_font,
            font_size=self.font_title_size,
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 左右对比
        # 左侧 - 数字人民币（绿色正面）
        rmb_icon = self.load_png_icon("bank_building", height=1.5).shift(LEFT * 2.0 + UP * 1.5)
        rmb_label = Text("数字人民币", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(rmb_icon, DOWN, buff=0.2)
        rmb_sub = Text("造币技术数字化", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(rmb_label, DOWN, buff=0.1)
        rmb_group = Group(rmb_icon, rmb_label, rmb_sub)

        # 中间
        neq = Text("≠", font=self.title_font, font_size=self.font_title_size, color=RED).shift(UP * 1.5)

        # 右侧 - 山寨币（红色负面）
        btc_icon = self.load_png_icon("bitcoin", height=1.5).shift(RIGHT * 2.0 + UP * 1.5)
        btc_label = Text("山寨币", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(btc_icon, DOWN, buff=0.2)
        btc_sub = Text("完全两码事", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(btc_label, DOWN, buff=0.1)
        btc_group = Group(btc_icon, btc_label, btc_sub)

        # 3. 底部警告
        warning = Text(
            "千万别搞混了！",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(rmb_group, shift=RIGHT), Write(neq), FadeIn(btc_group, shift=LEFT), run_time=step_time)
        self.play(Write(warning), Circumscribe(warning, color=RED), run_time=step_time)
        self.wait(step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)

        口播稿：记住一个铁律：没有国家信用背书的币，不管它技术多牛，本质上都是资金盘。
                你看到的暴富故事，背后都是无数人血本无归。
                创造信用是世界上最难的事，也是一个人最大的价值。
                与其追各种空气币，不如好好经营自己的信用和能力。

        关键词/短语：
        - "铁律" -> warning 图标
        - "没有国家信用背书 = 资金盘" -> 红色核心
        - "经营自己的信用和能力" -> 金色策略

        动态标题：「没有信用背书就是资金盘」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "没有信用背书就是资金盘",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(UP * 4.0)

        # 2. 铁律强调
        warning_icon = self.load_png_icon("warning", height=1.5).move_to(UP * 2.0)
        iron_rule = Text(
            "技术再牛，没国家背书也是空气",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).next_to(warning_icon, DOWN, buff=0.3)
        rule_group = Group(warning_icon, iron_rule)

        # 3. 暴富 vs 血本无归
        truth = Text(
            "暴富故事背后 = 无数人血本无归",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).shift(DOWN * 0.5)

        # 4. 正确做法
        strategy = Text(
            "经营自己的信用和能力",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 2.5)

        # 5. 底部金句
        golden = Text(
            "创造信用是最大的价值",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(rule_group, shift=UP), run_time=step_time)
        self.play(Write(truth), run_time=step_time)
        self.play(Write(strategy), run_time=step_time)
        self.play(Write(golden), Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action)

        口播稿：区块链是好技术，但别被人拿它当幌子割你韭菜。
                觉得有用就转发给身边的朋友，关注我，下期见。

        动态标题：「别被割韭菜」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "别被割韭菜",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "区块链是好技术，别被当幌子",
            font=self.body_font,
            font_size=self.font_body_size,
            color=WHITE
        ).move_to(UP * 2.0)
        takeaway_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=GOLD, fill_opacity=0.1)
        takeaway_box.surround(takeaway, buff=0.3)
        takeaway_group = VGroup(takeaway_box, takeaway)

        # 3. 互动图标
        like_icon = self.load_png_icon("thumbs_up", height=1.5).move_to(LEFT * 2.5 + DOWN * 0.5)
        like_label = Text("转发", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
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
