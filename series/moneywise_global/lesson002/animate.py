import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical

class Lesson002VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 002: The 4 Rules of Real Money
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
        Title: The Trap of Fake Investments
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 8.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "The Trap")
        title = self.create_title(title_text, color=self.COLOR_RISK)
        
        # Warning and loss icons
        trap_icon = self.load_png_icon("danger.png", height=2.0).move_to(UP * 1.0)
        loss_icon = self.load_png_icon("loss.png", height=2.0).move_to(DOWN * 1.5)
        
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(trap_icon, shift=DOWN), run_time=step_time)
        self.play(FadeIn(loss_icon, shift=UP), run_time=step_time)
        self.play(Flash(loss_icon, color=RED, flash_radius=1.5), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        Title: What Makes Money Real
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Real Money")
        title = self.create_title(title_text, color=GOLD)
        
        # Government -> Money flow
        govt = self.load_png_icon("bank.png", height=2.0).move_to(LEFT * 2.5 + UP * 0.5)
        money = self.load_png_icon("money.png", height=2.0).move_to(RIGHT * 2.5 + UP * 0.5)
        
        arrow = Arrow(govt.get_right(), money.get_left(), color=WHITE)
        tax_label = Text("Seigniorage", font=self.body_font, font_size=32, color=YELLOW).next_to(arrow, UP)
        
        # Fake money (crypto without backing)
        scam_icon = self.load_png_icon("cryptocurrency.png", height=1.5).move_to(DOWN * 2.5)
        cross = Cross(scam_icon, color=RED)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(govt), FadeIn(money), Create(arrow), run_time=step_time)
        self.play(Write(tax_label), run_time=step_time)
        self.play(FadeIn(scam_icon), run_time=step_time)
        self.play(Create(cross), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        Title: Gresham's Law in Action
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Gresham's Law")
        title = self.create_title(title_text, color=self.COLOR_RISK)
        
        # Good money vs bad money
        good_money = self.load_png_icon("gold_bars.png", height=2.0).move_to(LEFT * 2)
        bad_money = self.load_png_icon("loss.png", height=2.0).move_to(RIGHT * 2)
        
        # Bad drives out good
        arrow = Arrow(bad_money.get_center(), good_money.get_center(), color=RED, buff=1.2)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(good_money), FadeIn(bad_money), run_time=step_time)
        self.play(GrowArrow(arrow), run_time=step_time)
        self.play(good_money.animate.set_opacity(0.3), bad_money.animate.scale(1.2), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        Title: Are You the Exit Liquidity?
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 8.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Exit Liquidity?")
        title = self.create_title(title_text, color=ORANGE)
        
        person = self.load_png_icon("thinking.png", height=2.5)
        question = Text("?", font_size=96, color=YELLOW).next_to(person, UP + RIGHT)
        
        meme_coin = self.load_png_icon("cryptocurrency.png", height=1.5).move_to(DOWN * 2 + RIGHT * 2)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(person), run_time=step_time)
        self.play(Write(question), run_time=step_time)
        self.play(FadeIn(meme_coin, shift=UP), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        Title: The 4 Essentials Checklist
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 12.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "4 Essentials")
        title = self.create_title(title_text, color=GREEN)
        
        # 4 checklist items
        items = Group()
        
        # 1. Power Backing
        row1 = Group(
            self.load_png_icon("shield.png", height=0.8),
            Text("Power Backing", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5)
        
        # 2. Hard Collateral
        row2 = Group(
            self.load_png_icon("gold_bars.png", height=0.8),
            Text("Hard Collateral", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5)
        
        # 3. Real Profit
        row3 = Group(
            self.load_png_icon("profit.png", height=0.8),
            Text("Real Profit", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5)
        
        # 4. Can Pay Tax
        row4 = Group(
            self.load_png_icon("tax.png", height=0.8),
            Text("Can Pay Tax", font=self.body_font, font_size=28)
        ).arrange(RIGHT, buff=0.5)
        
        items.add(row1, row2, row3, row4)
        items.arrange(DOWN, buff=0.7).move_to(DOWN * 0.5)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(row1, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(row2, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(row3, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(row4, shift=RIGHT), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 8.0
        t_trans = self.transition_time
        
        N = 3
        step_time = (page_duration - t_trans) / N

        title = self.create_title("Stay MoneyWise", color=GOLD).move_to(UP * 3.5)
        
        bulb = self.load_png_icon("light_bulb.png", height=2.5).move_to(UP * 0.5)
        sub_text = Text("Subscribe for More", font=self.body_font, font_size=40, color=WHITE).next_to(bulb, DOWN, buff=0.5)
        
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(bulb, scale=0.5), Write(sub_text), run_time=step_time)
        self.play(bulb.animate.scale(1.1), Flash(bulb, color=GOLD, flash_radius=1.8), run_time=step_time)
        
        self.wait(step_time)
