import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical

class Lesson004VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 004: Bank Tiers Explained - Choose the Right Bank for You
    """

    def create_title(self, text, color=WHITE, max_width=6.5):
        """Create a title that fits within max_width, auto-scaling if needed."""
        font_size = self.font_title_size
        title = Text(text, font=self.title_font, font_size=font_size, color=color)
        
        if title.width > max_width:
            scale_factor = max_width / title.width
            title.scale(scale_factor)
        
        return title.move_to(UP * 4.0)

    def build_scene_1(self, scene_data):
        """
        Scene 1: Hook / Pain Point
        Title: Why Your Bank Choice Matters More Than You Think
        Script: Ever walked into a bank and wondered if you're getting the best deal?
        """
        # 1. Setup Audio & Time
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 8.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        # 2. Visual Elements
        title_text = scene_data.get("h2_heading", "Bank Choice Matters")
        title = self.create_title(title_text, color=self.COLOR_RISK)
        
        # Bank building with question mark
        bank_icon = self.load_png_icon("bank_building.png", height=2.5).move_to(UP * 0.5)
        
        # Hidden fees text
        fee_text = Text("Hidden Fees?", font=self.body_font, font_size=40, color=RED).move_to(LEFT * 2 + DOWN * 1.5)
        rate_text = Text("Low Rates?", font=self.body_font, font_size=40, color=RED).move_to(RIGHT * 2 + DOWN * 1.5)
        
        # Dollar signs flying away
        dollar = Text("$$$", font=self.body_font, font_size=48, color=GREEN).move_to(DOWN * 3)

        # 3. Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(bank_icon, shift=DOWN), run_time=step_time)
        self.play(FadeIn(fee_text, shift=RIGHT), FadeIn(rate_text, shift=LEFT), run_time=step_time)
        self.play(Write(dollar), run_time=step_time)
        self.play(dollar.animate.shift(UP * 0.5).set_opacity(0.3), Flash(bank_icon, color=RED, flash_radius=1.5), run_time=step_time)

        # 4. Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        Title: The Four Types of Banks Explained
        Script: Think of banks like a pyramid. At the top, you have the big national banks...
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Four Bank Types")
        title = self.create_title(title_text, color=GOLD)
        
        # Pyramid structure - 4 tiers
        # Top: Big National Banks
        tier1 = Group(
            self.load_png_icon("bank_building.png", height=1.0),
            Text("Big Banks", font=self.body_font, font_size=28, color=BLUE)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.0)
        
        # Second: Regional Banks
        tier2 = Group(
            self.load_png_icon("business_building.png", height=1.0),
            Text("Regional Banks", font=self.body_font, font_size=28, color=GREEN)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 0.5)
        
        # Third: Credit Unions
        tier3 = Group(
            self.load_png_icon("people.png", height=1.0),
            Text("Credit Unions", font=self.body_font, font_size=28, color=ORANGE)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 1.0)
        
        # Fourth: Online Banks
        tier4 = Group(
            self.load_png_icon("mobile.png", height=1.0),
            Text("Online Banks", font=self.body_font, font_size=28, color=PURPLE)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.5)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(tier1, shift=DOWN), run_time=step_time)
        self.play(FadeIn(tier2, shift=DOWN), run_time=step_time)
        self.play(FadeIn(tier3, shift=DOWN), run_time=step_time)
        self.play(FadeIn(tier4, shift=DOWN), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        Title: How Different Banks Affect Your Wallet
        Script: Big banks have convenience but often pay the lowest interest rates...
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Impact on Wallet")
        title = self.create_title(title_text, color=self.COLOR_RISK)
        
        # Comparison: Big Bank vs Online Bank rates
        big_bank_box = VGroup(
            Text("Big Bank", font=self.body_font, font_size=32, color=BLUE),
            Text("0.01%", font=self.body_font, font_size=56, color=RED),
            Text("savings rate", font=self.body_font, font_size=24, color=GRAY)
        ).arrange(DOWN, buff=0.2).move_to(LEFT * 2.5 + UP * 0.5)
        
        online_bank_box = VGroup(
            Text("Online Bank", font=self.body_font, font_size=32, color=PURPLE),
            Text("4.5%", font=self.body_font, font_size=56, color=GREEN),
            Text("savings rate", font=self.body_font, font_size=24, color=GRAY)
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 2.5 + UP * 0.5)
        
        # Arrow showing difference
        vs_text = Text("vs", font=self.body_font, font_size=40, color=WHITE).move_to(UP * 0.5)
        
        # Impact text
        impact = Text("10x Higher Interest!", font=self.body_font, font_size=36, color=GOLD).move_to(DOWN * 2.5)
        rect = SurroundingRectangle(impact, color=GOLD, buff=0.2)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(big_bank_box, shift=RIGHT), run_time=step_time)
        self.play(Write(vs_text), FadeIn(online_bank_box, shift=LEFT), run_time=step_time)
        self.play(Write(impact), Create(rect), run_time=step_time)
        self.play(Flash(online_bank_box, color=GREEN, flash_radius=1.5), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        Title: Which Bank Type Matches Your Lifestyle
        Script: If you value face-to-face service... online banks shine... credit unions are your match.
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 8.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Find Your Match")
        title = self.create_title(title_text, color=ORANGE)
        
        # Three personas with matching bank types
        persona1 = Group(
            self.load_png_icon("customer_support.png", height=1.2),
            Text("Need Service?", font=self.body_font, font_size=24),
            Text("→ Traditional", font=self.body_font, font_size=24, color=BLUE)
        ).arrange(DOWN, buff=0.2).move_to(LEFT * 2.5 + UP * 0.5)
        
        persona2 = Group(
            self.load_png_icon("growing_money.png", height=1.2),
            Text("Want Rates?", font=self.body_font, font_size=24),
            Text("→ Online", font=self.body_font, font_size=24, color=PURPLE)
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 2.5 + UP * 0.5)
        
        persona3 = Group(
            self.load_png_icon("family.png", height=1.2),
            Text("Community?", font=self.body_font, font_size=24),
            Text("→ Credit Union", font=self.body_font, font_size=24, color=ORANGE)
        ).arrange(DOWN, buff=0.2).move_to(ORIGIN + DOWN * 2)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(persona1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(persona2, shift=LEFT), run_time=step_time)
        self.play(FadeIn(persona3, shift=UP), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        Title: Three Steps to Finding Your Perfect Bank
        Script: First, check if your current bank is FDIC insured...
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 12.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "3 Steps")
        title = self.create_title(title_text, color=GREEN)
        
        # Checklist items
        # 1. Check FDIC
        row1 = Group(
            self.load_png_icon("shield.png", height=0.9),
            Text("Check FDIC Insurance", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5).move_to(UP * 1.5)
        
        # 2. Compare rates
        row2 = Group(
            self.load_png_icon("analytics.png", height=0.9),
            Text("Compare Interest Rates", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5).move_to(ORIGIN)
        
        # 3. Calculate fees
        row3 = Group(
            self.load_png_icon("calculator.png", height=0.9),
            Text("Calculate Annual Fees", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 1.5)
        
        # Result
        result = Text("Save $100s/year!", font=self.body_font, font_size=36, color=GOLD).move_to(DOWN * 3)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(row1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(row2, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(row3, shift=RIGHT), Write(result), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        Title: Stay MoneyWise
        Script: Ready to make smarter money moves? Subscribe for more tips...
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 8.0
        t_trans = self.transition_time
        
        N = 3
        step_time = (page_duration - t_trans) / N

        title = self.create_title("Stay MoneyWise", color=GOLD).move_to(UP * 3.5)
        
        # Light bulb icon for wisdom
        bulb = self.load_png_icon("light_bulb.png", height=2.5).move_to(UP * 0.5)
        sub_text = Text("Subscribe for More", font=self.body_font, font_size=40, color=WHITE).next_to(bulb, DOWN, buff=0.5)
        
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(bulb, scale=0.5), Write(sub_text), run_time=step_time)
        self.play(bulb.animate.scale(1.1), Flash(bulb, color=GOLD, flash_radius=1.8), run_time=step_time)
        
        self.wait(step_time)
