import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import SunziLessonVertical

class LessonXXVerticalScenes(SunziLessonVertical):
    """
    通用模板：孙子兵法竖屏课程
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """场景1: 痛点 (引入) - 视觉逻辑：提出问题 -> 现状展示 -> 严重后果"""
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 1. 自动化时间管理：假设有4个play动作
        step_time = (page_duration - t_trans) / 4

        # 2. 布局设计 (锁定在中间3/5)
        # 顶部标题 (y=4)
        title = Text("这里填入痛点标题", font=self.title_font, font_size=self.font_title_size * 0.9, color=YELLOW).move_to(UP * 4)
        
        # 中间核心内容 (使用 Group 包裹图片)
        center_icon = self.load_png_icon("icon_name", height=2.5).shift(UP * 0.5)
        center_text = Text("这里填入短语", font=self.body_font, font_size=self.font_body_size * 0.8, color=GRAY).next_to(center_icon, DOWN)
        center_group = Group(center_icon, center_text) # 包含图片，必须用 Group

        # 底部补充内容
        bottom_element = Text("底层逻辑/后果", font=self.title_font, font_size=self.font_title_size * 0.8, color=RED).move_to(DOWN * 3)

        # 3. 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(FadeIn(center_group, shift=UP), run_time=step_time)
        self.play(Write(bottom_element), run_time=step_time)
        self.play(Indicate(bottom_element), run_time=step_time)
        
        # 4. 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """场景2: 知识 (是什么) - 视觉逻辑：引言 -> 兵法原文(分行) -> 具象化解释"""
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 假设5个动作
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部：《孙子兵法》说 (分行展示)
        who_says = Text("《孙子兵法》说：", font=self.title_font, font_size=self.font_title_size * 0.7, color=GOLD_A).move_to(UP * 4.2)
        quote_core = Text("“这里填入兵法原句”", font=self.title_font, font_size=self.font_title_size * 0.8, color=GOLD).next_to(who_says, DOWN, buff=0.4)
        
        # 2. 中部：具象化图标
        main_icon = self.load_png_icon("icon_name", height=3).shift(UP * 0.2)
        
        # 3. 底部：解析文字
        explain_text = Text("一句话解释", font=self.title_font, font_size=self.font_title_size * 0.8, color=ORANGE).move_to(DOWN * 3.5)

        self.play(Write(who_says), run_time=step_time)
        self.play(Write(quote_core), run_time=step_time)
        self.play(FadeIn(main_icon), run_time=step_time)
        self.play(Write(explain_text), run_time=step_time)
        self.play(Circumscribe(explain_text), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """场景3: 剖析 (为什么) - 视觉逻辑：对比/因果 -> 痛点深挖"""
        # 参考 build_scene_1 的 step_time 逻辑
        pass

    def build_scene_4(self, scene):
        """场景4: 策略 (怎么做) - 视觉逻辑：行动指令 -> 三个具体方法/工具"""
        # 使用 Group 组织多个图标
        pass

    def build_scene_5(self, scene):
        """场景5: 升华 (应用) - 视觉逻辑：错误 vs 正确 -> 愿景金句"""
        # 底部使用 RoundedRectangle 制作金句框
        pass

    def get_cover_decoration_icons(self):
        """
        根据 build_scene_1 到 build_scene_5 的动画内容中用到的png图片，选择封面装饰图标，不超过5个
        例子：
        return ["brain", "book", "trophy"]
        """
        return ["brain", "book", "trophy"]