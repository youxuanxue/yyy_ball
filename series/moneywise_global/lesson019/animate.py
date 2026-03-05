import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson019VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 19: Why Cash Flow Beats Net Worth
    The Real Measure of Financial Freedom
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
        title_text = "The Millionaire\nWho's Broke"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size, 
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Millionaire on paper
        person_rich = self.load_png_icon("businessman", height=1.6).move_to(LEFT * 2.5 + UP * 1.2)
        label_rich = Text("$1M Net Worth", font_size=22, color=GOLD).next_to(person_rich, UP, buff=0.2)
        
        # Trapped assets
        trapped_items = VGroup(
            Text("🏠 House (can't sell)", font_size=18, color=RED),
            Text("📊 401k (can't touch)", font_size=18, color=RED),
            Text("💼 Business (demands time)", font_size=18, color=RED)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(person_rich, DOWN, buff=0.3)
        
        # Free person
        person_free = self.load_png_icon("happy", height=1.6).move_to(RIGHT * 2.5 + UP * 1.2)
        label_free = Text("$500K Net Worth", font_size=22, color=WHITE).next_to(person_free, UP, buff=0.2)
        free_text = Text("Lives freely!", font_size=22, color=GREEN, weight=BOLD).next_to(person_free, DOWN, buff=0.3)
        
        # Key insight
        insight = Text("The difference?\nCASH FLOW", 
                      font_size=36, color=GOLD, weight=BOLD, line_spacing=1.2).move_to(DOWN * 3.5)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            FadeIn(person_rich, shift=DOWN),
            Write(label_rich),
            run_time=step_time
        )
        self.play(Write(trapped_items), run_time=step_time)
        self.play(
            FadeIn(person_free, shift=DOWN),
            Write(label_free),
            Write(free_text),
            run_time=step_time
        )
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
        title_text = "Snapshot vs\nMovie"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Net Worth side
        nw_header = Text("NET WORTH", font_size=26, color=BLUE, weight=BOLD)
        nw_formula = Text("Own - Owe", font_size=22, color=WHITE)
        nw_icon = self.load_png_icon("calculator", height=1.0)
        nw_desc = Text("A snapshot\nin time", font_size=20, color=LIGHT_GRAY, line_spacing=1.1)
        nw_measure = Text("Measures:\nAccumulation", font_size=18, color=BLUE, line_spacing=1.1)
        
        nw_group = Group(nw_header, nw_formula, nw_icon, nw_desc, nw_measure).arrange(DOWN, buff=0.2)
        nw_box = SurroundingRectangle(nw_group, color=BLUE, buff=0.3, stroke_width=2)
        nw_section = Group(nw_box, nw_group).move_to(LEFT * 2.8 + UP * 0.3)
        
        # Cash Flow side
        cf_header = Text("CASH FLOW", font_size=26, color=GREEN, weight=BOLD)
        cf_formula = Text("In - Out (monthly)", font_size=22, color=WHITE)
        cf_icon = self.load_png_icon("money_circulation", height=1.0)
        cf_desc = Text("An ongoing\nmovie", font_size=20, color=LIGHT_GRAY, line_spacing=1.1)
        cf_measure = Text("Measures:\nFREEDOM", font_size=18, color=GREEN, weight=BOLD, line_spacing=1.1)
        
        cf_group = Group(cf_header, cf_formula, cf_icon, cf_desc, cf_measure).arrange(DOWN, buff=0.2)
        cf_box = SurroundingRectangle(cf_group, color=GREEN, buff=0.3, stroke_width=2)
        cf_section = Group(cf_box, cf_group).move_to(RIGHT * 2.8 + UP * 0.3)
        
        # Bottom insight
        insight = Text("High net worth ≠ Freedom", 
                      font_size=28, color=ORANGE, weight=BOLD).move_to(DOWN * 4.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(nw_section, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(cf_section, shift=LEFT), run_time=step_time)
        self.play(
            nw_box.animate.set_fill(BLUE, opacity=0.1),
            cf_box.animate.set_fill(GREEN, opacity=0.15),
            run_time=step_time
        )
        self.play(Write(insight), run_time=step_time)
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
        title_text = "The Freedom\nFormula"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Formula visual
        formula_box = RoundedRectangle(corner_radius=0.2, width=9, height=2, 
                                       color=GOLD, fill_opacity=0.1, stroke_width=3)
        formula_text = Text("Passive Income > Living Expenses", 
                           font_size=28, color=GOLD, weight=BOLD)
        equals = Text("= FREEDOM", font_size=32, color=GREEN, weight=BOLD)
        formula_group = VGroup(formula_text, equals).arrange(DOWN, buff=0.3)
        formula_group.move_to(formula_box)
        formula_section = Group(formula_box, formula_group).move_to(UP * 1.5)
        
        # Two paths
        path_nw = VGroup(
            Text("Focus: Net Worth", font_size=22, color=BLUE, weight=BOLD),
            Text("→ Retire rich", font_size=20, color=WHITE),
            Text("→ But stressed", font_size=20, color=RED)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).move_to(LEFT * 2.8 + DOWN * 1.5)
        
        path_cf = VGroup(
            Text("Focus: Cash Flow", font_size=22, color=GREEN, weight=BOLD),
            Text("→ Buy time back", font_size=20, color=WHITE),
            Text("→ True freedom", font_size=20, color=GREEN)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).move_to(RIGHT * 2.5 + DOWN * 1.5)
        
        # Key message
        message = Text("It's not accumulation.\nIt's what flows in.", 
                      font_size=28, color=GOLD, line_spacing=1.2).move_to(DOWN * 4.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            FadeIn(formula_section, scale=0.9),
            run_time=step_time
        )
        self.play(
            formula_box.animate.set_stroke(width=5),
            run_time=step_time * 0.5
        )
        self.play(
            Write(path_nw),
            Write(path_cf),
            run_time=step_time
        )
        self.play(Write(message), run_time=step_time)
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
        title_text = "When to Shift\nYour Focus"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Who benefits
        audiences = [
            ("High Earners", "Trapped despite big paychecks", "businessman"),
            ("Diligent Savers", "Growing accounts, no progress feel", "piggy_bank"),
            ("Retirees", "Can't easily access wealth", "elderly")
        ]
        
        audience_items = []
        for label, issue, icon_name in audiences:
            icon = self.load_png_icon(icon_name, height=1.2)
            main_text = Text(label, font_size=24, color=WHITE, weight=BOLD)
            sub_text = Text(issue, font_size=18, color=ORANGE)
            text_group = VGroup(main_text, sub_text).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            item = Group(icon, text_group).arrange(RIGHT, buff=0.4)
            audience_items.append(item)
        
        audience_items[0].move_to(UP * 1.5)
        audience_items[1].move_to(DOWN * 0.3)
        audience_items[2].move_to(DOWN * 2.1)
        
        # Insight
        insight = Text("Cash flow thinking\nchanges everything.", 
                      font_size=28, color=GREEN, weight=BOLD, line_spacing=1.2).move_to(DOWN * 4.0)
        
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
        self.play(Write(insight), run_time=step_time)
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
        title_text = "Three Steps to\nBuild Cash Flow"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        steps = [
            ("1", "Track monthly\nin vs out", GREEN, "calculator"),
            ("2", "Convert assets to\nincome producers", BLUE, "house"),
            ("3", "Reinvest to create\nmore cash flow", PURPLE, "increase")
        ]
        
        step_items = []
        for num, text, color, icon_name in steps:
            num_circle = Circle(radius=0.45, color=color, fill_opacity=0.2, stroke_width=3)
            num_text = Text(num, font_size=30, color=color, weight=BOLD).move_to(num_circle)
            icon = self.load_png_icon(icon_name, height=0.9)
            step_text = Text(text, font_size=22, color=WHITE, line_spacing=1.1)
            
            item = Group(num_circle, num_text, icon, step_text).arrange(RIGHT, buff=0.25)
            step_items.append((item, num_circle, color))
        
        positions = [UP * 1.5, DOWN * 0.5, DOWN * 2.5]
        for i, (item, _, _) in enumerate(step_items):
            item.move_to(positions[i])
        
        # Income examples
        examples = Text("Rentals • Dividends • Royalties", 
                       font_size=22, color=LIGHT_GRAY).move_to(DOWN * 4.0)
        
        footer = Text("Start small. Grow consistently.", 
                     font_size=26, color=GOLD, weight=BOLD).move_to(DOWN * 4.7)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        
        for item, circle, color in step_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=step_time)
        
        self.play(
            *[circle.animate.set_fill(color, opacity=0.4) for _, circle, color in step_items],
            run_time=step_time
        )
        self.play(
            Write(examples),
            Write(footer),
            run_time=step_time
        )
        
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

        title = Text("Let It Flow", font=self.title_font, 
                    font_size=self.font_title_size, color=GOLD, line_spacing=1.1).move_to(UP * 3.5)
        
        brand = Text("MoneyWise", font_size=56, color=GOLD, weight=BOLD).move_to(UP * 1.0)
        
        flow_icon = self.load_png_icon("money_circulation", height=2.0).move_to(DOWN * 0.5)
        
        tagline = Text("Real financial\nfreedom awaits.", 
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
            FadeIn(flow_icon, scale=0.5),
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
