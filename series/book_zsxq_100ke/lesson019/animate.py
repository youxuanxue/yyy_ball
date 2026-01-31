import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson019VerticalScenes(Zsxq100keLessonVertical):
    """
    第019课：为什么不建议你炒股
    主题：普通人在股市的真实处境
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)
        
        口播稿：你是不是也这样：一买股票就跌，一卖就涨？
                别以为是运气差，这是大部分散户的宿命。
                今天告诉你一个扎心的真相：普通人炒股，大概率是亏钱的。
        
        动态标题：「一买就跌，一卖就涨？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部动态标题
        title = Text(
            "一买就跌，一卖就涨？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(UP * 4.0)
        
        # 2. 散户困境
        buy_text = Text("买入", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(LEFT * 2.0 + UP * 1.8)
        buy_arrow = Text("↓", font=self.title_font, font_size=self.font_title_size, color=RED).next_to(buy_text, DOWN, buff=0.2)
        buy_result = Text("跌", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(buy_arrow, DOWN, buff=0.2)
        buy_group = VGroup(buy_text, buy_arrow, buy_result)

        sell_text = Text("卖出", font=self.body_font, font_size=self.font_body_size, color=RED).shift(RIGHT * 2.0 + UP * 1.8)
        sell_arrow = Text("↑", font=self.title_font, font_size=self.font_title_size, color=GREEN).next_to(sell_text, DOWN, buff=0.2)
        sell_result = Text("涨", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(sell_arrow, DOWN, buff=0.2)
        sell_group = VGroup(sell_text, sell_arrow, sell_result)

        # 3. 扎心图标
        sad_icon = self.load_png_icon("sad", height=1.5).shift(DOWN * 1.0)
        sad_text = Text("散户宿命", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(sad_icon, DOWN, buff=0.2)
        sad_group = Group(sad_icon, sad_text)

        # 4. 底部结论
        conclusion = Text(
            "普通人炒股，大概率亏钱", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(buy_group, shift=DOWN), FadeIn(sell_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(sad_group, shift=UP), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=RED), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)
        
        口播稿：诺贝尔经济学奖得主塞勒说：
                失去10块钱的痛苦，要捡到20块钱才能抵消。这叫损失厌恶。
                股票跌了20%，你要赚40%才能心理平衡。
                但中国股市80%的时间在跌。
        
        动态标题：「什么是损失厌恶？」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "什么是损失厌恶？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 诺奖得主名言
        quote = Text(
            "丢10块的痛苦 = 捡20块的快乐", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).move_to(UP * 2.0)
        author = Text("—— 诺贝尔奖得主塞勒", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(quote, DOWN, buff=0.2)

        # 3. 股票应用
        stock_example = VGroup(
            Text("跌20%", font=self.body_font, font_size=self.font_body_size, color=RED),
            Text("→ 要赚40%才能心理平衡", font=self.body_font, font_size=self.font_body_size, color=WHITE),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.5)

        # 4. 扎心数据
        data = Text(
            "中国股市80%时间在跌", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 2.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(quote), FadeIn(author), run_time=step_time)
        self.play(FadeIn(stock_example), run_time=step_time)
        self.play(Write(data), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)
        
        口播稿：问题的关键在于，普通人在股市里没有利用价值。
                大资金能带来信心和资源，散户能带来什么？只有手里那点小钱。
                你就是韭菜，被机构收割是常态。
        
        动态标题：「散户的利用价值是什么？」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "散户的利用价值是什么？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 大资金 vs 散户
        big_money = Text("大资金", font=self.body_font, font_size=self.font_body_size, color=GOLD).shift(LEFT * 2.0 + UP * 1.8)
        big_value = Text("带来信心和资源", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(big_money, DOWN, buff=0.2)
        big_group = VGroup(big_money, big_value)

        retail = Text("散户", font=self.body_font, font_size=self.font_body_size, color=GRAY).shift(RIGHT * 2.0 + UP * 1.8)
        retail_value = Text("只有那点小钱", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(retail, DOWN, buff=0.2)
        retail_group = VGroup(retail, retail_value)

        # 3. 韭菜图标（用植物叶子替代）
        leek_icon = self.load_png_icon("leaf", height=1.5).shift(DOWN * 0.8)
        leek_text = Text("韭菜", font=self.title_font, font_size=self.font_title_size, color=GREEN).next_to(leek_icon, DOWN, buff=0.2)
        leek_group = Group(leek_icon, leek_text)

        # 4. 底部结论
        conclusion = Text(
            "被机构收割是常态", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(big_group, shift=RIGHT), FadeIn(retail_group, shift=LEFT), run_time=step_time)
        self.play(FadeIn(leek_group, shift=UP), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=RED), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)
        
        口播稿：什么人可以炒股？
                有闲钱、有时间、有专业知识，三样都占齐的人。
                普通上班族，工资是主要收入来源，根本没时间盯盘研究，炒股就是送钱。
        
        动态标题：「什么人适合炒股？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "什么人适合炒股？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 三个条件
        conditions = VGroup(
            Text("✓ 有闲钱", font=self.body_font, font_size=self.font_body_size, color=GREEN),
            Text("✓ 有时间", font=self.body_font, font_size=self.font_body_size, color=GREEN),
            Text("✓ 有专业知识", font=self.body_font, font_size=self.font_body_size, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 1.2)

        requirement = Text("三样都占齐", font=self.title_font, font_size=self.font_title_size, color=GOLD).next_to(conditions, DOWN, buff=0.4)

        # 3. 上班族
        worker_icon = self.load_png_icon("businessman", height=1.2).shift(DOWN * 1.5)
        worker_text = Text("普通上班族", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(worker_icon, DOWN, buff=0.2)
        worker_warning = Text("没时间盯盘 = 送钱", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(worker_text, DOWN, buff=0.15)
        worker_group = Group(worker_icon, worker_text, worker_warning)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(LaggedStart(*[FadeIn(c) for c in conditions], lag_ratio=0.2), run_time=step_time)
        self.play(Write(requirement), run_time=step_time)
        self.play(FadeIn(worker_group, shift=UP), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)
        
        口播稿：普通人想参与股市，最好的方式是买公募基金。
                让专业的基金经理帮你选股，你只需要选一个靠谱的基金。
                记住：正规渠道买，别信群里的野生股神。
        
        动态标题：「普通人的更好选择」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "普通人的更好选择", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 公募基金
        fund_icon = self.load_png_icon("investment_portfolio", height=1.8).shift(UP * 1.5)
        fund_text = Text("公募基金", font=self.title_font, font_size=self.font_title_size, color=GOLD).next_to(fund_icon, DOWN, buff=0.3)
        fund_desc = Text("让专业经理帮你选股", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(fund_text, DOWN, buff=0.2)
        fund_group = Group(fund_icon, fund_text, fund_desc)

        # 3. 两个要点
        point1 = Text("✓ 正规渠道买", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(LEFT * 2.0 + DOWN * 2.0)
        point2 = Text("✗ 别信野生股神", font=self.body_font, font_size=self.font_body_size, color=RED).shift(RIGHT * 2.0 + DOWN * 2.0)
        points_group = VGroup(point1, point2)

        # 4. 底部总结
        summary = Text(
            "基金是更好的选择", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(fund_group, shift=DOWN), run_time=step_time)
        self.play(FadeIn(points_group), run_time=step_time)
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action)
        
        口播稿：炒股不适合大多数人，认清这点很重要。
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

        # 2. 核心收获
        takeaway = Text(
            "炒股不适合大多数人", 
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
