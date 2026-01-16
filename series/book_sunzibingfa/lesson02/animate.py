import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate.sunzi_lesson_vertical import SunziLessonVertical


class Lesson02VerticalScenes(SunziLessonVertical):
    """
    第2课：胜利大模型
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点 (引入) - 视觉逻辑：提出问题 -> 现状展示 -> 严重后果
        
        口播稿关键词/短语：
        - "努力" -> work_in_bed 图标表现努力
        - "考试没考好/比赛输了/竞选票数不够" -> fail 图标 + 灰色调
        - "为什么有的人总能赢" -> winner 图标 + 金色
        - "秘密" -> idea 图标表现悬念
        
        动态标题：「明明很努力，为什么还是输？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、努力图标、三个失败场景、赢家悬念）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题 (y=4.0) - 从口播「明明很努力」「还是输了」提取
        title = Text(
            "明明很努力，为什么还是输？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=YELLOW
        ).move_to(UP * 4.0)
        
        # 2. 中部核心内容 - 展示努力但失败的场景
        # 图标 work_in_bed 存在于 all_png_names.txt
        effort_icon = self.load_png_icon("work_in_bed", height=2.0).shift(UP * 1.5)
        effort_text = Text("拼命努力", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(effort_icon, DOWN, buff=0.3)
        effort_group = Group(effort_icon, effort_text)
        
        # 3. 三个失败场景（使用 fail 图标 + 文字描述）
        # 图标 fail, exam 存在于 all_png_names.txt
        fail_icon = self.load_png_icon("fail", height=1.2)
        
        # 左侧：考试
        exam_text = Text("考试没考好", font=self.body_font, font_size=self.font_small_size, color=GRAY)
        exam_group = Group(fail_icon.copy(), exam_text).arrange(DOWN, buff=0.2).move_to(LEFT * 2.5 + DOWN * 1.5)
        
        # 中间：比赛
        race_text = Text("比赛输了", font=self.body_font, font_size=self.font_small_size, color=GRAY)
        race_group = Group(fail_icon.copy(), race_text).arrange(DOWN, buff=0.2).move_to(DOWN * 1.5)
        
        # 右侧：竞选
        vote_text = Text("竞选落选", font=self.body_font, font_size=self.font_small_size, color=GRAY)
        vote_group = Group(fail_icon.copy(), vote_text).arrange(DOWN, buff=0.2).move_to(RIGHT * 2.5 + DOWN * 1.5)
        
        fail_scenes = Group(exam_group, race_group, vote_group)
        
        # 4. 底部悬念 - 「为什么有的人总能赢？」
        # 图标 winner 存在于 all_png_names.txt
        winner_icon = self.load_png_icon("winner", height=1.5).move_to(DOWN * 4.0 + LEFT * 3)
        secret_text = Text("为什么有的人总能赢？", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(winner_icon, RIGHT)
        bottom_group = Group(winner_icon, secret_text)

        # 5. 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(effort_group, shift=UP), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(exam_group, shift=UP),
                FadeIn(race_group, shift=UP),
                FadeIn(vote_group, shift=UP),
                lag_ratio=0.3
            ), 
            run_time=step_time
        )
        # 努力图标变灰，表示努力白费
        self.play(effort_icon.animate.set_opacity(0.3), run_time=step_time)
        self.play(FadeIn(winner_icon, shift=RIGHT), Write(secret_text), run_time=step_time)
        self.play(Indicate(secret_text, color=GOLD), run_time=step_time)
        
        # 6. 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识 (是什么) - 视觉逻辑：引言 -> 兵法原文(分行) -> 具象化解释
        
        口播稿关键词/短语：
        - "两千多年前" -> 历史感
        - "经之以五事，校之以计" -> 兵法原文，金色强调
        - "道、天、地、将、法" -> 五个核心概念
        - "检查五件大事" -> checklist 图标
        
        动态标题：「孙武的胜利公式」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、兵法引言、原文两行、五事展示、总结）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部：孙武的胜利公式
        title = Text(
            "孙武的胜利公式", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.2)

        # 2. 兵法原文（分行展示，使用「」避免语法错误）
        who_says = Text(
            "《孙子兵法》说：", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD_A
        ).next_to(title, DOWN, buff=0.5)
        
        quote_line1 = Text(
            "「经之以五事，校之以计，而索其情」", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).next_to(who_says, DOWN, buff=0.3)
        
        quote_line2 = Text(
            "「一曰道，二曰天，三曰地，四曰将，五曰法」", 
            font=self.title_font, 
            font_size=self.font_small_size, 
            color=GOLD
        ).next_to(quote_line1, DOWN, buff=0.2)
        
        # 3. 中部图标 - checklist 表示检查清单
        # 图标 checklist 存在于 all_png_names.txt
        checklist_icon = self.load_png_icon("checklist", height=2.5).move_to(DOWN * 0.8)
        
        # 4. 底部：五事文字展示
        five_items = Text(
            "道 · 天 · 地 · 将 · 法", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(DOWN * 3.0)
        
        explain_text = Text(
            "想要赢，先检查五件大事！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(who_says), run_time=step_time)
        self.play(Write(quote_line1), run_time=step_time)
        self.play(Write(quote_line2), run_time=step_time)
        self.play(FadeIn(checklist_icon, shift=UP), Write(five_items), run_time=step_time)
        self.play(Write(explain_text), Circumscribe(five_items, color=ORANGE), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析 (为什么) - 视觉逻辑：对比 -> 清单思维
        
        口播稿关键词/短语：
        - "出门前检查清单" -> to_do_list 图标
        - "丢三落四" -> 混乱/灰色
        - "高手做事之前" -> 有序/金色
        - "赢家不是靠运气，是靠准备" -> 核心金句
        
        动态标题：「赢家靠的不是运气」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、左侧失败者、右侧成功者、对比强调、底部金句、金句强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text(
            "赢家靠的不是运气", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=YELLOW
        ).move_to(UP * 4.0)
        
        # 2. 左右对比布局
        # 左侧：没有清单的人（丢三落四）
        # 使用几何形状表示混乱状态（没有专门的"混乱"图标）
        left_icon = self.load_png_icon("question_mark", height=1.8)
        left_label = Text("没有清单", font=self.body_font, font_size=self.font_body_size, color=GRAY)
        left_desc = Text("丢三落四", font=self.body_font, font_size=self.font_small_size, color=RED)
        left_group = Group(left_icon, left_label, left_desc).arrange(DOWN, buff=0.3).move_to(LEFT * 2.0 + UP * 1.0)
        
        # 右侧：有清单的高手
        # 图标 to_do_list 存在于 all_png_names.txt
        right_icon = self.load_png_icon("to_do_list", height=1.8)
        right_label = Text("使用清单", font=self.body_font, font_size=self.font_body_size, color=GOLD)
        right_desc = Text("准备充分", font=self.body_font, font_size=self.font_small_size, color=GREEN)
        right_group = Group(right_icon, right_label, right_desc).arrange(DOWN, buff=0.3).move_to(RIGHT * 2.0 + UP * 1.0)
        
        # 3. 中间 VS 标志
        vs_text = Text("VS", font=self.title_font, font_size=self.font_title_size, color=WHITE).move_to(UP * 1.0)
        
        # 4. 底部金句框
        quote_text = Text(
            "赢家不是靠运气，是靠准备！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)
        
        quote_bg = RoundedRectangle(
            height=1.2,
            corner_radius=0.2, 
            color=GOLD, 
            fill_opacity=0.15
        ).surround(quote_text, buff=0.2)
        
        quote_group = VGroup(quote_bg, quote_text)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(left_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(vs_text), FadeIn(right_group, shift=LEFT), run_time=step_time)
        # 强调对比：左侧变暗，右侧发光
        self.play(
            left_group.animate.set_opacity(0.5),
            Indicate(right_group, color=GOLD),
            run_time=step_time
        )
        self.play(FadeIn(quote_group, shift=UP), run_time=step_time)
        self.play(Circumscribe(quote_text, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 策略 (怎么做) - 视觉逻辑：行动指令 -> 逐项弹出
        
        口播稿关键词/短语：
        - "五项" -> 五个检查项
        - "道：做的事对不对" -> compass 图标（方向）
        - "天：时机好不好" -> sun/clock 图标（时机）
        - "地：环境合不合适" -> earth_globe 图标（环境）
        - "将：能力够不够" -> person 图标（人）
        - "法：计划好不好" -> planner 图标（计划）
        
        动态标题：「成功清单五项检查」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：7个动作（标题、五个检查项逐一弹出、总结强调）
        step_time = (page_duration - t_trans) / 7

        # 1. 顶部标题
        title = Text(
            "成功清单五项检查", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.2)
        
        # 2. 五项检查内容（使用图标 + 文字）
        # 所有图标已在 all_png_names.txt 中确认存在
        items_data = [
            ("compass", "道", "做的事对不对？", BLUE),
            ("sun", "天", "时机好不好？", ORANGE),
            ("earth_globe", "地", "环境合不合适？", GREEN),
            ("person", "将", "能力够不够？", PURPLE),
            ("planner", "法", "计划好不好？", RED),
        ]
        
        items = []
        start_y = 2.5
        for i, (icon_name, label, desc, color) in enumerate(items_data):
            icon = self.load_png_icon(icon_name, height=1.0)
            label_text = Text(label, font=self.title_font, font_size=self.font_title_size, color=color)
            desc_text = Text(desc, font=self.body_font, font_size=self.font_body_size, color=WHITE)
            
            item_group = Group(icon, label_text, desc_text).arrange(RIGHT, buff=0.3)
            item_group.move_to(UP * (start_y - i * 1.3))
            items.append(item_group)
        
        # 3. 底部总结
        summary = Text(
            "做事之前，先过一遍清单！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        
        # 逐项弹出五个检查项
        for item in items:
            self.play(FadeIn(item, shift=RIGHT), run_time=step_time)
        
        # 总结强调
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 升华 (应用) - 视觉逻辑：愿景金句
        
        口播稿关键词/短语：
        - "成功不是天才的专利" -> 打破误解
        - "有准备的人的奖励" -> winner/medal 图标
        - "考试、比赛、交朋友" -> 多场景应用
        - "总能赢的人" -> 终极愿景
        
        动态标题：「成为总能赢的人」
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、错误观念、正确观念、应用场景、金句、强调）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text(
            "成为总能赢的人", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.2)
        
        # 2. 上方：打破误解
        wrong_text = Text(
            "成功不是天才的专利", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(UP * 2.5)
        
        # 划掉线（表示否定）
        cross_line = Line(
            wrong_text.get_left() + LEFT * 0.2,
            wrong_text.get_right() + RIGHT * 0.2,
            color=RED,
            stroke_width=4
        )
        
        # 3. 中部：正确观念 + 图标
        # 图标 gold_medal 存在于 all_png_names.txt
        medal_icon = self.load_png_icon("gold_medal", height=2.0).move_to(UP * 0.5)
        
        right_text = Text(
            "是有准备的人的奖励！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).next_to(medal_icon, DOWN, buff=0.5)
        
        # 4. 应用场景
        scenes_text = Text(
            "考试 · 比赛 · 交朋友", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=WHITE
        ).move_to(DOWN * 2.0)
        
        # 5. 底部金句框
        quote_text = Text(
            "用好成功清单，你也能成为赢家！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)
        
        quote_bg = RoundedRectangle(
            height=1.2,
            corner_radius=0.2, 
            color=GOLD, 
            fill_opacity=0.2
        ).surround(quote_text, buff=0.2)
        
        quote_group = VGroup(quote_bg, quote_text)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(wrong_text), run_time=step_time)
        self.play(
            Create(cross_line),
            FadeIn(medal_icon, shift=UP),
            Write(right_text),
            run_time=step_time
        )
        self.play(Write(scenes_text), run_time=step_time)
        self.play(FadeIn(quote_group, shift=UP), run_time=step_time)
        self.play(Indicate(quote_text, color=GOLD, scale_factor=1.1), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def get_cover_decoration_icons(self):
        """
        根据 build_scene_1 到 build_scene_5 的动画内容中用到的 png 图片，
        选择封面装饰图标，不超过5个。
        所有图标名称已在 all_png_names.txt 中确认存在：
        - checklist: 核心概念（成功清单）
        - winner: 胜利主题
        - compass: 道（方向）
        - gold_medal: 奖励/成功
        - to_do_list: 清单思维
        """
        return ["checklist", "winner", "compass", "gold_medal", "to_do_list"]
