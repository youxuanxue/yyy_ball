import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson009VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 9: How the Stock Market Really Works
    Understanding IPOs, P/E Ratios, and What Drives Stock Prices
    """

    def build_scene_1(self, scene_data):
        """
        Scene 1: Hook / Pain Point
        'Ever wonder why companies bother going public?'
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title - wrap for vertical display
        title_text = "The Real Reason\nCompanies Go Public"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size, 
                    color=self.COLOR_RISK, line_spacing=1.1).move_to(UP * 4.0)
        
        # Visual: Company building with money flowing in
        company_icon = self.load_png_icon("company", height=2.5).move_to(LEFT * 2.0 + UP * 0.5)
        
        # Money icons flowing towards company
        money_icons = Group()
        positions = [RIGHT * 3 + UP * 1.5, RIGHT * 2.5 + DOWN * 0.5, RIGHT * 3.5 + UP * 0.3]
        for pos in positions:
            m = self.load_png_icon("money", height=1.0).move_to(pos)
            money_icons.add(m)
        
        # Arrow from public to company
        arrow = Arrow(start=RIGHT * 1.5, end=LEFT * 0.5 + UP * 0.5, 
                     color=GREEN, stroke_width=6, buff=0.3).move_to(UP * 0.5)
        
        # Key insight text
        insight_text = Text("Access to other\npeople's money", 
                           font_size=36, color=GOLD, weight=BOLD, 
                           line_spacing=1.2).move_to(DOWN * 2.5)
        
        # "Legally, at scale" text
        scale_text = Text("Legally. At Scale. Forever.", 
                         font_size=30, color=WHITE).move_to(DOWN * 4.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(company_icon, shift=RIGHT), run_time=step_time)
        self.play(
            LaggedStart(
                *[FadeIn(m, shift=LEFT) for m in money_icons],
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        self.play(GrowArrow(arrow), run_time=step_time)
        self.play(Write(insight_text), run_time=step_time)
        self.play(Write(scale_text), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        'An IPO solves two big problems: visibility and accessibility.'
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "What an IPO\nActually Does"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Problem 1: Visibility
        problem1_box = RoundedRectangle(width=3.5, height=3.5, corner_radius=0.2,
                                        color=BLUE_B, fill_opacity=0.3, stroke_width=3)
        problem1_icon = self.load_png_icon("globe", height=1.2)
        problem1_label = Text("Problem #1", font_size=22, color=LIGHT_GRAY)
        problem1_title = Text("Visibility", font_size=28, color=WHITE, weight=BOLD)
        problem1_desc = Text("World knows\nabout you", font_size=20, color=GREEN, line_spacing=1.1)
        
        problem1_content = Group(problem1_icon, problem1_label, problem1_title, problem1_desc).arrange(DOWN, buff=0.25)
        problem1_content.move_to(problem1_box)
        problem1_group = Group(problem1_box, problem1_content).move_to(LEFT * 2.5 + UP * 0.5)
        
        # Problem 2: Accessibility
        problem2_box = RoundedRectangle(width=3.5, height=3.5, corner_radius=0.2,
                                        color=GREEN_B, fill_opacity=0.3, stroke_width=3)
        problem2_icon = self.load_png_icon("handshake", height=1.2)
        problem2_label = Text("Problem #2", font_size=22, color=LIGHT_GRAY)
        problem2_title = Text("Accessibility", font_size=28, color=WHITE, weight=BOLD)
        problem2_desc = Text("Easy to buy\nyour stock", font_size=20, color=GREEN, line_spacing=1.1)
        
        problem2_content = Group(problem2_icon, problem2_label, problem2_title, problem2_desc).arrange(DOWN, buff=0.25)
        problem2_content.move_to(problem2_box)
        problem2_group = Group(problem2_box, problem2_content).move_to(RIGHT * 2.5 + UP * 0.5)
        
        # Equals sign and result
        equals = Text("=", font_size=60, color=WHITE).move_to(DOWN * 2.5)
        
        # Result: Superpower
        result_icon = self.load_png_icon("investment", height=1.5).move_to(DOWN * 3.8)
        result_text = Text("A Capital Superpower", font_size=32, color=GOLD, 
                          weight=BOLD).move_to(DOWN * 5.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(problem1_group, shift=UP), run_time=step_time)
        self.play(FadeIn(problem2_group, shift=UP), run_time=step_time)
        self.play(
            problem1_box.animate.set_stroke(color=BLUE, width=4),
            problem2_box.animate.set_stroke(color=GREEN, width=4),
            run_time=step_time
        )
        self.play(Write(equals), run_time=step_time)
        self.play(FadeIn(result_icon, shift=UP), run_time=step_time)
        self.play(Write(result_text), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        'Going public transforms how a company is valued.'
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title - wrap long title
        title_text = "Why Being Public\nChanges Everything"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Comparison: Private vs Public company valuation
        # Private Company
        private_box = RoundedRectangle(width=3.5, height=4.0, corner_radius=0.2,
                                       color=GRAY, fill_opacity=0.2, stroke_width=3)
        private_label = Text("Private\nCompany", font_size=26, color=WHITE, 
                            weight=BOLD, line_spacing=1.0)
        private_earnings = Text("Earns: $1M/year", font_size=20, color=LIGHT_GRAY)
        private_value = Text("Value: $1-2M", font_size=24, color=RED)
        
        private_content = VGroup(private_label, private_earnings, private_value).arrange(DOWN, buff=0.4)
        private_content.move_to(private_box)
        private_group = VGroup(private_box, private_content).move_to(LEFT * 2.5 + UP * 0.8)
        
        # Arrow transformation
        transform_arrow = Arrow(start=LEFT * 0.5, end=RIGHT * 0.5, 
                               color=GOLD, stroke_width=6).move_to(UP * 0.8)
        transform_text = Text("Goes\nPublic", font_size=20, color=GOLD,
                             line_spacing=1.0).next_to(transform_arrow, UP, buff=0.2)
        
        # Public Company
        public_box = RoundedRectangle(width=3.5, height=4.0, corner_radius=0.2,
                                      color=GREEN_B, fill_opacity=0.3, stroke_width=3)
        public_label = Text("Public\nCompany", font_size=26, color=WHITE, 
                           weight=BOLD, line_spacing=1.0)
        public_earnings = Text("Earns: $1M/year", font_size=20, color=LIGHT_GRAY)
        public_value = Text("Value: $20-30M", font_size=24, color=GREEN, weight=BOLD)
        public_pe = Text("(20-30x P/E)", font_size=18, color=GOLD)
        
        public_content = VGroup(public_label, public_earnings, public_value, public_pe).arrange(DOWN, buff=0.3)
        public_content.move_to(public_box)
        public_group = VGroup(public_box, public_content).move_to(RIGHT * 2.5 + UP * 0.8)
        
        # P/E Ratio explanation
        pe_text = Text("P/E Ratio = Price ÷ Earnings", 
                      font_size=28, color=WHITE).move_to(DOWN * 2.2)
        
        # Key insight
        insight = Text("Market pays for\nfuture potential", 
                      font_size=32, color=GOLD, weight=BOLD,
                      line_spacing=1.2).move_to(DOWN * 3.8)
        insight_box = SurroundingRectangle(insight, color=GOLD, buff=0.25, stroke_width=2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(private_group, shift=RIGHT), run_time=step_time)
        self.play(GrowArrow(transform_arrow), Write(transform_text), run_time=step_time)
        self.play(FadeIn(public_group, shift=LEFT), run_time=step_time)
        self.play(
            public_box.animate.set_stroke(color=GREEN, width=4),
            Flash(public_value, color=GREEN),
            run_time=step_time
        )
        self.play(Write(pe_text), run_time=step_time)
        self.play(Write(insight), Create(insight_box), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        'Understanding what drives stock prices helps you invest smarter.'
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "What This Means\nfor Your Portfolio"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # What drives stock prices - ranked list
        factors = [
            ("1", "Market Conditions", "Bull vs Bear Market", BLUE),
            ("2", "Sector Trends", "Hot industries", GREEN),
            ("3", "News & Sentiment", "Headlines move prices", ORANGE),
            ("4", "Fundamentals", "Actual business value", GOLD)
        ]
        
        factor_items = []
        
        for num, factor_name, desc, color in factors:
            # Number
            num_circle = Circle(radius=0.4, color=color, fill_opacity=0.8, stroke_width=0)
            num_text = Text(num, font_size=32, color=BLACK, weight=BOLD).move_to(num_circle)
            num_group = VGroup(num_circle, num_text)
            
            # Factor name and description
            factor_title = Text(factor_name, font_size=26, color=WHITE, weight=BOLD)
            factor_desc = Text(desc, font_size=20, color=LIGHT_GRAY)
            text_group = VGroup(factor_title, factor_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            
            item = Group(num_group, text_group).arrange(RIGHT, buff=0.5)
            factor_items.append(item)
        
        # Position items
        for i, item in enumerate(factor_items):
            item.move_to(UP * (2.0 - i * 1.5) + LEFT * 0.5)
        
        # Warning message
        warning = Text("Price ≠ Value", font_size=36, color=RED, weight=BOLD).move_to(DOWN * 3.5)
        warning_box = SurroundingRectangle(warning, color=RED, buff=0.2, stroke_width=2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT) for item in factor_items],
                lag_ratio=0.4
            ),
            run_time=step_time * 2
        )
        # Highlight the order
        self.play(
            *[item[0][0].animate.set_fill(opacity=1.0) for item in factor_items],
            run_time=step_time
        )
        self.play(Write(warning), Create(warning_box), run_time=step_time)
        self.play(Flash(warning_box, color=RED), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        'When evaluating any stock, check the P/E ratio first.'
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "How to Evaluate\nStocks Like a Pro"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Checklist items
        checklist = [
            ("Check P/E Ratio", "Compare to industry average", "analytics"),
            ("High P/E", "Paying premium for growth", "increase"),
            ("Low P/E", "Value opportunity or problems", "decrease"),
            ("Hold Long-Term", "Ignore daily noise", "target")
        ]
        
        check_items = []
        
        for title_txt, desc, icon_name in checklist:
            # Checkbox
            checkbox = Square(side_length=0.5, color=GREEN, fill_opacity=0, stroke_width=3)
            checkmark = Text("✓", font_size=30, color=GREEN, weight=BOLD).move_to(checkbox)
            check_group = VGroup(checkbox, checkmark)
            checkmark.set_opacity(0)  # Hidden initially
            
            # Text
            item_title = Text(title_txt, font_size=26, color=WHITE, weight=BOLD)
            item_desc = Text(desc, font_size=20, color=LIGHT_GRAY)
            text_group = VGroup(item_title, item_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            
            # Icon
            icon = self.load_png_icon(icon_name, height=0.8)
            
            item = Group(check_group, text_group, icon).arrange(RIGHT, buff=0.4)
            check_items.append((item, checkmark))
        
        # Position items
        for i, (item, _) in enumerate(check_items):
            item.move_to(UP * (2.0 - i * 1.5) + LEFT * 0.3)
        
        # Footer message
        footer = Text("Focus on businesses\nyou understand", 
                     font_size=30, color=GREEN, weight=BOLD,
                     line_spacing=1.2).move_to(DOWN * 4.2)
        footer_box = SurroundingRectangle(footer, color=GREEN, buff=0.2, stroke_width=2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        
        # Show items one by one with checkmarks
        for item, checkmark in check_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=step_time * 0.7)
            self.play(checkmark.animate.set_opacity(1), run_time=step_time * 0.3)
        
        self.play(Write(footer), Create(footer_box), run_time=step_time)
        self.play(Flash(footer_box, color=GREEN), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        'Follow MoneyWise for weekly insights.'
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
        tagline = Text("Understanding Markets\nis Financial Freedom", 
                      font_size=36, color=WHITE, line_spacing=1.2).move_to(DOWN * 0.8)
        
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
