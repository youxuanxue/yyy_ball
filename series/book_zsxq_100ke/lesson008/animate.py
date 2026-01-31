import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson008VerticalScenes(Zsxq100keLessonVertical):
    """
    第008课：公开弄钱与个人投资
    副标题：钱从哪来，合法募资的门道
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：引发共鸣 -> 反常识观点 -> 抓住注意力
        
        口播稿关键词/短语：
        - "银行1块钱就能存" vs "信托100万起投" -> 门槛对比
        - "有些基金能打广告，有些只能偷偷私下推" -> 公开 vs 私募
        - "合法弄钱有几种方法" -> 核心问题
        
        动态标题：「1块 vs 100万？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、银行1块、信托100万、VS对比、疑问、结论）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题 (y=4.0) - 引发好奇
        title = Text(
            "1块 vs 100万？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 左侧：银行1块钱起存
        # 图标来源：bank_building 在 script.json icons 中
        bank_icon = self.load_png_icon("bank_building", height=1.8).move_to(UP * 1.5 + LEFT * 2.2)
        bank_label = Text("银行", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(bank_icon, DOWN, buff=0.2)
        bank_amount = Text("1块钱起", font=self.title_font, font_size=self.font_body_size, color=GREEN).next_to(bank_label, DOWN, buff=0.2)
        bank_group = Group(bank_icon, bank_label, bank_amount)
        
        # 3. 右侧：信托100万起投
        # 图标来源：investment_portfolio 在 script.json icons 中
        trust_icon = self.load_png_icon("investment_portfolio", height=1.8).move_to(UP * 1.5 + RIGHT * 2.2)
        trust_label = Text("信托", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(trust_icon, DOWN, buff=0.2)
        trust_amount = Text("100万起", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(trust_label, DOWN, buff=0.2)
        trust_group = Group(trust_icon, trust_label, trust_amount)
        
        # 4. 中间 VS
        vs_text = Text("VS", font=self.title_font, font_size=self.font_body_size, color=RED).move_to(UP * 1.5)
        
        # 5. 疑问文字
        question_text = Text(
            "为什么差这么多？", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(DOWN * 1.5)
        
        # 6. 底部结论 - 引出主题
        conclusion = Text(
            "合法弄钱有几种方法", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(bank_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(trust_group, shift=LEFT), run_time=step_time)
        self.play(FadeIn(vs_text, scale=0.5), run_time=step_time)
        self.play(Write(question_text), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：核心概念 -> 分类结构 -> 清晰对比
        
        口播稿关键词/短语：
        - "银行吸储最牛，1块钱起，全国都能收" -> 银行特权
        - "信托和私募门槛高，100万起投，最多50到200人" -> 高门槛限制
        - "公募基金1块钱起，但只能投股票债券" -> 公募特点
        - "规则不一样，玩法就不一样" -> 总结
        
        动态标题：「合法募资四大类」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、银行、信托私募、公募、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部：核心概念标题
        title = Text(
            "合法募资四大类", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 第一类：银行吸储
        row1_icon = self.load_png_icon("bank_building", height=1.2).move_to(UP * 2.2 + LEFT * 3.0)
        row1_text = Text("银行吸储", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(row1_icon, RIGHT, buff=0.3)
        row1_detail = Text("1块起，全国收", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(row1_text, RIGHT, buff=0.3)
        row1 = Group(row1_icon, row1_text, row1_detail)
        
        # 3. 第二类：信托/私募
        row2_icon = self.load_png_icon("lock", height=1.2).move_to(UP * 0.8 + LEFT * 3.0)
        row2_text = Text("信托/私募", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(row2_icon, RIGHT, buff=0.3)
        row2_detail = Text("100万起，限人数", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(row2_text, RIGHT, buff=0.3)
        row2 = Group(row2_icon, row2_text, row2_detail)
        
        # 4. 第三类：公募基金
        row3_icon = self.load_png_icon("crowdfunding", height=1.2).move_to(DOWN * 0.6 + LEFT * 3.0)
        row3_text = Text("公募基金", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(row3_icon, RIGHT, buff=0.3)
        row3_detail = Text("1块起，投股债", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(row3_text, RIGHT, buff=0.3)
        row3 = Group(row3_icon, row3_text, row3_detail)
        
        rows = [row2, row3]
        
        # 5. 底部总结
        summary = Text(
            "规则不同，玩法不同", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(row1, shift=RIGHT), run_time=step_time)
        # 使用 LaggedStart 逐项弹出其他类别
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=RIGHT) for row in rows], 
                lag_ratio=0.4
            ), 
            run_time=step_time * 2
        )
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：核心洞察 -> 逻辑链条 -> 安全性
        
        口播稿关键词/短语：
        - "门槛越低，监管越严" -> 核心洞察
        - "银行能1块钱起存，是因为有存款保险和严格监管" -> 银行逻辑
        - "私募门槛高，是因为认为你是合格投资者，能承担风险" -> 私募逻辑
        - "懂这个逻辑，才能分辨正规军和野路子" -> 落脚点
        
        动态标题：「门槛背后的逻辑」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、核心洞察、低门槛逻辑、高门槛逻辑、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "门槛背后的逻辑", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 核心洞察 - 金句框
        insight = Text(
            "门槛越低 = 监管越严", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(UP * 2.5)
        insight_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(insight, buff=0.4)
        insight_group = VGroup(insight_box, insight)
        
        # 3. 低门槛逻辑：银行
        low_icon = self.load_png_icon("bank_building", height=1.2).move_to(UP * 0.5 + LEFT * 3.0)
        low_text = Text("银行1块起", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(low_icon, RIGHT, buff=0.3)
        low_arrow = Text("→", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(low_text, RIGHT, buff=0.2)
        low_reason = Text("存款保险+严监管", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(low_arrow, RIGHT, buff=0.2)
        low_group = Group(low_icon, low_text, low_arrow, low_reason)
        
        # 4. 高门槛逻辑：私募
        high_icon = self.load_png_icon("lock", height=1.2).move_to(DOWN * 1.2 + LEFT * 3.5)
        high_text = Text("私募100万起", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(high_icon, RIGHT, buff=0.3)
        high_arrow = Text("→", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(high_text, RIGHT, buff=0.2)
        high_reason = Text("合格投资者自担风险", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(high_arrow, RIGHT, buff=0.2)
        high_group = Group(high_icon, high_text, high_arrow, high_reason)
        
        # 5. 底部结论
        conclusion = Text(
            "懂逻辑，辨正规与野路子", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(insight_group, scale=0.8), run_time=step_time)
        self.play(FadeIn(low_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(high_group, shift=RIGHT), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：具象化场景 -> 红旗警示 -> 引发警觉
        
        口播稿关键词/短语：
        - "1块钱起，还承诺高收益，十有八九是非法集资" -> 红旗1
        - "100万起的私募，拆成几万块卖给你，也是违规的" -> 红旗2
        - "正规的募资，门槛和规则都是明确的" -> 正确做法
        
        动态标题：「这些是骗局信号」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、红旗1、红旗2、正确做法、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "这些是骗局信号", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(UP * 4.0)
        
        # 2. 红旗1：低门槛+高收益
        flag1_text = Text("✗ 1块钱起 + 高收益承诺", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(UP * 2.0)
        flag1_warn = Text("→ 非法集资！", font=self.title_font, font_size=self.font_body_size, color=RED).next_to(flag1_text, DOWN, buff=0.3)
        flag1_group = VGroup(flag1_text, flag1_warn)
        
        # 3. 红旗2：私募拆份额
        flag2_text = Text("✗ 100万私募拆成几万卖", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(DOWN * 0.5)
        flag2_warn = Text("→ 违规操作！", font=self.title_font, font_size=self.font_body_size, color=RED).next_to(flag2_text, DOWN, buff=0.3)
        flag2_group = VGroup(flag2_text, flag2_warn)
        
        # 4. 正确做法
        correct_text = Text(
            "✓ 正规募资：门槛和规则明确", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).move_to(DOWN * 2.5)
        correct_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GREEN, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GREEN
        ).surround(correct_text, buff=0.4)
        correct_group = VGroup(correct_box, correct_text)
        
        # 5. 底部结论
        conclusion = Text(
            "遇到就要警惕！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 4.2)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(flag1_group), run_time=step_time)
        self.play(Write(flag2_group), run_time=step_time)
        self.play(FadeIn(correct_group, scale=0.8), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=RED), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：行动步骤 -> 逐项弹出 -> 强调可执行
        
        口播稿关键词/短语：
        - "看门槛看牌照" -> 核心口诀
        - "100万以下的，要么是银行存款，要么是公募基金" -> 判断标准1
        - "100万以上的信托和私募，得去正规平台买" -> 判断标准2
        - "没有牌照满嘴跑火车的，离远点" -> 避坑原则
        
        动态标题：「看门槛看牌照」
        使用 LaggedStart 实现逐项弹出效果
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、口诀、三条策略、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "判断标准", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心口诀 - 金句框
        slogan = Text(
            "看门槛 + 看牌照", 
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
        item1 = Text("① 100万以下：银行存款或公募基金", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(UP * 0.8)
        item2 = Text("② 100万以上：正规平台买信托/私募", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 0.4)
        item3 = Text("③ 没牌照的：离远点！", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(DOWN * 1.6)
        
        items = [item1, item2, item3]
        
        # 4. 底部结论
        conclusion = Text(
            "门槛+牌照，一看就懂", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
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
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：低门槛互动 -> 强调动画 -> 引导关注
        
        口播稿关键词/短语：
        - "下次有人拉你投资，先问问门槛和牌照" -> 互动任务
        - "点赞收藏" -> 互动号召
        - "下期聊股票" -> 预告
        
        动态标题：「记住这两问」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、互动任务、互动图标、系列口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 核心CTA标题
        title = Text(
            "记住这两问", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 3.5)
        
        # 2. 互动任务
        task_text = Text(
            "门槛多少？牌照有吗？", 
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
        - bank_building: 银行募资核心概念
        - investment_portfolio: 信托/私募投资
        - crowdfunding: 公募基金
        - lock: 门槛限制/私募
        - coins: 理财/金钱
        """
        return ["bank_building", "investment_portfolio", "crowdfunding", "lock", "coins"]
