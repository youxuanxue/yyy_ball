import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson014VerticalScenes(Zsxq100keLessonVertical):
    """
    第014课：企业借钱的两条路
    主题：信用贷和抵押贷，到底怎么选？
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)
        
        口播稿：你是不是觉得，企业要借钱，只要有实力就行？错！
                在中国，企业借钱只有两条路：要么你信用够硬，银行信任你；
                要么你有房子抵押，拿资产换钱。没有第三条路！
        
        关键词/短语：
        - "两条路" -> 左右对比布局
        - "信用够硬" -> 信用卡/文档图标
        - "房子抵押" -> 房子图标
        
        动态标题：「企业借钱只有两条路」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、问题、两条路、结论）
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部动态标题 (y=4.0)
        title = Text(
            "企业借钱只有两条路", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 误区提示
        wrong_text = Text(
            "「有实力就能借到钱？」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(UP * 2.0)
        cross_mark = Text("✗", font=self.title_font, font_size=self.font_title_size, color=RED).next_to(wrong_text, LEFT, buff=0.3)
        wrong_group = VGroup(cross_mark, wrong_text)

        # 3. 两条路（左右布局）
        # 左侧：信用贷
        credit_icon = self.load_png_icon("document", height=1.5).shift(LEFT * 2.0 + DOWN * 0.3)
        credit_label = Text("信用贷", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(credit_icon, DOWN, buff=0.2)
        credit_desc = Text("银行信任你", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(credit_label, DOWN, buff=0.15)
        credit_group = Group(credit_icon, credit_label, credit_desc)
        
        # 右侧：抵押贷
        house_icon = self.load_png_icon("house", height=1.5).shift(RIGHT * 2.0 + DOWN * 0.3)
        house_label = Text("抵押贷", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(house_icon, DOWN, buff=0.2)
        house_desc = Text("拿资产换钱", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(house_label, DOWN, buff=0.15)
        house_group = Group(house_icon, house_label, house_desc)

        # 4. 底部结论
        conclusion = Text(
            "没有第三条路！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(wrong_group, shift=UP), run_time=step_time)
        self.play(
            FadeIn(credit_group, shift=RIGHT), 
            FadeIn(house_group, shift=LEFT), 
            run_time=step_time
        )
        self.play(Write(conclusion), Circumscribe(conclusion, color=RED), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)
        
        口播稿：简单说，企业贷款就两种。一种叫信用贷，银行看你企业的规模、利润、现金流，
                觉得你靠谱就放款，不要抵押物。另一种叫抵押贷，你得拿房子押给银行，
                房子值多少钱，贷多少款。
        
        动态标题：「两种贷款有什么区别？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "两种贷款有什么区别？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 信用贷解释
        credit_title = Text("信用贷", font=self.title_font, font_size=self.font_title_size, color=BLUE).shift(UP * 2.5)
        credit_icon = self.load_png_icon("credit_card", height=1.2).next_to(credit_title, DOWN, buff=0.3)
        credit_desc = Text(
            "看规模、利润、现金流", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).next_to(credit_icon, DOWN, buff=0.2)
        credit_note = Text("不要抵押物", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(credit_desc, DOWN, buff=0.15)
        credit_group = Group(credit_title, credit_icon, credit_desc, credit_note)
        
        # 3. 抵押贷解释
        mortgage_title = Text("抵押贷", font=self.title_font, font_size=self.font_title_size, color=GOLD).shift(DOWN * 1.0)
        mortgage_icon = self.load_png_icon("house", height=1.2).next_to(mortgage_title, DOWN, buff=0.3)
        mortgage_desc = Text(
            "房子值多少，贷多少", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).next_to(mortgage_icon, DOWN, buff=0.2)
        mortgage_group = Group(mortgage_title, mortgage_icon, mortgage_desc)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(credit_group, shift=DOWN), run_time=2* step_time)
        self.play(FadeIn(mortgage_group, shift=UP), run_time=2*step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)
        
        口播稿：问题的关键在于，能拿到信用贷的企业越来越少了。
                以前国企、上市公司能纯信用借钱，现在呢？
                民企想借信用贷难如登天。银行不是不想放，是不敢放，风险太大。
        
        动态标题：「信用贷越来越难借了」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "信用贷越来越难借了", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 对比：以前 vs 现在（用多个文本块排版，避免直接使用 \n）
        col_max_width = 3.4
        
        def _fit_width(mob, max_w=col_max_width):
            """按最大宽度缩放文本，避免窄屏溢出。"""
            if mob.width > max_w:
                mob.scale_to_fit_width(max_w)
            return mob
        
        # 左侧：以前（更容易拿到信用贷）
        before_icon = self.load_png_icon("building", height=1.1).move_to(LEFT * 2.8 + UP * 2.3)
        before_label = Text("以前", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(before_icon, DOWN, buff=0.15)
        before_line1 = _fit_width(Text("国企、上市公司", font=self.body_font, font_size=self.font_body_size, color=GREEN)).next_to(before_label, DOWN, buff=0.2)
        before_line2 = _fit_width(Text("能纯信用借钱", font=self.body_font, font_size=self.font_body_size, color=GREEN)).next_to(before_line1, DOWN, buff=0.12)
        # 注意：VGroup 只能包含 VMobject；PNG 图标是 ImageMobject，需要用 Group
        before_group = Group(before_icon, before_label, before_line1, before_line2)
        
        # 右侧：现在（民企越来越难）
        now_icon = self.load_png_icon("user", height=1.1).move_to(RIGHT * 2.8 + UP * 2.3)
        now_label = Text("现在", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(now_icon, DOWN, buff=0.15)
        now_warning = self.load_png_icon("warning", height=0.55).next_to(now_label, RIGHT, buff=0.25)
        now_line1 = _fit_width(Text("民企想借信用贷", font=self.body_font, font_size=self.font_body_size, color=RED)).next_to(now_label, DOWN, buff=0.2)
        now_line2 = _fit_width(Text("难如登天", font=self.body_font, font_size=self.font_body_size, color=RED)).next_to(now_line1, DOWN, buff=0.12)
        now_group = Group(now_icon, now_label, now_warning, now_line1, now_line2)
        
        # 3. 中间分隔：信用贷 -> 变难（图标 + 箭头）
        arrow = Arrow(LEFT * 0.9, RIGHT * 0.9, color=GRAY).shift(UP * 1.4)
        credit_icon = self.load_png_icon("credit_card", height=0.6).next_to(arrow, UP, buff=0.15)
        mid_group = Group(credit_icon, arrow)

        # 4. 底部原因（拆成多个文本块，增强视觉层次）
        bank_icon = self.load_png_icon("bank", height=1.0).shift(LEFT * 3.0 + DOWN * 2.4)
        reason_line1 = _fit_width(Text("银行不是不想放", font=self.title_font, font_size=self.font_title_size, color=GRAY), max_w=5.5)
        reason_line2 = _fit_width(Text("而是“不敢放”", font=self.title_font, font_size=self.font_title_size, color=ORANGE), max_w=5.5)
        reason_text = VGroup(reason_line1, reason_line2).arrange(DOWN, aligned_edge=LEFT, buff=0.12).next_to(bank_icon, RIGHT, buff=0.35)
        
        risk_icon = self.load_png_icon("warning", height=0.75)
        risk_text = Text("风险太大", font=self.body_font, font_size=self.font_body_size, color=RED)
        risk_group = Group(risk_icon, risk_text).arrange(RIGHT, buff=0.2).next_to(reason_text, DOWN, aligned_edge=LEFT, buff=0.25)
        reason_group = Group(bank_icon, reason_text, risk_group)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(before_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(mid_group), FadeIn(now_group, shift=LEFT), run_time=step_time)
        self.play(FadeIn(reason_group, shift=UP), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)
        
        口播稿：如果你是小企业主，银行主要看两个东西：税贷和征信贷。
                交的税多，证明你赚钱，银行就敢放款。
                征信好，从来不逾期，银行也愿意给你机会。
                这是金融科技带来的新路子。
        
        动态标题：「小企业主的新机会」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "小企业主的新机会", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 企业主图标
        business_icon = self.load_png_icon("businessman", height=1.5).shift(UP * 2.0)
        business_label = Text("小企业主", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(business_icon, DOWN, buff=0.2)
        business_group = Group(business_icon, business_label)

        # 3. 两种新路子
        # 税贷
        tax_icon = self.load_png_icon("document", height=1.2).shift(LEFT * 2.0 + DOWN * 0.8)
        tax_label = Text("税贷", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(tax_icon, DOWN, buff=0.2)
        tax_desc = Text("交税多=赚钱多", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(tax_label, DOWN, buff=0.1)
        tax_group = Group(tax_icon, tax_label, tax_desc)

        # 征信贷
        credit_icon = self.load_png_icon("credit_card", height=1.2).shift(RIGHT * 2.0 + DOWN * 0.8)
        credit_label = Text("征信贷", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(credit_icon, DOWN, buff=0.2)
        credit_desc = Text("不逾期=信用好", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(credit_label, DOWN, buff=0.1)
        credit_group = Group(credit_icon, credit_label, credit_desc)

        # 4. 底部总结
        summary = Text("金融科技带来的新路子", font=self.title_font, font_size=self.font_title_size, color=GOLD).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(business_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(tax_group, shift=UP), FadeIn(credit_group, shift=UP), run_time=step_time)
        self.play(Write(summary), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)
        
        口播稿：记住三点：第一，别小看纳税记录，交的税越多，能借的钱越多；
                第二，保护好企业征信，两年内别逾期超过6次；
                第三，有房产的话，一抵给银行，利息最低，二抵给小贷，利息高但救急。
        
        动态标题：「企业借钱三条建议」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：3个动作（标题、三条建议逐项弹出、总结）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "企业借钱三条建议", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三条建议
        tip1_icon = self.load_png_icon("document", height=0.8).shift(LEFT * 3.0 + UP * 1.8)
        tip1_text = Text(
            "①纳税记录是借款筹码", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(tip1_icon, RIGHT, buff=0.3)
        tip1 = Group(tip1_icon, tip1_text)

        tip2_icon = self.load_png_icon("shield", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        tip2_text = Text(
            "②保护征信别逾期", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).next_to(tip2_icon, RIGHT, buff=0.3)
        tip2 = Group(tip2_icon, tip2_text)

        tip3_icon = self.load_png_icon("house", height=0.8).shift(LEFT * 3.0 + DOWN * 1.2)
        tip3_text = Text(
            "③有房产一抵给银行", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).next_to(tip3_icon, RIGHT, buff=0.3)
        tip3 = Group(tip3_icon, tip3_text)

        tips = [tip1, tip2, tip3]

        # 3. 底部总结
        summary = Text(
            "信用和资产是硬通货", 
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
        
        口播稿：企业借钱这事儿，信用和资产是硬通货。
                觉得有收获的话，点个赞，关注我，咱们下期继续聊理财那些事儿。
        
        动态标题：「学到了吗？」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
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
            "信用和资产是硬通货", 
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
