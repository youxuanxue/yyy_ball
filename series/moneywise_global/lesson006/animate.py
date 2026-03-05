import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical

class Lesson006VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 006: Who Regulates Your Money? Understanding Financial Regulators
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
        Title: Who's Really Protecting Your Money?
        Script: Ever wonder who's actually watching over your money?
        """
        # 1. Setup Audio & Time
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 8.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        # 2. Visual Elements
        title_text = scene_data.get("h2_heading", "Protecting Your Money")
        title = self.create_title(title_text, color=self.COLOR_RISK)
        
        # Money with shield protection
        money_icon = self.load_png_icon("stack_of_money.png", height=2.0).move_to(UP * 0.5)
        
        # Question marks around
        q1 = Text("?", font=self.body_font, font_size=60, color=YELLOW).move_to(LEFT * 2.5 + UP * 1)
        q2 = Text("?", font=self.body_font, font_size=60, color=YELLOW).move_to(RIGHT * 2.5 + UP * 1)
        
        # Shield appearing
        shield = self.load_png_icon("shield.png", height=1.5).move_to(DOWN * 1.5)
        protect_text = Text("Who's Watching?", font=self.body_font, font_size=36, color=GOLD).move_to(DOWN * 3)

        # 3. Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(money_icon, shift=DOWN), run_time=step_time)
        self.play(Write(q1), Write(q2), run_time=step_time)
        self.play(FadeIn(shield, shift=UP), run_time=step_time)
        self.play(Write(protect_text), Flash(shield, color=GREEN, flash_radius=1.2), run_time=step_time)

        # 4. Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        Title: The Big Three Financial Regulators Explained
        Script: Think of financial regulators as referees in a game...
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Big Three Regulators")
        title = self.create_title(title_text, color=GOLD)
        
        # Three regulators as pillars
        # Federal Reserve
        fed = Group(
            self.load_png_icon("bank_building.png", height=1.2),
            Text("Federal Reserve", font=self.body_font, font_size=22, color=BLUE),
            Text("Money & Rates", font=self.body_font, font_size=18, color=GRAY)
        ).arrange(DOWN, buff=0.2).move_to(LEFT * 2.5 + UP * 0.5)
        
        # SEC
        sec = Group(
            self.load_png_icon("stocks.png", height=1.2),
            Text("SEC", font=self.body_font, font_size=22, color=GREEN),
            Text("Investments", font=self.body_font, font_size=18, color=GRAY)
        ).arrange(DOWN, buff=0.2).move_to(ORIGIN + UP * 0.5)
        
        # FDIC
        fdic = Group(
            self.load_png_icon("safe.png", height=1.2),
            Text("FDIC", font=self.body_font, font_size=22, color=ORANGE),
            Text("Bank Deposits", font=self.body_font, font_size=18, color=GRAY)
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 2.5 + UP * 0.5)
        
        # Together they protect
        together = Text("Together: Stability & Protection", font=self.body_font, font_size=28, color=GOLD).move_to(DOWN * 2.5)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(fed, shift=DOWN), run_time=step_time)
        self.play(FadeIn(sec, shift=DOWN), run_time=step_time)
        self.play(FadeIn(fdic, shift=DOWN), run_time=step_time)
        self.play(Write(together), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        Title: How Regulators Protect Your Wealth
        Script: The FDIC insures your deposits up to $250,000...
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Protection for You")
        title = self.create_title(title_text, color=self.COLOR_RISK)
        
        # FDIC protection highlight
        fdic_box = VGroup(
            Text("FDIC Insurance", font=self.body_font, font_size=32, color=GREEN),
            Text("$250,000", font=self.body_font, font_size=56, color=GOLD),
            Text("per depositor, per bank", font=self.body_font, font_size=22, color=GRAY)
        ).arrange(DOWN, buff=0.2).move_to(UP * 1)
        
        # Shield around it
        shield_rect = SurroundingRectangle(fdic_box, color=GREEN, buff=0.3, corner_radius=0.2)
        
        # SEC disclosure
        sec_text = VGroup(
            Text("SEC Requires:", font=self.body_font, font_size=28, color=BLUE),
            Text("Risk Disclosure", font=self.body_font, font_size=24, color=WHITE)
        ).arrange(DOWN, buff=0.1).move_to(DOWN * 2)
        
        # Protected text
        protected = Text("Your savings are protected!", font=self.body_font, font_size=30, color=GOLD).move_to(DOWN * 3.5)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(fdic_box, shift=DOWN), run_time=step_time)
        self.play(Create(shield_rect), run_time=step_time)
        self.play(FadeIn(sec_text, shift=UP), run_time=step_time)
        self.play(Write(protected), Flash(fdic_box, color=GREEN, flash_radius=1.5), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        Title: Why Every Saver and Investor Should Care
        Script: This applies to everyone with a bank account...
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 8.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Who Should Care")
        title = self.create_title(title_text, color=ORANGE)
        
        # Different types of people
        saver = Group(
            self.load_png_icon("deposit.png", height=1.2),
            Text("Bank Account", font=self.body_font, font_size=24),
            Text("Holders", font=self.body_font, font_size=24)
        ).arrange(DOWN, buff=0.2).move_to(LEFT * 2.5 + UP * 0.5)
        
        investor = Group(
            self.load_png_icon("stocks.png", height=1.2),
            Text("Stock", font=self.body_font, font_size=24),
            Text("Investors", font=self.body_font, font_size=24)
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 2.5 + UP * 0.5)
        
        retiree = Group(
            self.load_png_icon("pensioner.png", height=1.2),
            Text("Retirement", font=self.body_font, font_size=24),
            Text("Savers", font=self.body_font, font_size=24)
        ).arrange(DOWN, buff=0.2).move_to(ORIGIN + DOWN * 2)

        everyone = Text("= Everyone!", font=self.body_font, font_size=40, color=GOLD).move_to(DOWN * 3.5)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(saver, shift=RIGHT), FadeIn(investor, shift=LEFT), run_time=step_time)
        self.play(FadeIn(retiree, shift=UP), run_time=step_time)
        self.play(Write(everyone), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        Title: Three Steps to Maximize Your Protection
        Script: Verify your bank is FDIC insured...
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 12.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Maximize Protection")
        title = self.create_title(title_text, color=GREEN)
        
        # Checklist items
        row1 = Group(
            self.load_png_icon("check_mark.png", height=0.8),
            Text("Verify FDIC Insurance", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5).move_to(UP * 1.5)
        
        row2 = Group(
            self.load_png_icon("check_mark.png", height=0.8),
            Text("Check SEC Registration", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5).move_to(ORIGIN)
        
        row3 = Group(
            self.load_png_icon("check_mark.png", height=0.8),
            Text("Stay Under $250K/Bank", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 1.5)
        
        # Result
        result = Text("Knowledge = Protection", font=self.body_font, font_size=36, color=GOLD).move_to(DOWN * 3)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(row1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(row2, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(row3, shift=RIGHT), Write(result), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        Title: Stay MoneyWise
        Script: Want to understand how the financial system really works?
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
