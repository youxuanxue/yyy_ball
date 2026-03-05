import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson012VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 12: Think Like the Best Decision-Makers
    Why Independent Thinking Protects Your Money
    """

    def build_scene_1(self, scene_data):
        """
        Scene 1: Hook / Pain Point
        'Ever wonder why smart people still get outplayed...'
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        N = 6
        step_time = (page_duration - t_trans) / N

        title_text = "Why Smart People\nStill Get Outplayed"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=self.COLOR_RISK, line_spacing=1.1).move_to(UP * 4.0)

        # Visual: crowd following, pitch, question mark
        crowd_icon = self.load_png_icon("people", height=1.8).move_to(LEFT * 2.2 + UP * 0.5)
        pitch_icon = self.load_png_icon("agreement", height=1.6).move_to(ORIGIN + DOWN * 0.5)
        warning_icon = self.load_png_icon("warning", height=1.6).move_to(RIGHT * 2.5 + UP * 0.5)

        # Key phrase
        truth_text = Text("If you can't find the reason,\nyou might be the one played.",
                         font_size=28, color=WHITE, line_spacing=1.2).move_to(DOWN * 2.2)
        bottom = Text("Find the rationality behind every move.",
                     font_size=30, color=GOLD, weight=BOLD).move_to(DOWN * 3.8)

        self.play(Write(title), run_time=step_time)
        self.play(
            FadeIn(crowd_icon, shift=RIGHT),
            FadeIn(pitch_icon, scale=0.8),
            run_time=step_time
        )
        self.play(FadeIn(warning_icon, shift=DOWN), run_time=step_time)
        self.play(Write(truth_text), run_time=step_time)
        self.play(Write(bottom), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        'The best decision-makers think in two ways...'
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        N = 8
        step_time = (page_duration - t_trans) / N

        title_text = "How Top Thinkers\nSee the Full Picture"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)

        # Two ways: 1) Patterns 2) Ask why
        way1_box = RoundedRectangle(width=3.8, height=1.8, corner_radius=0.2,
                                     color=BLUE_B, fill_opacity=0.3, stroke_width=3)
        icon1 = self.load_png_icon("chart", height=1.0)
        label1 = Text("1. Patterns", font_size=26, color=WHITE, weight=BOLD)
        desc1 = Text("Group similar situations.\nLearn from history.", font_size=20, color=LIGHT_GRAY, line_spacing=1.1)
        content1 = Group(icon1, VGroup(label1, desc1).arrange(DOWN, buff=0.1)).arrange(RIGHT, buff=0.3)
        content1.move_to(way1_box)
        part1 = Group(way1_box, content1).move_to(LEFT * 2.2 + UP * 1.5)

        way2_box = RoundedRectangle(width=3.8, height=1.8, corner_radius=0.2,
                                    color=GREEN_B, fill_opacity=0.3, stroke_width=3)
        icon2 = self.load_png_icon("question_mark", height=1.0)
        label2 = Text("2. Ask Why", font_size=26, color=WHITE, weight=BOLD)
        desc2 = Text("What do they want?\nWhat's their incentive?", font_size=20, color=LIGHT_GRAY, line_spacing=1.1)
        content2 = Group(icon2, VGroup(label2, desc2).arrange(DOWN, buff=0.1)).arrange(RIGHT, buff=0.3)
        content2.move_to(way2_box)
        part2 = Group(way2_box, content2).move_to(RIGHT * 2.2 + UP * 1.5)

        takeaway = Text("Don't take words at face value.",
                       font_size=32, color=GOLD, weight=BOLD).move_to(DOWN * 3.2)
        takeaway_box = SurroundingRectangle(takeaway, color=GOLD, buff=0.2, stroke_width=2)

        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(part1, shift=DOWN), run_time=step_time)
        self.play(FadeIn(part2, shift=DOWN), run_time=step_time)
        self.play(
            way1_box.animate.set_stroke(color=BLUE, width=4),
            way2_box.animate.set_stroke(color=GREEN, width=4),
            run_time=step_time
        )
        self.play(Write(takeaway), Create(takeaway_box), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        'There are no bored people and no real fools at the money table...'
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        N = 6
        step_time = (page_duration - t_trans) / N

        title_text = "There Are No Fools\nat the Table"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)

        # Left: Surface story | Right: Real story
        surface_label = Text("Surface", font_size=28, color=RED, weight=BOLD).move_to(LEFT * 2.2 + UP * 2.0)
        surface_text = Text("Believe the pitch.\nTrust the story.", font_size=24, color=LIGHT_GRAY, line_spacing=1.2)
        surface_text.move_to(LEFT * 2.2 + DOWN * 0.2)
        surface_box = SurroundingRectangle(Group(surface_label, surface_text), color=RED, buff=0.25, stroke_width=2)

        real_label = Text("Real", font_size=28, color=GREEN, weight=BOLD).move_to(RIGHT * 2.2 + UP * 2.0)
        real_text = Text("Incentives.\nPosition.\nWho benefits?", font_size=24, color=WHITE, line_spacing=1.2)
        real_text.move_to(RIGHT * 2.2 + DOWN * 0.2)
        real_box = SurroundingRectangle(Group(real_label, real_text), color=GREEN, buff=0.25, stroke_width=2)

        vs_text = Text("VS", font_size=36, color=GOLD, weight=BOLD).move_to(ORIGIN + UP * 0.5)
        gap_text = Text("Can't find the reason?\nThe gap is in your thinking.",
                       font_size=30, color=WHITE, line_spacing=1.2).move_to(DOWN * 3.5)

        self.play(Write(title), run_time=step_time)
        self.play(
            Write(surface_label), Write(surface_text), Create(surface_box),
            run_time=step_time
        )
        self.play(GrowFromCenter(vs_text), run_time=step_time)
        self.play(
            Write(real_label), Write(real_text), Create(real_box),
            run_time=step_time
        )
        self.play(Write(gap_text), run_time=step_time)
        self.play(Flash(real_box, color=GREEN), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        'This applies to you if you've ever taken a hot tip...'
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        N = 6
        step_time = (page_duration - t_trans) / N

        title_text = "When to Question\nWhat You Hear"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)

        scenarios = [
            ("Hot tip", "stocks", "Who gains?"),
            ("Contract", "agreement", "Read the fine print."),
            ("Expert advice", "businessman", "Check their incentives.")
        ]
        items = []
        for txt, icon_name, desc in scenarios:
            icon = self.load_png_icon(icon_name, height=1.2)
            main = Text(txt, font_size=26, color=WHITE, weight=BOLD)
            sub = Text(desc, font_size=22, color=LIGHT_GRAY)
            row = Group(icon, VGroup(main, sub).arrange(DOWN, buff=0.05, aligned_edge=LEFT)).arrange(RIGHT, buff=0.4)
            items.append(row)
        items[0].move_to(UP * 1.8)
        items[1].move_to(DOWN * 0.2)
        items[2].move_to(DOWN * 2.2)

        pause_text = Text("Pause. Ask: whose interest does this serve?",
                         font_size=30, color=GOLD, weight=BOLD, line_spacing=1.2).move_to(DOWN * 3.8)
        question_icon = self.load_png_icon("question_mark", height=1.2).next_to(pause_text, LEFT, buff=0.4)

        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(*[FadeIn(item, shift=RIGHT) for item in items], lag_ratio=0.35),
            run_time=step_time * 2
        )
        self.play(Write(pause_text), FadeIn(question_icon, scale=0.5), run_time=step_time)
        self.play(Flash(question_icon, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        'Step one: before any money decision, list who benefits...'
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        N = 7
        step_time = (page_duration - t_trans) / N

        title_text = "Your Pre-Decision\nChecklist"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)

        steps = [
            ("1", "Who benefits and how?", BLUE),
            ("2", "Similar past cases?", GREEN),
            ("3", "Assume everyone is rational.", PURPLE)
        ]
        step_items = []
        for num, q_text, color in steps:
            box = Square(side_length=0.55, color=color, stroke_width=3)
            num_text = Text(num, font_size=26, color=color, weight=BOLD).move_to(box)
            q = Text(q_text, font_size=24, color=WHITE, line_spacing=1.1)
            row = Group(Group(box, num_text), q).arrange(RIGHT, buff=0.35)
            step_items.append((row, box, color))
        positions = [UP * 2.0, UP * 0.3, DOWN * 1.4]
        for (row, _, _), pos in zip(step_items, positions):
            row.move_to(pos)

        rule_text = Text("Can't explain their motive?\nDon't bet your money.",
                        font_size=32, color=RED, weight=BOLD, line_spacing=1.2).move_to(DOWN * 3.8)
        rule_box = SurroundingRectangle(rule_text, color=RED, buff=0.2, stroke_width=2)

        self.play(Write(title), run_time=step_time)
        for (row, box, color) in step_items:
            self.play(FadeIn(row, shift=RIGHT), run_time=step_time * 0.8)
        self.play(
            *[box.animate.set_fill(color, opacity=0.25) for _, box, color in step_items],
            run_time=step_time
        )
        self.play(Write(rule_text), Create(rule_box), run_time=step_time)
        self.play(Flash(rule_box, color=RED), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        'Want to sharpen your thinking and protect your wealth?'
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time

        N = 4
        step_time = (page_duration - t_trans) / N

        title = Text("See the Full Picture", font=self.title_font,
                    font_size=self.font_title_size, color=GOLD, line_spacing=1.1).move_to(UP * 3.5)

        brand = Text("MoneyWise", font_size=56, color=GOLD, weight=BOLD).move_to(UP * 1.0)
        brain_icon = self.load_png_icon("brain", height=2.0).move_to(DOWN * 0.5)

        tagline = Text("Sharpen your thinking.\nProtect your wealth.",
                      font_size=32, color=WHITE, line_spacing=1.2).move_to(DOWN * 2.5)

        icon_like = self.load_png_icon("thumbs_up", height=1.5)
        icon_share = self.load_png_icon("share", height=1.5)
        icon_subscribe = self.load_png_icon("check", height=1.5)
        cta_icons = Group(icon_like, icon_share, icon_subscribe).arrange(RIGHT, buff=1.5).move_to(DOWN * 4.5)

        label_like = Text("Like", font_size=24, color=WHITE).next_to(icon_like, DOWN, buff=0.3)
        label_share = Text("Share", font_size=24, color=WHITE).next_to(icon_share, DOWN, buff=0.3)
        label_subscribe = Text("Follow", font_size=24, color=GOLD).next_to(icon_subscribe, DOWN, buff=0.3)
        labels = VGroup(label_like, label_share, label_subscribe)

        self.play(Write(title), run_time=step_time)
        self.play(
            GrowFromCenter(brand),
            FadeIn(brain_icon, scale=0.5),
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
