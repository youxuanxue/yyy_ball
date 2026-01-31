import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson005VerticalScenes(Zsxq100keLessonVertical):
    """
    第005课：房价会崩盘吗？
    副标题：为什么等房价崩了再买是个伪命题
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：引发共鸣 -> 反常识观点 -> 抓住注意力
        
        口播稿关键词/短语：
        - "等房价崩盘" -> 误区认知
        - "抄底捡漏" -> 幻想
        - "扎心的真相" -> 反转
        - "永远不会来" -> 结论
        
        动态标题：「等着抄底？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、幻想文字、房子图标、真相反转、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题 (y=4.0) - 引发好奇
        title = Text(
            "等着抄底？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 幻想文字 - 等房价崩盘
        dream_text = Text(
            "「等房价崩了再买」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(UP * 2.5)
        dream_cross = Cross(dream_text, stroke_color=RED, stroke_width=4)
        
        # 3. 中部房子图标 - 表示房产
        # 图标来源：house 在 all_png_names.txt
        house_icon = self.load_png_icon("house", height=2.5).move_to(UP * 0.3)
        
        # 4. 扎心真相
        truth_text = Text(
            "扎心真相", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(DOWN * 1.8)
        
        # 5. 底部结论 - 永远不会来
        conclusion = Text(
            "这一天可能永远不来", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(dream_text), Create(dream_cross), run_time=step_time)
        self.play(FadeIn(house_icon, scale=0.5), run_time=step_time)
        self.play(Write(truth_text), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=RED), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：核心概念 -> 对比解释 -> 清晰区分
        
        口播稿关键词/短语：
        - "专家说" -> 误区来源
        - "永远涨的东西" -> 自由市场逻辑
        - "日本房价" -> 反例
        - "大前提" -> 关键转折
        - "社会主义市场经济" -> 核心概念
        - "受管制" -> 本质区别
        
        动态标题：「市场的真相」
        使用左右对比布局：自由市场 vs 中国市场
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、专家说、对比、中国特色、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部：核心概念标题
        title = Text(
            "市场的真相", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 专家说法（被打叉）
        expert_text = Text(
            "「世界上没有永远涨的东西」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(UP * 2.5)
        
        # 3. 左右对比
        # 左侧：自由市场
        left_title = Text("自由市场", font=self.title_font, font_size=self.font_body_size, color=GRAY).move_to(UP * 0.8 + LEFT * 2.2)
        left_desc = Text("价格自由\n完全竞争", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(left_title, DOWN, buff=0.3)
        left_group = VGroup(left_title, left_desc)
        
        # 右侧：中国市场
        right_title = Text("中国市场", font=self.title_font, font_size=self.font_body_size, color=GOLD).move_to(UP * 0.8 + RIGHT * 2.2)
        right_desc = Text("价格管制\n政策调控", font=self.body_font, font_size=self.font_small_size, color=GOLD).next_to(right_title, DOWN, buff=0.3)
        right_group = VGroup(right_title, right_desc)
        
        # 中间 VS
        vs_text = Text("VS", font=self.title_font, font_size=self.font_body_size, color=RED).move_to(UP * 0.8)
        
        # 4. 核心结论
        key_point = Text(
            "房价、土地、买卖都受管制", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).move_to(DOWN * 1.8)
        key_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=BLUE, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=BLUE
        ).surround(key_point, buff=0.4)
        key_group = VGroup(key_box, key_point)
        
        # 5. 底部总结
        summary = Text(
            "大前提都不存在", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(expert_text), run_time=step_time)
        self.play(
            FadeIn(left_group, shift=RIGHT),
            FadeIn(right_group, shift=LEFT),
            FadeIn(vs_text, scale=0.5),
            run_time=step_time
        )
        self.play(FadeIn(key_group, shift=UP), run_time=step_time)
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：数据冲击 -> 连锁反应 -> 恐怖后果
        
        口播稿关键词/短语：
        - "70%的财富是房产" -> 数据1
        - "银行70%的抵押物是住宅" -> 数据2
        - "地方财政靠卖地" -> 数据3
        - "银行垮、财政崩" -> 连锁反应
        - "社会停摆" -> 恐怖后果
        
        动态标题：「房价崩了会怎样」
        使用递进式布局展示连锁反应
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、三个数据LaggedStart、连锁反应、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "房价崩了会怎样", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(UP * 4.0)
        
        # 2. 三个关键数据
        # 数据1：财富
        data1_icon = self.load_png_icon("money", height=1.0).move_to(UP * 2.2 + LEFT * 3.5)
        data1_text = Text("70%财富是房产", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(data1_icon, RIGHT, buff=0.3)
        data1 = Group(data1_icon, data1_text)
        
        # 数据2：银行抵押
        data2_icon = self.load_png_icon("bank", height=1.0).move_to(UP * 0.8 + LEFT * 3.5)
        data2_text = Text("70%抵押物是住宅", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(data2_icon, RIGHT, buff=0.3)
        data2 = Group(data2_icon, data2_text)
        
        # 数据3：财政
        data3_icon = self.load_png_icon("building", height=1.0).move_to(DOWN * 0.6 + LEFT * 3.5)
        data3_text = Text("地方财政靠卖地", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(data3_icon, RIGHT, buff=0.3)
        data3 = Group(data3_icon, data3_text)
        
        data_items = [data1, data2, data3]
        
        # 3. 连锁反应
        chain_text = Text(
            "银行垮 → 财政崩 → 社会停摆", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(DOWN * 2.2)
        
        # 4. 底部结论
        conclusion = Text(
            "谁也承受不起这个后果", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        # 使用 LaggedStart 逐项弹出数据
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT) for item in data_items], 
                lag_ratio=0.4
            ), 
            run_time=2*step_time
        )
        self.play(Write(chain_text), Circumscribe(chain_text, color=RED), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：具象化场景 -> 对号入座 -> 引发认同
        
        口播稿关键词/短语：
        - "正在观望" -> 人群1
        - "等着房价腰斩" -> 幻想
        - "刚买了房" -> 人群2
        - "担心资产缩水" -> 焦虑
        - "定心丸" -> 解药
        - "崩盘的前提条件根本不存在" -> 核心观点
        
        动态标题：「这课说给谁听」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、人群1、人群2、定心丸、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "这课说给谁听", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 4.0)
        
        # 2. 人群1：观望等腰斩
        group1_icon = self.load_png_icon("anxious", height=1.5).move_to(UP * 2.0 + LEFT * 2.5)
        group1_text = Text("正在观望\n等腰斩再买", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(group1_icon, RIGHT, buff=0.4)
        group1 = Group(group1_icon, group1_text)
        
        # 3. 人群2：刚买房担心缩水
        group2_icon = self.load_png_icon("house", height=1.5).move_to(DOWN * 0.2 + LEFT * 2.5)
        group2_text = Text("刚买了房\n担心资产缩水", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(group2_icon, RIGHT, buff=0.4)
        group2 = Group(group2_icon, group2_text)
        
        # 4. 定心丸
        pill_text = Text(
            "给你吃颗定心丸", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).move_to(DOWN * 2.2)
        pill_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GREEN, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GREEN
        ).surround(pill_text, buff=0.4)
        pill_group = VGroup(pill_box, pill_text)
        
        # 5. 底部结论
        conclusion = Text(
            "崩盘前提根本不存在", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(group1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(group2, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(pill_group, scale=0.8), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：终极大招 -> 历史教训 -> 核心逻辑
        
        口播稿关键词/短语：
        - "央行印钞买房" -> 终极大招
        - "充当最终买家" -> 机制
        - "美联储已经这么干了" -> 案例
        - "日本和香港的教训" -> 历史
        - "绝对不能让它崩盘" -> 核心逻辑
        
        动态标题：「政府的底牌」
        使用 LaggedStart 实现逐项弹出效果
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、终极大招、案例、教训、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "政府的底牌", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 终极大招 - 金句框
        trick_text = Text(
            "逼到份上，央行印钞买房", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(UP * 2.2)
        trick_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(trick_text, buff=0.4)
        trick_group = VGroup(trick_box, trick_text)
        
        # 3. 案例和教训
        case1 = Text("✓ 美联储已经这么干了", font=self.body_font, font_size=self.font_body_size, color=BLUE).move_to(UP * 0.5)
        case2 = Text("✗ 日本90年代：主动刺破，惨痛教训", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(DOWN * 0.5)
        case3 = Text("✗ 香港98年：金融危机，刻骨铭心", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(DOWN * 1.5)
        
        cases = [case1, case2, case3]
        
        # 4. 底部结论
        conclusion = Text(
            "绝对不能让房价崩盘", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(trick_group, scale=0.8), Circumscribe(trick_text, color=GOLD), run_time=step_time)
        # 使用 LaggedStart 逐项弹出，lag_ratio=0.3
        self.play(
            LaggedStart(
                *[FadeIn(case, shift=RIGHT) for case in cases], 
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
        - "有道理" -> 认同
        - "点个赞" -> 互动1
        - "关注我" -> 互动2
        - "转发给他" -> 互动3
        - "等着房价崩的朋友" -> 传播对象
        
        动态标题：「动动手指」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、互动图标、转发提示、系列口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 核心CTA标题
        title = Text(
            "觉得有道理？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 3.5)
        
        # 2. 点赞图标
        # 图标来源：like 在 all_png_names.txt
        like_icon = self.load_png_icon("like", height=2.0).move_to(LEFT * 2 + UP * 0.8)
        like_text = Text("点赞", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_text)
        
        # 3. 关注图标
        # 图标来源：add_user 在 all_png_names.txt
        follow_icon = self.load_png_icon("add_user", height=2.0).move_to(RIGHT * 2 + UP * 0.8)
        follow_text = Text("关注", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(follow_icon, DOWN, buff=0.2)
        follow_group = Group(follow_icon, follow_text)
        
        icons_group = Group(like_group, follow_group)
        
        # 4. 转发提示
        share_text = Text(
            "转发给等房价崩的朋友", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(DOWN * 1.5)
        
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
        self.play(FadeIn(icons_group, shift=UP), run_time=step_time)
        self.play(Write(share_text), run_time=step_time)
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
        - house: 房产核心概念
        - bank: 银行抵押物
        - money: 财富
        - real_estate: 房地产
        - coins: 金融资产
        """
        return ["house", "bank", "money", "real_estate", "coins"]
