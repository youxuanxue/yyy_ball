import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical

class Lesson005VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 005: Will Housing Prices Crash? The Truth About Real Estate
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
        Title: The Housing Crash Everyone Keeps Waiting For
        Script: Are you waiting for a housing crash before you buy?
        """
        # 1. Setup Audio & Time
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 8.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        # 2. Visual Elements
        title_text = scene_data.get("h2_heading", "Housing Crash")
        title = self.create_title(title_text, color=self.COLOR_RISK)
        
        # House with question mark - waiting for crash
        house_icon = self.load_png_icon("house.png", height=2.0).move_to(UP * 0.5)
        
        # Crash arrow pointing down
        crash_arrow = Arrow(start=UP * 0.5, end=DOWN * 1.5, color=RED, stroke_width=8).next_to(house_icon, RIGHT, buff=0.5)
        crash_text = Text("Crash?", font=self.body_font, font_size=40, color=RED).next_to(crash_arrow, RIGHT, buff=0.3)
        
        # Question mark for waiting
        wait_text = Text("Still Waiting...", font=self.body_font, font_size=36, color=ORANGE).move_to(DOWN * 2.5)
        hourglass = self.load_png_icon("hourglass.png", height=1.2).next_to(wait_text, LEFT, buff=0.3)

        # 3. Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(house_icon, shift=DOWN), run_time=step_time)
        self.play(GrowArrow(crash_arrow), Write(crash_text), run_time=step_time)
        self.play(FadeIn(hourglass), Write(wait_text), run_time=step_time)
        self.play(Flash(house_icon, color=GOLD, flash_radius=1.5), run_time=step_time)

        # 4. Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        Title: Why Real Estate Behaves Differently Than Stocks
        Script: Real estate isn't like stocks. It's deeply tied to government policy...
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Real Estate vs Stocks")
        title = self.create_title(title_text, color=GOLD)
        
        # Three pillars supporting real estate
        # House at top
        house = self.load_png_icon("real_estate.png", height=1.5).move_to(UP * 1.5)
        
        # Three pillars
        pillar1 = Group(
            self.load_png_icon("bank_building.png", height=1.0),
            Text("Government", font=self.body_font, font_size=20)
        ).arrange(DOWN, buff=0.2).move_to(LEFT * 2.5 + DOWN * 1)
        
        pillar2 = Group(
            self.load_png_icon("bank.png", height=1.0),
            Text("Banks", font=self.body_font, font_size=20)
        ).arrange(DOWN, buff=0.2).move_to(ORIGIN + DOWN * 1)
        
        pillar3 = Group(
            self.load_png_icon("family.png", height=1.0),
            Text("Families", font=self.body_font, font_size=20)
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 2.5 + DOWN * 1)
        
        # Support text
        support = Text("Powerful Forces Resist Crashes", font=self.body_font, font_size=28, color=GREEN).move_to(DOWN * 3)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(house, shift=DOWN), run_time=step_time)
        self.play(FadeIn(pillar1, shift=UP), FadeIn(pillar2, shift=UP), FadeIn(pillar3, shift=UP), run_time=step_time)
        self.play(Write(support), run_time=step_time)
        self.play(house.animate.scale(1.1), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        Title: Why Governments Don't Let Housing Markets Collapse
        Script: Governments have strong incentives to prevent housing crashes...
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Government Protection")
        title = self.create_title(title_text, color=self.COLOR_RISK)
        
        # If crash -> consequences
        crash_scenario = VGroup(
            Text("If Housing Crashes:", font=self.body_font, font_size=32, color=RED),
        ).move_to(UP * 2)
        
        # Consequences icons
        consequence1 = Group(
            self.load_png_icon("bank.png", height=1.0),
            Text("Bank Failures", font=self.body_font, font_size=22, color=RED)
        ).arrange(DOWN, buff=0.2).move_to(LEFT * 2.5 + UP * 0.2)
        
        consequence2 = Group(
            self.load_png_icon("pensioner.png", height=1.0),
            Text("Retirement Lost", font=self.body_font, font_size=22, color=RED)
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 2.5 + UP * 0.2)
        
        # Solution: Shield
        solution = Group(
            self.load_png_icon("shield.png", height=1.5),
            Text("Central Bank Intervenes", font=self.body_font, font_size=28, color=GREEN)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 2)
        
        rect = SurroundingRectangle(solution, color=GREEN, buff=0.2)

        self.play(Write(title), run_time=step_time)
        self.play(Write(crash_scenario[0]), run_time=step_time)
        self.play(FadeIn(consequence1, shift=DOWN), FadeIn(consequence2, shift=DOWN), run_time=step_time)
        self.play(FadeIn(solution, shift=UP), run_time=step_time)
        self.play(Create(rect), Flash(solution, color=GREEN, flash_radius=1.5), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        Title: Who Needs to Rethink Their Housing Strategy
        Script: If you're renting while waiting for a crash...
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 8.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Who This Affects")
        title = self.create_title(title_text, color=ORANGE)
        
        # Three personas
        renter = Group(
            self.load_png_icon("user.png", height=1.2),
            Text("Renters", font=self.body_font, font_size=24),
            Text("Losing equity", font=self.body_font, font_size=20, color=RED)
        ).arrange(DOWN, buff=0.2).move_to(LEFT * 2.5 + UP * 0.5)
        
        owner = Group(
            self.load_png_icon("house.png", height=1.2),
            Text("Owners", font=self.body_font, font_size=24),
            Text("More protected", font=self.body_font, font_size=20, color=GREEN)
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 2.5 + UP * 0.5)
        
        first_time = Group(
            self.load_png_icon("family.png", height=1.2),
            Text("First-Time Buyers", font=self.body_font, font_size=24),
            Text("Stop timing market", font=self.body_font, font_size=20, color=GOLD)
        ).arrange(DOWN, buff=0.2).move_to(ORIGIN + DOWN * 2)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(renter, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(owner, shift=LEFT), run_time=step_time)
        self.play(FadeIn(first_time, shift=UP), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        Title: Three Smart Real Estate Strategies
        Script: Here's your action plan...
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 12.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Smart Strategies")
        title = self.create_title(title_text, color=GREEN)
        
        # Checklist items
        # 1. Don't time the market
        row1 = Group(
            self.load_png_icon("clock.png", height=0.9),
            Text("Don't time the market", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5).move_to(UP * 1.5)
        
        # 2. Focus on cash flow
        row2 = Group(
            self.load_png_icon("money.png", height=0.9),
            Text("Focus on cash flow", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5).move_to(ORIGIN)
        
        # 3. Build emergency fund first
        row3 = Group(
            self.load_png_icon("safe.png", height=0.9),
            Text("Emergency fund first", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 1.5)
        
        # Result
        result = Text("Patience > Speculation", font=self.body_font, font_size=36, color=GOLD).move_to(DOWN * 3)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(row1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(row2, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(row3, shift=RIGHT), Write(result), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        Title: Stay MoneyWise
        Script: Want to make smarter housing decisions?
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
