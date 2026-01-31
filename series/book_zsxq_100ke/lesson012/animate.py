import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson012VerticalScenes(Zsxq100keLessonVertical):
    """
    第012课：帝王将相一样思考
    副标题：顶层思维与独立判断
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：引发共鸣 -> 反常识观点 -> 抓住注意力
        
        口播稿关键词/短语：
        - "皇帝思维离你很远" -> 误区认知
        - "帝王将相的思考方式" -> 核心概念
        - "独立决策、全面兼顾" -> 关键能力
        - "看错人是要命的" -> 冲击力
        - "投资决策一样管用" -> 落脚点
        
        动态标题：「皇帝思维离你远？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、误区文字、皇冠图标组、反转文字、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部动态标题 (y=4.0) - 引发好奇
        title = Text(
            "皇帝思维离你远？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 误区文字 - 帝王思维与我无关
        wrong_text = Text(
            "「跟我有什么关系」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(UP * 2.5)
        wrong_cross = Cross(wrong_text, stroke_color=RED, stroke_width=4)
        
        # 3. 皇冠图标 - 帝王思维的核心象征
        # 图标来源：crown 在 icons 列表中
        crown_icon = self.load_png_icon("crown", height=2.5).move_to(UP * 0.3)
        crown_label = Text(
            "最全面最客观", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(crown_icon, DOWN, buff=0.3)
        crown_group = Group(crown_icon, crown_label)
        
        # 4. 关键洞察 - 看错人是要命的
        insight_text = Text(
            "看错人是要命的！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(DOWN * 2.5)
        
        # 5. 底部结论
        conclusion = Text(
            "投资决策一样管用", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(wrong_text), Create(wrong_cross), run_time=step_time)
        self.play(FadeIn(crown_group, scale=0.8), run_time=step_time)
        self.play(Write(insight_text), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：核心概念 -> 三个要点 -> 清晰分类
        
        口播稿关键词/短语：
        - "帝王思维有三个核心" -> 核心数字
        - "归集同类" -> 第一点
        - "历史总在重复，找类似案例" -> 解释
        - "看穿意图" -> 第二点
        - "分析每个人的环境和动机" -> 解释
        - "多角度验证" -> 第三点
        - "一件事至少三个信息源确认" -> 解释
        
        动态标题：「帝王思维三核心」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、三个核心点LaggedStart、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部：核心概念标题
        title = Text(
            "帝王思维三核心", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 三个核心要点 - 图标+文字组合
        # 第一点：归集同类 - 使用 book 图标（历史案例）
        point1_icon = self.load_png_icon("book", height=1.2).move_to(UP * 2.2 + LEFT * 2.0)
        point1_title = Text("① 归集同类", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(point1_icon, RIGHT, buff=0.3)
        point1_desc = Text("历史总在重复", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(point1_title, DOWN, buff=0.1, aligned_edge=LEFT)
        point1 = Group(point1_icon, point1_title, point1_desc)
        
        # 第二点：看穿意图 - 使用 brain 图标（分析思考）
        point2_icon = self.load_png_icon("brain", height=1.2).move_to(UP * 0.6 + LEFT * 2.0)
        point2_title = Text("② 看穿意图", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(point2_icon, RIGHT, buff=0.3)
        point2_desc = Text("分析动机环境", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(point2_title, DOWN, buff=0.1, aligned_edge=LEFT)
        point2 = Group(point2_icon, point2_title, point2_desc)
        
        # 第三点：多角度验证 - 使用 scales 图标（多方验证）
        point3_icon = self.load_png_icon("scales", height=1.2).move_to(DOWN * 1.0 + LEFT * 2.0)
        point3_title = Text("③ 多角度验证", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(point3_icon, RIGHT, buff=0.3)
        point3_desc = Text("至少三个信息源", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(point3_title, DOWN, buff=0.1, aligned_edge=LEFT)
        point3 = Group(point3_icon, point3_title, point3_desc)
        
        points = [point1, point2, point3]
        
        # 3. 底部总结
        summary = Text(
            "独立决策 全面兼顾", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)
        summary_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(summary, buff=0.4)
        summary_group = VGroup(summary_box, summary)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        # 使用 LaggedStart 逐项弹出三个核心
        self.play(
            LaggedStart(
                *[FadeIn(point, shift=RIGHT) for point in points], 
                lag_ratio=0.3
            ), 
            run_time=step_time * 2
        )
        self.play(FadeIn(summary_group, scale=0.8), run_time=step_time)
        self.play(Circumscribe(summary, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：核心洞察 -> 信息过滤 -> 独立思考
        
        口播稿关键词/短语：
        - "普通人的信息是被过滤的" -> 核心洞察
        - "商鞅说治国之道在于弱民" -> 权威引用
        - "你接收的信息可能是别人想让你看到的" -> 关键警示
        - "学会独立思考，交叉验证" -> 应对策略
        - "不被单一信源忽悠" -> 落脚点
        
        动态标题：「信息被过滤了」
        使用对比布局：被动接受 vs 独立思考
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、商鞅引用、对比展示、独立思考建议、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "你的信息被过滤了", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(UP * 4.0)
        
        # 2. 商鞅引用 - 权威背书
        quote_text = Text(
            "「治国之道在于弱民」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(UP * 2.3)
        quote_source = Text(
            "— 商鞅", 
            font=self.body_font, 
            font_size=self.font_small_size, 
            color=DARK_GRAY
        ).next_to(quote_text, DOWN, buff=0.2)
        quote_group = VGroup(quote_text, quote_source)
        
        # 3. 对比：被动接受 vs 独立思考
        # 左侧：被动接受（错误）
        left_icon = self.load_png_icon("brain", height=1.5).move_to(UP * 0.5 + LEFT * 2.5)
        left_text = Text("被动接受", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(left_icon, DOWN, buff=0.2)
        left_cross = Cross(Group(left_icon, left_text), stroke_color=RED, stroke_width=3)
        left_group = Group(left_icon, left_text, left_cross)
        
        # 右侧：独立思考（正确）
        right_icon = self.load_png_icon("idea", height=1.5).move_to(UP * 0.5 + RIGHT * 2.5)
        right_text = Text("独立思考", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(right_icon, DOWN, buff=0.2)
        right_check = Text("✓", font=self.title_font, font_size=self.font_title_size, color=GREEN).next_to(right_text, RIGHT, buff=0.2)
        right_group = Group(right_icon, right_text, right_check)
        
        # 中间 VS
        vs_text = Text("VS", font=self.title_font, font_size=self.font_body_size, color=ORANGE).move_to(UP * 0.5)
        
        # 4. 底部核心建议
        advice_text = Text(
            "交叉验证，不被单一信源忽悠", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(DOWN * 2.5)
        advice_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(advice_text, buff=0.4)
        advice_group = VGroup(advice_box, advice_text)
        
        # 5. 底部结论
        conclusion = Text(
            "独立思考是最贵的能力", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.2)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(quote_group, shift=DOWN), run_time=step_time)
        self.play(
            FadeIn(left_group, shift=RIGHT), 
            FadeIn(right_group, shift=LEFT),
            FadeIn(vs_text, scale=0.5),
            run_time=step_time
        )
        self.play(FadeIn(advice_group, scale=0.8), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：具象化场景 -> 投资决策 -> 引发认同
        
        口播稿关键词/短语：
        - "投资决策" -> 核心场景
        - "理财产品" -> 具体对象
        - "销售说的天花乱坠" -> 问题描述
        - "想想他的动机是什么" -> 思考点1
        - "类似产品历史上表现如何" -> 思考点2
        - "有没有第三方信息验证" -> 思考点3
        - "多问几个为什么，少踩很多坑" -> 结论
        
        动态标题：「投资决策必用」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、场景描述、三个思考点LaggedStart、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "投资决策必用", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 4.0)
        
        # 2. 场景描述 - 理财产品销售
        scene_desc = Text(
            "销售说得天花乱坠？", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(UP * 2.5)
        
        # 3. 三个思考点
        # 思考点1：动机分析
        think1_icon = self.load_png_icon("brain", height=1.0).move_to(UP * 1.0 + LEFT * 2.5)
        think1_text = Text("他的动机是什么？", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(think1_icon, RIGHT, buff=0.3)
        think1 = Group(think1_icon, think1_text)
        
        # 思考点2：历史表现
        think2_icon = self.load_png_icon("book", height=1.0).move_to(DOWN * 0.2 + LEFT * 2.5)
        think2_text = Text("历史表现如何？", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(think2_icon, RIGHT, buff=0.3)
        think2 = Group(think2_icon, think2_text)
        
        # 思考点3：第三方验证
        think3_icon = self.load_png_icon("scales", height=1.0).move_to(DOWN * 1.4 + LEFT * 2.5)
        think3_text = Text("有第三方验证吗？", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(think3_icon, RIGHT, buff=0.3)
        think3 = Group(think3_icon, think3_text)
        
        thinks = [think1, think2, think3]
        
        # 4. 底部结论
        conclusion = Text(
            "多问为什么，少踩坑", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)
        conclusion_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(conclusion, buff=0.4)
        conclusion_group = VGroup(conclusion_box, conclusion)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(scene_desc), run_time=step_time)
        # 使用 LaggedStart 逐项弹出思考点
        self.play(
            LaggedStart(
                *[FadeIn(t, shift=RIGHT) for t in thinks], 
                lag_ratio=0.3
            ), 
            run_time=2*step_time
        )
        self.play(FadeIn(conclusion_group, scale=0.8), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：行动步骤 -> 逐项弹出 -> 强调可执行
        
        口播稿关键词/短语：
        - "三问法" -> 核心方法
        - "历史上有没有类似的" -> 第一问
        - "对方这么说图什么" -> 第二问
        - "有没有其他信息源能验证" -> 第三问
        - "大多数忽悠就现形了" -> 效果
        - "独立思考是最贵的能力" -> 结论
        
        动态标题：「三问法」
        使用 LaggedStart 实现逐项弹出效果
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、核心口诀、三问LaggedStart、效果提示、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "记住三问法", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心口诀框
        slogan = Text(
            "三问破忽悠", 
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
        
        # 3. 三问列表
        question1 = Text("① 历史上有没有类似的？", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(UP * 0.8)
        question2 = Text("② 对方这么说图什么？", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 0.2)
        question3 = Text("③ 有其他信息源验证吗？", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 1.2)
        
        questions = [question1, question2, question3]
        
        # 4. 效果提示
        effect_text = Text(
            "忽悠立刻现形", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(DOWN * 2.5)
        
        # 5. 底部结论
        conclusion = Text(
            "独立思考是最贵的能力", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(slogan_group, scale=0.8), run_time=step_time)
        # 使用 LaggedStart 逐项弹出，lag_ratio=0.3
        self.play(
            LaggedStart(
                *[FadeIn(q, shift=RIGHT) for q in questions], 
                lag_ratio=0.3
            ), 
            run_time=step_time
        )
        self.play(Write(effect_text), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：低门槛互动 -> 强调动画 -> 引导关注
        
        口播稿关键词/短语：
        - "帝王思维是什么" -> 回顾
        - "下次做决策前，试试这个三问法" -> 互动任务
        - "点赞收藏" -> 互动号召
        - "每天一课，日日生金" -> 系列口号
        
        动态标题：「试试三问法」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、互动任务、互动图标、系列口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 核心CTA标题
        title = Text(
            "下次决策试试三问法", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 3.5)
        
        # 2. 互动任务 - 皇冠图标
        crown_icon = self.load_png_icon("crown", height=2.0).move_to(UP * 2.0)
        task_text = Text(
            "像帝王一样思考", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(crown_icon, DOWN, buff=0.3)
        task_group = Group(crown_icon, task_text)
        
        # 3. 点赞图标
        # 图标来源：like 在 all_png_names.txt
        like_icon = self.load_png_icon("like", height=1.8).move_to(LEFT * 2 + DOWN * 1.5)
        like_text = Text("点赞", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_text)
        
        # 4. 收藏图标
        # 图标来源：add_to_favorites 在 all_png_names.txt
        fav_icon = self.load_png_icon("add_to_favorites", height=1.8).move_to(RIGHT * 2 + DOWN * 1.5)
        fav_text = Text("收藏", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(fav_icon, DOWN, buff=0.2)
        fav_group = Group(fav_icon, fav_text)
        
        icons_group = Group(like_group, fav_group)
        
        # 5. 系列口号 - 金句框
        slogan_text = Text(
            "每天一课，日日生金！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.0)
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
        self.play(FadeIn(task_group, scale=0.8), Circumscribe(task_text, color=GOLD), run_time=step_time)
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
        - crown: 帝王思维的核心象征
        - brain: 独立思考、看穿意图
        - book: 归集同类、历史案例
        - scales: 多角度验证、公正判断
        - idea: 独立判断、洞察力
        """
        return ["crown", "brain", "book", "scales", "idea"]
