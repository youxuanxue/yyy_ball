import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson010VerticalScenes(Zsxq100keLessonVertical):
    """
    第010课：镰刀韭菜与防割
    副标题：割韭菜的四大要素
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：引发共鸣 -> 反常识观点 -> 抓住注意力
        
        口播稿关键词/短语：
        - "最大的镰刀是政府" -> 反常识核心
        - "收税和印钞" -> 两把镰刀
        - "一张100块成本1块钱" -> 铸币税
        - "这99块叫铸币税" -> 核心概念
        
        动态标题：「谁在割韭菜？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、误区文字、两把镰刀、铸币税说明、铸币税金额、结论）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题 (y=4.0) - 引发好奇
        title = Text(
            "谁在割韭菜？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 误区文字 - 只有骗子才割韭菜
        wrong_text = Text(
            "「只有骗子才割韭菜？」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(UP * 2.5)
        wrong_cross = Cross(wrong_text, stroke_color=RED, stroke_width=4)
        
        # 3. 左侧：收税（镰刀1）
        # 图标来源：government 表示政府收税
        tax_icon = self.load_png_icon("government", height=1.5).move_to(UP * 0.5 + LEFT * 2.2)
        tax_label = Text("收税", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(tax_icon, DOWN, buff=0.2)
        tax_group = Group(tax_icon, tax_label)
        
        # 4. 右侧：印钞（镰刀2）
        # 图标来源：banknotes 表示印钞
        print_icon = self.load_png_icon("banknotes", height=1.5).move_to(UP * 0.5 + RIGHT * 2.2)
        print_label = Text("印钞", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(print_icon, DOWN, buff=0.2)
        print_group = Group(print_icon, print_label)
        
        # 5. 中间标识 - 两把镰刀
        scissors_icon = self.load_png_icon("scissors", height=1.2).move_to(UP * 0.5)
        
        # 6. 铸币税说明
        mint_text = Text(
            "100块成本1块，99块是铸币税", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(DOWN * 1.5)
        
        # 7. 底部结论
        conclusion = Text(
            "最大的镰刀是政府", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(wrong_text), Create(wrong_cross), run_time=step_time)
        self.play(
            FadeIn(tax_group, shift=RIGHT), 
            FadeIn(print_group, shift=LEFT),
            FadeIn(scissors_icon, scale=0.5),
            run_time=step_time
        )
        self.play(Write(mint_text), run_time=step_time)
        self.play(Circumscribe(mint_text, color=ORANGE), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=RED), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：核心概念 -> 分类结构 -> 四大要素
        
        口播稿关键词/短语：
        - "花别人的钱办自己的事" -> 割韭菜定义
        - "政府割韭菜：收税、印钞、国有企业" -> 政府三招
        - "反哺社会，修路盖学校" -> 政府义务
        - "牌照、信用、产出、义务" -> 四大要素
        
        动态标题：「割韭菜的定义」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、定义、政府三招、反哺、四要素）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部：核心概念标题
        title = Text(
            "什么是割韭菜？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 定义 - 花别人的钱办自己的事
        definition = Text(
            "「花别人的钱办自己的事」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(UP * 2.5)
        definition_box = RoundedRectangle(
            height=1.0, 
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=2, 
            fill_opacity=0.1, 
            fill_color=GOLD
        ).surround(definition, buff=0.3)
        definition_group = VGroup(definition_box, definition)
        
        # 3. 政府三招
        gov_text = Text("政府三招：收税 + 印钞 + 国企", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(UP * 1.0)
        
        # 4. 但是政府会反哺
        but_text = Text("但政府会反哺：修路、盖学校", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(UP * 0.0)
        
        # 5. 私人四大要素 - 核心内容
        elements_title = Text("私人割韭菜四大要素：", font=self.body_font, font_size=self.font_body_size, color=ORANGE).move_to(DOWN * 1.2)
        
        # 四大要素横向排列
        elem1 = Text("牌照", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(DOWN * 2.5 + LEFT * 3.0)
        elem2 = Text("信用", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(DOWN * 2.5 + LEFT * 1.0)
        elem3 = Text("产出", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(DOWN * 2.5 + RIGHT * 1.0)
        elem4 = Text("义务", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(DOWN * 2.5 + RIGHT * 3.0)
        elements = [elem1, elem2, elem3, elem4]
        
        # 6. 底部总结框
        summary = Text(
            "四要素缺一不可", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(definition_group, shift=DOWN), run_time=step_time)
        self.play(Write(gov_text), Write(but_text), run_time=step_time)
        self.play(
            Write(elements_title),
            LaggedStart(
                *[FadeIn(elem, shift=UP) for elem in elements], 
                lag_ratio=0.2
            ), 
            run_time=step_time
        )
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：正规 vs 骗子 -> 义务是关键
        
        口播稿关键词/短语：
        - "正规的割韭菜是有义务的" -> 核心洞察
        - "政府割完要给你提供公共服务" -> 政府义务
        - "银行割完要保障你的存款" -> 银行义务
        - "骗子只有镰刀没有义务" -> 骗子本质
        - "有没有实在的产出和义务" -> 判断标准
        
        动态标题：「义务是关键」
        使用对比布局：正规 vs 骗子
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、正规方、骗子方、对比箭头、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "义务是关键", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 左侧：正规方（有义务）
        # 正规标题
        legit_title = Text("正规割韭菜", font=self.title_font, font_size=self.font_body_size, color=GREEN).move_to(UP * 2.2 + LEFT * 2.2)
        # 政府义务
        legit_gov = Text("政府 → 公共服务", font=self.body_font, font_size=self.font_small_size, color=GREEN).move_to(UP * 1.0 + LEFT * 2.2)
        # 银行义务
        legit_bank = Text("银行 → 保障存款", font=self.body_font, font_size=self.font_small_size, color=GREEN).move_to(UP * 0.2 + LEFT * 2.2)
        # 勾选图标
        shield_icon = self.load_png_icon("shield", height=1.2).move_to(DOWN * 1.0 + LEFT * 2.2)
        check_text = Text("✓ 有义务", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(shield_icon, DOWN, buff=0.2)
        legit_group = Group(legit_title, legit_gov, legit_bank, shield_icon, check_text)
        
        # 3. 右侧：骗子（无义务）
        # 骗子标题
        scam_title = Text("骗子割韭菜", font=self.title_font, font_size=self.font_body_size, color=RED).move_to(UP * 2.2 + RIGHT * 2.2)
        # 无产出
        scam_text1 = Text("只拿钱，不产出", font=self.body_font, font_size=self.font_small_size, color=RED).move_to(UP * 1.0 + RIGHT * 2.2)
        # 无义务
        scam_text2 = Text("出了事，不负责", font=self.body_font, font_size=self.font_small_size, color=RED).move_to(UP * 0.2 + RIGHT * 2.2)
        # 警告图标
        warning_icon = self.load_png_icon("warning", height=1.2).move_to(DOWN * 1.0 + RIGHT * 2.2)
        cross_text = Text("✗ 无义务", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(warning_icon, DOWN, buff=0.2)
        scam_group = Group(scam_title, scam_text1, scam_text2, warning_icon, cross_text)
        
        # 4. 中间 VS
        vs_text = Text("VS", font=self.title_font, font_size=self.font_body_size, color=ORANGE).move_to(UP * 0.5)
        
        # 5. 底部结论
        conclusion = Text(
            "看有没有产出和义务", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)
        conclusion_box = RoundedRectangle(
            height=1.2,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(conclusion, buff=0.4)
        conclusion_group = VGroup(conclusion_box, conclusion)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(legit_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(scam_group, shift=LEFT), FadeIn(vs_text, scale=0.5), run_time=step_time)
        self.play(FadeIn(conclusion_group, scale=0.8), run_time=step_time)
        self.play(Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：具象化场景 -> 四个判断维度
        
        口播稿关键词/短语：
        - "有人拉你投资" -> 场景触发
        - "承诺高收益却说不清产出" -> 警示信号
        - "没牌照、没信用背书、没实际产出、不承担义务" -> 四个红旗
        - "四个要素对一对，骗子无处藏" -> 结论
        
        动态标题：「警惕这些信号」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、场景触发、四个红旗、警示框、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "警惕这些信号", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(UP * 4.0)
        
        # 2. 场景触发
        trigger_text = Text(
            "有人拉你投资，承诺高收益...", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(UP * 2.5)
        
        # 3. 四个红旗警示 - 使用图标+文字
        # 没牌照
        flag1_icon = self.load_png_icon("certificate", height=1.0).move_to(UP * 1.0 + LEFT * 2.5)
        flag1_text = Text("✗ 没牌照", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(flag1_icon, RIGHT, buff=0.2)
        flag1 = Group(flag1_icon, flag1_text)
        
        # 没信用
        flag2_icon = self.load_png_icon("scales", height=1.0).move_to(UP * 0.0 + LEFT * 2.5)
        flag2_text = Text("✗ 没信用背书", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(flag2_icon, RIGHT, buff=0.2)
        flag2 = Group(flag2_icon, flag2_text)
        
        # 没产出
        flag3_icon = self.load_png_icon("money", height=1.0).move_to(DOWN * 1.0 + LEFT * 2.5)
        flag3_text = Text("✗ 没实际产出", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(flag3_icon, RIGHT, buff=0.2)
        flag3 = Group(flag3_icon, flag3_text)
        
        # 不承担义务
        flag4_icon = self.load_png_icon("shield", height=1.0).move_to(DOWN * 2.0 + LEFT * 2.5)
        flag4_text = Text("✗ 不承担义务", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(flag4_icon, RIGHT, buff=0.2)
        flag4 = Group(flag4_icon, flag4_text)
        
        flags = [flag1, flag2, flag3, flag4]
        
        # 4. 警示框
        warning_box_text = Text(
            "全是野路子！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(DOWN * 0.5 + RIGHT * 2.0)
        warning_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=RED, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=RED
        ).surround(warning_box_text, buff=0.3)
        warning_group = VGroup(warning_box, warning_box_text)
        
        # 5. 底部结论
        conclusion = Text(
            "四要素对一对，骗子无处藏", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(trigger_text), run_time=step_time)
        # 使用 LaggedStart 逐项弹出红旗
        self.play(
            LaggedStart(
                *[FadeIn(flag, shift=RIGHT) for flag in flags], 
                lag_ratio=0.3
            ), 
            run_time=step_time
        )
        self.play(FadeIn(warning_group, scale=0.8), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：四要素检验法 -> 逐项弹出 -> 强调可执行
        
        口播稿关键词/短语：
        - "四要素检验法" -> 核心口诀
        - "第一问牌照，有没有金融许可证" -> 步骤1
        - "第二问信用，谁给他背书" -> 步骤2
        - "第三问产出，钱投出去能产生什么" -> 步骤3
        - "第四问义务，出了问题谁负责" -> 步骤4
        - "四个都说不清的，赶紧跑" -> 行动结论
        
        动态标题：「四要素检验法」
        使用 LaggedStart 实现逐项弹出效果
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、口诀框、四个步骤、行动结论、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "四要素检验法", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心口诀 - 金句框
        slogan = Text(
            "问四遍，防被骗", 
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
        
        # 3. 四个步骤
        step1 = Text("① 问牌照：有没有金融许可证？", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(UP * 1.0)
        step2 = Text("② 问信用：谁给他背书？", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(UP * 0.0)
        step3 = Text("③ 问产出：钱投出去产生什么？", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 1.0)
        step4 = Text("④ 问义务：出问题谁负责？", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 2.0)
        
        steps = [step1, step2, step3, step4]
        
        # 4. 行动结论
        action_text = Text(
            "说不清的，赶紧跑！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(slogan_group, scale=0.8), run_time=step_time)
        # 使用 LaggedStart 逐项弹出，lag_ratio=0.3
        self.play(
            LaggedStart(
                *[FadeIn(step, shift=RIGHT) for step in steps], 
                lag_ratio=0.3
            ), 
            run_time=2*step_time
        )
        self.play(Write(action_text), Circumscribe(action_text, color=RED), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：低门槛互动 -> 强调动画 -> 引导关注
        
        口播稿关键词/短语：
        - "知道怎么识别镰刀了吧" -> 总结
        - "用四要素法检验一下" -> 行动建议
        - "点赞收藏" -> 互动号召
        - "下期继续" -> 预告
        
        动态标题：「用四要素防割」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、互动任务、互动图标、系列口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 核心CTA标题
        title = Text(
            "用四要素防割", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 3.5)
        
        # 2. 互动任务
        task_text = Text(
            "下次投资前检验一下", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(UP * 1.8)
        
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
        self.play(Write(task_text), Circumscribe(task_text, color=GOLD), run_time=step_time)
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
        - scissors: 镰刀/割韭菜核心概念
        - money: 金钱/理财主题
        - shield: 防护/防割
        - warning: 警示/识别骗子
        - certificate: 牌照/四要素之一
        """
        return ["scissors", "money", "shield", "warning", "certificate"]
