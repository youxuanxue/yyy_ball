import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson006VerticalScenes(Zsxq100keLessonVertical):
    """
    第006课：金融界的天庭
    副标题：一行三会，谁在管你的钱
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：引发共鸣 -> 反常识观点 -> 抓住注意力
        
        口播稿关键词/短语：
        - "央行、银保监、证监会" -> 三个机构名词
        - "离你很远" -> 误解认知
        - "都在他们的眼皮子底下" -> 核心反转
        - "金融界的天庭" -> 比喻，用 crown 图标
        - "谁在管你的钱" -> 引发思考
        
        动态标题：「谁在管你的钱？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、误解、三机构图标组、反转文字、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题 (y=4.0) - 引发好奇
        title = Text(
            "谁在管你的钱？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 误解文字 - 离我很远
        wrong_text = Text(
            "「这些机构离我很远」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(UP * 2.5)
        wrong_cross = Cross(wrong_text, stroke_color=RED, stroke_width=4)
        
        # 3. 三大机构图标并排展示
        # 图标来源：bank_building (央行), shield (银保监), stocks (证监会)
        icon_央行 = self.load_png_icon("bank_building", height=1.5).move_to(UP * 0.5 + LEFT * 2.8)
        label_央行 = Text("央行", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(icon_央行, DOWN, buff=0.2)
        group_央行 = Group(icon_央行, label_央行)
        
        icon_银保监 = self.load_png_icon("shield", height=1.5).move_to(UP * 0.5)
        label_银保监 = Text("银保监", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(icon_银保监, DOWN, buff=0.2)
        group_银保监 = Group(icon_银保监, label_银保监)
        
        icon_证监会 = self.load_png_icon("stocks", height=1.5).move_to(UP * 0.5 + RIGHT * 2.8)
        label_证监会 = Text("证监会", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(icon_证监会, DOWN, buff=0.2)
        group_证监会 = Group(icon_证监会, label_证监会)
        
        all_icons = Group(group_央行, group_银保监, group_证监会)
        
        # 4. 反转文字 - 都在他们眼皮子底下
        reveal_text = Text(
            "你的每一分钱", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(DOWN * 1.8)
        reveal_text2 = Text(
            "都在他们眼皮子底下", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).next_to(reveal_text, DOWN, buff=0.2)
        
        # 5. 底部结论 - 金融界的天庭
        # 图标来源：crown 象征天庭权威
        crown_icon = self.load_png_icon("crown", height=1.2).move_to(DOWN * 3.5 + LEFT * 2.5)
        conclusion = Text(
            "金融界的天庭", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).next_to(crown_icon, RIGHT, buff=0.3)
        conclusion_group = Group(crown_icon, conclusion)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(wrong_text), Create(wrong_cross), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(group_央行, shift=UP),
                FadeIn(group_银保监, shift=UP),
                FadeIn(group_证监会, shift=UP),
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        self.play(Write(reveal_text), Write(reveal_text2), run_time=step_time)
        self.play(FadeIn(conclusion_group, scale=0.8), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：核心概念 -> 层级结构 -> 清晰分类
        
        口播稿关键词/短语：
        - "三大监管机构" -> 核心数字
        - "央行是央妈，管货币政策，决定印多少钱" -> 第一机构
        - "银保监管银行和保险公司" -> 第二机构
        - "证监会管股票和证券公司" -> 第三机构
        - "一行两会" -> 核心概念
        - "银监和保监合并了" -> 变化说明
        
        动态标题：「一行两会」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、央行、银保监、证监会、总结）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部：核心概念标题
        title = Text(
            "一行两会", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 央行 - 图标 + 文字说明
        央行_icon = self.load_png_icon("printer", height=1.3).move_to(UP * 2.3 + LEFT * 3.2)
        央行_title = Text("央行（央妈）", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(央行_icon, RIGHT, buff=0.3)
        央行_desc = Text("管货币政策，决定印多少钱", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(央行_title, DOWN, buff=0.15, aligned_edge=LEFT)
        央行_group = Group(央行_icon, 央行_title, 央行_desc)
        
        # 3. 银保监 - 图标 + 文字说明
        银保监_icon = self.load_png_icon("safe", height=1.3).move_to(UP * 0.3 + LEFT * 3.2)
        银保监_title = Text("银保监", font=self.title_font, font_size=self.font_body_size, color=GREEN).next_to(银保监_icon, RIGHT, buff=0.3)
        银保监_desc = Text("管银行和保险公司", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(银保监_title, DOWN, buff=0.15, aligned_edge=LEFT)
        银保监_group = Group(银保监_icon, 银保监_title, 银保监_desc)
        
        # 4. 证监会 - 图标 + 文字说明
        证监会_icon = self.load_png_icon("stocks", height=1.3).move_to(DOWN * 1.7 + LEFT * 3.2)
        证监会_title = Text("证监会", font=self.title_font, font_size=self.font_body_size, color=BLUE).next_to(证监会_icon, RIGHT, buff=0.3)
        证监会_desc = Text("管股票和证券公司", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(证监会_title, DOWN, buff=0.15, aligned_edge=LEFT)
        证监会_group = Group(证监会_icon, 证监会_title, 证监会_desc)
        
        # 5. 底部总结 - 金句框
        summary = Text(
            "银监+保监 → 银保监", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(央行_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(银保监_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(证监会_group, shift=RIGHT), run_time=step_time)
        self.play(Write(summary), Circumscribe(summary, color=ORANGE), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：核心洞察 -> 监管职能 -> 底线
        
        口播稿关键词/短语：
        - "有监管才有底线" -> 核心洞察
        - "银行能不能乱放贷？银保监说了算" -> 职能1
        - "上市公司能不能造假？证监会盯着" -> 职能2
        - "规则是他们定的" -> 权力来源
        - "不懂规则就容易踩坑" -> 警示
        
        动态标题：「有监管才有底线」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、银保监职能、证监会职能、规则提示、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "有监管才有底线", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 银保监职能 - 问答形式
        q1 = Text("银行能不能乱放贷？", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(UP * 2.3 + LEFT * 2.0)
        a1 = Text("→ 银保监说了算", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(q1, RIGHT, buff=0.3)
        row1 = VGroup(q1, a1)
        
        # 3. 证监会职能 - 问答形式
        q2 = Text("上市公司能不能造假？", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(UP * 0.8 + LEFT * 1.5)
        a2 = Text("→ 证监会盯着", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(q2, RIGHT, buff=0.3)
        row2 = VGroup(q2, a2)
        
        # 4. 规则提示 - 金句框
        rule_text = Text(
            "规则是他们定的", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(DOWN * 1.0)
        rule_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=ORANGE, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=ORANGE
        ).surround(rule_text, buff=0.4)
        rule_group = VGroup(rule_box, rule_text)
        
        # 5. 底部警示结论
        conclusion = Text(
            "不懂规则，容易踩坑！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(q1), FadeIn(a1, shift=LEFT), run_time=step_time)
        self.play(Write(q2), FadeIn(a2, shift=LEFT), run_time=step_time)
        self.play(FadeIn(rule_group, scale=0.8), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=RED), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：具象化场景 -> 对号入座 -> 引发认同
        
        口播稿关键词/短语：
        - "买理财、炒股票、存大额资金" -> 三个场景
        - "遇到问题找对部门" -> 核心指引
        - "买银行理财找银保监投诉" -> 场景1
        - "炒股被骗找证监会举报" -> 场景2
        - "搞清楚门道，关键时刻能救命" -> 落脚点
        
        动态标题：「遇到问题找谁？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、三场景、银保监投诉、证监会举报、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "遇到问题找谁？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 4.0)
        
        # 2. 三个需要知道的场景
        场景_icon1 = self.load_png_icon("deposit", height=1.0).move_to(UP * 2.3 + LEFT * 1.5)
        场景_text1 = Text("买理财", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(场景_icon1, RIGHT, buff=0.3)
        场景1 = Group(场景_icon1, 场景_text1)
        
        场景_icon2 = self.load_png_icon("stocks", height=1.0).next_to(场景_icon1, DOWN)
        场景_text2 = Text("炒股票", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(场景_icon2, RIGHT, buff=0.3)
        场景2 = Group(场景_icon2, 场景_text2)
        
        场景_icon3 = self.load_png_icon("coins", height=1.0).next_to(场景_icon2, DOWN)
        场景_text3 = Text("存大额", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(场景_icon3, RIGHT, buff=0.3)
        场景3 = Group(场景_icon3, 场景_text3)
        
        all_场景 = Group(场景1, 场景2, 场景3)
        
        # 3. 投诉渠道1 - 银行理财找银保监
        channel1_icon = self.load_png_icon("safe", height=1.2).move_to(DOWN * 1.5 + LEFT * 3.5)
        channel1_text = Text("银行理财出问题 → 找银保监", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(channel1_icon, RIGHT, buff=0.3)
        channel1 = Group(channel1_icon, channel1_text)
        
        # 4. 投诉渠道2 - 炒股被骗找证监会
        channel2_icon = self.load_png_icon("shield", height=1.2).next_to(channel1_icon, DOWN)
        channel2_text = Text("炒股被骗 → 找证监会", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(channel2_icon, RIGHT, buff=0.3)
        channel2 = Group(channel2_icon, channel2_text)
        
        # 5. 底部结论
        conclusion = Text(
            "搞清门道，关键时刻能救命！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(场景1, shift=DOWN),
                FadeIn(场景2, shift=DOWN),
                FadeIn(场景3, shift=DOWN),
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        self.play(FadeIn(channel1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(channel2, shift=RIGHT), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：行动步骤 -> 逐项弹出 -> 强调可执行
        
        口播稿关键词/短语：
        - "口诀：央行管印钱，银保监管存钱，证监会管炒钱" -> 核心口诀
        - "买理财之前，先看是谁发的" -> 策略1
        - "银行的归银保监管，券商的归证监会管" -> 策略2
        - "有牌照的正规军，出了事至少能找到人" -> 策略3
        
        动态标题：「记住这个口诀」
        使用 LaggedStart 实现逐项弹出效果
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、口诀、三策略LaggedStart、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "记住这个口诀", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心口诀 - 金句框
        slogan_line1 = Text("央行管印钱", font=self.title_font, font_size=self.font_body_size, color=GOLD).move_to(UP * 2.5)
        slogan_line2 = Text("银保监管存钱", font=self.title_font, font_size=self.font_body_size, color=GREEN).next_to(slogan_line1, DOWN, buff=0.5)
        slogan_line3 = Text("证监会管炒钱", font=self.title_font, font_size=self.font_body_size, color=BLUE).next_to(slogan_line2, DOWN, buff=0.5)
        slogan_group = VGroup(slogan_line1, slogan_line2, slogan_line3)
        
        slogan_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.1,
            fill_color=GOLD
        ).surround(slogan_group, buff=0.3)
        slogan_with_box = VGroup(slogan_box, slogan_group)
        
        # 3. 策略列表
        item1 = Text("① 买理财前，先看是谁发的", font=self.body_font, font_size=self.font_body_size, color=WHITE).move_to(DOWN * 0.5)
        item2 = Text("② 银行的归银保监，券商的归证监会", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(item1, DOWN, buff=0.5)
        item3 = Text("③ 有牌照的正规军，出事能找到人", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(item2, DOWN, buff=0.5)
        
        items = [item1, item2, item3]
        
        # 4. 底部结论
        # 图标来源：certificate 代表牌照
        cert_icon = self.load_png_icon("certificate", height=1.0).move_to(DOWN * 4.0 + LEFT * 2.5)
        conclusion = Text(
            "正规牌照 = 有人管", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).next_to(cert_icon, RIGHT, buff=0.3)
        conclusion_group = Group(cert_icon, conclusion)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(slogan_with_box, scale=0.9), run_time=step_time)
        # 使用 LaggedStart 逐项弹出，lag_ratio=0.3
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT) for item in items], 
                lag_ratio=0.3
            ), 
            run_time=2*step_time
        )
        self.play(FadeIn(conclusion_group, scale=0.8), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：低门槛互动 -> 强调动画 -> 引导关注
        
        口播稿关键词/短语：
        - "现在你知道金融界的天庭了吧" -> 回顾
        - "下次买理财之前，先查查发行方有没有牌照" -> 互动任务
        - "点赞收藏" -> 互动号召
        - "下期继续聊理财干货" -> 预告
        
        动态标题：「查牌照，防踩坑」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、互动任务、互动图标、系列口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 核心CTA标题
        title = Text(
            "查牌照，防踩坑", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 3.5)
        
        # 2. 互动任务 - 金句框
        task_text = Text(
            "买理财前，先查发行方牌照", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(UP * 1.8)
        task_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(task_text, buff=0.4)
        task_group = VGroup(task_box, task_text)
        
        # 3. 点赞图标
        # 图标来源：like 在 all_png_names.txt
        like_icon = self.load_png_icon("like", height=2.0).move_to(LEFT * 2 + DOWN * 0.3)
        like_text = Text("点赞", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_text)
        
        # 4. 收藏图标
        # 图标来源：add_to_favorites 在 all_png_names.txt
        fav_icon = self.load_png_icon("add_to_favorites", height=2.0).move_to(RIGHT * 2 + DOWN * 0.3)
        fav_text = Text("收藏", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(fav_icon, DOWN, buff=0.2)
        fav_group = Group(fav_icon, fav_text)
        
        icons_group = Group(like_group, fav_group)
        
        # 5. 系列口号 - 金句框
        slogan_text = Text(
            "每天一课，日日生金！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)
        slogan_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=GOLD
        ).surround(slogan_text, buff=0.5)
        slogan_group = VGroup(slogan_box, slogan_text)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(task_group, scale=0.9), Circumscribe(task_text, color=GOLD), run_time=step_time)
        self.play(FadeIn(icons_group, shift=UP), run_time=step_time)
        self.play(
            FadeIn(slogan_group, scale=0.8), 
            Circumscribe(slogan_text, color=GOLD, fade_out=True),
            run_time=step_time
        )

        # 不需要淡出，作为结尾画面保留
        self.wait(0.5)

    def get_cover_decoration_icons(self):
        """
        根据 build_scene_1 到 build_scene_6 的动画内容和 script.json 的 icons 字段
        选择封面装饰图标，不超过5个。
        
        选用图标及其理由：
        - bank_building: 央行/银行核心概念
        - crown: 金融界的天庭
        - shield: 银保监监管保护
        - stocks: 证监会/股票
        - certificate: 牌照/正规军
        """
        return ["bank_building", "crown", "shield", "stocks", "certificate"]
