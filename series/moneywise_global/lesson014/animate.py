import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson014VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 14: Why Collateral is King in Lending
    The Asset Banks Trust Most When You Borrow
    """

    def build_scene_1(self, scene_data):
        """
        Scene 1: Hook / Pain Point
        'When you borrow money, lenders face a simple problem...'
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "The Lender's Dilemma"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size, 
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Visual: Lender with question mark, borrower on other side
        bank_icon = self.load_png_icon("bank_building", height=2.0).move_to(LEFT * 2.5 + UP * 1.0)
        question = self.load_png_icon("question_mark", height=1.5).next_to(bank_icon, UP, buff=0.2)
        
        person_icon = self.load_png_icon("user", height=1.8).move_to(RIGHT * 2.5 + UP * 1.0)
        money_icon = self.load_png_icon("money", height=1.2).move_to(ORIGIN + UP * 1.0)
        
        # Arrow from bank to person with money
        arrow = Arrow(bank_icon.get_right(), person_icon.get_left(), buff=0.3, color=GREEN)
        
        # Assets comparison (below)
        happy_asset = self.load_png_icon("house", height=1.3).move_to(LEFT * 2.0 + DOWN * 2.0)
        happy_label = Text("Safe", font_size=24, color=GREEN).next_to(happy_asset, DOWN, buff=0.2)
        safe_box = SurroundingRectangle(Group(happy_asset, happy_label), color=GREEN, buff=0.2)
        
        nervous_asset = self.load_png_icon("car", height=1.3).move_to(RIGHT * 2.0 + DOWN * 2.0)
        nervous_label = Text("Nervous", font_size=24, color=ORANGE).next_to(nervous_asset, DOWN, buff=0.2)
        nervous_box = SurroundingRectangle(Group(nervous_asset, nervous_label), color=ORANGE, buff=0.2)
        
        # Bottom text
        bottom_text = Text("Not all collateral is equal.", 
                          font_size=32, color=WHITE, weight=BOLD).move_to(DOWN * 4.2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            FadeIn(bank_icon, shift=RIGHT),
            FadeIn(question, scale=0.5),
            run_time=step_time
        )
        self.play(
            FadeIn(person_icon, shift=LEFT),
            GrowArrow(arrow),
            FadeIn(money_icon, shift=DOWN),
            run_time=step_time
        )
        self.play(
            FadeIn(happy_asset, shift=UP),
            Write(happy_label),
            Create(safe_box),
            run_time=step_time
        )
        self.play(
            FadeIn(nervous_asset, shift=UP),
            Write(nervous_label),
            Create(nervous_box),
            run_time=step_time
        )
        self.play(Write(bottom_text), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        'Collateral is an asset you pledge as security...'
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "What Makes\nCollateral Valuable"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Three qualities of good collateral
        qualities = [
            ("Easy to Value", "calculator", BLUE),
            ("Holds Worth", "safe", GREEN),
            ("Easy to Sell", "handshake", PURPLE)
        ]
        
        quality_items = []
        for txt, icon_name, color in qualities:
            box = RoundedRectangle(width=4.5, height=1.5, corner_radius=0.2,
                                   color=color, fill_opacity=0.2, stroke_width=3)
            icon = self.load_png_icon(icon_name, height=0.9)
            label = Text(txt, font_size=26, color=WHITE, weight=BOLD)
            content = Group(icon, label).arrange(RIGHT, buff=0.4)
            content.move_to(box)
            quality_items.append(Group(box, content))
        
        # Position qualities
        quality_items[0].move_to(UP * 1.8)
        quality_items[1].move_to(ORIGIN)
        quality_items[2].move_to(DOWN * 1.8)
        
        # Gold standard: Real Estate
        gold_text = Text("Real Estate =\nGold Standard", 
                        font_size=36, color=GOLD, weight=BOLD, line_spacing=1.2).move_to(DOWN * 3.8)
        house_icon = self.load_png_icon("house", height=1.5).next_to(gold_text, LEFT, buff=0.5)
        gold_box = SurroundingRectangle(Group(house_icon, gold_text), color=GOLD, buff=0.3, stroke_width=3)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(quality_items[0], shift=DOWN), run_time=step_time)
        self.play(FadeIn(quality_items[1], shift=DOWN), run_time=step_time)
        self.play(FadeIn(quality_items[2], shift=DOWN), run_time=step_time)
        self.play(
            FadeIn(house_icon, shift=RIGHT),
            Write(gold_text),
            run_time=step_time
        )
        self.play(Create(gold_box), run_time=step_time)
        self.play(Flash(gold_box, color=GOLD), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        'Why does real estate dominate?...'
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "Why Real Estate\nRules Collateral"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # House in center with benefits around it
        house_icon = self.load_png_icon("house", height=2.5).move_to(ORIGIN)
        
        # Benefits circling the house
        benefits = [
            ("Stable Values", UP * 2.0 + LEFT * 2.0),
            ("60-70% LTV", UP * 2.0 + RIGHT * 2.0),
            ("Low Default", DOWN * 2.0 + LEFT * 2.0),
            ("Easy to Sell", DOWN * 2.0 + RIGHT * 2.0)
        ]
        
        benefit_texts = []
        for txt, pos in benefits:
            t = Text(txt, font_size=24, color=WHITE, weight=BOLD).move_to(pos)
            benefit_texts.append(t)
        
        # Connecting lines
        lines = []
        for t in benefit_texts:
            line = DashedLine(house_icon.get_center(), t.get_center(), color=GREEN, dash_length=0.1)
            lines.append(line)
        
        # Key insight
        insight = Text("People prioritize\nmortgage payments.", 
                      font_size=32, color=GREEN, weight=BOLD, line_spacing=1.2).move_to(DOWN * 4.2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(house_icon, scale=0.8), run_time=step_time)
        self.play(
            *[Create(line) for line in lines],
            run_time=step_time
        )
        self.play(
            LaggedStart(
                *[Write(t) for t in benefit_texts],
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        self.play(
            house_icon.animate.scale(1.1),
            run_time=step_time
        )
        self.play(Write(insight), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        'This matters if you're seeking a loan...'
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "How This Affects\nYour Borrowing"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Two scenarios
        # Left: Has home equity - good terms
        left_header = Text("Home Equity", font_size=28, color=GREEN, weight=BOLD)
        home_icon = self.load_png_icon("house", height=1.5)
        left_benefits = VGroup(
            Text("✓ Better rates", font_size=22, color=WHITE),
            Text("✓ Higher limits", font_size=22, color=WHITE)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        left_group = Group(left_header, home_icon, left_benefits).arrange(DOWN, buff=0.3).move_to(LEFT * 2.5 + UP * 0.5)
        left_box = SurroundingRectangle(left_group, color=GREEN, buff=0.3, stroke_width=2)
        
        # Right: Other collateral - tough terms
        right_header = Text("Other Assets", font_size=28, color=ORANGE, weight=BOLD)
        car_icon = self.load_png_icon("car", height=1.5)
        right_cons = VGroup(
            Text("✗ Tougher terms", font_size=22, color=LIGHT_GRAY),
            Text("✗ Lower amounts", font_size=22, color=LIGHT_GRAY)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        right_group = Group(right_header, car_icon, right_cons).arrange(DOWN, buff=0.3).move_to(RIGHT * 2.5 + UP * 0.5)
        right_box = SurroundingRectangle(right_group, color=ORANGE, buff=0.3, stroke_width=2)
        
        # Bottom message
        bottom_text = Text("Know what lenders want.", 
                          font_size=32, color=WHITE, weight=BOLD).move_to(DOWN * 3.5)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            FadeIn(left_group, shift=RIGHT),
            Create(left_box),
            run_time=step_time
        )
        self.play(
            FadeIn(right_group, shift=LEFT),
            Create(right_box),
            run_time=step_time
        )
        self.play(
            left_box.animate.set_stroke(color=GREEN, width=4),
            right_box.animate.set_stroke(color=ORANGE, width=4),
            run_time=step_time
        )
        self.play(Write(bottom_text), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        'Before borrowing, assess your collateral options...'
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "Smart Collateral\nDecisions"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Three steps
        steps = [
            ("1", "Calculate home equity:\nValue - What You Owe", GREEN, "calculator"),
            ("2", "Consider timing:\nEquity loans take longer", BLUE, "clock"),
            ("3", "Never pledge assets\nyou can't afford to lose", RED, "warning")
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
        
        # Position steps
        positions = [UP * 1.5, DOWN * 0.5, DOWN * 2.5]
        for i, (item, _, _) in enumerate(step_items):
            item.move_to(positions[i])
        
        # Footer warning
        footer = Text("Default = Lose the asset.", 
                     font_size=32, color=RED, weight=BOLD).move_to(DOWN * 4.3)
        footer_box = SurroundingRectangle(footer, color=RED, buff=0.2, stroke_width=2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        
        for item, checkbox, color in step_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=step_time)
        
        # Check first two boxes
        check_icons = []
        for i, (item, checkbox, color) in enumerate(step_items[:2]):
            check_icon = self.load_png_icon("check_mark", height=0.5).move_to(checkbox)
            check_icons.append((check_icon, checkbox, color))
        
        self.play(
            *[FadeIn(check, scale=0.5) for check, _, _ in check_icons],
            *[checkbox.animate.set_fill(color, opacity=0.3) for _, checkbox, color in check_icons],
            run_time=step_time
        )
        
        self.play(Write(footer), Create(footer_box), run_time=step_time)
        self.play(Flash(footer_box, color=RED), run_time=step_time)
        
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

        # Title
        title = Text("Borrow Smarter", font=self.title_font, 
                    font_size=self.font_title_size, color=GOLD, line_spacing=1.1).move_to(UP * 3.5)
        
        # MoneyWise branding
        brand = Text("MoneyWise", font_size=56, color=GOLD, weight=BOLD).move_to(UP * 1.0)
        
        # House with shield
        house_icon = self.load_png_icon("house", height=2.0).move_to(DOWN * 0.5)
        shield_icon = self.load_png_icon("security_shield", height=1.2).move_to(house_icon.get_center() + DOWN * 0.2)
        
        # Tagline
        tagline = Text("Your assets,\nyour leverage.", 
                      font_size=34, color=WHITE, line_spacing=1.2).move_to(DOWN * 2.5)
        
        # CTA icons
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
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            GrowFromCenter(brand),
            FadeIn(house_icon, scale=0.5),
            FadeIn(shield_icon, scale=0.5),
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
