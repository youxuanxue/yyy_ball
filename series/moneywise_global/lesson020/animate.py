import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson020VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 20: The Wealth Formula Banks Use
    Assets Minus Liabilities Equals Your True Position
    """

    def build_scene_1(self, scene_data):
        """
        Scene 1: Hook / Pain Point
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "The Document\nBanks Trust Most"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size, 
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Bank building
        bank_icon = self.load_png_icon("bank_building", height=2.0).move_to(LEFT * 2.5 + UP * 1.0)
        
        # Balance sheet document
        doc_icon = self.load_png_icon("document", height=2.2).move_to(RIGHT * 2.0 + UP * 1.0)
        doc_label = Text("BALANCE\nSHEET", font_size=24, color=GOLD, weight=BOLD, 
                        line_spacing=1.1).move_to(doc_icon)
        
        # Simple preview
        preview = VGroup(
            Text("Assets | Liabilities", font_size=22, color=WHITE),
            Text("───────────────", font_size=18, color=LIGHT_GRAY),
            Text("The Difference = Truth", font_size=20, color=GREEN)
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 1.8)
        
        # Question
        question = Text("What if you applied this\nto YOUR finances?", 
                       font_size=30, color=GOLD, weight=BOLD, line_spacing=1.2).move_to(DOWN * 4.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            FadeIn(bank_icon, shift=RIGHT),
            run_time=step_time
        )
        self.play(
            FadeIn(doc_icon, scale=0.8),
            Write(doc_label),
            run_time=step_time
        )
        self.play(Write(preview), run_time=step_time)
        self.play(Write(question), run_time=step_time)
        self.wait(step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "The Wealth\nEquation"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Assets side
        assets_header = Text("ASSETS", font_size=28, color=GREEN, weight=BOLD)
        assets_items = VGroup(
            Text("💵 Cash", font_size=20, color=WHITE),
            Text("📈 Investments", font_size=20, color=WHITE),
            Text("🏠 Property", font_size=20, color=WHITE),
            Text("🚗 Vehicles", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        assets_group = VGroup(assets_header, assets_items).arrange(DOWN, buff=0.3)
        assets_box = SurroundingRectangle(assets_group, color=GREEN, buff=0.3, stroke_width=2)
        assets_section = Group(assets_box, assets_group).move_to(LEFT * 2.8 + UP * 0.8)
        
        # Minus sign
        minus = Text("−", font_size=60, color=WHITE, weight=BOLD).move_to(ORIGIN + UP * 0.8)
        
        # Liabilities side
        liab_header = Text("LIABILITIES", font_size=28, color=RED, weight=BOLD)
        liab_items = VGroup(
            Text("🏦 Mortgages", font_size=20, color=WHITE),
            Text("🚙 Car loans", font_size=20, color=WHITE),
            Text("💳 Credit cards", font_size=20, color=WHITE),
            Text("🎓 Student debt", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        liab_group = VGroup(liab_header, liab_items).arrange(DOWN, buff=0.3)
        liab_box = SurroundingRectangle(liab_group, color=RED, buff=0.3, stroke_width=2)
        liab_section = Group(liab_box, liab_group).move_to(RIGHT * 2.8 + UP * 0.8)
        
        # Result
        equals_line = Line(LEFT * 4, RIGHT * 4, color=GOLD, stroke_width=3).move_to(DOWN * 2.0)
        result = Text("= NET WORTH", font_size=36, color=GOLD, weight=BOLD).move_to(DOWN * 2.8)
        
        outcome = VGroup(
            Text("Positive = Wealth", font_size=24, color=GREEN),
            Text("Negative = Work to do", font_size=24, color=ORANGE)
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 4.2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(assets_section, shift=RIGHT), run_time=step_time)
        self.play(GrowFromCenter(minus), run_time=step_time * 0.5)
        self.play(FadeIn(liab_section, shift=LEFT), run_time=step_time)
        self.play(
            Create(equals_line),
            Write(result),
            run_time=step_time
        )
        self.play(Write(outcome), run_time=step_time)
        self.wait(step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "Why Tracking\nTransforms Results"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Trend visual - up and down
        chart_icon = self.load_png_icon("line_chart", height=2.0).move_to(UP * 1.5)
        
        # Benefits
        benefits = [
            ("Assets Growing ↑", GREEN, "Motivated to continue"),
            ("Liabilities Shrinking ↓", BLUE, "Progress visible"),
            ("Catch Problems Early", ORANGE, "Fix before crisis")
        ]
        
        benefit_items = []
        for main, color, sub in benefits:
            main_text = Text(main, font_size=26, color=color, weight=BOLD)
            sub_text = Text(sub, font_size=20, color=WHITE)
            item = VGroup(main_text, sub_text).arrange(DOWN, buff=0.1)
            benefit_items.append(item)
        
        benefit_items[0].move_to(DOWN * 0.5)
        benefit_items[1].move_to(DOWN * 1.8)
        benefit_items[2].move_to(DOWN * 3.1)
        
        # Key insight
        insight = Text("One calculation.\nMonthly clarity.", 
                      font_size=28, color=GOLD, weight=BOLD, line_spacing=1.2).move_to(DOWN * 4.5)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(chart_icon, scale=0.8), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(benefit_items[0], shift=RIGHT),
                FadeIn(benefit_items[1], shift=RIGHT),
                FadeIn(benefit_items[2], shift=RIGHT),
                lag_ratio=0.4
            ),
            run_time=step_time * 2
        )
        self.play(Write(insight), run_time=step_time)
        self.wait(step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "From Students\nto the Wealthy"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Life stages
        stages = [
            ("Students", "Set baseline", "student"),
            ("Professionals", "Track progress", "businessman"),
            ("Pre-Retirees", "Ensure on target", "elderly"),
            ("Wealthy", "Manage portfolios", "money_bag")
        ]
        
        stage_items = []
        for label, purpose, icon_name in stages:
            icon = self.load_png_icon(icon_name, height=1.0)
            main_text = Text(label, font_size=24, color=WHITE, weight=BOLD)
            sub_text = Text(purpose, font_size=18, color=LIGHT_GRAY)
            text_group = VGroup(main_text, sub_text).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            item = Group(icon, text_group).arrange(RIGHT, buff=0.4)
            stage_items.append(item)
        
        stage_items[0].move_to(UP * 1.8)
        stage_items[1].move_to(UP * 0.4)
        stage_items[2].move_to(DOWN * 1.0)
        stage_items[3].move_to(DOWN * 2.4)
        
        # Universal message
        message = Text("One formula.\nUniversal application.", 
                      font_size=28, color=GOLD, weight=BOLD, line_spacing=1.2).move_to(DOWN * 4.2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT) for item in stage_items],
                lag_ratio=0.3
            ),
            run_time=step_time * 2
        )
        self.play(Write(message), run_time=step_time)
        self.wait(step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 8
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "Four Steps to Your\nBalance Sheet"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        steps = [
            ("1", "List every asset\n& current value", GREEN, "plus"),
            ("2", "List every liability\n& balance owed", RED, "minus"),
            ("3", "Calculate the\ndifference", BLUE, "calculator"),
            ("4", "Update monthly\n& watch trend", PURPLE, "calendar")
        ]
        
        step_items = []
        for num, text, color, icon_name in steps:
            num_box = Square(side_length=0.6, color=color, stroke_width=3, fill_opacity=0.2)
            num_text = Text(num, font_size=28, color=color, weight=BOLD).move_to(num_box)
            icon = self.load_png_icon(icon_name, height=0.7)
            step_text = Text(text, font_size=20, color=WHITE, line_spacing=1.1)
            
            item = Group(num_box, num_text, icon, step_text).arrange(RIGHT, buff=0.25)
            step_items.append((item, num_box, color))
        
        positions = [UP * 1.8, UP * 0.3, DOWN * 1.2, DOWN * 2.7]
        for i, (item, _, _) in enumerate(step_items):
            item.move_to(positions[i])
        
        footer = Text("Growing assets +\nShrinking liabilities\n= WINNING", 
                     font_size=26, color=GOLD, weight=BOLD, line_spacing=1.2).move_to(DOWN * 4.5)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        
        for item, box, color in step_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=step_time)
        
        self.play(
            *[box.animate.set_fill(color, opacity=0.4) for _, box, color in step_items],
            run_time=step_time
        )
        self.play(Write(footer), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        title = Text("Know Your Number", font=self.title_font, 
                    font_size=self.font_title_size, color=GOLD, line_spacing=1.1).move_to(UP * 3.5)
        
        brand = Text("MoneyWise", font_size=56, color=GOLD, weight=BOLD).move_to(UP * 1.0)
        
        scale_icon = self.load_png_icon("balance", height=2.0).move_to(DOWN * 0.5)
        
        tagline = Text("See your true\nfinancial position.", 
                      font_size=34, color=WHITE, line_spacing=1.2).move_to(DOWN * 2.5)
        
        icon_like = self.load_png_icon("thumbs_up", height=1.5)
        icon_share = self.load_png_icon("share", height=1.5)
        icon_subscribe = self.load_png_icon("check", height=1.5)
        
        cta_icons = Group(icon_like, icon_share, icon_subscribe).arrange(RIGHT, buff=1.5).move_to(DOWN * 4.5)
        
        labels = VGroup(
            Text("Like", font_size=24, color=WHITE),
            Text("Share", font_size=24, color=WHITE),
            Text("Follow", font_size=24, color=GOLD)
        )
        labels[0].next_to(icon_like, DOWN, buff=0.3)
        labels[1].next_to(icon_share, DOWN, buff=0.3)
        labels[2].next_to(icon_subscribe, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=step_time)
        self.play(
            GrowFromCenter(brand),
            FadeIn(scale_icon, scale=0.5),
            run_time=step_time
        )
        self.play(Write(tagline), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(icon_like, scale=0.5),
                FadeIn(icon_share, scale=0.5),
                FadeIn(icon_subscribe, scale=0.5),
                lag_ratio=0.3
            ),
            Write(labels),
            run_time=step_time
        )
        
        self.wait(t_trans)
