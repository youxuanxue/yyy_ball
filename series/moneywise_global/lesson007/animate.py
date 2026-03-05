import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson007VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 7: What Are Underlying Assets?
    The Hidden Truth Behind Every Investment
    """

    def build_scene_1(self, scene_data):
        """
        Scene 1: Hook / Pain Point
        'Ever bought an investment product and had no idea what your money actually funded?'
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = scene_data.get("h2_heading", "The Hidden Danger")
        # Split long titles for better display
        if len(title_text) > 30:
            title_text = "The Hidden Danger in\nComplex Investments"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size, 
                    color=self.COLOR_RISK, line_spacing=1.1).move_to(UP * 4.0)
        
        # Visual: Multiple layers hiding something
        # Outer box (complex product)
        outer_box = RoundedRectangle(width=5, height=4, corner_radius=0.3, 
                                     color=GRAY, fill_opacity=0.2, stroke_width=3)
        middle_box = RoundedRectangle(width=3.5, height=2.8, corner_radius=0.2,
                                      color=GRAY_B, fill_opacity=0.3, stroke_width=2)
        inner_box = RoundedRectangle(width=2, height=1.6, corner_radius=0.1,
                                     color=GRAY_C, fill_opacity=0.4, stroke_width=1)
        
        question_mark = Text("?", font_size=80, color=RED, weight=BOLD)
        
        layers = VGroup(outer_box, middle_box, inner_box, question_mark).move_to(DOWN * 0.5)
        
        # Labels
        label_outer = Text("Investment Product", font_size=24, color=WHITE).next_to(outer_box, UP, buff=0.2)
        label_hidden = Text("What's Really Inside?", font_size=28, color=RED).next_to(layers, DOWN, buff=0.8)
        
        # Warning icon
        warning_icon = self.load_png_icon("warning", height=1.5).move_to(DOWN * 4.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(outer_box), run_time=step_time)
        self.play(FadeIn(middle_box), FadeIn(inner_box), run_time=step_time)
        self.play(Write(label_outer), run_time=step_time * 0.5)
        self.play(GrowFromCenter(question_mark), Flash(question_mark, color=RED), run_time=step_time)
        self.play(Write(label_hidden), FadeIn(warning_icon, shift=UP), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        'An underlying asset is the real thing your investment ultimately funds.'
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = scene_data.get("h2_heading", "What Are Underlying Assets?")
        # Already short enough, no need to split
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Gift box metaphor: Multiple boxes, smallest one contains the real asset
        # Create nested boxes visual
        box_large = RoundedRectangle(width=6, height=3.5, corner_radius=0.3,
                                     color=BLUE_B, fill_opacity=0.2, stroke_width=3)
        box_medium = RoundedRectangle(width=4, height=2.3, corner_radius=0.2,
                                      color=BLUE_C, fill_opacity=0.3, stroke_width=2)
        box_small = RoundedRectangle(width=2, height=1.2, corner_radius=0.1,
                                     color=GOLD, fill_opacity=0.5, stroke_width=3)
        
        # Labels for layers
        label_fund = Text("Fund", font_size=20, color=WHITE).move_to(box_large.get_corner(UR) + DL * 0.4)
        label_trust = Text("Trust", font_size=18, color=WHITE).move_to(box_medium.get_corner(UR) + DL * 0.3)
        label_asset = Text("Underlying\nAsset", font_size=22, color=GOLD, weight=BOLD).move_to(box_small)
        
        boxes = Group(box_large, box_medium, box_small, label_fund, label_trust).move_to(UP * 0.8)
        label_asset.move_to(box_small)
        
        # Examples of underlying assets
        example_title = Text("Could Be:", font_size=28, color=WHITE).move_to(DOWN * 2.0)
        
        # Load icons for examples
        icon_house = self.load_png_icon("real_estate", height=1.2)
        icon_stocks = self.load_png_icon("stocks", height=1.2)
        icon_loan = self.load_png_icon("loan", height=1.2)
        
        label_house = Text("Real Estate", font_size=18, color=WHITE)
        label_stocks = Text("Stocks", font_size=18, color=WHITE)
        label_loan = Text("Loans", font_size=18, color=WHITE)
        
        example_1 = Group(icon_house, label_house).arrange(DOWN, buff=0.2)
        example_2 = Group(icon_stocks, label_stocks).arrange(DOWN, buff=0.2)
        example_3 = Group(icon_loan, label_loan).arrange(DOWN, buff=0.2)
        
        examples = Group(example_1, example_2, example_3).arrange(RIGHT, buff=1.0).move_to(DOWN * 3.5)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(box_large), run_time=step_time)
        self.play(FadeIn(box_medium), Write(label_fund), run_time=step_time)
        self.play(FadeIn(box_small), Write(label_trust), run_time=step_time)
        self.play(Write(label_asset), box_small.animate.set_stroke(color=GOLD, width=4), run_time=step_time)
        self.play(Write(example_title), run_time=step_time * 0.5)
        self.play(
            LaggedStart(
                FadeIn(example_1, shift=UP),
                FadeIn(example_2, shift=UP),
                FadeIn(example_3, shift=UP),
                lag_ratio=0.3
            ),
            run_time=step_time * 1.5
        )
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        'Complex products can hide risky assets.'
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = scene_data.get("h2_heading", "Why This Matters")
        # Split long title for better display
        if len(title_text) > 30:
            title_text = "Why Underlying Assets\nMatter for Your Wealth"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Visual: "Safe Looking" vs "Reality"
        # Left side: Nice looking package
        package_nice = RoundedRectangle(width=3.5, height=2.5, corner_radius=0.2,
                                        color=GREEN, fill_opacity=0.3, stroke_width=3)
        label_nice = Text("Looks Safe", font_size=24, color=GREEN).next_to(package_nice, UP, buff=0.3)
        check_icon = self.load_png_icon("check_mark", height=1.0).move_to(package_nice)
        nice_side = Group(package_nice, label_nice, check_icon).move_to(LEFT * 2.5 + UP * 1.0)
        
        # Right side: Hidden risk
        package_risky = RoundedRectangle(width=3.5, height=2.5, corner_radius=0.2,
                                         color=RED, fill_opacity=0.3, stroke_width=3)
        label_risky = Text("Hidden Risk", font_size=24, color=RED).next_to(package_risky, UP, buff=0.3)
        warning_icon = self.load_png_icon("warning", height=1.0).move_to(package_risky)
        risky_side = Group(package_risky, label_risky, warning_icon).move_to(RIGHT * 2.5 + UP * 1.0)
        
        # Arrow between them
        arrow = Arrow(LEFT * 0.5, RIGHT * 0.5, color=WHITE, stroke_width=3).move_to(UP * 1.0)
        
        # Key message
        key_message = Text("The packaging doesn't matter.\nWhat's inside does.", 
                          font_size=32, color=WHITE, line_spacing=1.3).move_to(DOWN * 2.0)
        
        # Highlight box around key message
        highlight = SurroundingRectangle(key_message, color=GOLD, buff=0.3, stroke_width=2)
        
        # Bottom warning
        bottom_text = Text("If you can't identify the underlying asset,\nyou can't assess the real risk.",
                          font_size=26, color=RED, line_spacing=1.2).move_to(DOWN * 4.2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(nice_side), run_time=step_time)
        self.play(GrowArrow(arrow), run_time=step_time * 0.5)
        self.play(FadeIn(risky_side), Flash(warning_icon, color=RED), run_time=step_time)
        self.play(Write(key_message), run_time=step_time)
        self.play(Create(highlight), Write(bottom_text), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        'This applies to anyone buying mutual funds, ETFs, bonds, or structured products.'
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = scene_data.get("h2_heading", "Who Needs to Know This")
        # Split long title for better display
        if len(title_text) > 30:
            title_text = "Who Needs to Understand\nUnderlying Assets"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Create product cards
        products = ["Mutual Funds", "ETFs", "Bonds", "Structured\nProducts"]
        product_cards = VGroup()
        
        colors = [BLUE_B, GREEN_B, PURPLE_E, ORANGE]
        
        for i, prod in enumerate(products):
            card = RoundedRectangle(width=3.8, height=1.5, corner_radius=0.2,
                                   color=colors[i], fill_opacity=0.3, stroke_width=2)
            label = Text(prod, font_size=26, color=WHITE).move_to(card)
            product_cards.add(VGroup(card, label))
        
        product_cards.arrange_in_grid(rows=2, cols=2, buff=0.5).move_to(UP * 0.5)
        
        # Person icon with question
        person_icon = self.load_png_icon("user", height=1.5).move_to(DOWN * 2.5)
        question = Text("Are you investing in any of these?", font_size=30, color=WHITE).move_to(DOWN * 4.0)
        
        # Pointer lines from person to products
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(
                *[FadeIn(card, shift=DOWN) for card in product_cards],
                lag_ratio=0.2
            ),
            run_time=step_time * 2
        )
        self.play(FadeIn(person_icon, shift=UP), run_time=step_time)
        self.play(Write(question), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        'Before investing, ask three questions.'
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = scene_data.get("h2_heading", "How to Evaluate Any Investment")
        # Split for better display
        if len(title_text) > 25:
            title_text = "How to Evaluate\nAny Investment"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Three questions with icons
        questions = [
            ("1", "What's the underlying asset?", "magnifying_glass"),
            ("2", "Who manages these assets?", "manager"),
            ("3", "What if things go wrong?", "shield")
        ]
        
        question_items = []
        
        for num, text, icon_name in questions:
            # Number circle
            circle = Circle(radius=0.4, color=GOLD, fill_opacity=0.8, stroke_width=0)
            num_text = Text(num, font_size=32, color=BLACK, weight=BOLD).move_to(circle)
            num_group = VGroup(circle, num_text)
            
            # Question text
            q_text = Text(text, font_size=28, color=WHITE)
            
            # Icon
            icon = self.load_png_icon(icon_name, height=0.8)
            
            # Arrange
            item = Group(num_group, q_text, icon).arrange(RIGHT, buff=0.5)
            question_items.append(item)
        
        # Position items manually
        question_items[0].move_to(UP * 2.0)
        question_items[1].next_to(question_items[0], DOWN, buff=0.8, aligned_edge=LEFT)
        question_items[2].next_to(question_items[1], DOWN, buff=0.8, aligned_edge=LEFT)
        
        # Footer message
        footer = Text("Transparency protects your money.", font_size=32, color=GREEN,
                     weight=BOLD).move_to(DOWN * 3.5)
        footer_box = SurroundingRectangle(footer, color=GREEN, buff=0.2, stroke_width=2)
        
        # Search icon
        search_icon = self.load_png_icon("search", height=1.2).move_to(DOWN * 4.8)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(question_items[0], shift=RIGHT), run_time=step_time)
        self.play(FadeIn(question_items[1], shift=RIGHT), run_time=step_time)
        self.play(FadeIn(question_items[2], shift=RIGHT), run_time=step_time)
        # Highlight the number circles (num_group is first element in each item)
        self.play(
            question_items[0][0][0].animate.set_fill(GREEN, opacity=0.8),
            question_items[1][0][0].animate.set_fill(GREEN, opacity=0.8),
            question_items[2][0][0].animate.set_fill(GREEN, opacity=0.8),
            run_time=step_time
        )
        self.play(Write(footer), Create(footer_box), run_time=step_time)
        self.play(FadeIn(search_icon, shift=UP), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        'Subscribe to MoneyWise'
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        # Title
        title = Text("Subscribe for More", font=self.title_font, 
                    font_size=self.font_title_size, color=GOLD, line_spacing=1.1).move_to(UP * 3.5)
        
        # MoneyWise branding
        brand = Text("MoneyWise", font_size=56, color=GOLD, weight=BOLD).move_to(UP * 1.0)
        
        # Tagline
        tagline = Text("Smarter Financial Decisions,\nOne Lesson at a Time", 
                      font_size=32, color=WHITE, line_spacing=1.2).move_to(DOWN * 0.8)
        
        # CTA icons
        icon_like = self.load_png_icon("thumbs_up", height=1.5)
        icon_share = self.load_png_icon("share", height=1.5)
        icon_subscribe = self.load_png_icon("check", height=1.5)
        
        cta_icons = Group(icon_like, icon_share, icon_subscribe).arrange(RIGHT, buff=1.5).move_to(DOWN * 3.0)
        
        # Labels under icons
        label_like = Text("Like", font_size=24, color=WHITE)
        label_share = Text("Share", font_size=24, color=WHITE)
        label_subscribe = Text("Subscribe", font_size=24, color=GOLD)
        
        label_like.next_to(icon_like, DOWN, buff=0.3)
        label_share.next_to(icon_share, DOWN, buff=0.3)
        label_subscribe.next_to(icon_subscribe, DOWN, buff=0.3)
        
        labels = VGroup(label_like, label_share, label_subscribe)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            GrowFromCenter(brand),
            Write(tagline),
            run_time=step_time
        )
        self.play(
            LaggedStart(
                FadeIn(icon_like, scale=0.5),
                FadeIn(icon_share, scale=0.5),
                FadeIn(icon_subscribe, scale=0.5),
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        self.play(
            Write(labels),
            icon_subscribe.animate.scale(1.2),
            run_time=step_time
        )
        
        # No fade out at the end - hold the final frame
        self.wait(t_trans)
