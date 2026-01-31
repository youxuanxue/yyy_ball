import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson007VerticalScenes(Zsxq100keLessonVertical):
    """
    第007课：监管套利与底层资产
    副标题：大鳄们钻空子的套路
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：引发共鸣 -> 反常识观点 -> 抓住注意力
        
        口播稿关键词/短语：
        - "金融监管很严格" -> 误区认知
        - "钻监管的空子" -> 反转
        - "银监、保监、证监" -> 三个监管机构
        - "合到一起看，辣眼睛" -> 冲击点
        - "监管套利" -> 核心概念
        
        动态标题：「监管严就安全？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、误区文字、三监管图标、合规但违规、监管套利结论、淡出）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题 (y=4.0) - 引发好奇
        title = Text(
            "监管严就安全？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 误区文字 - 大鳄们很守规矩
        wrong_text = Text(
            "「大鳄们应该很守规矩」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(UP * 2.5)
        wrong_cross = Cross(wrong_text, stroke_color=RED, stroke_width=4)
        
        # 3. 三个监管机构 - 使用银行图标表示监管
        # 图标来源：bank_building 在可用图标列表中
        jianyin_icon = self.load_png_icon("bank_building", height=1.2).move_to(UP * 0.8 + LEFT * 2.5)
        jianyin_label = Text("银监✓", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(jianyin_icon, DOWN, buff=0.15)
        jianyin_group = Group(jianyin_icon, jianyin_label)
        
        jianbao_icon = self.load_png_icon("shield", height=1.2).move_to(UP * 0.8)
        jianbao_label = Text("保监✓", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(jianbao_icon, DOWN, buff=0.15)
        jianbao_group = Group(jianbao_icon, jianbao_label)
        
        jianzheng_icon = self.load_png_icon("scales", height=1.2).move_to(UP * 0.8 + RIGHT * 2.5)
        jianzheng_label = Text("证监✓", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(jianzheng_icon, DOWN, buff=0.15)
        jianzheng_group = Group(jianzheng_icon, jianzheng_label)
        
        regulators = Group(jianyin_group, jianbao_group, jianzheng_group)
        
        # 4. 合到一起看 - 辣眼睛
        combine_text = Text(
            "合到一起看？", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(DOWN * 1.2)
        
        violation_text = Text(
            "辣眼睛！违规！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(DOWN * 2.2)
        
        # 5. 底部结论 - 监管套利
        conclusion = Text(
            "这就是「监管套利」", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(wrong_text), Create(wrong_cross), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(jianyin_group, shift=DOWN),
                FadeIn(jianbao_group, shift=DOWN),
                FadeIn(jianzheng_group, shift=DOWN),
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        self.play(Write(combine_text), run_time=step_time)
        self.play(Write(violation_text), Circumscribe(violation_text, color=RED), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：核心概念 -> 白话解释 -> 案例说明
        
        口播稿关键词/短语：
        - "打擦边球" -> 核心比喻
        - "一行三会各管一段" -> 各管各的
        - "铁路警察各管一段" -> 比喻
        - "银行的钱转几手" -> 资金流转
        - "最后跑去买股票" -> 最终投向
        - "宝能买万科" -> 经典案例
        
        动态标题：「什么是监管套利」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、解释、资金流转、案例、淡出）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部：核心概念标题
        title = Text(
            "什么是监管套利", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 简单解释
        explain_text = Text(
            "「简单说就是打擦边球」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).move_to(UP * 2.5)
        
        # 3. 资金流转示意 - 银行→转手→股票
        # 使用 money_transfer 和 layers 图标
        bank_icon = self.load_png_icon("bank_building", height=1.3).move_to(UP * 0.5 + LEFT * 3.0)
        bank_label = Text("银行", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(bank_icon, DOWN, buff=0.1)
        bank_group = Group(bank_icon, bank_label)
        
        arrow1 = Text("→", font=self.body_font, font_size=self.font_body_size, color=WHITE).move_to(UP * 0.5 + LEFT * 1.5)
        
        transfer_icon = self.load_png_icon("money_transfer", height=1.3).move_to(UP * 0.5)
        transfer_label = Text("转几手", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(transfer_icon, DOWN, buff=0.1)
        transfer_group = Group(transfer_icon, transfer_label)
        
        arrow2 = Text("→", font=self.body_font, font_size=self.font_body_size, color=WHITE).move_to(UP * 0.5 + RIGHT * 1.5)
        
        # 使用 spy 图标表示股票操作
        stock_icon = self.load_png_icon("spy", height=1.3).move_to(UP * 0.5 + RIGHT * 3.0)
        stock_label = Text("买股票", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(stock_icon, DOWN, buff=0.1)
        stock_group = Group(stock_icon, stock_label)
        
        flow_group = Group(bank_group, arrow1, transfer_group, arrow2, stock_group)
        
        # 4. 每一手合规，串起来违规
        rule_text = Text(
            "每一手都合规，串起来就是违规", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(DOWN * 1.5)
        
        # 5. 案例提示
        case_text = Text(
            "宝能买万科就是这么玩的", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(DOWN * 3.0)
        case_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2,
            stroke_color=GOLD,
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(case_text, buff=0.4)
        case_group = VGroup(case_box, case_text)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(explain_text), run_time=step_time)
        self.play(
            FadeIn(bank_group, shift=RIGHT),
            FadeIn(arrow1),
            FadeIn(transfer_group, shift=RIGHT),
            FadeIn(arrow2),
            FadeIn(stock_group, shift=RIGHT),
            run_time=step_time
        )
        self.play(Write(rule_text), Circumscribe(rule_text, color=ORANGE), run_time=step_time)
        self.play(FadeIn(case_group, scale=0.8), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：核心洞察 -> 风险揭示 -> 监管改革
        
        口播稿关键词/短语：
        - "钱转来转去" -> 资金链条
        - "最后投向了哪里" -> 关键问题
        - "你可能根本不知道" -> 信息不对称
        - "你以为买的是稳健理财" -> 误区
        - "其实底层资产可能是高风险股票" -> 真相
        - "银保监合并、资管新规出台" -> 监管改革
        
        动态标题：「钱去哪了？」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、误区vs真相、监管改革、淡出）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "你的钱去哪了？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 4.0)
        
        # 2. 左侧：你以为（误区）
        left_title = Text("你以为", font=self.title_font, font_size=self.font_body_size, color=GRAY).move_to(UP * 2.0 + LEFT * 2.2)
        left_content = Text("稳健理财", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(UP * 0.8 + LEFT * 2.2)
        left_group = VGroup(left_title, left_content)
        
        # 3. 右侧：实际上（真相）
        right_title = Text("实际上", font=self.title_font, font_size=self.font_body_size, color=ORANGE).move_to(UP * 2.0 + RIGHT * 2.2)
        right_content = Text("高风险股票", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(UP * 0.8 + RIGHT * 2.2)
        right_group = VGroup(right_title, right_content)
        
        # 中间 VS
        vs_text = Text("VS", font=self.title_font, font_size=self.font_body_size, color=WHITE).move_to(UP * 1.4)
        
        # 4. 警告图标和文字
        warning_icon = self.load_png_icon("warning", height=1.5).move_to(DOWN * 1.0)
        warning_text = Text(
            "底层资产你根本不知道！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).next_to(warning_icon, DOWN, buff=0.3)
        warning_group = Group(warning_icon, warning_text)
        
        # 5. 监管改革
        reform_text = Text(
            "银保监合并 + 资管新规", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)
        reform_sub = Text(
            "就是为了堵这个漏洞", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=GOLD
        ).next_to(reform_text, DOWN, buff=0.2)
        reform_group = VGroup(reform_text, reform_sub)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(
            FadeIn(left_group, shift=RIGHT),
            FadeIn(vs_text),
            FadeIn(right_group, shift=LEFT),
            run_time=step_time
        )
        self.play(FadeIn(warning_group, scale=0.8), run_time=step_time)
        self.play(Circumscribe(warning_text, color=RED), run_time=step_time)
        self.play(Write(reform_group), Circumscribe(reform_text, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：具象化场景 -> 对号入座 -> 引发警觉
        
        口播稿关键词/短语：
        - "结构复杂的理财产品" -> 警惕场景
        - "层层嵌套" -> 特征1
        - "看不懂投向" -> 特征2
        - "有猫腻" -> 风险提示
        - "穿透到底" -> 监管要求
        - "我的钱最终投到哪里去了" -> 关键问题
        
        动态标题：「这些理财要小心」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、特征列表、警示、关键问题、淡出）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "这些理财要小心", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 4.0)
        
        # 2. 危险特征列表
        # 使用 layers 图标表示嵌套
        feature1_icon = self.load_png_icon("layers", height=1.2).move_to(UP * 2.0 + LEFT * 3.0)
        feature1_text = Text("层层嵌套", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(feature1_icon, RIGHT, buff=0.3)
        feature1 = Group(feature1_icon, feature1_text)
        
        feature2_icon = self.load_png_icon("document", height=1.2).move_to(UP * 0.5 + LEFT * 3.0)
        feature2_text = Text("看不懂投向", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(feature2_icon, RIGHT, buff=0.3)
        feature2 = Group(feature2_icon, feature2_text)
        
        feature3_icon = self.load_png_icon("spy", height=1.2).move_to(DOWN * 1.0 + LEFT * 3.0)
        feature3_text = Text("结构复杂", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(feature3_icon, RIGHT, buff=0.3)
        feature3 = Group(feature3_icon, feature3_text)
        
        features = [feature1, feature2, feature3]
        
        # 3. 警示文字
        warning_text = Text(
            "很可能有猫腻！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(DOWN * 2.5)
        warning_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2,
            stroke_color=RED,
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=RED
        ).surround(warning_text, buff=0.4)
        warning_group = VGroup(warning_box, warning_text)
        
        # 4. 底部关键问题
        question = Text(
            "问一句：钱最终投哪了？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.2)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(
            LaggedStart(
                *[FadeIn(f, shift=RIGHT) for f in features],
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        self.play(FadeIn(warning_group, scale=0.8), run_time=step_time)
        self.play(Circumscribe(warning_text, color=RED), run_time=step_time)
        self.play(Write(question), Circumscribe(question, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：行动步骤 -> 逐项弹出 -> 强调可执行
        
        口播稿关键词/短语：
        - "看底层资产" -> 核心原则
        - "问清楚钱最终投向什么" -> 策略1
        - "房子、债券还是股票" -> 底层资产类型
        - "层数越多，风险越不透明" -> 策略2
        - "结构简单、底层资产清晰" -> 策略3
        - "别被花里胡哨的包装迷惑" -> 警示
        
        动态标题：「买理财的原则」
        使用 LaggedStart 实现逐项弹出效果
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、口诀、三策略、结论、淡出）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "买理财的原则", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心口诀 - 金句框
        slogan = Text(
            "看底层资产！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(UP * 2.5)
        slogan_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2,
            stroke_color=GOLD,
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(slogan, buff=0.4)
        slogan_group = VGroup(slogan_box, slogan)
        
        # 3. 策略列表
        item1 = Text("① 问清楚：钱投向房子、债券还是股票？", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(UP * 0.8)
        item2 = Text("② 看层数：层数越多，风险越不透明", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 0.4)
        item3 = Text("③ 选简单：结构简单、底层清晰", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 1.6)
        
        items = [item1, item2, item3]
        
        # 4. 底部结论
        conclusion = Text(
            "别被包装迷惑！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(slogan_group, scale=0.8), Circumscribe(slogan, color=GOLD), run_time=step_time)
        # 使用 LaggedStart 逐项弹出，lag_ratio=0.3
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT) for item in items],
                lag_ratio=0.3
            ),
            run_time=2*step_time
        )
        self.play(Write(conclusion), Circumscribe(conclusion, color=ORANGE), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：低门槛互动 -> 强调动画 -> 引导关注
        
        口播稿关键词/短语：
        - "知道什么是监管套利和底层资产了吧" -> 总结
        - "下次买理财记得问清楚底层投向" -> 行动提示
        - "点赞收藏" -> 互动号召
        - "下期继续聊" -> 预告
        
        动态标题：「记住这一点」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、行动提示、互动图标、系列口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 核心CTA标题
        title = Text(
            "记住这一点", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 3.5)
        
        # 2. 行动提示
        action_text = Text(
            "买理财前问清楚底层投向", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(UP * 1.8)
        action_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2,
            stroke_color=GOLD,
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(action_text, buff=0.4)
        action_group = VGroup(action_box, action_text)
        
        # 3. 点赞图标
        like_icon = self.load_png_icon("like", height=2.0).move_to(LEFT * 2 + DOWN * 0.3)
        like_text = Text("点赞", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_text)
        
        # 4. 收藏图标
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
        self.play(FadeIn(action_group, scale=0.8), Circumscribe(action_text, color=GOLD), run_time=step_time)
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
        - bank_building: 银行/监管核心概念
        - layers: 层层嵌套/底层资产
        - spy: 钻空子/套利行为
        - warning: 风险警示
        - scales: 监管平衡/合规
        """
        return ["bank_building", "layers", "spy", "warning", "scales"]
