import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson028VerticalScenes(Zsxq100keLessonVertical):
    """
    第028课：财富归集
    主题：追回你浪费的一半家产
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)

        口播稿：我问你一个问题：你现在有多少钱？别说大概，说个精确数字。说不出来对吧？
                那再问，你明天立刻能拿出去花的活钱有多少？更说不清了吧。
                告诉你一个扎心的事实，百分之八十七以上的人零钱都是闲置的。
                你口袋里的钱，正在悄悄蒸发。

        关键词/短语：
        - "有多少钱" -> question_mark 图标
        - "说不出来" -> 灰色焦虑
        - "87%闲置" -> 红色数据
        - "悄悄蒸发" -> 红色警示

        动态标题：「你的钱在悄悄蒸发」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "你的钱在悄悄蒸发",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 灵魂拷问
        q_icon = self.load_png_icon("question_mark", height=1.5).move_to(UP * 2.0)
        q_text = Text(
            "你现在有多少钱？说不出来吧",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).next_to(q_icon, DOWN, buff=0.3)
        q_group = Group(q_icon, q_text)

        # 3. 数据强调
        data_num = Text(
            "87%",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).shift(DOWN * 0.5)
        data_text = Text(
            "的人零钱都是闲置的",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).next_to(data_num, DOWN, buff=0.2)

        # 4. 底部扎心
        hook = Text(
            "口袋里的钱正在悄悄蒸发",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(q_group, shift=UP), run_time=step_time)
        self.play(Write(data_num), FadeIn(data_text), run_time=step_time)
        self.play(Write(hook), run_time=step_time)
        self.play(Circumscribe(hook, color=RED), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)

        口播稿：什么叫财富归集？就是把散落在各处的零钱，集中起来去投资。
                中国人零钱规模超两万亿，这些钱躺在微信、支付宝、银行卡里睡大觉。
                零钱不归集的后果就是莫名其妙花没了，回头还不知道花哪儿了。
                你的一半家产，就这么无声无息流失了。

        关键词/短语：
        - "财富归集" -> money_circulation 图标
        - "两万亿" -> 数据强调
        - "莫名其妙花没了" -> 红色
        - "一半家产流失" -> 金色警示

        动态标题：「什么是财富归集？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "什么是财富归集？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 核心定义
        circ_icon = self.load_png_icon("money_circulation", height=1.5).move_to(UP * 2.0)
        definition = Text(
            "把散落各处的零钱集中投资",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(circ_icon, DOWN, buff=0.3)
        def_group = Group(circ_icon, definition)

        # 3. 数据 + 现状
        scale = Text(
            "中国人零钱规模超2万亿",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).shift(DOWN * 0.3)
        problem = Text(
            "莫名其妙花没了，还不知道花哪了",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).next_to(scale, DOWN, buff=0.3)

        # 4. 底部警示
        warning = Text(
            "一半家产无声无息流失了",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(def_group, shift=DOWN), run_time=step_time)
        self.play(Write(scale), Write(problem), run_time=step_time)
        self.play(Write(warning), run_time=step_time)
        self.play(Circumscribe(warning, color=RED), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)

        口播稿：你知道为什么早买房的人财务状况反而更好吗？不是因为房子涨了多少，
                而是买房强制把零钱归集了。每个月还房贷，就是被迫把零钱变成长期资产。
                个人财富管理最重要的事，就是短期收入长期投资化，别让钱在口袋里躺着贬值。

        关键词/短语：
        - "买房 = 强制归集" -> house 图标
        - "零钱变长期资产" -> 转变过程
        - "短期收入长期投资化" -> 金色核心

        动态标题：「买房人为啥财务更好？」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "买房人为啥财务更好？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 房子图标 + 核心逻辑
        house_icon = self.load_png_icon("house", height=1.5).move_to(UP * 1.8)
        reason = Text(
            "买房 = 强制把零钱归集",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).next_to(house_icon, DOWN, buff=0.3)
        house_group = Group(house_icon, reason)

        # 3. 转变过程
        before = Text("零钱散落各处", font=self.body_font, font_size=self.font_body_size, color=GRAY).shift(LEFT * 2.0 + DOWN * 0.5)
        arrow = Text("→", font=self.title_font, font_size=self.font_title_size, color=WHITE).shift(DOWN * 0.5)
        after = Text("长期资产", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(RIGHT * 2.0 + DOWN * 0.5)

        # 4. 底部金句
        golden = Text(
            "短期收入长期投资化",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(house_group, shift=UP), run_time=step_time)
        self.play(FadeIn(before), Write(arrow), FadeIn(after), run_time=step_time)
        self.play(Write(golden), run_time=step_time)
        self.play(Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)

        口播稿：什么情况最该做零钱归集？
                第一，每月工资到手别留太多活钱。
                第二，年终奖、报销款到账就投。
                第三，微信红包、零散进账，凑整了马上买基金。
                只要工作稳定身体健康，不必给自己留太高余地。

        关键词/短语：
        - "三种情况" -> 逐项展示
        - "工资/年终奖/红包" -> 三种来源

        动态标题：「什么时候该归集？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "什么时候该归集？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三种情况
        s1_icon = self.load_png_icon("cash_in_hand", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        s1_text = Text("①工资到手别留太多活钱", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(s1_icon, RIGHT, buff=0.3)
        s1 = Group(s1_icon, s1_text)

        s2_icon = self.load_png_icon("dollar_bag", height=0.8).shift(LEFT * 3.0 + UP * 0.5)
        s2_text = Text("②年终奖报销款到账就投", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(s2_icon, RIGHT, buff=0.3)
        s2 = Group(s2_icon, s2_text)

        s3_icon = self.load_png_icon("coins", height=0.8).shift(LEFT * 3.0 + DOWN * 1.0)
        s3_text = Text("③红包零散进账凑整买基金", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(s3_icon, RIGHT, buff=0.3)
        s3 = Group(s3_icon, s3_text)

        items = [s1, s2, s3]

        # 3. 底部结论
        conclusion = Text(
            "工作稳定健康，不必留太多余地",
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
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        self.wait(step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)

        口播稿：三个实操要点。
                第一，尽量不把收入零钱化，账上有钱马上投出去。
                第二，零钱也要追求收益，凑够几百块就买一次基金，积少成多。
                第三，建个专门的投资账户，所有闲钱都往里汇，让归集变成习惯。
                钱包的元气，来自每一笔零钱的归集。

        关键词/短语：
        - "三个要点" -> LaggedStart 逐项弹出
        - "钱包的元气" -> 金色金句

        动态标题：「三招归集你的零钱」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "三招归集你的零钱",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三个要点
        p1_icon = self.load_png_icon("money_transfer", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        p1_text = Text("①有钱马上投出去", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(p1_icon, RIGHT, buff=0.3)
        p1_sub = Text("别把收入零钱化", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(p1_text, DOWN, buff=0.1).align_to(p1_text, LEFT)
        p1 = Group(p1_icon, p1_text, p1_sub)

        p2_icon = self.load_png_icon("growing_money", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        p2_text = Text("②凑几百块就买基金", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(p2_icon, RIGHT, buff=0.3)
        p2_sub = Text("积少成多追收益", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(p2_text, DOWN, buff=0.1).align_to(p2_text, LEFT)
        p2 = Group(p2_icon, p2_text, p2_sub)

        p3_icon = self.load_png_icon("bank_cards", height=0.8).shift(LEFT * 3.0 + DOWN * 1.4)
        p3_text = Text("③建专门投资账户", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(p3_icon, RIGHT, buff=0.3)
        p3_sub = Text("让归集变成习惯", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(p3_text, DOWN, buff=0.1).align_to(p3_text, LEFT)
        p3 = Group(p3_icon, p3_text, p3_sub)

        points = [p1, p2, p3]

        # 3. 底部金句
        golden = Text(
            "钱包的元气来自每笔零钱的归集",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(p, shift=RIGHT) for p in points], lag_ratio=0.3),
            run_time=2 * step_time
        )
        self.play(Write(golden), run_time=step_time)
        self.play(Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action)

        口播稿：理财就是积少成多，积小胜为大胜。从今天开始归集你的零钱吧。
                点赞关注，下期聊十万块钱怎么配置。

        动态标题：「积少成多·积小胜为大胜」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "积少成多·积小胜为大胜",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "从今天开始归集你的零钱",
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
