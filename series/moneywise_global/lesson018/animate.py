import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson018VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 18: Debt Is a Tool Not a Trap
    How Smart People Use Borrowed Money to Build Wealth
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
        title_text = "The Debt\nParadox"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size, 
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Wealthy person with debt
        rich_icon = self.load_png_icon("businessman", height=2.0).move_to(LEFT * 2.5 + UP * 0.8)
        cash_icon = self.load_png_icon("money_bag", height=1.2).move_to(LEFT * 2.5 + DOWN * 1.0)
        
        # Question
        question = Text("Has cash...\nbut borrows anyway?", 
                       font_size=28, color=WHITE, line_spacing=1.2).move_to(RIGHT * 1.5 + UP * 0.8)
        question_mark = self.load_png_icon("question_mark", height=1.5).move_to(RIGHT * 2.5 + DOWN * 0.5)
        
        # Tool visual
        tool_icon = self.load_png_icon("tool", height=1.8).move_to(DOWN * 2.5)
        tool_label = Text("Debt = Tool", font_size=36, color=GOLD, weight=BOLD).move_to(DOWN * 4.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            FadeIn(rich_icon, shift=DOWN),
            FadeIn(cash_icon, shift=UP),
            run_time=step_time
        )
        self.play(
            Write(question),
            FadeIn(question_mark, scale=0.5),
            run_time=step_time
        )
        self.play(
            FadeIn(tool_icon, scale=0.5),
            run_time=step_time
        )
        self.play(Write(tool_label), run_time=step_time)
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
        title_text = "Good Debt vs\nBad Debt"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Good debt side
        good_header = Text("GOOD DEBT", font_size=28, color=GREEN, weight=BOLD)
        good_sub = Text("Puts money IN", font_size=20, color=GREEN)
        good_items = VGroup(
            Text("• Rental properties", font_size=20, color=WHITE),
            Text("• Business investment", font_size=20, color=WHITE),
            Text("• Education ROI", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        good_icon = self.load_png_icon("house", height=1.0)
        
        good_group = Group(good_header, good_sub, good_icon, good_items).arrange(DOWN, buff=0.2)
        good_box = SurroundingRectangle(good_group, color=GREEN, buff=0.3, stroke_width=2)
        good_section = Group(good_box, good_group).move_to(LEFT * 2.8 + UP * 0.3)
        
        # Bad debt side
        bad_header = Text("BAD DEBT", font_size=28, color=RED, weight=BOLD)
        bad_sub = Text("Takes money OUT", font_size=20, color=RED)
        bad_items = VGroup(
            Text("• Credit card spending", font_size=20, color=WHITE),
            Text("• Depreciating cars", font_size=20, color=WHITE),
            Text("• Vacation loans", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        bad_icon = self.load_png_icon("shopping_cart", height=1.0)
        
        bad_group = Group(bad_header, bad_sub, bad_icon, bad_items).arrange(DOWN, buff=0.2)
        bad_box = SurroundingRectangle(bad_group, color=RED, buff=0.3, stroke_width=2)
        bad_section = Group(bad_box, bad_group).move_to(RIGHT * 2.8 + UP * 0.3)
        
        # The test
        test_text = Text("The test: Does it\ngenerate returns?", 
                        font_size=30, color=GOLD, weight=BOLD, line_spacing=1.2).move_to(DOWN * 3.8)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            FadeIn(good_section, shift=RIGHT),
            run_time=step_time
        )
        self.play(
            FadeIn(bad_section, shift=LEFT),
            run_time=step_time
        )
        self.play(
            good_box.animate.set_fill(GREEN, opacity=0.1),
            bad_box.animate.set_fill(RED, opacity=0.1),
            run_time=step_time
        )
        self.play(Write(test_text), run_time=step_time)
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
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "The Power of\nLeverage"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Scenario 1: No leverage
        scenario1_header = Text("NO LEVERAGE", font_size=24, color=WHITE, weight=BOLD)
        scenario1_invest = Text("Invest: $100K (yours)", font_size=20, color=WHITE)
        scenario1_return = Text("Earn 10%: $10K", font_size=20, color=GREEN)
        scenario1_result = Text("Return: 10%", font_size=22, color=GREEN, weight=BOLD)
        scenario1 = VGroup(scenario1_header, scenario1_invest, scenario1_return, scenario1_result).arrange(DOWN, buff=0.15)
        scenario1_box = SurroundingRectangle(scenario1, color=WHITE, buff=0.25, stroke_width=2)
        scenario1_group = Group(scenario1_box, scenario1).move_to(LEFT * 2.8 + UP * 0.8)
        
        # Scenario 2: With leverage
        scenario2_header = Text("WITH LEVERAGE", font_size=24, color=GOLD, weight=BOLD)
        scenario2_invest = Text("Invest: $20K + $80K loan", font_size=20, color=WHITE)
        scenario2_return = Text("Earn 10%: $10K", font_size=20, color=GREEN)
        scenario2_result = Text("Return: 50%!", font_size=22, color=GOLD, weight=BOLD)
        scenario2 = VGroup(scenario2_header, scenario2_invest, scenario2_return, scenario2_result).arrange(DOWN, buff=0.15)
        scenario2_box = SurroundingRectangle(scenario2, color=GOLD, buff=0.25, stroke_width=2)
        scenario2_group = Group(scenario2_box, scenario2).move_to(RIGHT * 2.8 + UP * 0.8)
        
        # Arrow between
        arrow = Arrow(LEFT * 0.8 + UP * 0.8, RIGHT * 0.8 + UP * 0.8, color=GOLD, stroke_width=4)
        
        # Key insight
        insight = Text("Same profit,\n5x the return rate!", 
                      font_size=32, color=GOLD, weight=BOLD, line_spacing=1.2).move_to(DOWN * 2.5)
        rocket = self.load_png_icon("rocket", height=1.5).move_to(DOWN * 4.3)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(scenario1_group, shift=RIGHT), run_time=step_time)
        self.play(GrowArrow(arrow), run_time=step_time * 0.5)
        self.play(FadeIn(scenario2_group, shift=LEFT), run_time=step_time)
        self.play(
            scenario2_box.animate.set_fill(GOLD, opacity=0.15),
            run_time=step_time
        )
        self.play(
            Write(insight),
            FadeIn(rocket, shift=UP),
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
        title_text = "When Leverage\nMakes Sense"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Who benefits
        audiences = [
            ("Home Buyers", "Appreciating assets", "house"),
            ("Entrepreneurs", "Scale faster", "small_business"),
            ("Investors", "Amplify returns", "chart")
        ]
        
        audience_items = []
        for label, benefit, icon_name in audiences:
            icon = self.load_png_icon(icon_name, height=1.2)
            main_text = Text(label, font_size=26, color=WHITE, weight=BOLD)
            sub_text = Text(benefit, font_size=20, color=GREEN)
            text_group = VGroup(main_text, sub_text).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            item = Group(icon, text_group).arrange(RIGHT, buff=0.5)
            audience_items.append(item)
        
        audience_items[0].move_to(UP * 1.5)
        audience_items[1].move_to(DOWN * 0.3)
        audience_items[2].move_to(DOWN * 2.1)
        
        # Warning
        warning_icon = self.load_png_icon("warning", height=1.0).move_to(LEFT * 2.5 + DOWN * 4.0)
        warning_text = Text("Amplifies losses too!", 
                           font_size=26, color=ORANGE, weight=BOLD).move_to(RIGHT * 0.5 + DOWN * 4.0)
        
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
        self.play(
            FadeIn(warning_icon, scale=0.5),
            Write(warning_text),
            run_time=step_time
        )
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
        title_text = "Three Rules for\nSmart Debt"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        rules = [
            ("1", "Appreciating assets\nor income generators", GREEN, "increase"),
            ("2", "Return must exceed\ninterest cost", BLUE, "percentage"),
            ("3", "Never beyond what\nyou can lose", ORANGE, "shield")
        ]
        
        rule_items = []
        for num, text, color, icon_name in rules:
            num_circle = Circle(radius=0.45, color=color, fill_opacity=0.2, stroke_width=3)
            num_text = Text(num, font_size=30, color=color, weight=BOLD).move_to(num_circle)
            icon = self.load_png_icon(icon_name, height=0.9)
            rule_text = Text(text, font_size=22, color=WHITE, line_spacing=1.1)
            
            item = Group(num_circle, num_text, icon, rule_text).arrange(RIGHT, buff=0.25)
            rule_items.append((item, num_circle, color))
        
        positions = [UP * 1.5, DOWN * 0.5, DOWN * 2.5]
        for i, (item, _, _) in enumerate(rule_items):
            item.move_to(positions[i])
        
        # Bottom message
        footer_line1 = Text("Conservative = Wealth", font_size=28, color=GREEN, weight=BOLD)
        footer_line2 = Text("Aggressive = Nightmares", font_size=28, color=RED, weight=BOLD)
        footer = VGroup(footer_line1, footer_line2).arrange(DOWN, buff=0.2).move_to(DOWN * 4.3)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        
        for item, circle, color in rule_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=step_time)
        
        self.play(
            *[circle.animate.set_fill(color, opacity=0.4) for _, circle, color in rule_items],
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

        title = Text("Use Debt Wisely", font=self.title_font, 
                    font_size=self.font_title_size, color=GOLD, line_spacing=1.1).move_to(UP * 3.5)
        
        brand = Text("MoneyWise", font_size=56, color=GOLD, weight=BOLD).move_to(UP * 1.0)
        
        tool_icon = self.load_png_icon("tool", height=2.0).move_to(DOWN * 0.5)
        
        tagline = Text("Master the tool\nthat builds empires.", 
                      font_size=32, color=WHITE, line_spacing=1.2).move_to(DOWN * 2.5)
        
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
            FadeIn(tool_icon, scale=0.5),
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
