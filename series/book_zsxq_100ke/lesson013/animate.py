import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson013VerticalScenes(Zsxq100keLessonVertical):
    """
    第013课：放贷没那么简单
    主题：为什么你有钱也不能随便借给别人？
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)
        
        口播稿：你有没有想过，自己手里有点闲钱，借给朋友赚点利息，这买卖挺美？
                但我告诉你，在中国，放贷可不是你想放就能放的。
                为啥银行躺着都能赚钱？因为人家有牌照，你没有！
        
        关键词/短语：
        - "闲钱" -> 钱袋图标
        - "银行躺着赚钱" -> 银行图标
        - "牌照" -> 强调牌照是关键
        
        动态标题：「有钱也不能随便借？」（反常识引发好奇）
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、钱袋+问号、银行图标+牌照、扎心结论）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部动态标题 (y=4.0) - 反常识标题引发好奇
        title = Text(
            "有钱也不能随便借？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 中部：钱袋 + 问号（表达困惑）
        money_icon = self.load_png_icon("money", height=2.0).shift(LEFT * 1.5 + UP * 1.0)
        question = Text("？", font=self.title_font, font_size=self.font_title_size * 1.5, color=GRAY).next_to(money_icon, RIGHT, buff=0.5)
        money_group = Group(money_icon, question)

        # 3. 银行图标 + 牌照文字
        bank_icon = self.load_png_icon("bank", height=2.0).shift(DOWN * 1.0)
        license_text = Text("牌照", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(bank_icon, DOWN, buff=0.3)
        bank_group = Group(bank_icon, license_text)

        # 4. 底部扎心结论
        conclusion = Text(
            "银行有牌照，你没有！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(money_group, shift=UP), run_time=step_time)
        self.play(FadeIn(bank_group, shift=UP), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=RED), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)
        
        口播稿：简单说，发放贷款在中国是需要金融牌照的。
                你得有银保监会发的许可证，才能合法地把钱借出去收利息。
                目前能放贷的主要就两类：银行和信托公司。其他人借钱给别人？法规上是不允许的。
        
        关键词/短语：
        - "金融牌照" -> 文档/许可证图标
        - "银保监会" -> 官方权威感
        - "银行和信托公司" -> 两类机构对比
        
        动态标题：「谁能合法放贷？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、牌照解释、两类机构、底部总结）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "谁能合法放贷？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 牌照 = 许可证（核心概念）
        license_icon = self.load_png_icon("document", height=1.8).shift(UP * 2.0)
        license_label = Text(
            "金融牌照 = 放贷许可证", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).next_to(license_icon, DOWN, buff=0.3)
        license_group = Group(license_icon, license_label)
        
        # 3. 两类机构：银行 + 信托
        bank_icon = self.load_png_icon("bank", height=1.5).shift(LEFT * 2.0 + DOWN * 0.8)
        bank_label = Text("银行", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(bank_icon, DOWN, buff=0.2)
        bank_group = Group(bank_icon, bank_label)
        
        trust_icon = self.load_png_icon("safe", height=1.5).shift(RIGHT * 2.0 + DOWN * 0.8)
        trust_label = Text("信托公司", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(trust_icon, DOWN, buff=0.2)
        trust_group = Group(trust_icon, trust_label)
        
        # 4. 底部总结
        summary = Text(
            "只有这两类能合法放贷", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)
        summary_box = RoundedRectangle(height=1.2, corner_radius=0.3, color=GOLD, fill_opacity=0.15)
        summary_box.surround(summary, buff=0.4)
        summary_group = VGroup(summary_box, summary)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(license_group, shift=DOWN), run_time=step_time)
        self.play(
            FadeIn(bank_group, shift=UP), 
            FadeIn(trust_group, shift=UP), 
            run_time=step_time
        )
        self.play(FadeIn(summary_group), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)
        
        口播稿：问题的关键在于，银行之所以赚钱，不只是因为利息高。
                而是因为全市场的钱，只有它能合法借出去！
                别人想抢生意都没资格。这就是牌照的价值，它是一张合法收钱的通行证。
        
        关键词/短语：
        - "不只是利息高" -> 打破误区（左侧红色）
        - "只有它能合法借出去" -> 真相（右侧绿色）
        - "牌照的价值" -> 核心洞察
        
        动态标题：「银行为啥躺赚？」
        视觉逻辑：左右对比布局
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、误区、真相、核心结论）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "银行为啥躺赚？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 左侧：误区（红色/灰色）
        wrong_label = Text("✗ 误区", font=self.body_font, font_size=self.font_small_size, color=RED).shift(LEFT * 2.2 + UP * 2.0)
        wrong_text = Text(
            "利息高", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).next_to(wrong_label, DOWN, buff=0.4)
        wrong_group = VGroup(wrong_label, wrong_text)

        # 3. 右侧：真相（绿色）
        right_label = Text("✓ 真相", font=self.body_font, font_size=self.font_small_size, color=GREEN).shift(RIGHT * 2.2 + UP * 2.0)
        right_text = Text(
            "独家资格", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).next_to(right_label, DOWN, buff=0.4)
        right_group = VGroup(right_label, right_text)

        # 4. 中间分隔线
        divider = Line(UP * 2.0, DOWN * 0.5, color=GRAY, stroke_width=2).shift(DOWN * 0.3)

        # 5. 底部核心结论
        conclusion = Text(
            "牌照 = 合法收钱通行证", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.0)
        conclusion_box = RoundedRectangle(height=1.2, corner_radius=0.3, color=GOLD, fill_opacity=0.15)
        conclusion_box.surround(conclusion, buff=0.4)
        conclusion_group = VGroup(conclusion_box, conclusion)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(wrong_group, shift=RIGHT), FadeIn(divider), run_time=step_time)
        self.play(FadeIn(right_group, shift=LEFT), run_time=step_time)
        self.play(FadeIn(conclusion_group, shift=UP), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)
        
        口播稿：如果你是个小企业主，想借钱周转，银行是首选。
                如果银行不批，还有小贷公司、担保公司这些类金融机构。
                但要注意，它们利息通常更高，风险也更大。
        
        关键词/短语：
        - "小企业主" -> 商人/企业图标
        - "银行首选" -> 银行图标（绿色推荐）
        - "小贷公司、担保公司" -> 警示
        
        动态标题：「借钱找谁？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、企业主场景、银行首选、备选+警示）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "借钱找谁？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 企业主场景
        business_icon = self.load_png_icon("businessman", height=1.8).shift(UP * 1.8)
        business_label = Text(
            "小企业主想借钱周转", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).next_to(business_icon, DOWN, buff=0.3)
        business_group = Group(business_icon, business_label)

        # 3. 首选：银行（绿色推荐）
        bank_icon = self.load_png_icon("bank", height=1.5).shift(LEFT * 2.0 + DOWN * 1.0)
        bank_label = Text("银行", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(bank_icon, DOWN, buff=0.2)
        recommend = Text("✓ 首选", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(bank_label, DOWN, buff=0.15)
        bank_group = Group(bank_icon, bank_label, recommend)

        # 4. 备选：小贷/担保（黄色警示）
        loan_icon = self.load_png_icon("loan", height=1.5).shift(RIGHT * 2.0 + DOWN * 1.0)
        loan_label = Text("小贷/担保", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(loan_icon, DOWN, buff=0.2)
        warning = Text("⚠ 利息高", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(loan_label, DOWN, buff=0.15)
        loan_group = Group(loan_icon, loan_label, warning)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(business_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(bank_group, shift=UP), run_time=step_time)
        self.play(FadeIn(loan_group, shift=UP), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)
        
        口播稿：作为普通人，记住三点：
                第一，别轻信民间高息揽储，没牌照的都是非法集资；
                第二，借钱找正规渠道，银行、持牌小贷都行；
                第三，想赚利息？买银行理财或者债券基金，让专业机构帮你放贷。
        
        关键词/短语：
        - "三点" -> 逐项展示
        - "非法集资" -> 红色警示
        - "正规渠道" -> 绿色安全
        - "银行理财/债券基金" -> 金色收益
        
        动态标题：「普通人怎么做？」
        使用 LaggedStart 逐项弹出
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：3个动作（标题、三条建议逐项弹出、底部总结）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "普通人怎么做？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三条建议
        tip1_icon = self.load_png_icon("warning", height=0.8).shift(LEFT * 3.0 + UP * 1.8)
        tip1_text = Text(
            "①别信民间高息揽储", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=RED
        ).next_to(tip1_icon, RIGHT, buff=0.3)
        tip1 = Group(tip1_icon, tip1_text)

        tip2_icon = self.load_png_icon("shield", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        tip2_text = Text(
            "②借钱找正规渠道", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).next_to(tip2_icon, RIGHT, buff=0.3)
        tip2 = Group(tip2_icon, tip2_text)

        tip3_icon = self.load_png_icon("money", height=0.8).shift(LEFT * 3.0 + DOWN * 1.2)
        tip3_text = Text(
            "③买理财让机构帮你放贷", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(tip3_icon, RIGHT, buff=0.3)
        tip3 = Group(tip3_icon, tip3_text)

        tips = [tip1, tip2, tip3]

        # 3. 底部总结
        summary = Text(
            "牌照是硬道理", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(tip, shift=RIGHT) for tip in tips], lag_ratio=0.3), 
            run_time=3*step_time
        )
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action)
        
        口播稿：现在你知道了，放贷这事儿，牌照才是硬道理。
                觉得有收获的话，点个赞，关注我，咱们下期继续聊理财那些事儿。
        
        关键词/短语：
        - "点赞" -> 点赞图标
        - "关注" -> 关注图标
        - "下期继续" -> 预告
        
        动态标题：「学到了吗？」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、核心收获、互动图标、口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "学到了吗？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获回顾
        takeaway = Text(
            "放贷这事儿，牌照是硬道理", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(UP * 2.0)
        takeaway_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=GOLD, fill_opacity=0.1)
        takeaway_box.surround(takeaway, buff=0.3)
        takeaway_group = VGroup(takeaway_box, takeaway)

        # 3. 互动图标
        like_icon = self.load_png_icon("thumbs_up", height=1.8).move_to(LEFT * 2.0 + DOWN * 0.5)
        like_label = Text("点赞", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_label)
        
        follow_icon = self.load_png_icon("user", height=1.8).move_to(RIGHT * 2.0 + DOWN * 0.5)
        follow_label = Text("关注", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(follow_icon, DOWN, buff=0.2)
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

        # 结尾画面保持
        self.wait(t_trans)
