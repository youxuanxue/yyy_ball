import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson016VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 16: Become Who Banks Want to Lend To
    Building a Credit Profile That Gets You Approved
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
        title_text = "The Hidden\nApproval Checklist"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size, 
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Bank icon with checklist
        bank_icon = self.load_png_icon("bank_building", height=2.2).move_to(LEFT * 2.5 + UP * 0.8)
        
        # Checklist visual
        checklist_items = [
            ("Track Record", True),
            ("Income Stability", True),
            ("Debt Capacity", True),
            ("???", False)
        ]
        
        checklist_rows = []
        for i, (item, checked) in enumerate(checklist_items):
            checkbox = Square(side_length=0.5, color=WHITE if checked else LIGHT_GRAY, stroke_width=2)
            if checked:
                check = self.load_png_icon("check_mark", height=0.4).move_to(checkbox)
            else:
                check = Text("?", font_size=24, color=LIGHT_GRAY).move_to(checkbox)
            text = Text(item, font_size=22, color=WHITE if checked else LIGHT_GRAY)
            row = Group(checkbox, check, text).arrange(RIGHT, buff=0.2)
            checklist_rows.append(row)
        
        checklist = Group(*checklist_rows).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(RIGHT * 1.5 + UP * 0.8)
        
        # Key message
        message = Text("Not secret.\nNot random.", 
                      font_size=36, color=GOLD, weight=BOLD, line_spacing=1.2).move_to(DOWN * 2.8)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(bank_icon, shift=RIGHT), run_time=step_time)
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=LEFT) for item in checklist],
                lag_ratio=0.3
            ),
            run_time=step_time * 2
        )
        self.play(Write(message), run_time=step_time)
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
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "Three Things\nBanks Measure"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Three pillars
        pillars = [
            ("TRACK\nRECORD", "Payment history\nCredit age", "time", GREEN),
            ("CURRENT\nSTABILITY", "Steady income\nEmployment", "check_mark", BLUE),
            ("DEBT\nCAPACITY", "Room for more\nresponsible debt", "percentage", PURPLE)
        ]
        
        pillar_groups = []
        for label, desc, icon_name, color in pillars:
            header = Text(label, font_size=24, color=color, weight=BOLD, line_spacing=1.1)
            icon = self.load_png_icon(icon_name, height=1.0)
            description = Text(desc, font_size=18, color=WHITE, line_spacing=1.1)
            
            pillar_content = Group(header, icon, description).arrange(DOWN, buff=0.25)
            pillar_box = RoundedRectangle(
                corner_radius=0.2, width=pillar_content.width + 0.6, 
                height=pillar_content.height + 0.5, color=color, stroke_width=2
            ).move_to(pillar_content)
            
            pillar = Group(pillar_box, pillar_content)
            pillar_groups.append(pillar)
        
        pillar_groups[0].move_to(LEFT * 3.5 + UP * 0.5)
        pillar_groups[1].move_to(ORIGIN + UP * 0.5)
        pillar_groups[2].move_to(RIGHT * 3.5 + UP * 0.5)
        
        # Foundation
        foundation = Text("Your Credit Profile", 
                         font_size=32, color=GOLD, weight=BOLD).move_to(DOWN * 3.5)
        foundation_line = Line(LEFT * 5, RIGHT * 5, color=GOLD, stroke_width=3).move_to(DOWN * 2.8)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(Create(foundation_line), Write(foundation), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(pillar_groups[0], shift=UP),
                FadeIn(pillar_groups[1], shift=UP),
                FadeIn(pillar_groups[2], shift=UP),
                lag_ratio=0.3
            ),
            run_time=step_time * 2
        )
        self.play(
            *[p[0].animate.set_fill(opacity=0.1) for p in pillar_groups],
            run_time=step_time
        )
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
        title_text = "Why Profile Matters\nMore Than Score"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Comparison: Good vs Bad profile
        good_header = Text("Strong Profile", font_size=26, color=GREEN, weight=BOLD)
        bad_header = Text("Weak Profile", font_size=26, color=RED, weight=BOLD)
        
        good_benefits = VGroup(
            Text("✓ Lower interest rates", font_size=22, color=GREEN),
            Text("✓ Higher limits", font_size=22, color=GREEN),
            Text("✓ Better terms", font_size=22, color=GREEN),
            Text("✓ More negotiating power", font_size=22, color=GREEN)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        
        bad_drawbacks = VGroup(
            Text("✗ Higher rates", font_size=22, color=RED),
            Text("✗ Lower limits", font_size=22, color=RED),
            Text("✗ Worse terms", font_size=22, color=RED),
            Text("✗ Take what's offered", font_size=22, color=RED)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        
        good_group = VGroup(good_header, good_benefits).arrange(DOWN, buff=0.3)
        bad_group = VGroup(bad_header, bad_drawbacks).arrange(DOWN, buff=0.3)
        
        good_group.move_to(LEFT * 2.8 + UP * 0.5)
        bad_group.move_to(RIGHT * 2.8 + UP * 0.5)
        
        # Divider
        divider = DashedLine(UP * 2.5, DOWN * 1.5, color=LIGHT_GRAY, stroke_width=2).move_to(ORIGIN + UP * 0.5)
        
        # Bottom message
        savings_text = Text("$$$$ in savings", font_size=36, color=GOLD, weight=BOLD).move_to(DOWN * 3.0)
        money_icon = self.load_png_icon("money_bag", height=1.5).move_to(DOWN * 4.5)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(Create(divider), run_time=step_time * 0.5)
        self.play(
            FadeIn(good_group, shift=RIGHT),
            FadeIn(bad_group, shift=LEFT),
            run_time=step_time
        )
        self.play(
            good_benefits.animate.set_opacity(1),
            bad_drawbacks.animate.set_opacity(1),
            run_time=step_time
        )
        self.play(
            Write(savings_text),
            FadeIn(money_icon, shift=UP),
            run_time=step_time
        )
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
        title_text = "Whether Starting\nor Rebuilding"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Audience groups
        groups = [
            ("Young Adults", "Building first credit", "student"),
            ("Professionals", "Seeking home loans", "businessman"),
            ("Entrepreneurs", "Needing capital", "small_business")
        ]
        
        audience_items = []
        for label, desc, icon_name in groups:
            icon = self.load_png_icon(icon_name, height=1.3)
            main_text = Text(label, font_size=26, color=WHITE, weight=BOLD)
            sub_text = Text(desc, font_size=20, color=LIGHT_GRAY)
            text_group = VGroup(main_text, sub_text).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            item = Group(icon, text_group).arrange(RIGHT, buff=0.5)
            audience_items.append(item)
        
        audience_items[0].move_to(UP * 1.5)
        audience_items[1].move_to(DOWN * 0.3)
        audience_items[2].move_to(DOWN * 2.1)
        
        # Unifying message
        message = Text("The rules work for all.", 
                      font_size=32, color=GOLD, weight=BOLD).move_to(DOWN * 4.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(audience_items[0], shift=RIGHT),
                FadeIn(audience_items[1], shift=RIGHT),
                FadeIn(audience_items[2], shift=RIGHT),
                lag_ratio=0.4
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
        title_text = "Four Moves to\nStrengthen Your Profile"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        steps = [
            ("1", "Automate payments\nNever miss one", GREEN, "automation"),
            ("2", "Keep old accounts\nCredit age matters", BLUE, "time"),
            ("3", "Stay under 30%\nUtilization", PURPLE, "percentage"),
            ("4", "Space applications\nAvoid credit hits", ORANGE, "calendar")
        ]
        
        step_items = []
        for num, text, color, icon_name in steps:
            num_circle = Circle(radius=0.4, color=color, fill_opacity=0.2, stroke_width=3)
            num_text = Text(num, font_size=28, color=color, weight=BOLD).move_to(num_circle)
            icon = self.load_png_icon(icon_name, height=0.8)
            step_text = Text(text, font_size=20, color=WHITE, line_spacing=1.1)
            
            item = Group(num_circle, num_text, icon, step_text).arrange(RIGHT, buff=0.25)
            step_items.append((item, num_circle, color))
        
        positions = [UP * 1.8, UP * 0.3, DOWN * 1.2, DOWN * 2.7]
        for i, (item, _, _) in enumerate(step_items):
            item.move_to(positions[i])
        
        footer = Text("Small actions compound.", 
                     font_size=30, color=GOLD, weight=BOLD).move_to(DOWN * 4.3)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        
        for item, circle, color in step_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=step_time)
        
        self.play(
            *[circle.animate.set_fill(color, opacity=0.4) for _, circle, color in step_items],
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

        title = Text("Take Control", font=self.title_font, 
                    font_size=self.font_title_size, color=GOLD, line_spacing=1.1).move_to(UP * 3.5)
        
        brand = Text("MoneyWise", font_size=56, color=GOLD, weight=BOLD).move_to(UP * 1.0)
        
        trophy_icon = self.load_png_icon("trophy", height=2.0).move_to(DOWN * 0.5)
        
        tagline = Text("Start building today.", 
                      font_size=36, color=WHITE).move_to(DOWN * 2.3)
        
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
            FadeIn(trophy_icon, scale=0.5),
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
