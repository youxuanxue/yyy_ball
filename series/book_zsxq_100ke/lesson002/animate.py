import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson002VerticalScenes(Zsxq100keLessonVertical):
    """
    第002课：货币、空气币、瑞幸收割
    副标题：记住四大本质，远离投资陷阱
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：引发共鸣 -> 反常识观点 -> 抓住注意力
        
        口播稿关键词/短语：
        - "比特币发财" vs "血本无归" -> 对比布局
        - "99%的虚拟币" -> 数字强调
        - "一场局" -> 警告色
        - "瑞幸咖啡" -> 案例引用
        
        动态标题：「炒币，发财还是入坑？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、发财图标、亏损图标、99%数字、结论、强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题 (y=4.0) - 引发好奇的标题
        title = Text(
            "炒币，发财还是入坑？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 左侧：发财的人 - 代表比特币暴富
        # 图标来源：bitcoin 在 all_png_names.txt
        bitcoin_icon = self.load_png_icon("bitcoin", height=1.8).move_to(UP * 1.5 + LEFT * 2.0)
        win_label = Text("发财", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(bitcoin_icon, DOWN, buff=0.2)
        win_group = Group(bitcoin_icon, win_label)
        
        # 3. 右侧：血本无归 - 代表亏损
        # 图标来源：bankruptcy 在 all_png_names.txt
        loss_icon = self.load_png_icon("bankruptcy", height=1.8).move_to(UP * 1.5 + RIGHT * 2.0)
        loss_label = Text("血本无归", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(loss_icon, DOWN, buff=0.2)
        loss_group = Group(loss_icon, loss_label)
        
        # 4. 中间：问号
        vs_text = Text("VS", font=self.title_font, font_size=self.font_title_size, color=WHITE).move_to(UP * 1.5)
        
        # 5. 核心数字：99%
        percent_text = Text(
            "99%的虚拟币", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 1.5)
        
        # 6. 底部结论
        conclusion = Text(
            "本质就是一场局", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(win_group, shift=UP), run_time=step_time)
        self.play(FadeIn(vs_text), FadeIn(loss_group, shift=UP), run_time=step_time)
        self.play(Write(percent_text), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)
        self.play(Circumscribe(conclusion, color=RED), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：核心概念 -> 白话解释 -> 比喻类比
        
        口播稿关键词/短语：
        - "铸币税" -> 核心概念
        - "70%是铜，30%是铅和锡" -> 比例图示
        - "100块钱印刷成本1块" -> 数据对比
        - "建路修桥养公务员" -> 用途说明
        
        动态标题：「什么是铸币税？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、概念框、古代铜钱、现代纸币、总结）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部：核心概念标题
        title = Text(
            "什么是铸币税？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 铸币税概念框
        concept_text = Text(
            "「铸币税」", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 2.5)
        concept_box = RoundedRectangle(
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.1,
            fill_color=GOLD
        ).surround(concept_text, buff=0.4)
        concept_group = VGroup(concept_box, concept_text)
        
        # 3. 古代铜钱示意
        # 图标来源：coins 在 all_png_names.txt
        coin_icon = self.load_png_icon("coins", height=1.5).move_to(UP * 0.5 + LEFT * 2.0)
        coin_label = Text("古代铜钱", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(coin_icon, DOWN, buff=0.2)
        coin_detail = Text("70%铜 + 30%杂质", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(coin_label, DOWN, buff=0.1)
        coin_group = Group(coin_icon, coin_label, coin_detail)
        
        # 4. 现代纸币示意
        # 图标来源：money 在 all_png_names.txt
        money_icon = self.load_png_icon("money", height=1.5).move_to(UP * 0.5 + RIGHT * 2.0)
        money_label = Text("现代纸币", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(money_icon, DOWN, buff=0.2)
        money_detail = Text("成本1元 → 面值100元", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(money_label, DOWN, buff=0.1)
        money_group = Group(money_icon, money_label, money_detail)
        
        # 5. 箭头连接
        arrow = Arrow(
            start=LEFT * 0.8 + UP * 0.5, 
            end=RIGHT * 0.8 + UP * 0.5, 
            color=WHITE,
            buff=0.1
        )
        
        # 6. 底部总结
        summary = Text(
            "国家收铸币税 = 建路修桥养公务员", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(concept_group, shift=UP), run_time=step_time)
        self.play(FadeIn(coin_group, shift=RIGHT), FadeIn(arrow), run_time=step_time)
        self.play(FadeIn(money_group, shift=LEFT), run_time=step_time)
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：误区展示 -> 真相揭露 -> 对比
        
        口播稿关键词/短语：
        - "国家货币能流通" -> 正面
        - "能交税，背后有行政力量" -> 背书
        - "虚拟币不能交税，没人背书" -> 反面
        - "庄家控盘炒作" -> 陷阱
        
        动态标题：「国家货币 vs 虚拟币」
        使用左右对比布局
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、左侧标签、左侧内容、右侧标签、右侧内容、结论）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text(
            "国家货币 vs 虚拟币", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 中间分割线
        divider = Line(
            start=UP * 2.5, 
            end=DOWN * 1.5, 
            color=WHITE, 
            stroke_width=2
        )
        
        # 3. 左侧：国家货币（正面）
        left_title = Text("国家货币", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(UP * 2.5 + LEFT * 2.2)
        # 图标来源：money_circulation 在 all_png_names.txt
        left_icon = self.load_png_icon("money_circulation", height=1.5).move_to(UP * 1.0 + LEFT * 2.2)
        left_point1 = Text("✓ 能交税", font=self.body_font, font_size=self.font_small_size, color=GREEN).move_to(DOWN * 0.2 + LEFT * 2.2)
        left_point2 = Text("✓ 有政府背书", font=self.body_font, font_size=self.font_small_size, color=GREEN).move_to(DOWN * 0.8 + LEFT * 2.2)
        left_group = Group(left_title, left_icon, left_point1, left_point2)
        
        # 4. 右侧：虚拟币（反面）
        right_title = Text("虚拟币", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(UP * 2.5 + RIGHT * 2.2)
        # 图标来源：bitcoin 在 all_png_names.txt
        right_icon = self.load_png_icon("bitcoin", height=1.5).move_to(UP * 1.0 + RIGHT * 2.2)
        right_point1 = Text("✗ 不能交税", font=self.body_font, font_size=self.font_small_size, color=RED).move_to(DOWN * 0.2 + RIGHT * 2.2)
        right_point2 = Text("✗ 无人背书", font=self.body_font, font_size=self.font_small_size, color=RED).move_to(DOWN * 0.8 + RIGHT * 2.2)
        right_group = Group(right_title, right_icon, right_point1, right_point2)
        
        # 5. 底部结论
        conclusion_box = RoundedRectangle(
            corner_radius=0.15, 
            width=7.5, 
            height=1.0, 
            stroke_color=RED, 
            fill_opacity=0.1, 
            fill_color=RED
        ).move_to(DOWN * 3.0)
        conclusion_text = Text(
            "庄家控盘炒作 → 收割走人", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(conclusion_box.get_center())
        conclusion_group = VGroup(conclusion_box, conclusion_text)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Create(divider), run_time=step_time)
        self.play(FadeIn(left_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(right_group, shift=LEFT), run_time=step_time)
        self.play(FadeIn(conclusion_group, shift=UP), run_time=step_time)
        self.play(Circumscribe(conclusion_text, color=RED), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：具象化场景 -> 对号入座 -> 引发认同
        
        口播稿关键词/短语：
        - "某个币涨疯了" -> 投机信号
        - "错过就亏大了" -> FOMO心理
        - "公司故事讲得好，从来不赚钱" -> 瑞幸案例
        - "击鼓传花" -> 本质揭示
        
        动态标题：「这些情况要警惕」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、警告1、警告2、警告图标、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "这些情况要警惕", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 4.0)
        
        # 2. 警告信号1
        # 图标来源：warning 在 all_png_names.txt
        warn_icon1 = self.load_png_icon("warning", height=1.2).move_to(UP * 2.0 + LEFT * 3.0)
        warn_text1 = Text(
            "「某个币涨疯了，\n错过就亏大了」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE,
            line_spacing=1.2
        ).next_to(warn_icon1, RIGHT, buff=0.3)
        warn_group1 = Group(warn_icon1, warn_text1)
        
        # 3. 警告信号2
        warn_icon2 = self.load_png_icon("warning", height=1.2).move_to(DOWN * 0.3 + LEFT * 3.0)
        warn_text2 = Text(
            "「公司故事讲得好，\n但从来不赚钱」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE,
            line_spacing=1.2
        ).next_to(warn_icon2, RIGHT, buff=0.3)
        warn_group2 = Group(warn_icon2, warn_text2)
        
        # 4. 大警告图标
        big_warn = self.load_png_icon("high_priority", height=2.5).move_to(DOWN * 2.0)
        
        # 5. 底部结论
        conclusion = Text(
            "十有八九是击鼓传花", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(warn_group1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(warn_group2, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(big_warn, scale=0.5), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=RED), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：行动步骤 -> 逐项弹出 -> 强调可执行
        
        口播稿关键词/短语：
        - "投资四大本质" -> 核心框架
        - "强大力量背书" -> 条件1
        - "过硬的抵押物" -> 条件2
        - "正向产出能赚钱" -> 条件3
        - "能交税" -> 条件4
        
        动态标题：「投资四大本质」
        使用 LaggedStart 实现逐项弹出效果
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、四大本质LaggedStart、强调框、结论）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "投资四大本质", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 四大本质列表
        # 图标来源：checklist 在 all_png_names.txt
        item1_icon = self.load_png_icon("checked_checkbox", height=0.8).move_to(UP * 2.2 + LEFT * 3.0)
        item1_text = Text("① 有强大力量背书", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(item1_icon, RIGHT, buff=0.2)
        item1 = Group(item1_icon, item1_text)
        
        item2_icon = self.load_png_icon("checked_checkbox", height=0.8).move_to(UP * 0.9 + LEFT * 3.0)
        item2_text = Text("② 有过硬的抵押物", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(item2_icon, RIGHT, buff=0.2)
        item2 = Group(item2_icon, item2_text)
        
        item3_icon = self.load_png_icon("checked_checkbox", height=0.8).move_to(DOWN * 0.4 + LEFT * 3.0)
        item3_text = Text("③ 有正向产出能赚钱", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(item3_icon, RIGHT, buff=0.2)
        item3 = Group(item3_icon, item3_text)
        
        item4_icon = self.load_png_icon("checked_checkbox", height=0.8).move_to(DOWN * 1.7 + LEFT * 3.0)
        item4_text = Text("④ 能交税", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(item4_icon, RIGHT, buff=0.2)
        item4 = Group(item4_icon, item4_text)
        
        items = [item1, item2, item3, item4]
        
        # 3. 核心口号框
        slogan_text = Text(
            "符合任意一个才值得投", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.2)
        slogan_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(slogan_text, buff=0.5)
        slogan_group = VGroup(slogan_box, slogan_text)
        
        # 4. 底部警告
        warning = Text(
            "四个都没有还拼命涨 = 坑", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(DOWN * 4.5)

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
        self.play(FadeIn(slogan_group, scale=0.8), run_time=step_time)
        self.play(Write(warning), Circumscribe(slogan_text, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：低门槛互动 -> 强调动画 -> 引导关注
        
        口播稿关键词/短语：
        - "建议收藏" -> 收藏动作
        - "对照一遍" -> 核查动作
        - "点赞关注" -> 互动号召
        
        动态标题：「记住四大本质」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、收藏提示、互动图标、口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 核心CTA标题
        title = Text(
            "记住四大本质", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 3.5)
        
        # 2. 收藏提示
        save_text = Text(
            "建议收藏，投资前对照一遍", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
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
        self.play(Write(save_text), run_time=step_time)
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
        - coins: 核心概念「铸币税」
        - bitcoin: 虚拟币话题
        - money_circulation: 货币流通
        - warning: 警惕信号
        - checklist: 四大本质
        """
        return ["coins", "bitcoin", "money_circulation", "warning", "checklist"]
