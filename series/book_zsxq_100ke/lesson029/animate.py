import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson029VerticalScenes(Zsxq100keLessonVertical):
    """
    第029课：十万块的投资法
    主题：非大户人家的财富配置方案
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)

        口播稿：假如你现在有十万块闲钱，怎么投资？是全买股票、全买基金，还是放银行吃利息？
                很多人面对这个问题就懵了，要么把鸡蛋全放一个篮子里，
                要么东买一点西买一点毫无章法。
                今天教你一套非大户人家的财富配置方案，十万块也能玩出花来。

        关键词/短语：
        - "十万块怎么投" -> money 图标
        - "全放一个篮子" -> 红色错误
        - "毫无章法" -> 灰色焦虑
        - "玩出花来" -> 金色转折

        动态标题：「十万块怎么投资？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "十万块怎么投资？",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 钱包图标
        money_icon = self.load_png_icon("stack_of_money", height=2.0).move_to(UP * 1.5)
        confusion = Text(
            "全买股票？全买基金？放银行？",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).next_to(money_icon, DOWN, buff=0.3)
        money_group = Group(money_icon, confusion)

        # 3. 错误做法
        wrong = Text(
            "鸡蛋全放一个篮子 / 毫无章法",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).shift(DOWN * 1.0)

        # 4. 底部转折
        hook = Text(
            "教你一套非大户的配置方案",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(money_group, shift=UP), run_time=step_time)
        self.play(Write(wrong), run_time=step_time)
        self.play(Write(hook), run_time=step_time)
        self.play(Circumscribe(hook, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)

        口播稿：财富配置有四大原则。轻重结合，动产和不动产都要有。
                长短结合，长期养老规划搭配短期证券投资。
                高低结合，低收益存款配高收益投资。
                整散结合，大额投入和零散收入都要管起来。
                记住这四个词：轻重、长短、高低、整散。

        关键词/短语：
        - "四大原则" -> 逐项展示
        - "轻重/长短/高低/整散" -> 四色区分

        动态标题：「财富配置四大原则」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：6个动作
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text(
            "财富配置四大原则",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 四大原则
        p1 = Text("①轻重结合", font=self.body_font, font_size=self.font_body_size, color=BLUE).shift(LEFT * 2.0 + UP * 2.0)
        p1_sub = Text("动产+不动产", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(p1, DOWN, buff=0.1)
        g1 = VGroup(p1, p1_sub)

        p2 = Text("②长短结合", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(RIGHT * 2.0 + UP * 2.0)
        p2_sub = Text("养老+短期投资", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(p2, DOWN, buff=0.1)
        g2 = VGroup(p2, p2_sub)

        p3 = Text("③高低结合", font=self.body_font, font_size=self.font_body_size, color=GOLD).shift(LEFT * 2.0 + DOWN * 0.3)
        p3_sub = Text("存款+高收益", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(p3, DOWN, buff=0.1)
        g3 = VGroup(p3, p3_sub)

        p4 = Text("④整散结合", font=self.body_font, font_size=self.font_body_size, color=ORANGE).shift(RIGHT * 2.0 + DOWN * 0.3)
        p4_sub = Text("大额+零散都管", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(p4, DOWN, buff=0.1)
        g4 = VGroup(p4, p4_sub)

        # 3. 底部总结
        summary = Text(
            "轻重·长短·高低·整散",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(g1, shift=DOWN), run_time=step_time)
        self.play(FadeIn(g2, shift=DOWN), run_time=step_time)
        self.play(FadeIn(g3, shift=UP), run_time=step_time)
        self.play(FadeIn(g4, shift=UP), run_time=step_time)
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)

        口播稿：为什么要这么配？因为单一投资风险太大。全买股票，暴跌了哭都来不及；
                全存银行，通胀把钱吃掉了。搭配着来，才能东方不亮西方亮。
                十万块的投资画像是这样：三口之家普通白领，留够六个月开支后的余额。
                先保命，再赚钱。

        关键词/短语：
        - "全买股票 -> 暴跌" -> 红色错误
        - "全存银行 -> 通胀" -> 灰色错误
        - "东方不亮西方亮" -> 金色正确
        - "先保命再赚钱" -> 金色核心

        动态标题：「为什么要搭配着来」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "为什么要搭配着来",
            font=self.title_font,
            font_size=self.font_title_size,
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 两种错误对比
        err1 = Text("全买股票 → 暴跌哭都来不及", font=self.body_font, font_size=self.font_body_size, color=RED).shift(UP * 2.0)
        err2 = Text("全存银行 → 通胀把钱吃掉", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(err1, DOWN, buff=0.4)

        # 3. 正确做法
        right_way = Text(
            "搭配着来 → 东方不亮西方亮",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GREEN
        ).next_to(err2, DOWN, buff=0.5)

        # 4. 投资画像
        profile = Text(
            "三口之家·留六个月开支·余额投资",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).shift(DOWN * 1.5)

        # 5. 底部金句
        golden = Text(
            "先保命，再赚钱",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(err1), Write(err2), run_time=step_time)
        self.play(Write(right_way), run_time=step_time)
        self.play(Write(profile), run_time=step_time)
        self.play(Write(golden), Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)

        口播稿：具体怎么分？百分之十五买重疾保险，四十岁前必须买。
                百分之二十到三十买大盘指数基金，沪深三百定投。
                剩下百分之四十五到七十，放在行业指数或股票基金里，牛市重仓券商指数。

        关键词/短语：
        - "15%保险" -> shield 图标
        - "20-30%指数基金" -> bar_chart 图标
        - "45-70%行业基金" -> stocks 图标

        动态标题：「十万块这么分」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "十万块这么分",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三大板块
        ins_icon = self.load_png_icon("shield", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        ins_text = Text("15% → 重疾保险", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(ins_icon, RIGHT, buff=0.3)
        ins_sub = Text("40岁前必须买", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(ins_text, DOWN, buff=0.1).align_to(ins_text, LEFT)
        ins = Group(ins_icon, ins_text, ins_sub)

        idx_icon = self.load_png_icon("bar_chart", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        idx_text = Text("20-30% → 大盘指数基金", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(idx_icon, RIGHT, buff=0.3)
        idx_sub = Text("沪深300定投", font=self.body_font, font_size=self.font_small_size, color=BLUE).next_to(idx_text, DOWN, buff=0.1).align_to(idx_text, LEFT)
        idx = Group(idx_icon, idx_text, idx_sub)

        stk_icon = self.load_png_icon("stocks", height=0.8).shift(LEFT * 3.0 + DOWN * 1.4)
        stk_text = Text("45-70% → 行业/股票基金", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(stk_icon, RIGHT, buff=0.3)
        stk_sub = Text("牛市重仓券商指数", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(stk_text, DOWN, buff=0.1).align_to(stk_text, LEFT)
        stk = Group(stk_icon, stk_text, stk_sub)

        blocks = [ins, idx, stk]

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(ins, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(idx, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(stk, shift=RIGHT), run_time=step_time)
        self.wait(step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)

        口播稿：几个注意事项。指数基金别一次买完，分两三次在大盘下跌时入场，摊低成本。
                行业基金要敢于重仓，小打小闹赚不到钱。
                还有一条铁律：千万别拿这钱买车！
                车是消费品，买到手就贬值，家财万贯带毛的不算。把钱投到能生钱的地方才是正道。

        关键词/短语：
        - "分批入场" -> 绿色策略
        - "敢于重仓" -> 金色进取
        - "千万别买车" -> 红色铁律
        - "投到能生钱的地方" -> 金色核心

        动态标题：「注意：千万别拿钱买车」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "注意：千万别拿钱买车",
            font=self.title_font,
            font_size=self.font_title_size,
            color=RED
        ).move_to(UP * 4.0)

        # 2. 注意事项
        tip1 = Text("指数基金分两三次入场，摊低成本", font=self.body_font, font_size=self.font_body_size, color=GREEN).shift(UP * 2.0)
        tip2 = Text("行业基金敢于重仓，小打小闹没用", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(tip1, DOWN, buff=0.4)

        # 3. 铁律 - 别买车
        car_icon = self.load_png_icon("car", height=1.2).shift(DOWN * 0.5)
        car_warning = Text(
            "车是消费品，买到手就贬值",
            font=self.body_font,
            font_size=self.font_body_size,
            color=RED
        ).next_to(car_icon, DOWN, buff=0.2)
        car_group = Group(car_icon, car_warning)

        # 4. 底部金句
        golden = Text(
            "把钱投到能生钱的地方",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(tip1), Write(tip2), run_time=step_time)
        self.play(FadeIn(car_group, shift=UP), run_time=step_time)
        self.play(Write(golden), run_time=step_time)
        self.play(Circumscribe(golden, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action)

        口播稿：十万块不多，但配置对了照样能钱生钱。
                觉得有用就点赞收藏，关注我，下期聊聊大盘见顶的信号。

        动态标题：「配置对了照样钱生钱」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "配置对了照样钱生钱",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "十万块也能玩出花来",
            font=self.body_font,
            font_size=self.font_body_size,
            color=WHITE
        ).move_to(UP * 2.0)
        takeaway_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=GOLD, fill_opacity=0.1)
        takeaway_box.surround(takeaway, buff=0.3)
        takeaway_group = VGroup(takeaway_box, takeaway)

        # 3. 互动图标
        like_icon = self.load_png_icon("thumbs_up", height=1.5).move_to(LEFT * 2.5 + DOWN * 0.5)
        like_label = Text("点赞收藏", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_label)

        follow_icon = self.load_png_icon("add_user", height=1.5).move_to(RIGHT * 2.5 + DOWN * 0.5)
        follow_label = Text("关注", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(follow_icon, DOWN, buff=0.2)
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

        self.save_scene_thumbnail(6)
        # 结尾画面保持
        self.wait(t_trans)
