import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson003VerticalScenes(Zsxq100keLessonVertical):
    """
    第003课：上头如何管经济
    副标题：掌握政策信号，踩准投资节拍
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：引发共鸣 -> 反常识观点 -> 抓住注意力
        
        口播稿关键词/短语：
        - "股市涨跌、房价起伏" -> 市场波动图标
        - "无形的手在操控" -> 神秘感
        - "跟上头同频" -> 核心观点
        - "高考琢磨出题老师" -> 类比引入
        
        动态标题：「投资为何总踏空？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、股市图标、房价图标、无形的手、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题 (y=4.0) - 引发好奇的标题
        title = Text(
            "投资为何总踏空？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 左侧：股市涨跌
        # 图标来源：stocks_growth 在 all_png_names.txt
        stock_icon = self.load_png_icon("stocks_growth", height=1.8).move_to(UP * 1.5 + LEFT * 2.0)
        stock_label = Text("股市涨跌", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(stock_icon, DOWN, buff=0.2)
        stock_group = Group(stock_icon, stock_label)
        
        # 3. 右侧：房价起伏
        # 图标来源：real_estate 在 all_png_names.txt
        house_icon = self.load_png_icon("real_estate", height=1.8).move_to(UP * 1.5 + RIGHT * 2.0)
        house_label = Text("房价起伏", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(house_icon, DOWN, buff=0.2)
        house_group = Group(house_icon, house_label)
        
        # 4. 中间：无形的手
        # 图标来源：hand 在 all_png_names.txt（代表调控的手）
        hand_icon = self.load_png_icon("hand", height=2.5).move_to(DOWN * 0.8)
        hand_label = Text("「无形的手」", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(hand_icon, DOWN, buff=0.2)
        hand_group = Group(hand_icon, hand_label)
        
        # 5. 底部结论
        conclusion = Text(
            "跟上头同频才能赚到钱", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(stock_group, shift=UP), run_time=step_time)
        self.play(FadeIn(house_group, shift=UP), run_time=step_time)
        self.play(FadeIn(hand_group, scale=0.8), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：核心概念 -> 白话解释 -> 比喻类比
        
        口播稿关键词/短语：
        - "货币手段和财政手段" -> 两个分支
        - "央行" -> 核心机构
        - "中国人民银行" -> 官方名称
        - "央妈" -> 圈内称呼
        
        动态标题：「上头管经济的两招」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、央行图标、货币手段、财政手段、总结）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部：核心概念标题
        title = Text(
            "上头管经济的两招", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 央行核心（上方居中）
        # 图标来源：bank 在 all_png_names.txt
        bank_icon = self.load_png_icon("bank", height=2.0).move_to(UP * 2.0)
        bank_label = Text("央行「央妈」", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(bank_icon, DOWN, buff=0.2)
        bank_sublabel = Text("中国人民银行", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(bank_label, DOWN, buff=0.1)
        bank_group = Group(bank_icon, bank_label, bank_sublabel)
        
        # 3. 左侧：货币手段
        # 图标来源：money_circulation 在 all_png_names.txt
        money_icon = self.load_png_icon("money_circulation", height=1.5).move_to(DOWN * 0.8 + LEFT * 2.2)
        money_label = Text("货币手段", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(money_icon, DOWN, buff=0.2)
        money_detail = Text("降息·降准·逆回购", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(money_label, DOWN, buff=0.1)
        money_group = Group(money_icon, money_label, money_detail)
        
        # 4. 右侧：财政手段
        # 图标来源：government 在 all_png_names.txt
        fiscal_icon = self.load_png_icon("government", height=1.5).move_to(DOWN * 0.8 + RIGHT * 2.2)
        fiscal_label = Text("财政手段", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(fiscal_icon, DOWN, buff=0.2)
        fiscal_detail = Text("花钱·投资·新基建", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(fiscal_label, DOWN, buff=0.1)
        fiscal_group = Group(fiscal_icon, fiscal_label, fiscal_detail)
        
        # 5. 连接箭头
        arrow_left = Arrow(
            start=bank_icon.get_bottom() + DOWN * 0.3 + LEFT * 0.5,
            end=money_icon.get_top() + UP * 0.2,
            color=WHITE,
            buff=0.1,
            stroke_width=2
        )
        arrow_right = Arrow(
            start=bank_icon.get_bottom() + DOWN * 0.3 + RIGHT * 0.5,
            end=fiscal_icon.get_top() + UP * 0.2,
            color=WHITE,
            buff=0.1,
            stroke_width=2
        )
        
        # 6. 底部总结
        summary = Text(
            "央妈给市场发钱", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(bank_group, shift=DOWN), run_time=step_time)
        self.play(
            FadeIn(money_group, shift=RIGHT), 
            Create(arrow_left),
            run_time=step_time
        )
        self.play(
            FadeIn(fiscal_group, shift=LEFT), 
            Create(arrow_right),
            run_time=step_time
        )
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：误区展示 -> 真相揭露 -> 对比
        
        口播稿关键词/短语：
        - "三板斧" -> 核心框架
        - "降息" -> 第一招：少还房贷多消费
        - "降准" -> 第二招：给银行更多钱放贷
        - "逆回购" -> 第三招：印新钱买资产（放水主通道）
        
        动态标题：「央妈三板斧」
        使用递进布局展示三个工具
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、三板斧LaggedStart、强调放水、结论、强调框）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "央妈三板斧", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 第一招：降息
        item1_num = Text("①", font=self.title_font, font_size=self.font_body_size, color=GOLD).move_to(UP * 2.2 + LEFT * 3.5)
        item1_title = Text("降息", font=self.title_font, font_size=self.font_body_size, color=GREEN).next_to(item1_num, RIGHT, buff=0.2)
        item1_detail = Text("少还房贷，多消费", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(item1_title, RIGHT, buff=0.3)
        item1 = VGroup(item1_num, item1_title, item1_detail)
        
        # 3. 第二招：降准
        item2_num = Text("②", font=self.title_font, font_size=self.font_body_size, color=GOLD).move_to(UP * 0.8 + LEFT * 3.5)
        item2_title = Text("降准", font=self.title_font, font_size=self.font_body_size, color=GREEN).next_to(item2_num, RIGHT, buff=0.2)
        item2_detail = Text("给银行更多钱放贷", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(item2_title, RIGHT, buff=0.3)
        item2 = VGroup(item2_num, item2_title, item2_detail)
        
        # 4. 第三招：逆回购（重点）
        item3_num = Text("③", font=self.title_font, font_size=self.font_body_size, color=GOLD).move_to(DOWN * 0.6 + LEFT * 3.5)
        item3_title = Text("逆回购", font=self.title_font, font_size=self.font_body_size, color=ORANGE).next_to(item3_num, RIGHT, buff=0.2)
        item3_detail = Text("印钱买资产", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(item3_title, RIGHT, buff=0.3)
        item3 = VGroup(item3_num, item3_title, item3_detail)
        
        items = [item1, item2, item3]
        
        # 5. 放水主通道强调
        highlight_text = Text(
            "「放水主通道」", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(DOWN * 2.0)
        highlight_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=ORANGE, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=ORANGE
        ).surround(highlight_text, buff=0.4)
        highlight_group = VGroup(highlight_box, highlight_text)
        
        # 6. 底部结论
        conclusion = Text(
            "看懂这三招，就知道钱往哪流", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        # 使用 LaggedStart 逐项弹出
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT) for item in items], 
                lag_ratio=0.4
            ), 
            run_time=step_time
        )
        self.play(FadeIn(highlight_group, scale=0.8), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)
        self.play(Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：具象化场景 -> 对号入座 -> 引发认同
        
        口播稿关键词/短语：
        - "央行降准降息" -> 政策信号
        - "钱要变多了" -> 正面信号
        - "资产价格可能要涨" -> 机会提示
        - "加息收紧" -> 反向信号
        
        动态标题：「这些信号别错过」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、正面信号、正面结果、反面信号、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "这些信号别错过", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 4.0)
        
        # 2. 正面信号（上方）
        # 图标来源：positive_dynamic 在 all_png_names.txt
        up_icon = self.load_png_icon("positive_dynamic", height=1.5).move_to(UP * 2.0 + LEFT * 2.5)
        up_signal = Text("降准降息", font=self.title_font, font_size=self.font_body_size, color=GREEN).next_to(up_icon, RIGHT, buff=0.3)
        up_group = Group(up_icon, up_signal)
        
        # 3. 正面结果
        up_result_icon = self.load_png_icon("growing_money", height=1.2).move_to(UP * 0.5 + RIGHT * 2.0)
        up_result_text = Text("钱变多 → 资产要涨", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(up_result_icon, LEFT, buff=0.3)
        up_result = Group(up_result_icon, up_result_text)
        
        # 4. 箭头
        arrow_down = Arrow(
            start=UP * 1.2,
            end=UP * 0.8,
            color=GREEN,
            buff=0.1
        )
        
        # 5. 反面信号（下方）
        # 图标来源：negative_dynamic 在 all_png_names.txt
        down_icon = self.load_png_icon("negative_dynamic", height=1.5).move_to(DOWN * 1.5 + LEFT * 2.5)
        down_signal = Text("加息收紧", font=self.title_font, font_size=self.font_body_size, color=RED).next_to(down_icon, RIGHT, buff=0.3)
        down_group = Group(down_icon, down_signal)
        
        # 6. 反面结果
        down_result_text = Text("该保守点了", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(DOWN * 2.8)
        
        # 7. 底部结论
        conclusion = Text(
            "跟着政策信号走", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.2)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(up_group, shift=RIGHT), run_time=step_time)
        self.play(Create(arrow_down), FadeIn(up_result, shift=LEFT), run_time=step_time)
        self.play(FadeIn(down_group, shift=RIGHT), FadeIn(down_result_text, shift=UP), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：行动步骤 -> 逐项弹出 -> 强调可执行
        
        口播稿关键词/短语：
        - "关注LPR利率" -> 步骤1
        - "看财政往哪花钱" -> 步骤2
        - "新基建：5G、数据中心、人工智能" -> 政策风口
        - "钱流向哪个行业" -> 步骤3
        
        动态标题：「三步抓住政策风口」
        使用 LaggedStart 实现逐项弹出效果
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、三步骤LaggedStart、新基建图标、结论）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "三步抓住政策风口", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 步骤列表
        # 图标来源：checked_checkbox 在 all_png_names.txt
        item1_icon = self.load_png_icon("checked_checkbox", height=0.8).move_to(UP * 2.2 + LEFT * 3.2)
        item1_text = Text("① 关注每月LPR利率", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(item1_icon, RIGHT, buff=0.2)
        item1 = Group(item1_icon, item1_text)
        
        item2_icon = self.load_png_icon("checked_checkbox", height=0.8).move_to(UP * 0.9 + LEFT * 3.2)
        item2_text = Text("② 看财政往哪花钱", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(item2_icon, RIGHT, buff=0.2)
        item2 = Group(item2_icon, item2_text)
        
        item3_icon = self.load_png_icon("checked_checkbox", height=0.8).move_to(DOWN * 0.4 + LEFT * 3.2)
        item3_text = Text("③ 重点关注钱流向的行业", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(item3_icon, RIGHT, buff=0.2)
        item3 = Group(item3_icon, item3_text)
        
        items = [item1, item2, item3]
        
        # 3. 新基建关键词
        infra_title = Text("当下政策风口", font=self.body_font, font_size=self.font_body_size, color=ORANGE).move_to(DOWN * 2.0)
        infra_items = Text(
            "5G · 数据中心 · 人工智能", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(DOWN * 2.8)
        infra_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(infra_items, buff=0.4)
        infra_group = VGroup(infra_title, infra_box, infra_items)
        
        # 4. 底部结论
        conclusion = Text(
            "跟着钱走，踩准节拍", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.3)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        # 使用 LaggedStart 逐项弹出，lag_ratio=0.3
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT) for item in items], 
                lag_ratio=0.3
            ), 
            run_time=step_time
        )
        self.play(FadeIn(infra_group, scale=0.8), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(infra_items, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：低门槛互动 -> 强调动画 -> 引导关注
        
        口播稿关键词/短语：
        - "跟着上头走" -> 核心口号
        - "别跟政策拧着来" -> 强调
        - "点赞关注" -> 互动号召
        - "下期聊银行" -> 预告
        
        动态标题：「跟着政策走」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、核心口号、互动图标、系列口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 核心CTA标题
        title = Text(
            "投资要跟着上头走", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 3.5)
        
        # 2. 核心口号
        slogan_main = Text(
            "别跟政策拧着来", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 1.5)
        
        # 3. 点赞图标
        # 图标来源：like 在 all_png_names.txt
        like_icon = self.load_png_icon("like", height=2.0).move_to(LEFT * 2 + DOWN * 0.5)
        like_text = Text("点赞", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_text)
        
        # 4. 关注图标
        # 图标来源：add_user 在 all_png_names.txt
        follow_icon = self.load_png_icon("add_user", height=2.0).move_to(RIGHT * 2 + DOWN * 0.5)
        follow_text = Text("关注", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(follow_icon, DOWN, buff=0.2)
        follow_group = Group(follow_icon, follow_text)
        
        icons_group = Group(like_group, follow_group)
        
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
        self.play(Write(slogan_main), Circumscribe(slogan_main, color=GOLD), run_time=step_time)
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
        - bank: 央行核心概念
        - money_circulation: 货币政策
        - stocks_growth: 股市涨跌
        - growing_money: 钱往哪流
        - government: 财政手段
        """
        return ["bank", "money_circulation", "stocks_growth", "growing_money", "government"]
