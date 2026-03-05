import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson024VerticalScenes(Zsxq100keLessonVertical):
    """
    第024课：战略性房产投资
    主题：逻辑已变，下一个洼地在哪儿
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入)

        口播稿：买房最让人头疼的是什么？缺钱。看得上的地方买不起，买得起的区域又不确定能不能涨。
                但你知道吗？房价上涨的底层逻辑已经变了。
                上一轮叫城市化红利，这一轮叫经济治理溢价。搞懂这个，你就知道下一个洼地在哪儿。

        关键词/短语：
        - "买房头疼/缺钱" -> house 图标，灰色焦虑
        - "底层逻辑已变" -> 红色关键转折
        - "经济治理溢价" -> 金色核心概念

        动态标题：「买房的逻辑变了！」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题
        title = Text(
            "买房的逻辑变了！",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GRAY
        ).move_to(UP * 4.0)

        # 2. 房子图标 + 焦虑感
        house_icon = self.load_png_icon("house", height=2.0).move_to(UP * 1.5)
        pain_text = Text(
            "看得上的买不起，买得起的不确定",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).next_to(house_icon, DOWN, buff=0.3)
        house_group = Group(house_icon, pain_text)

        # 3. 逻辑转变：城市化红利 -> 经济治理溢价
        old_logic = Text(
            "上一轮：城市化红利",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GRAY
        ).shift(DOWN * 0.5 + LEFT * 0.5)
        new_logic = Text(
            "这一轮：经济治理溢价",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).next_to(old_logic, DOWN, buff=0.3)

        # 4. 底部悬念
        hook = Text(
            "搞懂它，找到下一个洼地",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(house_group, shift=UP), run_time=step_time)
        self.play(Write(old_logic), Write(new_logic), run_time=step_time)
        self.play(Write(hook), run_time=step_time)
        self.play(Circumscribe(hook, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What)

        口播稿：城市扩容有三种方式。第一种，本地划出一个重点打造的新区。
                第二种，周围的卫星城被划进来，撤市设区，变成都市圈的一部分。
                第三种，扩权，市县区一级获得更大的行政和经济管理权限。
                这三种方式，决定了哪些区域的房价会起飞。

        关键词/短语：
        - "三种方式" -> 逐项展示
        - "新区/撤市设区/扩权" -> 蓝色知识色调
        - "房价起飞" -> 金色

        动态标题：「城市扩容三种方式」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "城市扩容三种方式",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三种扩容方式
        way1_icon = self.load_png_icon("building", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        way1_text = Text(
            "①划出重点新区",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(way1_icon, RIGHT, buff=0.3)
        way1 = Group(way1_icon, way1_text)

        way2_icon = self.load_png_icon("globe", height=0.8).shift(LEFT * 3.0 + UP * 0.5)
        way2_text = Text(
            "②撤市设区，并入都市圈",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(way2_icon, RIGHT, buff=0.3)
        way2 = Group(way2_icon, way2_text)

        way3_icon = self.load_png_icon("management", height=0.8).shift(LEFT * 3.0 + DOWN * 1.0)
        way3_text = Text(
            "③扩权，提升管理权限",
            font=self.body_font,
            font_size=self.font_body_size,
            color=BLUE
        ).next_to(way3_icon, RIGHT, buff=0.3)
        way3 = Group(way3_icon, way3_text)

        ways = [way1, way2, way3]

        # 3. 底部结论
        conclusion = Text(
            "扩容方式决定房价起飞区域",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(w, shift=RIGHT) for w in ways], lag_ratio=0.3),
            run_time=2 * step_time
        )
        self.play(Write(conclusion), run_time=step_time)
        self.play(Circumscribe(conclusion, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why)

        口播稿：核心逻辑是什么？真正有潜力的区域，不是本级领导说了算的，
                而是省级甚至国家一级有更高规划的地方。
                说白了就是好地方要让治理能力强的人来管。
                就像深圳为核心的大深圳统筹合作示范区，
                把优质资源集中给最能干的团队，这才是房价上涨的真正推手。

        关键词/短语：
        - "省级/国家级规划" -> 层级关系
        - "大深圳示范区" -> 具体案例
        - "房价上涨的真正推手" -> 金色强调

        动态标题：「谁决定了房价涨不涨」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "谁决定了房价涨不涨",
            font=self.title_font,
            font_size=self.font_title_size,
            color=BLUE
        ).move_to(UP * 4.0)

        # 2. 核心观点
        core = Text(
            "更高层级的规划 = 真正的推手",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).move_to(UP * 2.5)

        # 3. 层级递进 - 从本级到国家级
        local = Text("本级领导", font=self.body_font, font_size=self.font_body_size, color=GRAY).shift(LEFT * 2.5 + UP * 0.5)
        arrow1 = Text("→", font=self.title_font, font_size=self.font_title_size, color=WHITE).shift(UP * 0.5)
        province = Text("省级规划", font=self.body_font, font_size=self.font_body_size, color=BLUE).shift(RIGHT * 2.5 + UP * 0.5)

        # 4. 案例 - 大深圳
        case_icon = self.load_png_icon("real_estate", height=1.2).shift(DOWN * 0.8)
        case_text = Text(
            "大深圳统筹合作示范区",
            font=self.body_font,
            font_size=self.font_body_size,
            color=GOLD
        ).next_to(case_icon, DOWN, buff=0.2)
        case_group = Group(case_icon, case_text)

        # 5. 底部结论
        conclusion = Text(
            "优质资源给最能干的团队",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(core), run_time=step_time)
        self.play(FadeIn(local), Write(arrow1), FadeIn(province), run_time=step_time)
        self.play(FadeIn(case_group, shift=UP), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When)

        口播稿：什么地方值得重点关注？三个关键词：扩容区域的节点位置、枢纽位置、核心关键地段。
                不是所有扩容区都会涨，要涨的是承担连接和聚集功能的点位。
                比如交通枢纽、产业聚集区、行政中心周边。

        关键词/短语：
        - "节点/枢纽/核心" -> 三个关键词
        - "交通枢纽" -> transportation 图标
        - "产业聚集区" -> business_building 图标

        动态标题：「三个关键词锁定洼地」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "三个关键词锁定洼地",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 三个关键位置
        node_icon = self.load_png_icon("pin", height=0.8).shift(LEFT * 3.0 + UP * 2.0)
        node_text = Text("①节点位置", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(node_icon, RIGHT, buff=0.3)
        node_sub = Text("交通枢纽站点", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(node_text, DOWN, buff=0.1).align_to(node_text, LEFT)
        node = Group(node_icon, node_text, node_sub)

        hub_icon = self.load_png_icon("network", height=0.8).shift(LEFT * 3.0 + UP * 0.3)
        hub_text = Text("②枢纽位置", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(hub_icon, RIGHT, buff=0.3)
        hub_sub = Text("产业聚集区", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(hub_text, DOWN, buff=0.1).align_to(hub_text, LEFT)
        hub = Group(hub_icon, hub_text, hub_sub)

        core_icon = self.load_png_icon("target", height=0.8).shift(LEFT * 3.0 + DOWN * 1.4)
        core_text = Text("③核心关键地段", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(core_icon, RIGHT, buff=0.3)
        core_sub = Text("行政中心周边", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(core_text, DOWN, buff=0.1).align_to(core_text, LEFT)
        core = Group(core_icon, core_text, core_sub)

        items = [node, hub, core]

        # 3. 底部结论
        conclusion = Text(
            "连接和聚集功能的点位才会涨",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(item, shift=RIGHT) for item in items], lag_ratio=0.3),
            run_time=step_time
        )
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        self.wait(step_time)

        self.save_scene_thumbnail(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How)

        口播稿：怎么判断？
                第一，关注国家级和省级的城市规划文件，看哪些区域被点名了。
                第二，看交通基建规划，地铁高铁通到哪，钱就流到哪。
                第三，看产业布局，有龙头企业入驻的片区潜力更大。
                第四，别追高，买在规划发布但还没大规模动工的阶段，性价比最高。

        关键词/短语：
        - "规划文件/基建/产业/别追高" -> 四步策略

        动态标题：「四招判断房产洼地」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：6个动作
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text(
            "四招判断房产洼地",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(UP * 4.0)

        # 2. 四步策略
        s1_icon = self.load_png_icon("document", height=0.8).shift(LEFT * 3.0 + UP * 2.2)
        s1_text = Text("①看城市规划文件", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(s1_icon, RIGHT, buff=0.3)
        s1 = Group(s1_icon, s1_text)

        s2_icon = self.load_png_icon("transportation", height=0.8).shift(LEFT * 3.0 + UP * 0.9)
        s2_text = Text("②看交通基建规划", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(s2_icon, RIGHT, buff=0.3)
        s2 = Group(s2_icon, s2_text)

        s3_icon = self.load_png_icon("business", height=0.8).shift(LEFT * 3.0 + DOWN * 0.4)
        s3_text = Text("③看产业布局", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(s3_icon, RIGHT, buff=0.3)
        s3 = Group(s3_icon, s3_text)

        s4_icon = self.load_png_icon("calendar", height=0.8).shift(LEFT * 3.0 + DOWN * 1.7)
        s4_text = Text("④别追高，买在规划阶段", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(s4_icon, RIGHT, buff=0.3)
        s4 = Group(s4_icon, s4_text)

        steps = [s1, s2, s3, s4]

        # 3. 底部金句
        summary = Text(
            "规划发布还没动工，性价比最高",
            font=self.title_font,
            font_size=self.font_title_size,
            color=GOLD
        ).move_to(DOWN * 3.5)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(s1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(s2, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(s3, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(s4, shift=RIGHT), run_time=step_time)
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.save_scene_thumbnail(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action)

        口播稿：房产投资的逻辑已经变了，别再用老思路买房。
                关注我，带你看清每一轮财富机会的底层密码。

        动态标题：「别用老思路买房」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        # 时间管理：4个动作
        step_time = (page_duration - t_trans) / 4

        # 1. 顶部标题
        title = Text(
            "别用老思路买房",
            font=self.title_font,
            font_size=self.font_title_size,
            color=ORANGE
        ).move_to(UP * 4.0)

        # 2. 核心收获
        takeaway = Text(
            "看清每一轮财富机会的底层密码",
            font=self.body_font,
            font_size=self.font_body_size,
            color=WHITE
        ).move_to(UP * 2.0)
        takeaway_box = RoundedRectangle(height=1.0, corner_radius=0.2, color=GOLD, fill_opacity=0.1)
        takeaway_box.surround(takeaway, buff=0.3)
        takeaway_group = VGroup(takeaway_box, takeaway)

        # 3. 互动图标
        like_icon = self.load_png_icon("thumbs_up", height=1.5).move_to(LEFT * 2.5 + DOWN * 0.5)
        like_label = Text("点赞", font=self.body_font, font_size=self.font_small_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
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
