import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson015VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 15: Your Borrowing Power Explained
    What Banks Actually Look For When You Apply for a Loan
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
        title_text = "The Loan\nApproval Puzzle"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size, 
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Two people: one approved, one denied
        person_approved = self.load_png_icon("happy", height=1.8).move_to(LEFT * 2.5 + UP * 1.0)
        approved_label = Text("Average Credit\nAPPROVED", font_size=22, color=GREEN, line_spacing=1.1).next_to(person_approved, DOWN, buff=0.3)
        check_icon = self.load_png_icon("check_mark", height=0.8).next_to(approved_label, RIGHT, buff=0.2)
        
        person_denied = self.load_png_icon("sad", height=1.8).move_to(RIGHT * 2.5 + UP * 1.0)
        denied_label = Text("Great Credit\nDENIED", font_size=22, color=RED, line_spacing=1.1).next_to(person_denied, DOWN, buff=0.3)
        fail_icon = self.load_png_icon("fail", height=0.8).next_to(denied_label, RIGHT, buff=0.2)
        
        # VS in middle
        vs_text = Text("VS", font_size=36, color=GOLD, weight=BOLD).move_to(ORIGIN + UP * 1.0)
        
        # Key question
        question = Text("What makes\nthe difference?", 
                       font_size=36, color=WHITE, weight=BOLD, line_spacing=1.2).move_to(DOWN * 2.5)
        question_icon = self.load_png_icon("question_mark", height=1.2).next_to(question, LEFT, buff=0.3)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            FadeIn(person_approved, shift=DOWN),
            Write(approved_label),
            FadeIn(check_icon, scale=0.5),
            run_time=step_time
        )
        self.play(GrowFromCenter(vs_text), run_time=step_time * 0.5)
        self.play(
            FadeIn(person_denied, shift=DOWN),
            Write(denied_label),
            FadeIn(fail_icon, scale=0.5),
            run_time=step_time
        )
        self.play(
            Write(question),
            FadeIn(question_icon, shift=RIGHT),
            run_time=step_time
        )
        self.play(
            question_icon.animate.scale(1.2),
            run_time=step_time
        )
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "Two Paths to\nLoan Approval"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Path 1: Collateral-based
        path1_header = Text("COLLATERAL-BASED", font_size=26, color=GREEN, weight=BOLD)
        house_icon = self.load_png_icon("house", height=1.2)
        path1_desc = Text("Have asset?\nGet loan.", font_size=22, color=WHITE, line_spacing=1.1)
        path1_note = Text("Credit matters less", font_size=18, color=LIGHT_GRAY)
        path1_group = Group(path1_header, house_icon, path1_desc, path1_note).arrange(DOWN, buff=0.25).move_to(LEFT * 2.5 + UP * 0.3)
        path1_box = SurroundingRectangle(path1_group, color=GREEN, buff=0.3, stroke_width=2)
        
        # Path 2: Credit-based
        path2_header = Text("CREDIT-BASED", font_size=26, color=BLUE, weight=BOLD)
        credit_icon = self.load_png_icon("credit_card", height=1.2)
        path2_desc = Text("No collateral?\nProve reliability.", font_size=22, color=WHITE, line_spacing=1.1)
        path2_note = Text("History is everything", font_size=18, color=LIGHT_GRAY)
        path2_group = Group(path2_header, credit_icon, path2_desc, path2_note).arrange(DOWN, buff=0.25).move_to(RIGHT * 2.5 + UP * 0.3)
        path2_box = SurroundingRectangle(path2_group, color=BLUE, buff=0.3, stroke_width=2)
        
        # Bottom insight
        insight = Text("Different paths,\nsame destination.", 
                      font_size=32, color=WHITE, weight=BOLD, line_spacing=1.2).move_to(DOWN * 3.8)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            FadeIn(path1_group, shift=RIGHT),
            Create(path1_box),
            run_time=step_time
        )
        self.play(
            FadeIn(path2_group, shift=LEFT),
            Create(path2_box),
            run_time=step_time
        )
        self.play(
            path1_box.animate.set_stroke(width=4),
            path2_box.animate.set_stroke(width=4),
            run_time=step_time
        )
        self.play(Write(insight), run_time=step_time)
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
        title_text = "How Modern Lending\nHas Evolved"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Data-driven factors
        factors = [
            ("Tax Payments", "analytics", "Business health indicator"),
            ("Banking Patterns", "bar_chart", "Consistency matters"),
            ("Cash Flow", "money_circulation", "Steady income wins")
        ]
        
        factor_items = []
        for name, icon_name, desc in factors:
            icon = self.load_png_icon(icon_name, height=1.0)
            main_text = Text(name, font_size=26, color=WHITE, weight=BOLD)
            sub_text = Text(desc, font_size=20, color=LIGHT_GRAY)
            text_group = VGroup(main_text, sub_text).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            item = Group(icon, text_group).arrange(RIGHT, buff=0.4)
            factor_items.append(item)
        
        # Position factors
        factor_items[0].move_to(UP * 1.5)
        factor_items[1].move_to(DOWN * 0.3)
        factor_items[2].move_to(DOWN * 2.1)
        
        # Key message
        message = Text("The game is changing.", 
                      font_size=34, color=GOLD, weight=BOLD).move_to(DOWN * 4.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(factor_items[0], shift=RIGHT),
                FadeIn(factor_items[1], shift=RIGHT),
                FadeIn(factor_items[2], shift=RIGHT),
                lag_ratio=0.4
            ),
            run_time=step_time * 2
        )
        self.play(
            *[item.animate.scale(1.05) for item in factor_items],
            run_time=step_time
        )
        self.play(Write(message), Flash(message, color=GOLD), run_time=step_time)
        
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
        title_text = "When to Explore\nYour Options"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Situations
        situations = [
            ("Financing a Home", "house"),
            ("Starting a Business", "small_business"),
            ("Emergency Funds", "warning")
        ]
        
        situation_items = []
        for txt, icon_name in situations:
            icon = self.load_png_icon(icon_name, height=1.3)
            label = Text(txt, font_size=28, color=WHITE, weight=BOLD)
            item = Group(icon, label).arrange(RIGHT, buff=0.5)
            situation_items.append(item)
        
        situation_items[0].move_to(UP * 1.5)
        situation_items[1].move_to(DOWN * 0.3)
        situation_items[2].move_to(DOWN * 2.1)
        
        # Bottom insight
        insight = Text("Knowing options\nexpands possibilities.", 
                      font_size=32, color=GREEN, weight=BOLD, line_spacing=1.2).move_to(DOWN * 4.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(situation_items[0], shift=RIGHT),
                FadeIn(situation_items[1], shift=RIGHT),
                FadeIn(situation_items[2], shift=RIGHT),
                lag_ratio=0.4
            ),
            run_time=step_time * 2
        )
        self.play(Write(insight), run_time=step_time)
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
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "Three Steps to Better\nApproval Odds"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        steps = [
            ("1", "Build a paper trail:\nConsistent activity", GREEN, "document"),
            ("2", "Know your assets:\nHome equity opens doors", BLUE, "house"),
            ("3", "Shop around:\nLenders differ", PURPLE, "search")
        ]
        
        step_items = []
        for num, step_text, color, icon_name in steps:
            checkbox = Square(side_length=0.7, color=color, stroke_width=3)
            num_text = Text(num, font_size=30, color=color, weight=BOLD).move_to(checkbox)
            check_group = VGroup(checkbox, num_text)
            
            icon = self.load_png_icon(icon_name, height=0.9)
            step_label = Text(step_text, font_size=22, color=WHITE, line_spacing=1.1)
            
            item = Group(check_group, icon, step_label).arrange(RIGHT, buff=0.3)
            step_items.append((item, checkbox, color))
        
        positions = [UP * 1.5, DOWN * 0.5, DOWN * 2.5]
        for i, (item, _, _) in enumerate(step_items):
            item.move_to(positions[i])
        
        footer = Text("The right match exists.", 
                     font_size=32, color=GOLD, weight=BOLD).move_to(DOWN * 4.3)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        
        for item, checkbox, color in step_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=step_time)
        
        check_icons = []
        for item, checkbox, color in step_items:
            check_icon = self.load_png_icon("check_mark", height=0.5).move_to(checkbox)
            check_icons.append((check_icon, checkbox, color))
        
        self.play(
            *[FadeIn(check, scale=0.5) for check, _, _ in check_icons],
            *[checkbox.animate.set_fill(color, opacity=0.3) for _, checkbox, color in check_icons],
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

        title = Text("Know Your Power", font=self.title_font, 
                    font_size=self.font_title_size, color=GOLD, line_spacing=1.1).move_to(UP * 3.5)
        
        brand = Text("MoneyWise", font_size=56, color=GOLD, weight=BOLD).move_to(UP * 1.0)
        
        brain_icon = self.load_png_icon("brain", height=2.0).move_to(DOWN * 0.5)
        
        tagline = Text("Your future starts\nwith knowledge.", 
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
            FadeIn(brain_icon, scale=0.5),
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
