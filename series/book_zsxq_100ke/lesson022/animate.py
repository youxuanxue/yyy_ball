import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson022VerticalScenes(Zsxq100keLessonVertical):
    """
    第022课：地摊经济
    主题：摆摊能发财吗？看清财富的四个层次
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)

        口播稿：前阵子地摊经济火得一塌糊涂，百度阿里都下场了，连必胜客都在路边支起了摊子。
                你身边是不是也有人拉你去练摊？先别急，今天咱们从财富管理的角度，
                帮你看清楚地摊这事到底值不值得干。

        关键词/短语：
        - "地摊经济火了" -> market_square 图标，灰色热度感
        - "百度阿里都下场" -> business 图标
        - "拉你去练摊" -> 焦虑灰色
        - "值不值得干" -> 金色转折悬念

        动态标题：「地摊经济真能发财？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题 - 灰色冷色调，引发好奇
        title = Text(
            "地摊经济真能发财？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 地摊图标 + "火得一塌糊涂"
        stall_icon = self.load_png_icon("market_square", height=2.0).move_to(UP * 1.5)
        hot_text = Text(
            "百度阿里都下场了",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).next_to(stall_icon, DOWN, buff=0.3)
        stall_group = Group(stall_icon, hot_text)

        # 3. "拉你去练摊" - 关键短语浮现
        pull_text = Text(
            "身边有人拉你去练摊？",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).shift(DOWN * 1.0)

        # 4. 底部悬念 - 金色转折
        hook = Text(
            "先别急，从财富管理角度看看",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(stall_group, shift=UP), run_time=step_time)
        self.play(Write(pull_text), run_time=step_time)
        self.play(Write(hook), run_time=step_time)
        self.play(Circumscribe(hook, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)

        口播稿：地摊本质上就是最原始的货物贸易。摊主不是生产商，货都是进来的，
                在信息透明的今天，基本不存在稀缺品。不管你是卖烤串还是卖袜子，
                目标客户都是冲动消费的路人。说白了，摆地摊就是在出售你的体力劳动，赚的是辛苦钱。

        关键词/短语：
        - "最原始的货物贸易" -> sell/shopping 图标
        - "出售体力劳动" -> worker 图标
        - "赚的是辛苦钱" -> 红色强调

        动态标题：「地摊的本质是什么？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题 - 金色知识色调
        title = Text(
            "地摊的本质是什么？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 核心定义
        definition = Text(
            "最原始的货物贸易",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).move_to(UP * 2.5)

        # 3. 图标辅助 - 卖东西 -> 冲动消费
        sell_icon = self.load_png_icon("sell", height=1.5).shift(LEFT * 2.0 + UP * 0.5)
        sell_label = Text("卖烤串卖袜子", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(sell_icon, DOWN, buff=0.2)
        sell_group = Group(sell_icon, sell_label)

        worker_icon = self.load_png_icon("worker", height=1.5).shift(RIGHT * 2.0 + UP * 0.5)
        worker_label = Text("出售体力劳动", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(worker_icon, DOWN, buff=0.2)
        worker_group = Group(worker_icon, worker_label)

        icons_group = Group(sell_group, worker_group)

        # 4. 底部结论 - 红色扎心
        conclusion = Text(
            "说白了，赚的就是辛苦钱",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(definition), run_time=step_time)
        self.play(FadeIn(icons_group, shift=UP), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)
        self.play(Circumscribe(conclusion, color=RED), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)

        口播稿：财富来源有四个层次。最底层是体力劳动收入，门槛低、替代性高、衰减快。
                第二层是脑力劳动收入，靠智慧吃饭，但不稳定。
                第三层是资产性收入，比如房产增值和租金，不用干活钱照样来。
                最顶层是资源性收入，牌照、IP、行业霸主地位，躺着都赚钱。

        关键词/短语：
        - "四个层次" -> 递进布局，从下到上
        - "体力 -> 脑力 -> 资产 -> 资源" -> 颜色从灰到金递进
        - "躺着都赚钱" -> 金色顶层强调

        动态标题：「财富的四个层次」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：6个动作
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text(
            "财富的四个层次",
            font=self.title_font,
            font_size=self.font_title_size,
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 四层递进 - 从底到顶，颜色从灰到金
        level1_icon = self.load_png_icon("worker", height=0.8).shift(LEFT * 3.0 + DOWN * 1.5)
        level1_text = Text("①体力劳动收入", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(level1_icon, RIGHT, buff=0.3)
        level1_sub = Text("门槛低·替代性高", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(level1_text, DOWN, buff=0.1).align_to(level1_text, LEFT)
        level1 = Group(level1_icon, level1_text, level1_sub)

        level2_icon = self.load_png_icon("brain", height=0.8).shift(LEFT * 3.0 + DOWN * 0.0)
        level2_text = Text("②脑力劳动收入", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(level2_icon, RIGHT, buff=0.3)
        level2_sub = Text("靠智慧·但不稳定", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(level2_text, DOWN, buff=0.1).align_to(level2_text, LEFT)
        level2 = Group(level2_icon, level2_text, level2_sub)

        level3_icon = self.load_png_icon("real_estate", height=0.8).shift(LEFT * 3.0 + UP * 1.5)
        level3_text = Text("③资产性收入", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(level3_icon, RIGHT, buff=0.3)
        level3_sub = Text("不干活钱照样来", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(level3_text, DOWN, buff=0.1).align_to(level3_text, LEFT)
        level3 = Group(level3_icon, level3_text, level3_sub)

        level4_icon = self.load_png_icon("goal", height=0.8).shift(LEFT * 3.0 + UP * 3.0)
        level4_text = Text("④资源性收入", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(level4_icon, RIGHT, buff=0.3)
        level4_sub = Text("牌照·IP·躺着赚钱", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(level4_text, DOWN, buff=0.1).align_to(level4_text, LEFT)
        level4 = Group(level4_icon, level4_text, level4_sub)

        # 3. 底部结论
        conclusion = Text(
            "地摊 = 最底层的体力劳动",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(level1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(level2, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(level3, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(level4, shift=RIGHT), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=RED), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)

        口播稿：如果你现在收入稳定，只是闲着想体验一下，偶尔摆个摊没问题，当社会实践。
                但千万别把地摊当成主业，更别辞职去练摊。
                你的时间和精力是最宝贵的资源，应该花在能让你往更高层级跃迁的事情上。

        关键词/短语：
        - "偶尔摆个摊" -> 绿色 OK
        - "千万别当主业" -> 红色警告
        - "时间和精力是最宝贵的资源" -> 金色强调

        动态标题：「摆摊可以，但别当主业」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "摆摊可以，但别当主业",
            font=self.title_font,
            font_size=self.font_title_size,
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 左右对比：可以做 vs 别做
        # 左侧 - 可以偶尔体验（绿色）
        ok_icon = self.load_png_icon("shopping", height=1.5).shift(LEFT * 2.0 + UP * 1.5)
        ok_label = Text("偶尔体验", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(ok_icon, DOWN, buff=0.2)
        ok_sub = Text("当社会实践", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(ok_label, DOWN, buff=0.1)
        ok_group = Group(ok_icon, ok_label, ok_sub)

        # 右侧 - 别当主业（红色）
        no_icon = self.load_png_icon("warning", height=1.5).shift(RIGHT * 2.0 + UP * 1.5)
        no_label = Text("别当主业", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(no_icon, DOWN, buff=0.2)
        no_sub = Text("更别辞职练摊", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(no_label, DOWN, buff=0.1)
        no_group = Group(no_icon, no_label, no_sub)

        # 3. 中间 VS
        vs_text = Text("VS", font=self.title_font, font_size=self.font_title_size, color=WHITE).shift(UP * 1.5)

        # 4. 底部金句
        golden = Text(
            "时间和精力是最宝贵的资源",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(ok_group, shift=RIGHT), FadeIn(vs_text), FadeIn(no_group, shift=LEFT), run_time=step_time)
        self.play(Write(golden), run_time=step_time)
        self.play(Circumscribe(golden, color=GOLD), run_time=step_time)
        self.wait(step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)

        口播稿：聪明的做法是什么？
                第一，把体力劳动升级成脑力劳动，学一门技能，提升你的稀缺性。
                第二，用脑力劳动赚来的钱去买入资产，让钱帮你生钱。
                第三，积累行业资源，打造你的个人IP。
                记住，从第一层往第四层爬，才是正确的财富路径。

        关键词/短语：
        - "体力 -> 脑力" -> 升级箭头
        - "买入资产" -> investment 图标
        - "打造个人IP" -> personal_growth 图标
        - "正确的财富路径" -> 金色强调

        动态标题：「三步跃迁财富层级」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "三步跃迁财富层级",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三步策略 - 逐项弹出
        step1_icon = self.load_png_icon("education", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        step1_text = Text(
            "①体力升级为脑力",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(step1_icon, RIGHT, buff=0.3)
        step1_sub = Text("学技能，提升稀缺性", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(step1_text, DOWN, buff=0.1).align_to(step1_text, LEFT)
        step1 = Group(step1_icon, step1_text, step1_sub)

        step2_icon = self.load_png_icon("investment", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        step2_text = Text(
            "②用赚的钱买入资产",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GREEN
        ).next_to(step2_icon, RIGHT, buff=0.3)
        step2_sub = Text("让钱帮你生钱", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(step2_text, DOWN, buff=0.1).align_to(step2_text, LEFT)
        step2 = Group(step2_icon, step2_text, step2_sub)

        step3_icon = self.load_png_icon("personal_growth", height=0.8).shift(LEFT * 3.0 + DOWN * 1.4)
        step3_text = Text(
            "③积累资源，打造IP",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).next_to(step3_icon, RIGHT, buff=0.3)
        step3_sub = Text("行业霸主地位", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(step3_text, DOWN, buff=0.1).align_to(step3_text, LEFT)
        step3 = Group(step3_icon, step3_text, step3_sub)

        steps = [step1, step2, step3]

        # 3. 底部总结
        summary = Text(
            "从第一层往第四层爬！",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(s, shift=RIGHT) for s in steps], lag_ratio=0.3),
            run_time=2 * step_time
        )
        self.play(Write(summary), run_time=step_time)
        self.play(Circumscribe(summary, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action)

        口播稿：地摊经济不是不能碰，但别被风口冲昏了头。
                看清财富的底层逻辑，才能做出聪明的选择。
                关注我，咱们下期继续聊。

        关键词/短语：
        - "看清底层逻辑" -> light_bulb 图标
        - "聪明的选择" -> 金色强调

        动态标题：「别被风口冲昏了头」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "别被风口冲昏了头",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "看清财富底层逻辑",
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
