import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson001VerticalScenes(Zsxq100keLessonVertical):
    """
    第001课：财富、黄金和避险
    副标题：印钞机时代，没有真正的避风港
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：引发共鸣 -> 反常识观点 -> 抓住注意力
        
        口播稿关键词/短语：
        - "买黄金" -> gold_bars 图标
        - "闪闪发光" -> 金色色调
        - "印钞机" -> printer 图标
        - "扎心的真相" -> 红色强调文字
        - "不存在真正能避险的东西" -> 核心痛点
        
        动态标题：「黄金能避险？」（引发怀疑，而非直接用"痛点"）
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、黄金图标、问号、印钞机、扎心文字、强调动画）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题 (y=4.0) - 引发怀疑的标题
        title = Text(
            "黄金能避险？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 中部：黄金图标 - 代表"买黄金"的直觉反应
        # 图标来源：gold_bars 在 all_png_names.txt 第2632行
        gold_icon = self.load_png_icon("gold_bars", height=2.0).move_to(UP * 1.5 + LEFT * 1.8)
        gold_label = Text("买黄金", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(gold_icon, DOWN, buff=0.2)
        gold_group = Group(gold_icon, gold_label)
        
        # 3. 问号图标 - 代表疑惑
        # 图标来源：question_mark 在 all_png_names.txt 第4805行
        question_icon = self.load_png_icon("question_mark", height=1.5).move_to(UP * 1.5)
        
        # 4. 印钞机图标 - 代表"印钞机发明"的转折
        # 图标来源：printer 在 all_png_names.txt 第4699行
        printer_icon = self.load_png_icon("printer", height=2.0).move_to(UP * 1.5 + RIGHT * 1.8)
        printer_label = Text("印钞机", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(printer_icon, DOWN, buff=0.2)
        printer_group = Group(printer_icon, printer_label)
        
        # 5. 底部扎心结论 - 核心痛点文字
        pain_text = Text(
            "没有真正的避风港", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 2.5)
        
        # 6. 底部补充说明
        sub_text = Text(
            "「黄金也不行」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).next_to(pain_text, DOWN, buff=0.3)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(gold_group, shift=UP), run_time=step_time)
        self.play(FadeIn(question_icon, scale=0.5), run_time=step_time)
        self.play(FadeIn(printer_group, shift=UP), run_time=step_time)
        self.play(Write(pain_text), FadeIn(sub_text), run_time=step_time)
        self.play(Circumscribe(pain_text, color=RED), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：核心概念 -> 白话解释 -> 比喻类比
        
        口播稿关键词/短语：
        - "马克思名言" -> 引用框
        - "货币天然不是黄金，但黄金天然是货币" -> 核心知识点
        - "开采难、总量少" -> 稀缺性
        - "纸币是黄金的提货券" -> 类比说明
        
        动态标题：「黄金为何值钱？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、名言框、解释、图标、总结）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部：核心概念标题
        title = Text(
            "黄金为何值钱？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 马克思名言框 - 核心知识点
        quote_text = Text(
            "「货币天然不是黄金，\n但黄金天然是货币」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GOLD,
            line_spacing=1.2
        ).move_to(UP * 2.0)
        quote_box = RoundedRectangle(
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.1,
            fill_color=GOLD
        ).surround(quote_text, buff=0.4)
        quote_group = VGroup(quote_box, quote_text)
        
        # 3. 白话解释
        explain_text = Text(
            "开采难、总量少 → 天生值钱", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(DOWN * 0.3)
        
        # 4. 黄金与纸币关系图示
        # 图标来源：gold_bars 在 all_png_names.txt 第2632行
        gold_small = self.load_png_icon("gold_bars", height=1.2).move_to(DOWN * 2.0 + LEFT * 2.0)
        arrow_right = Arrow(
            start=LEFT * 1.0 + DOWN * 2.0, 
            end=RIGHT * 0.5 + DOWN * 2.0, 
            color=WHITE,
            buff=0.1
        )
        # 图标来源：us_dollar 在 all_png_names.txt 第6125行
        dollar_icon = self.load_png_icon("us_dollar", height=1.2).move_to(DOWN * 2.0 + RIGHT * 2.0)
        relation_label = Text(
            "纸币 = 黄金提货券", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=GRAY
        ).move_to(DOWN * 3.2)
        relation_group = Group(gold_small, arrow_right, dollar_icon, relation_label)
        
        # 5. 底部一句话总结
        summary = Text(
            "稀缺性 = 价值", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.3)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(quote_group, shift=UP), run_time=step_time)
        self.play(Write(explain_text), run_time=step_time)
        self.play(FadeIn(relation_group, shift=UP), run_time=step_time)
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：误区展示 -> 真相揭露 -> 数据支撑
        
        口播稿关键词/短语：
        - "1974年" -> 时间节点
        - "美元放弃挂钩黄金" -> 关键转折
        - "100块钱印刷成本1块钱" -> 数据对比
        - "铸币税" -> 核心概念
        - "黄金不保值，更不增值" -> 认知矫正
        
        动态标题：「1974年发生了什么？」
        使用左右对比布局：左侧（旧认知）vs 右侧（新现实）
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、时间线、左侧旧认知、右侧新现实、铸币税、结论）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text(
            "1974年，世界变了", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 时间线分割
        timeline = Line(
            start=UP * 2.5, 
            end=DOWN * 0.5, 
            color=WHITE, 
            stroke_width=3
        )
        year_label = Text(
            "1974", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=YELLOW
        ).next_to(timeline, UP, buff=0.2)
        
        # 3. 左侧：旧认知（美元挂钩黄金）
        old_title = Text("之前", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(UP * 2.0 + LEFT * 2.2)
        # 图标来源：us_dollar 在 all_png_names.txt 第6125行
        dollar_old = self.load_png_icon("us_dollar", height=1.2).move_to(UP * 0.5 + LEFT * 2.2)
        link_text = Text("=", font=self.title_font, font_size=self.font_title_size, color=GREEN).next_to(dollar_old, DOWN, buff=0.2)
        # 图标来源：gold_bars 在 all_png_names.txt 第2632行
        gold_old = self.load_png_icon("gold_bars", height=1.2).next_to(link_text, DOWN, buff=0.2)
        old_group = Group(old_title, dollar_old, link_text, gold_old)
        
        # 4. 右侧：新现实（美元脱钩黄金）
        new_title = Text("之后", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(UP * 2.0 + RIGHT * 2.2)
        dollar_new = self.load_png_icon("us_dollar", height=1.2).move_to(UP * 0.5 + RIGHT * 2.2)
        unlink_text = Text("≠", font=self.title_font, font_size=self.font_title_size, color=RED).next_to(dollar_new, DOWN, buff=0.2)
        gold_new = self.load_png_icon("gold_bars", height=1.2).next_to(unlink_text, DOWN, buff=0.2)
        new_group = Group(new_title, dollar_new, unlink_text, gold_new)
        
        # 5. 铸币税说明
        tax_box = RoundedRectangle(
            corner_radius=0.15, 
            width=7.0, 
            height=1.2, 
            stroke_color=RED, 
            fill_opacity=0.1, 
            fill_color=RED
        ).move_to(DOWN * 3)
        tax_text = Text(
            "100元纸币 印刷成本1元\n剩下99元 = 铸币税", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=RED,
            line_spacing=1.2
        ).move_to(tax_box.get_center())
        tax_group = VGroup(tax_box, tax_text)
        
        # 6. 底部结论
        conclusion = Text(
            "黄金能换钱，但不保值", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Create(timeline), Write(year_label), run_time=step_time)
        self.play(FadeIn(old_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(new_group, shift=LEFT), run_time=step_time)
        self.play(FadeIn(tax_group, shift=UP), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：具象化场景 -> 对号入座 -> 引发认同
        
        口播稿关键词/短语：
        - "工薪族" -> worker 图标
        - "辛辛苦苦攒了点钱" -> coins 图标
        - "存银行会被通胀稀释" -> bank_building + 向下箭头
        - "囤黄金不涨反跌" -> gold_bars + 向下箭头
        - "每天都在发生" -> 日常场景
        
        动态标题：「你中招了吗？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、工薪族、存银行问题、囤黄金问题、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "你中招了吗？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 工薪族形象
        # 图标来源：worker 在 all_png_names.txt 第6444行
        worker_icon = self.load_png_icon("worker", height=2.0).move_to(UP * 2.0)
        worker_label = Text(
            "工薪族辛苦攒钱", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).next_to(worker_icon, DOWN, buff=0.3)
        worker_group = Group(worker_icon, worker_label)
        
        # 3. 左侧：存银行问题
        # 图标来源：bank_building 在 all_png_names.txt 第648行
        bank_icon = self.load_png_icon("bank_building", height=1.5).move_to(DOWN * 0.8 + LEFT * 2.0)
        bank_arrow = Arrow(
            start=bank_icon.get_bottom() + DOWN * 0.1, 
            end=bank_icon.get_bottom() + DOWN * 0.8, 
            color=RED, 
            buff=0
        )
        bank_text = Text("通胀稀释", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(bank_arrow, DOWN, buff=0.1)
        bank_group = Group(bank_icon, bank_arrow, bank_text)
        
        # 4. 右侧：囤黄金问题
        # 图标来源：gold_bars 在 all_png_names.txt 第2632行
        gold_icon = self.load_png_icon("gold_bars", height=1.5).move_to(DOWN * 0.8 + RIGHT * 2.0)
        gold_arrow = Arrow(
            start=gold_icon.get_bottom() + DOWN * 0.1, 
            end=gold_icon.get_bottom() + DOWN * 0.8, 
            color=RED, 
            buff=0
        )
        gold_text = Text("不涨反跌", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(gold_arrow, DOWN, buff=0.1)
        gold_group = Group(gold_icon, gold_arrow, gold_text)
        
        # 5. 底部结论
        conclusion = Text(
            "躺着等升值？不存在的", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(worker_group, shift=UP), run_time=step_time)
        self.play(FadeIn(bank_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(gold_group, shift=LEFT), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=RED), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：行动步骤 -> 逐项弹出 -> 强调可执行
        
        口播稿关键词/短语：
        - "印钞机在转，你就不能停" -> 核心逻辑
        - "学点理财知识" -> book/learning 图标
        - "让钱动起来" -> money_circulation 图标
        - "创造价值、创造收入" -> growing_money 图标
        - "躺平等升值的时代，早就结束了" -> 总结
        
        动态标题：「印钞机在转，你怎么办？」
        使用 LaggedStart 实现逐项弹出效果
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、三条策略LaggedStart、核心口号、总结强调）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "印钞机在转，你怎么办？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 4.0)
        
        # 2. 三条策略
        # 策略1：学点理财知识
        # 图标来源：book 在 all_png_names.txt 第830行
        strategy1_icon = self.load_png_icon("book", height=1.2).move_to(UP * 2.0 + LEFT * 2.5)
        strategy1_text = Text("① 学点理财知识", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(strategy1_icon, RIGHT, buff=0.3)
        strategy1 = Group(strategy1_icon, strategy1_text)
        
        # 策略2：让钱动起来
        # 图标来源：money_circulation 在 all_png_names.txt 第3951行
        strategy2_icon = self.load_png_icon("money_circulation", height=1.2).move_to(UP * 0.3 + LEFT * 2.5)
        strategy2_text = Text("② 让钱动起来", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(strategy2_icon, RIGHT, buff=0.3)
        strategy2 = Group(strategy2_icon, strategy2_text)
        
        # 策略3：创造价值和收入
        # 图标来源：growing_money 在 all_png_names.txt 第2755行
        strategy3_icon = self.load_png_icon("growing_money", height=1.2).move_to(DOWN * 1.4 + LEFT * 2.5)
        strategy3_text = Text("③ 不断创造价值", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(strategy3_icon, RIGHT, buff=0.3)
        strategy3 = Group(strategy3_icon, strategy3_text)
        
        strategies = [strategy1, strategy2, strategy3]
        
        # 3. 核心口号
        slogan_box = RoundedRectangle(
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        )
        slogan_text = Text(
            "你不能停！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.2)
        slogan_box.surround(slogan_text, buff=0.5)
        slogan_group = VGroup(slogan_box, slogan_text)
        
        # 4. 底部总结
        summary = Text(
            "躺平时代，早就结束了", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(DOWN * 4.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        # 使用 LaggedStart 逐项弹出策略，lag_ratio=0.3
        self.play(
            LaggedStart(
                *[FadeIn(s, shift=RIGHT) for s in strategies], 
                lag_ratio=0.3
            ), 
            run_time=step_time
        )
        self.play(FadeIn(slogan_group, scale=0.8), run_time=step_time)
        self.play(Write(summary), Circumscribe(slogan_text, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：低门槛互动 -> 强调动画 -> 引导关注
        
        口播稿关键词/短语：
        - "点个赞" -> like 图标
        - "关注我" -> add_user 图标
        - "每天一课" -> 系列口号
        - "跑赢大盘" -> 目标愿景
        
        动态标题：「有收获？点个赞！」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、点赞关注图标、系列口号、结尾等待）
        step_time = (page_duration - t_trans) / 4

        # 1. 核心CTA标题
        title = Text(
            "有收获？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 3.5)
        
        # 2. 点赞图标
        # 图标来源：like 在 all_png_names.txt 第3499行
        like_icon = self.load_png_icon("like", height=2.0).move_to(LEFT * 2 + UP * 0.5)
        like_text = Text("点赞", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_text)
        
        # 3. 关注图标
        # 图标来源：add_user 在 all_png_names.txt 第259行
        follow_icon = self.load_png_icon("add_user", height=2.0).move_to(RIGHT * 2 + UP * 0.5)
        follow_text = Text("关注", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(follow_icon, DOWN, buff=0.2)
        follow_group = Group(follow_icon, follow_text)
        
        icons_group = Group(like_group, follow_group)
        
        # 4. 系列口号 - 金句框
        slogan_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=GOLD
        )
        slogan_text = Text(
            "每天一课，日日生金！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 2.5)
        slogan_box.surround(slogan_text, buff=0.5)
        slogan_group = VGroup(slogan_box, slogan_text)
        
        # 5. 底部愿景
        vision = Text(
            "一起跑赢大盘", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(DOWN * 4.2)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(icons_group, shift=UP), run_time=step_time)
        self.play(
            FadeIn(slogan_group, scale=0.8), 
            Write(vision),
            run_time=step_time
        )
        # 结尾强调动画 - 使用 Circumscribe 而非 Indicate
        self.play(Circumscribe(slogan_text, color=GOLD, fade_out=True), run_time=step_time)

        # 不需要淡出，作为结尾画面保留
        self.wait(0.5)

    def get_cover_decoration_icons(self):
        """
        根据 build_scene_1 到 build_scene_6 的动画内容和 script.json 的 icons 字段
        选择封面装饰图标，不超过5个。
        
        选用图标及其理由：
        - gold_bars: 核心主题「黄金」
        - printer: 关键概念「印钞机」
        - money_circulation: 策略「让钱动起来」
        - bank_building: 场景「存银行」
        - growing_money: 目标「增值」
        
        所有图标名称已在 all_png_names.txt 中验证存在。
        """
        return ["gold_bars", "printer", "money_circulation", "bank_building", "growing_money"]
