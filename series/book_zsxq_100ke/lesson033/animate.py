import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson033VerticalScenes(Zsxq100keLessonVertical):
    """
    第033课：投资心态管理
    主题：控制自己才是最大的本事
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：亏钱到肚子疼 -> 心态才是敌人

        口播稿关键词/短语：
        - "亏到肚子疼" -> anxious 图标 + 灰色
        - "肝气犯胃" -> 红色数据
        - "心态才是敌人" -> 红色警示

        动态标题：「炒股亏到肚子疼？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、图标组、肝气犯胃、底部警示、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "炒股亏到肚子疼？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 焦虑图标 + 故事
        anxious_icon = self.load_png_icon("anxious", height=2.0).move_to(UP * 1.5)
        story_text = Text(
            "几个月赚的一天全亏回去",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).next_to(anxious_icon, DOWN, buff=0.3)
        story_group = Group(anxious_icon, story_text)

        # 3. 肝气犯胃
        medical_text = Text(
            "郁闷发不出去，顶到胃了",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).move_to(DOWN * 0.8)

        # 4. 底部真相
        truth = Text(
            "最大的敌人不是行情是心态",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(story_group, shift=UP), run_time=step_time)
        self.play(Write(medical_text), run_time=step_time)
        self.play(Write(truth), run_time=step_time)
        self.play(Circumscribe(truth, color=RED), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：不同投资品的波动范围

        口播稿关键词/短语：
        - "90%外汇" -> 最高风险
        - "50%股票" -> 中高风险
        - "20%基金" -> 适中
        - "10%房产" -> 低风险

        动态标题：「你能扛多大波动？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、四级风险逐项、底部结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "你能扛多大波动？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 风险等级列表
        r1 = Text("90% 波动 → 外汇期货", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(UP * 2.2)
        r2 = Text("50% 波动 → 炒股票", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(UP * 1.0)
        r3 = Text("20% 波动 → 买基金", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 0.2)
        r4 = Text("10% 波动 → 买房子", font=self.body_font, font_size=self.font_body_size, color=BLUE).move_to(DOWN * 1.4)

        # 3. 高亮推荐
        recommend_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=GREEN, fill_opacity=0.15)
        recommend_box.surround(r3, buff=0.3)

        # 4. 底部结论
        bottom = Text(
            "大多数人承受力是20%，选基金",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(r1), Write(r2), run_time=step_time)
        self.play(Write(r3), FadeIn(recommend_box), run_time=step_time)
        self.play(Write(r4), run_time=step_time)
        self.play(Write(bottom), Circumscribe(bottom, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：庄家vs散户对比

        口播稿关键词/短语：
        - "庄家团队作战" -> businessman + 组织
        - "散户一个人顶不住" -> person + 孤独
        - "投资是反人性的" -> 金色金句

        动态标题：「庄家靠心态收割你」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、庄家侧、散户侧、真相、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "庄家靠心态收割你",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(UP * 4.0)

        # 2. 左侧：庄家
        boss_icon = self.load_png_icon("businessman", height=1.5).move_to(LEFT * 2.0 + UP * 1.8)
        boss_label = Text("庄家", font=self.title_font, font_size=self.font_title_size, color=GREEN).next_to(boss_icon, DOWN, buff=0.2)
        boss_desc = Text("团队作战控制人性", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(boss_label, DOWN, buff=0.2)
        boss_group = Group(boss_icon, boss_label, boss_desc)

        # 3. 右侧：散户
        person_icon = self.load_png_icon("person", height=1.5).move_to(RIGHT * 2.0 + UP * 1.8)
        person_label = Text("散户", font=self.title_font, font_size=self.font_title_size, color=RED).next_to(person_icon, DOWN, buff=0.2)
        person_desc = Text("一个人顶不住", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(person_label, DOWN, buff=0.2)
        person_group = Group(person_icon, person_label, person_desc)

        # 4. VS
        vs_text = Text("VS", font=self.title_font, font_size=self.font_title_size, color=WHITE).move_to(UP * 1.8)

        # 5. 底部真相
        truth = Text(
            "投资是反人性的",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(boss_group, shift=RIGHT), FadeIn(vs_text), run_time=step_time)
        self.play(FadeIn(person_group, shift=LEFT), run_time=step_time)
        self.play(Write(truth), run_time=step_time)
        self.play(Circumscribe(truth, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：洗盘vs埋人对比

        口播稿关键词/短语：
        - "洗盘" -> 无利空大跌 + GRAY
        - "埋人" -> 放利好诱你进场 + RED
        - "恐惧时冷静，兴奋时警惕"

        动态标题：「洗盘还是埋人？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、洗盘、埋人、对比、底部金句）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "洗盘还是埋人？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 洗盘
        wash_icon = self.load_png_icon("decrease", height=1.2).move_to(LEFT * 2.0 + UP * 2.0)
        wash_label = Text("洗盘", font=self.title_font, font_size=self.font_title_size, color=GRAY).next_to(wash_icon, DOWN, buff=0.2)
        wash_desc = Text("无利空突然大跌", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(wash_label, DOWN, buff=0.2)
        wash_hint = Text("你想退出=洗盘", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(wash_desc, DOWN, buff=0.1)
        wash_group = Group(wash_icon, wash_label, wash_desc, wash_hint)

        # 3. 埋人
        trap_icon = self.load_png_icon("warning", height=1.2).move_to(RIGHT * 2.0 + UP * 2.0)
        trap_label = Text("埋人", font=self.title_font, font_size=self.font_title_size, color=RED).next_to(trap_icon, DOWN, buff=0.2)
        trap_desc = Text("放利好诱你进场", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(trap_label, DOWN, buff=0.2)
        trap_hint = Text("你想冲进去=埋人", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(trap_desc, DOWN, buff=0.1)
        trap_group = Group(trap_icon, trap_label, trap_desc, trap_hint)

        # 4. 分隔
        vs_text = Text("VS", font=self.title_font, font_size=self.font_title_size, color=WHITE).move_to(UP * 2.0)

        # 5. 底部金句
        golden = Text(
            "恐惧时冷静·兴奋时警惕",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(wash_group, shift=DOWN), FadeIn(vs_text), run_time=step_time)
        self.play(FadeIn(trap_group, shift=DOWN), run_time=step_time)
        self.play(Write(golden), run_time=step_time)
        self.play(Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：两个秘诀

        口播稿关键词/短语：
        - "承受范围内投资" -> shield + GREEN
        - "充沛体力" -> heart_health + BLUE
        - "控制久了就成习惯" -> 金色

        动态标题：「心态稳住的两个秘诀」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作（标题、秘诀1、秘诀2、金句、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "心态稳住的两个秘诀",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 秘诀1：承受范围内投资
        s1_icon = self.load_png_icon("shield", height=1.2).move_to(LEFT * 2.5 + UP * 1.8)
        s1_text = Text("①在承受范围内投资", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(s1_icon, RIGHT, buff=0.3)
        s1_sub = Text("大盘暴跌100点基金只跌2%", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(s1_text, DOWN, buff=0.1).align_to(s1_text, LEFT)
        s1_group = Group(s1_icon, s1_text, s1_sub)

        # 3. 秘诀2：充沛体力
        s2_icon = self.load_png_icon("heart_health", height=1.2).move_to(LEFT * 2.5 + DOWN * 0.3)
        s2_text = Text("②保持充沛的体力精神", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(s2_icon, RIGHT, buff=0.3)
        s2_sub = Text("重大决策前一天早点睡", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(s2_text, DOWN, buff=0.1).align_to(s2_text, LEFT)
        s2_group = Group(s2_icon, s2_text, s2_sub)

        # 4. 底部金句
        golden = Text(
            "控制久了就成习惯，习惯了就赢了",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(s1_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(s2_group, shift=RIGHT), run_time=step_time)
        self.play(Write(golden), run_time=step_time)
        self.play(Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：心态>技术 -> 互动引导

        动态标题：「心态把事做成」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作（标题、核心收获、互动图标、口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "心态把事做成",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "技术做好事，心态做成事",
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
