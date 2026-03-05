import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson021VerticalScenes(Zsxq100keLessonVertical):
    """
    第021课：公募基金
    主题：普通人搭上大佬顺风车的秘密
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)
        
        口播稿：你有没有发现，好的投资项目好像永远轮不到咱们普通人？
                别人投进去赚翻了，咱们连门都摸不着。
                这不是你的错，因为95%以上的优质项目，真的跟普通人绝缘。
                但有一种方式，能让你也搭上大佬的顺风车，今天咱们就来聊聊它。
        
        关键词/短语：
        - "好的投资项目" -> investment_portfolio 图标
        - "轮不到普通人" -> 灰色调，焦虑感
        - "95%优质项目绝缘" -> 红色强调数据
        - "搭上大佬的顺风车" -> 金色转折
        
        动态标题：「好项目为啥轮不到你？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题 - 灰色冷色调，营造焦虑感
        title = Text(
            "好项目为啥轮不到你？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 投资图标 + 关键短语"别人赚翻了"
        invest_icon = self.load_png_icon("investment_portfolio", height=2.0).move_to(UP * 1.5)
        miss_text = Text(
            "别人赚翻了，你连门都摸不着", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).next_to(invest_icon, DOWN, buff=0.3)
        invest_group = Group(invest_icon, miss_text)

        # 3. 数据强调 "95%"
        data_num = Text(
            "95%", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).shift(DOWN * 1.0)
        data_text = Text(
            "优质项目跟普通人绝缘", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=RED
        ).next_to(data_num, DOWN, buff=0.2)

        # 4. 底部转折 - 金色暗示希望
        hope = Text(
            "但有一种方式能搭上顺风车", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(invest_group, shift=UP), run_time=step_time)
        self.play(Write(data_num), FadeIn(data_text), run_time=step_time)
        self.play(Write(hope), run_time=step_time)
        self.play(Circumscribe(hope, color=GOLD), run_time=step_time)
        
        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)
        
        口播稿：简单说，基金就是大家把钱凑到一起，交给一个专业的人去投资。
                你可以把它想象成拼团，一个人买不起的好东西，一百个人一起买就够了。
                出钱的人叫投资人，管钱的人叫基金管理人，
                钱存在专门的银行账户里，那个银行叫托管人。
                三方按合同来，谁也别想乱来。
        
        关键词/短语：
        - "基金" -> money_bag_with_coins 图标
        - "拼团" -> group 图标，蓝色知识色调
        - "投资人/管理人/托管人" -> 三方关系图示
        
        动态标题：「基金就是拼团投资」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题 - 金色醒目
        title = Text(
            "基金就是「拼团投资」", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心定义
        definition = Text(
            "大家的钱凑一起，专业的人去投资", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).move_to(UP * 2.5)

        # 3. 三方关系图示：投资人 -> 基金 -> 管理人，下方托管人
        investor_icon = self.load_png_icon("group", height=1.2).shift(LEFT * 2.5 + UP * 0.5)
        investor_label = Text("投资人", font=self.body_font, font_size=self.font_small_size, color=WHITE).next_to(investor_icon, DOWN, buff=0.15)
        investor_group = Group(investor_icon, investor_label)

        arrow1 = Text("→", font=self.title_font, font_size=self.font_title_size, color=WHITE).shift(UP * 0.5)
        
        fund_icon = self.load_png_icon("money_bag_with_coins", height=1.2).shift(UP * 0.5)
        # 注意：不要给fund_icon加label避免和arrow重叠，用下方的形式
        
        arrow2 = Text("→", font=self.title_font, font_size=self.font_title_size, color=WHITE).shift(RIGHT * 1.2 + UP * 0.5)
        
        manager_icon = self.load_png_icon("businessman", height=1.2).shift(RIGHT * 2.5 + UP * 0.5)
        manager_label = Text("管理人", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(manager_icon, DOWN, buff=0.15)
        manager_group = Group(manager_icon, manager_label)

        flow_group = Group(investor_group, arrow1, fund_icon, arrow2, manager_group)

        # 4. 托管人 - 银行
        bank_icon = self.load_png_icon("bank_building", height=1.0).shift(DOWN * 1.5)
        bank_label = Text("托管人（银行）", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(bank_icon, DOWN, buff=0.15)
        bank_group = Group(bank_icon, bank_label)

        # 5. 底部总结
        summary = Text(
            "三方按合同，谁也别想乱来", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(definition), run_time=step_time)
        self.play(FadeIn(flow_group, shift=UP), run_time=step_time)
        self.play(FadeIn(bank_group, shift=UP), run_time=step_time)
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)
        
        口播稿：很多人觉得，我自己炒股不行吗？
                你想想，全世界80%的股市交易是专业基金在操盘，只有20%是散户。
                散户干得过大户吗？就像你觉得街边练拳的能打赢职业格斗选手吗？
                基金经理每天就研究这个，信息、资源、经验全面碾压，
                把钱交给专业的人，才是聪明的选择。
        
        关键词/短语：
        - "自己炒股" -> 灰色/红色错误认知
        - "80% vs 20%" -> 对比数据
        - "散户干不过大户" -> 对比布局
        - "专业的人" -> 金色/绿色正确认知
        
        动态标题：「散户干得过大户吗？」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "散户干得过大户吗？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(UP * 4.0)

        # 2. 左右对比布局：散户 vs 专业基金
        # 左侧 - 散户（灰色/红色）
        retail_icon = self.load_png_icon("user", height=1.5).shift(LEFT * 2.0 + UP * 1.5)
        retail_label = Text("散户", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(retail_icon, DOWN, buff=0.2)
        retail_pct = Text("20%", font=self.title_font, font_size=self.font_title_size, color=RED).next_to(retail_label, DOWN, buff=0.15)
        retail_group = Group(retail_icon, retail_label, retail_pct)

        # 中间 VS
        vs_text = Text("VS", font=self.title_font, font_size=self.font_title_size, color=WHITE).shift(UP * 1.5)

        # 右侧 - 专业基金（金色/绿色）
        pro_icon = self.load_png_icon("businessman", height=1.5).shift(RIGHT * 2.0 + UP * 1.5)
        pro_label = Text("专业基金", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(pro_icon, DOWN, buff=0.2)
        pro_pct = Text("80%", font=self.title_font, font_size=self.font_title_size, color=GREEN).next_to(pro_label, DOWN, buff=0.15)
        pro_group = Group(pro_icon, pro_label, pro_pct)

        # 3. 比喻 - "街边练拳 vs 职业格斗"
        analogy = Text(
            "街边练拳能打赢职业选手吗？", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).shift(DOWN * 1.0)

        # 4. 底部结论 - 正确认知
        conclusion = Text(
            "把钱交给专业的人", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(retail_group, shift=RIGHT), FadeIn(vs_text), FadeIn(pro_group, shift=LEFT), run_time=step_time)
        self.play(Write(analogy), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        self.wait(step_time)
        
        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)
        
        口播稿：如果你每个月能攒下几百块闲钱，不想放银行吃灰；
                或者你想投资但不懂选股、没时间盯盘；
                又或者你看好某个行业却不知道买哪只股票，
                那公募基金就是为你量身定做的。一百块就能起投，门槛低到没朋友。
        
        关键词/短语：
        - "攒下几百块" -> coins 图标
        - "不懂选股/没时间" -> confused 图标
        - "看好行业" -> line_chart 图标
        - "一百块起投" -> 绿色强调
        
        动态标题：「公募基金适合你吗？」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "公募基金适合你吗？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 三类适用人群 - 图标+文字，逐项弹出
        # 场景A：闲钱不想放银行
        icon_a = self.load_png_icon("coins", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        text_a = Text(
            "有闲钱不想放银行吃灰", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).next_to(icon_a, RIGHT, buff=0.3)
        group_a = Group(icon_a, text_a)

        # 场景B：不懂选股没时间盯盘
        icon_b = self.load_png_icon("confused", height=0.8).shift(LEFT * 3.0 + UP * 0.5)
        text_b = Text(
            "不懂选股、没时间盯盘", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).next_to(icon_b, RIGHT, buff=0.3)
        group_b = Group(icon_b, text_b)

        # 场景C：看好行业不知道买什么
        icon_c = self.load_png_icon("line_chart", height=0.8).shift(LEFT * 3.0 + DOWN * 1.0)
        text_c = Text(
            "看好行业不知买哪只股", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).next_to(icon_c, RIGHT, buff=0.3)
        group_c = Group(icon_c, text_c)

        items = [group_a, group_b, group_c]

        # 3. 底部结论 - 绿色强调低门槛
        conclusion = Text(
            "100块起投，门槛低到没朋友", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GREEN
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(item, shift=RIGHT) for item in items], lag_ratio=0.3), 
            run_time=step_time
        )
        self.play(Write(conclusion), Circumscribe(conclusion, color=GREEN), run_time=step_time)
        self.wait(step_time)
        
        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)
        
        口播稿：记住三步走。
                第一步，搞清自己能亏多少，保守就买债基货基，稳如老狗。
                第二步，看好大趋势就买指数基金，赌的是国运。
                第三步，想搏高收益就选股票型基金，
                但一定要看基金经理的历史业绩，别追网红经理，看三年以上排名才靠谱。
        
        关键词/短语：
        - "债基货基" -> safe 图标，绿色稳健
        - "指数基金" -> bar_chart 图标，蓝色理性
        - "股票型基金" -> stocks 图标，金色进取
        - "三步走" -> 逐项弹出 LaggedStart
        
        动态标题：「买基金三步走」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "买基金三步走", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 第一步：债基货基 - 稳健
        step1_icon = self.load_png_icon("safe", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        step1_text = Text(
            "①保守买债基货基", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).next_to(step1_icon, RIGHT, buff=0.3)
        step1_sub = Text("稳如老狗", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(step1_text, DOWN, buff=0.1).align_to(step1_text, LEFT)
        step1 = Group(step1_icon, step1_text, step1_sub)

        # 3. 第二步：指数基金 - 赌国运
        step2_icon = self.load_png_icon("bar_chart", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        step2_text = Text(
            "②看趋势买指数基金", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).next_to(step2_icon, RIGHT, buff=0.3)
        step2_sub = Text("赌的是国运", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(step2_text, DOWN, buff=0.1).align_to(step2_text, LEFT)
        step2 = Group(step2_icon, step2_text, step2_sub)

        # 4. 第三步：股票型基金 - 搏收益
        step3_icon = self.load_png_icon("stocks", height=0.8).shift(LEFT * 3.0 + DOWN * 1.4)
        step3_text = Text(
            "③搏收益选股票型基金", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(step3_icon, RIGHT, buff=0.3)
        step3_sub = Text("看三年以上业绩", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(step3_text, DOWN, buff=0.1).align_to(step3_text, LEFT)
        step3 = Group(step3_icon, step3_text, step3_sub)

        steps = [step1, step2, step3]

        # 5. 底部总结
        summary = Text(
            "别追网红，看业绩说话", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(s, shift=RIGHT) for s in steps], lag_ratio=0.3), 
            run_time=3 * step_time
        )
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)
        
        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action)
        
        口播稿：今天你搞懂公募基金了吗？觉得有用就点个赞，
                分享给身边还在盲目炒股的朋友。
                关注我，下期咱们聊聊私募基金到底是怎么回事。
        
        关键词/短语：
        - "点个赞" -> thumbs_up 图标
        - "分享" -> share 图标
        - "关注我" -> user 图标
        
        动态标题：「搞懂了吗？」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "搞懂公募基金了吗？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "公募基金，普通人的最佳选择", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(UP * 2.0)
        takeaway_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=GOLD, fill_opacity=0.1)
        takeaway_box.surround(takeaway, buff=0.3)
        takeaway_group = VGroup(takeaway_box, takeaway)

        # 3. 互动图标 - 点赞 + 分享 + 关注
        like_icon = self.load_png_icon("thumbs_up", height=1.5).move_to(LEFT * 2.5 + DOWN * 0.5)
        like_label = Text("点赞", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_label)
        
        share_icon = self.load_png_icon("share", height=1.5).move_to(DOWN * 0.5)
        share_label = Text("分享", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(share_icon, DOWN, buff=0.2)
        share_group = Group(share_icon, share_label)

        follow_icon = self.load_png_icon("user", height=1.5).move_to(RIGHT * 2.5 + DOWN * 0.5)
        follow_label = Text("关注", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(follow_icon, DOWN, buff=0.2)
        follow_group = Group(follow_icon, follow_label)
        
        icons_group = Group(like_group, share_group, follow_group)

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

        self.save_scene_thumbnail(6)
        # 结尾画面保持
        self.wait(t_trans)
