import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical

class Lesson003VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 003: How the Government Controls Your Money
    """

    def create_title(self, text, color=WHITE, max_width=6.5):
        """Create a title that fits within max_width, auto-scaling if needed."""
        # Start with default size
        font_size = self.font_title_size
        title = Text(text, font=self.title_font, font_size=font_size, color=color)
        
        # Scale down if too wide
        if title.width > max_width:
            scale_factor = max_width / title.width
            title.scale(scale_factor)
        
        return title.move_to(UP * 4.0)

    def build_scene_1(self, scene_data):
        """
        Scene 1: Hook / Pain Point
        Title: Why Your Interest Rates Keep Changing
        Script: Ever wonder why your savings account suddenly pays more interest, or why mortgage rates keep changing?
        """
        # 1. Setup Audio & Time
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 8.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        # 2. Visual Elements
        title_text = scene_data.get("h2_heading", "Interest Rates")
        title = self.create_title(title_text, color=self.COLOR_RISK)
        
        # Percentage symbol rising and falling
        percent_up = Text("↑ 5%", font=self.body_font, font_size=72, color=GREEN).move_to(LEFT * 2 + UP * 0.5)
        percent_down = Text("↓ 3%", font=self.body_font, font_size=72, color=RED).move_to(RIGHT * 2 + UP * 0.5)
        
        # Question mark (confusion)
        question = Text("?", font=self.body_font, font_size=120, color=YELLOW).move_to(DOWN * 1.5)
        
        bank_icon = self.load_png_icon("bank_building.png", height=2.0).move_to(DOWN * 2.5)

        # 3. Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(percent_up, shift=UP), FadeIn(percent_down, shift=DOWN), run_time=step_time)
        self.play(Write(question), run_time=step_time)
        self.play(FadeIn(bank_icon, shift=UP), run_time=step_time)
        self.play(Flash(bank_icon, color=GOLD, flash_radius=1.5), run_time=step_time)

        # 4. Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        Title: The Two Levers: Monetary and Fiscal Policy
        Script: The government manages the economy using two main tools. First, monetary policy...
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Two Levers")
        title = self.create_title(title_text, color=GOLD)
        
        # Left side: Monetary Policy (Fed)
        fed_icon = self.load_png_icon("bank.png", height=1.8).move_to(LEFT * 2.5 + UP * 1.0)
        fed_label = Text("Fed", font=self.body_font, font_size=36, color=WHITE).next_to(fed_icon, DOWN, buff=0.3)
        monetary_label = Text("Monetary\nPolicy", font=self.body_font, font_size=28, color=BLUE).next_to(fed_label, DOWN, buff=0.2)
        
        # Right side: Fiscal Policy (Congress)
        congress_icon = self.load_png_icon("policy_document.png", height=1.8).move_to(RIGHT * 2.5 + UP * 1.0)
        congress_label = Text("Congress", font=self.body_font, font_size=36, color=WHITE).next_to(congress_icon, DOWN, buff=0.3)
        fiscal_label = Text("Fiscal\nPolicy", font=self.body_font, font_size=28, color=GREEN).next_to(congress_label, DOWN, buff=0.2)
        
        # Metaphor
        metaphor = Text("Gas Pedal & Brake", font=self.body_font, font_size=40, color=YELLOW).move_to(DOWN * 2.5)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(fed_icon), Write(fed_label), run_time=step_time)
        self.play(Write(monetary_label), run_time=step_time)
        self.play(FadeIn(congress_icon), Write(congress_label), run_time=step_time)
        self.play(Write(fiscal_label), run_time=step_time)
        self.play(Write(metaphor), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        Title: Current Policy and Your Wallet
        Script: Here's what's happening right now: the Fed projects rates around 3.4% through 2026...
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Current Policy")
        title = self.create_title(title_text, color=self.COLOR_RISK)
        
        # Data display
        rate_box = VGroup(
            Text("Fed Rate 2026", font=self.body_font, font_size=32, color=WHITE),
            Text("3.4%", font=self.body_font, font_size=64, color=BLUE)
        ).arrange(DOWN, buff=0.3).move_to(LEFT * 2 + UP * 0.5)
        
        deficit_box = VGroup(
            Text("Deficit 2026", font=self.body_font, font_size=32, color=WHITE),
            Text("$1.7T", font=self.body_font, font_size=64, color=RED)
        ).arrange(DOWN, buff=0.3).move_to(RIGHT * 2 + UP * 0.5)
        
        # Impact icons
        mortgage_icon = self.load_png_icon("house.png", height=1.2).move_to(LEFT * 2.5 + DOWN * 2)
        loan_icon = self.load_png_icon("loan.png", height=1.2).move_to(ORIGIN + DOWN * 2)
        job_icon = self.load_png_icon("businessman.png", height=1.2).move_to(RIGHT * 2.5 + DOWN * 2)
        
        impact_text = Text("Your mortgage, loans, and job", font=self.body_font, font_size=28, color=YELLOW).move_to(DOWN * 3.5)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(rate_box, shift=DOWN), run_time=step_time)
        self.play(FadeIn(deficit_box, shift=DOWN), run_time=step_time)
        self.play(FadeIn(mortgage_icon), FadeIn(loan_icon), FadeIn(job_icon), run_time=step_time)
        self.play(Write(impact_text), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        Title: Who Needs to Pay Attention
        Script: If you have a mortgage, carry any debt, invest in stocks, or simply want job security...
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 8.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Who Needs This")
        title = self.create_title(title_text, color=ORANGE)
        
        # Icons representing different groups
        homeowner = Group(
            self.load_png_icon("house.png", height=1.5),
            Text("Homeowners", font=self.body_font, font_size=24)
        ).arrange(DOWN, buff=0.3).move_to(LEFT * 2.5 + UP * 0.5)
        
        debtor = Group(
            self.load_png_icon("credit_card.png", height=1.5),
            Text("Debt Holders", font=self.body_font, font_size=24)
        ).arrange(DOWN, buff=0.3).move_to(RIGHT * 2.5 + UP * 0.5)
        
        investor = Group(
            self.load_png_icon("stocks.png", height=1.5),
            Text("Investors", font=self.body_font, font_size=24)
        ).arrange(DOWN, buff=0.3).move_to(LEFT * 2.5 + DOWN * 2)
        
        worker = Group(
            self.load_png_icon("businessman.png", height=1.5),
            Text("Workers", font=self.body_font, font_size=24)
        ).arrange(DOWN, buff=0.3).move_to(RIGHT * 2.5 + DOWN * 2)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(homeowner, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(debtor, shift=LEFT), run_time=step_time)
        self.play(FadeIn(investor, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(worker, shift=LEFT), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        Title: Three Steps to Stay Ahead
        Script: Here's your action plan: First, follow Fed announcements...
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 12.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "3 Steps")
        title = self.create_title(title_text, color=GREEN)
        
        # Checklist items
        items = Group()
        
        # 1. Follow Fed
        row1 = Group(
            self.load_png_icon("calendar.png", height=0.8),
            Text("Follow Fed Announcements", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5)
        
        # 2. Lock rates
        row2 = Group(
            self.load_png_icon("lock.png", height=0.8),
            Text("Lock in Fixed Rates", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5)
        
        # 3. Know sectors
        row3 = Group(
            self.load_png_icon("chart.png", height=0.8),
            Text("Track Benefiting Sectors", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5)
        
        items.add(row1, row2, row3)
        items.arrange(DOWN, buff=0.8).move_to(DOWN * 0.5)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(row1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(row2, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(row3, shift=RIGHT), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        Title: Stay MoneyWise
        Script: Want to stay ahead of economic shifts? Subscribe to MoneyWise...
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 8.0
        t_trans = self.transition_time
        
        N = 3
        step_time = (page_duration - t_trans) / N

        title = self.create_title("Stay MoneyWise", color=GOLD).move_to(UP * 3.5)
        
        # Use light bulb icon for wisdom/insight
        bulb = self.load_png_icon("light_bulb.png", height=2.5).move_to(UP * 0.5)
        sub_text = Text("Subscribe for More", font=self.body_font, font_size=40, color=WHITE).next_to(bulb, DOWN, buff=0.5)
        
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(bulb, scale=0.5), Write(sub_text), run_time=step_time)
        self.play(bulb.animate.scale(1.1), Flash(bulb, color=GOLD, flash_radius=1.8), run_time=step_time)
        
        self.wait(step_time)
