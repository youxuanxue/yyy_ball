import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson017VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 17: How to Get the Cheapest Loan
    Strategies to Lock in the Lowest Interest Rate
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
        title_text = "The Hidden\nPrice Gap"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size, 
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Two borrowers comparison
        person1 = self.load_png_icon("sad", height=1.6).move_to(LEFT * 2.5 + UP * 1.2)
        person1_label = Text("Person A", font_size=22, color=WHITE).next_to(person1, UP, buff=0.2)
        person1_amount = Text("Pays $30K\nExtra", font_size=26, color=RED, weight=BOLD, line_spacing=1.1).next_to(person1, DOWN, buff=0.3)
        
        person2 = self.load_png_icon("happy", height=1.6).move_to(RIGHT * 2.5 + UP * 1.2)
        person2_label = Text("Person B", font_size=22, color=WHITE).next_to(person2, UP, buff=0.2)
        person2_amount = Text("Pays $15K\nExtra", font_size=26, color=GREEN, weight=BOLD, line_spacing=1.1).next_to(person2, DOWN, buff=0.3)
        
        # Same loan indicator
        same_text = Text("Same Loan Amount", font_size=28, color=LIGHT_GRAY).move_to(DOWN * 1.5)
        
        # Key insight
        insight = Text("The difference?\nKnowing how to shop.", 
                      font_size=32, color=GOLD, weight=BOLD, line_spacing=1.2).move_to(DOWN * 3.5)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            FadeIn(person1, shift=DOWN),
            Write(person1_label),
            FadeIn(person2, shift=DOWN),
            Write(person2_label),
            run_time=step_time
        )
        self.play(
            Write(person1_amount),
            Write(person2_amount),
            run_time=step_time
        )
        self.play(Write(same_text), run_time=step_time)
        self.play(Write(insight), run_time=step_time)
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
        title_text = "What Determines\nYour Rate"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Rate factors
        factors = [
            ("Credit Profile", "credit_card", GREEN),
            ("Loan Type", "document", BLUE),
            ("Collateral", "house", PURPLE),
            ("Lender Type", "bank_building", ORANGE)
        ]
        
        factor_items = []
        for text, icon_name, color in factors:
            icon = self.load_png_icon(icon_name, height=1.0)
            label = Text(text, font_size=24, color=WHITE, weight=BOLD)
            box = RoundedRectangle(corner_radius=0.15, width=4.5, height=1.2, 
                                  color=color, stroke_width=2, fill_opacity=0.1)
            content = Group(icon, label).arrange(RIGHT, buff=0.4)
            item = Group(box, content)
            content.move_to(box)
            factor_items.append(item)
        
        factor_items[0].move_to(UP * 1.8)
        factor_items[1].move_to(UP * 0.3)
        factor_items[2].move_to(DOWN * 1.2)
        factor_items[3].move_to(DOWN * 2.7)
        
        # Key message
        message = Text("Same risk, different prices.", 
                      font_size=30, color=GOLD, weight=BOLD).move_to(DOWN * 4.2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT) for item in factor_items],
                lag_ratio=0.3
            ),
            run_time=step_time * 2.5
        )
        self.play(Write(message), run_time=step_time)
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
        title_text = "The True Cost\nof Two Percent"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Loan details
        loan_info = VGroup(
            Text("$100,000 Loan", font_size=28, color=WHITE, weight=BOLD),
            Text("20 Year Term", font_size=24, color=LIGHT_GRAY)
        ).arrange(DOWN, buff=0.2).move_to(UP * 2.0)
        
        # Rate comparison bars
        rate_low = RoundedRectangle(corner_radius=0.1, width=3.5, height=0.8, 
                                    color=GREEN, fill_opacity=0.3, stroke_width=2)
        rate_low_label = Text("5% Rate", font_size=22, color=GREEN).move_to(rate_low)
        rate_low_group = Group(rate_low, rate_low_label).move_to(LEFT * 2.5 + UP * 0.2)
        
        rate_high = RoundedRectangle(corner_radius=0.1, width=5.0, height=0.8,
                                     color=RED, fill_opacity=0.3, stroke_width=2)
        rate_high_label = Text("7% Rate", font_size=22, color=RED).move_to(rate_high)
        rate_high_group = Group(rate_high, rate_high_label).move_to(RIGHT * 1.5 + UP * 0.2)
        
        # Cost difference
        arrow = Arrow(LEFT * 0.5 + DOWN * 0.8, RIGHT * 0.5 + DOWN * 0.8, color=GOLD, stroke_width=3)
        difference = Text("$20,000+\nDifference!", font_size=36, color=RED, weight=BOLD, 
                         line_spacing=1.1).move_to(DOWN * 2.0)
        
        # Warning items
        mistakes = VGroup(
            Text("• Not comparing", font_size=22, color=ORANGE),
            Text("• Not negotiating", font_size=22, color=ORANGE),
            Text("• Not preparing", font_size=22, color=ORANGE)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).move_to(DOWN * 4.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(loan_info, shift=DOWN), run_time=step_time)
        self.play(
            FadeIn(rate_low_group, shift=RIGHT),
            FadeIn(rate_high_group, shift=LEFT),
            run_time=step_time
        )
        self.play(
            GrowArrow(arrow),
            Write(difference),
            run_time=step_time
        )
        self.play(Write(mistakes), run_time=step_time)
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
        title_text = "From Cars to\nHomes to Business"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Loan types
        loan_types = [
            ("Car Loans", "car"),
            ("Home Mortgages", "house"),
            ("Business Loans", "small_business")
        ]
        
        type_items = []
        for txt, icon_name in loan_types:
            icon = self.load_png_icon(icon_name, height=1.4)
            label = Text(txt, font_size=28, color=WHITE, weight=BOLD)
            item = Group(icon, label).arrange(RIGHT, buff=0.5)
            type_items.append(item)
        
        type_items[0].move_to(UP * 1.5)
        type_items[1].move_to(DOWN * 0.3)
        type_items[2].move_to(DOWN * 2.1)
        
        # Bonus insight
        refinance = Text("Already have loans?\nRefinance to better rates.", 
                        font_size=28, color=GREEN, line_spacing=1.2).move_to(DOWN * 4.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(type_items[0], shift=RIGHT),
                FadeIn(type_items[1], shift=RIGHT),
                FadeIn(type_items[2], shift=RIGHT),
                lag_ratio=0.4
            ),
            run_time=step_time * 2
        )
        self.play(Write(refinance), run_time=step_time)
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
        title_text = "Your Rate-Hunting\nPlaybook"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        steps = [
            ("1", "Build profile first", GREEN, "user"),
            ("2", "Get 3+ quotes", BLUE, "search"),
            ("3", "Apply within 14 days", PURPLE, "calendar"),
            ("4", "Negotiate with offers", ORANGE, "handshake")
        ]
        
        step_items = []
        for num, text, color, icon_name in steps:
            num_box = Square(side_length=0.6, color=color, stroke_width=3, fill_opacity=0.2)
            num_text = Text(num, font_size=26, color=color, weight=BOLD).move_to(num_box)
            icon = self.load_png_icon(icon_name, height=0.8)
            step_text = Text(text, font_size=22, color=WHITE)
            
            item = Group(num_box, num_text, icon, step_text).arrange(RIGHT, buff=0.3)
            step_items.append((item, num_box, color))
        
        positions = [UP * 1.8, UP * 0.3, DOWN * 1.2, DOWN * 2.7]
        for i, (item, _, _) in enumerate(step_items):
            item.move_to(positions[i])
        
        footer = Text("Lenders expect negotiation.", 
                     font_size=28, color=GOLD, weight=BOLD).move_to(DOWN * 4.3)
        
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

        title = Text("Never Overpay", font=self.title_font, 
                    font_size=self.font_title_size, color=GOLD, line_spacing=1.1).move_to(UP * 3.5)
        
        brand = Text("MoneyWise", font_size=56, color=GOLD, weight=BOLD).move_to(UP * 1.0)
        
        money_icon = self.load_png_icon("money_bag", height=2.0).move_to(DOWN * 0.5)
        
        tagline = Text("Smart borrowing\nstarts here.", 
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
            FadeIn(money_icon, scale=0.5),
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
