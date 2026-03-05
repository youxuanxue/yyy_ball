import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson040VerticalScenes(Zsxq100keLessonVertical):
    """
    第040课：政府工程怎么玩
    主题：BT、BOT、PPP、EPC全解析
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：政府修路钱从哪来？

        口播稿关键词/短语：
        - "高速公路几十个亿" -> road 图标
        - "政府不赚钱" -> 矛盾揭示
        - "怎么建起来的" -> 好奇心

        动态标题：「修路的钱从哪来？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、工程场景、政府不赚钱、怎么建的、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "修路的钱从哪来？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 工程场景
        road_icon = self.load_png_icon("road", height=1.8).move_to(UP * 1.8)
        road_text = Text(
            "一条高速公路要几十个亿",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).next_to(road_icon, DOWN, buff=0.3)
        road_group = Group(road_icon, road_text)

        # 3. 矛盾
        conflict = Text(
            "地方政府不搞经营 没有盈利",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).move_to(DOWN * 0.5)

        # 4. 疑问
        question = Text(
            "桥、路、产业园怎么建起来的？",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).move_to(DOWN * 1.8)

        # 5. 底部
        bottom = Text(
            "今天给你揭开这个秘密",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(road_group, shift=UP), run_time=step_time)
        self.play(Write(conflict), run_time=step_time)
        self.play(Write(question), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：四种金融玩法

        口播稿关键词/短语：
        - "BT 建完了再给钱" -> 第一种
        - "BOT 建完了你先收费" -> 第二种
        - "PPP 合资一起干" -> 第三种
        - "EPC 只出设计不垫钱" -> 第四种

        动态标题：「四种金融玩法」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、BT+BOT、PPP+EPC、底部、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "四种金融玩法",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. BT和BOT
        bt_label = Text("BT", font=self.title_font, font_size=self.font_title_size, color=BLUE).move_to(LEFT * 2.0 + UP * 2.2)
        bt_desc = Text("建完再给钱", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(bt_label, DOWN, buff=0.15)

        bot_label = Text("BOT", font=self.title_font, font_size=self.font_title_size, color=GREEN).move_to(RIGHT * 2.0 + UP * 2.2)
        bot_desc = Text("建完你先收费", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(bot_label, DOWN, buff=0.15)

        # 3. PPP和EPC
        ppp_label = Text("PPP", font=self.title_font, font_size=self.font_title_size, color=GOLD).move_to(LEFT * 2.0 + DOWN * 0.3)
        ppp_desc = Text("合资一起干", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(ppp_label, DOWN, buff=0.15)

        epc_label = Text("EPC", font=self.title_font, font_size=self.font_title_size, color=ORANGE).move_to(RIGHT * 2.0 + DOWN * 0.3)
        epc_desc = Text("只出设计不垫钱", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(epc_label, DOWN, buff=0.15)

        # 4. 底部
        bottom = Text(
            "风险和收益各不相同",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(bt_label), Write(bt_desc), Write(bot_label), Write(bot_desc), run_time=step_time)
        self.play(Write(ppp_label), Write(ppp_desc), Write(epc_label), Write(epc_desc), run_time=step_time)
        self.play(Write(bottom), run_time=step_time)
        self.play(Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：政府工程不等于稳赚

        口播稿关键词/短语：
        - "BT尾款要不回来" -> 第一坑
        - "BOT收费权不覆盖成本" -> 第二坑
        - "PPP烂尾风险" -> 第三坑
        - "上市公司都栽了" -> 警示

        动态标题：「政府工程稳赚不赔？」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、三个风险逐项、上市公司警示、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "政府工程稳赚不赔？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(UP * 4.0)

        # 2. BT风险
        r1 = Text("BT  先干活 尾款好几年要不回", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(UP * 2.0)

        # 3. BOT风险
        r2 = Text("BOT  收费权不一定覆盖成本", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(UP * 0.5)

        # 4. PPP风险
        r3 = Text("PPP  规模大但烂尾风险不小", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(DOWN * 1.0)

        # 5. 警示
        warn_icon = self.load_png_icon("warning", height=0.8).move_to(LEFT * 3.0 + DOWN * 2.5)
        warn_text = Text("好几家上市公司都栽了", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(warn_icon, RIGHT, buff=0.3)
        warn_group = Group(warn_icon, warn_text)

        # 底部
        bottom = Text(
            "大错特错！",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(r1), run_time=step_time)
        self.play(Write(r2), Write(r3), run_time=step_time)
        self.play(FadeIn(warn_group, shift=RIGHT), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=RED), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：理财底层资产

        口播稿关键词/短语：
        - "银行理财或信托" -> 底层资产
        - "BT BOT PPP区别" -> 风险判断
        - "发达地区BT最安全" -> 安全排序

        动态标题：「你的理财可能就是这些」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、理财底层、区别判断、底部）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "你的理财可能就是这些",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 理财底层
        bank_icon = self.load_png_icon("bank_building", height=1.2).move_to(UP * 1.8)
        bank_text = Text(
            "银行理财、信托产品的底层",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(bank_icon, DOWN, buff=0.3)
        bank_sub = Text(
            "很可能就是给这类工程融资",
            font=self.body_font,
            font_size=self.font_small_size,
            color=GRAY
        ).next_to(bank_text, DOWN, buff=0.2)
        bank_group = Group(bank_icon, bank_text, bank_sub)

        # 3. 安全排序
        safe_text = Text("发达地区 BT 项目最安全", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 0.8)
        risk_text = Text("欠发达地区 PPP 要小心", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(DOWN * 1.8)

        # 4. 底部
        bottom = Text(
            "搞清楚就知道风险在哪",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(bank_group, shift=UP), run_time=step_time)
        self.play(Write(safe_text), Write(risk_text), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：选理财的排序

        口播稿关键词/短语：
        - "BT > BOT > PPP" -> 安全排序
        - "看项目在哪个城市" -> 财政实力
        - "东部省会最安全" -> 地域选择
        - "EPC门槛高" -> 补充

        动态标题：「选理财记住这个排序」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、排序、地域、EPC补充、底部）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "选理财记住这个排序",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 安全排序
        rank = Text(
            "BT  >  BOT  >  PPP",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GREEN
        ).move_to(UP * 2.0)
        rank_box = RoundedRectangle(height=1.2, corner_radius=0.2, color=GREEN, fill_opacity=0.1)
        rank_box.surround(rank, buff=0.3)
        rank_group = VGroup(rank_box, rank)
        rank_desc = Text(
            "先给钱的比拖着给的靠谱",
            font=self.body_font,
            font_size=self.font_small_size,
            color=GRAY
        ).next_to(rank_group, DOWN, buff=0.3)

        # 3. 地域选择
        city_icon = self.load_png_icon("building", height=0.8).shift(LEFT * 3.0 + DOWN * 0.5)
        city_text = Text("财政强的东部省会最安全", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(city_icon, RIGHT, buff=0.3)
        city_group = Group(city_icon, city_text)

        # 4. EPC补充
        epc_text = Text(
            "EPC 利润高但门槛也高",
            font=self.body_font,
            font_size=self.font_body_size,
            color=ORANGE
        ).move_to(DOWN * 2.0)

        # 5. 底部
        bottom = Text(
            "看清楚再投",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(rank_group, shift=UP), Write(rank_desc), run_time=step_time)
        self.play(FadeIn(city_group, shift=RIGHT), run_time=step_time)
        self.play(Write(epc_text), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：看理财更通透 -> 互动引导

        动态标题：「理财看得更通透」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、核心收获、互动图标、口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "理财看得更通透",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "搞懂政府工程 理财就通透了",
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
