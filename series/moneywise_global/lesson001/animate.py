import sys
import os
import numpy as np
import random
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical

class Lesson001VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 001: Why Gold Won't Save You From Inflation
    """

    def fit_text_to_width(self, text_obj, max_width=8.0):
        """Helper to scale text if it exceeds max width"""
        if text_obj.width > max_width:
            text_obj.scale_to_fit_width(max_width)
        return text_obj

    def create_engaging_title(self, text):
        """Creates a title with a background glow/underline"""
        title = Text(text, font=self.title_font, font_size=self.font_title_size, color=WHITE)
        self.fit_text_to_width(title)
        
        # Add glow effect (using multiple layers)
        glow = title.copy().set_color(BLUE).set_opacity(0.3).set_stroke(width=5)
        
        return VGroup(glow, title)

    def build_scene_1(self, scene_data):
        """
        Scene 1: Hook / Pain Point
        Visual Strategy: Contrast the "safe haven" myth with the reality of price drops.
        Enhanced: Broken Shield Concept + Dynamic Price Drop + Background Elements
        """
        # 1. Setup Audio & Time
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7 
        step_time = (page_duration - t_trans) / N

        # 2. Visual Elements
        # Background: Floating symbols
        bg_symbols = VGroup(*[Text("$", font_size=random.randint(20, 60), color=GRAY, fill_opacity=0.1) for _ in range(10)])
        for sym in bg_symbols:
            sym.move_to(np.array([random.uniform(-4, 4), random.uniform(-7, 7), 0]))
        self.add(bg_symbols)

        title_text = scene_data.get("h2_heading", "The Gold Safe Haven Myth")
        title_group = self.create_engaging_title(title_text).move_to(UP * 4.0)
        
        # Main Icon: Shield (Safe Haven) -> Broken
        # Icons available: shield.png, gold_bars.png, warning.png, decrease.png
        shield = self.load_png_icon("shield", height=2.5)
        shield_glow = Circle(radius=1.5, color=GOLD, fill_opacity=0.2).move_to(shield)
        
        # Chart Line (Downward)
        chart_axes = Axes(
            x_range=[0, 5], y_range=[0, 5], 
            x_length=6, y_length=4,
            tips=False, axis_config={"include_numbers": False}
        ).set_opacity(0.3).move_to(DOWN * 0.5)
        
        chart_line = Line(start=chart_axes.c2p(0, 4.5), end=chart_axes.c2p(5, 1), color=RED, stroke_width=8)
        
        # Text for price drop
        drop_text = Text("-10%", font=self.title_font, font_size=100, color=RED).move_to(ORIGIN).rotate(15*DEGREES)
        drop_text.set_stroke(color=WHITE, width=2)
        
        # Warning icon for impact
        warning_icon = self.load_png_icon("warning", height=1.0).move_to(drop_text.get_top() + UP*0.5)
        
        # 3. Animations
        self.play(FadeIn(title_group, shift=DOWN), run_time=step_time)
        
        # Show "Safe Haven" expectation
        self.play(
            FadeIn(shield, scale=0.5), 
            FadeIn(shield_glow),
            run_time=step_time
        )
        
        # Reality Hits - Gold Prices Plunge
        self.play(
            Create(chart_axes),
            Create(chart_line),
            shield.animate.set_color(GRAY).set_opacity(0.5), # Gold loses luster
            FadeOut(shield_glow),
            run_time=step_time
        )
        
        # Impact Moment
        self.play(
            Flash(shield, color=RED, line_length=1.0, flash_radius=1.5),
            GrowFromCenter(drop_text),
            FadeIn(warning_icon, shift=DOWN),
            run_time=step_time
        )
        
        # Emphasize Pain
        self.play(
            Wiggle(drop_text),
            bg_symbols.animate.set_color(RED).set_opacity(0.2), # Atmosphere changes
            run_time=step_time
        )
        
        # Question text with style
        question = Text("Safe Haven?", font=self.body_font, font_size=self.font_body_size + 10, color=WHITE)
        question_bg = SurroundingRectangle(question, color=RED, fill_color=BLACK, fill_opacity=0.8, corner_radius=0.2)
        q_group = VGroup(question_bg, question).move_to(DOWN * 3.0)
        
        self.play(FadeIn(q_group, shift=UP), run_time=step_time)
        
        # Background animation loop (subtle) during wait
        self.play(
            bg_symbols.animate.shift(UP * 0.5),
            run_time=step_time
        )

        # 4. Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        Visual Strategy: Explain Fiat Currency vs Gold Standard.
        Enhanced: Printing press animation, animated paper flight path.
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N
        
        title_text = scene_data.get("h2_heading", "How Modern Money Works")
        title_group = self.create_engaging_title(title_text).move_to(UP * 4.0)
        
        # 1971 Date Stamp styling
        date_stamp = Text("Since 1971", font=self.body_font, font_size=30, color=GOLD).next_to(title_group, DOWN)
        date_box = SurroundingRectangle(date_stamp, color=GOLD, buff=0.1, corner_radius=0.1)
        date_group = VGroup(date_box, date_stamp)

        # Icons
        dollar = self.load_png_icon("us_dollar", height=1.8).move_to(LEFT * 2.5)
        # Using print.png for printer if available or fallback
        printer_icon = self.load_png_icon("print", height=1.5).move_to(UP * 0.5)
        
        arrow = Arrow(start=LEFT, end=RIGHT, color=GRAY).scale(1.5)
        paper_stack = VGroup(*[Text("IOU", font_size=40, color=WHITE).move_to(RIGHT * 2.5 + i*DOWN*0.1 + i*RIGHT*0.1) for i in range(3)])
        
        # Hidden Tax visualization
        tax_text = Text("HIDDEN TAX", font=self.title_font, font_size=70, color=RED).move_to(DOWN * 2.5)
        tax_bg = BackgroundRectangle(tax_text, fill_color=BLACK, fill_opacity=0.9, buff=0.2)
        tax_border = SurroundingRectangle(tax_text, color=RED, buff=0.2)
        tax_group = VGroup(tax_bg, tax_text, tax_border)
        
        # Price tag showing inflation
        price_tag = self.load_png_icon("price_tag_usd", height=1.0).next_to(dollar, DOWN, buff=0.2)

        # Animations
        self.play(FadeIn(title_group), FadeIn(date_group), run_time=step_time)
        
        # Show Money is just Paper Faith
        self.play(FadeIn(dollar), FadeIn(printer_icon), run_time=step_time)
        
        # Printing animation - Paper flying out
        self.play(
            printer_icon.animate.scale(1.1).set_color(BLUE_E),
            run_time=step_time/2
        )
        self.play(
            printer_icon.animate.scale(1/1.1).set_color(BLUE),
            FadeIn(paper_stack, shift=DOWN),
            run_time=step_time/2
        )
        
        # Devaluation
        self.play(
            dollar.animate.set_opacity(0.3).scale(0.8), # Dollar shrinks and fades
            paper_stack.animate.scale(1.2), # IOUs grow
            FadeIn(price_tag, shift=UP), # Prices appear
            run_time=step_time
        )
        
        # Reveal the "Hidden Tax" concept
        self.play(
            FadeIn(tax_group, scale=0.5),
            run_time=step_time
        )
        
        self.play(
            Indicate(tax_text, color=RED),
            tax_border.animate.set_stroke(width=8),
            run_time=step_time
        )

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        Visual Strategy: Contrast Gold (Static) vs Liquidity Needs.
        Enhanced: VS Lightning, Grid Background, Panic Selling.
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Why Gold Fails")
        title_group = self.create_engaging_title(title_text).move_to(UP * 4.0)
        
        # Background Grid
        grid = NumberPlane(
            x_range=[-7, 7], y_range=[-7, 7], 
            background_line_style={"stroke_opacity": 0.1, "stroke_color": BLUE}
        )
        self.add(grid) # Add immediately
        
        # Left: Static Gold
        gold_icon = self.load_png_icon("gold_bars", height=2.0).move_to(LEFT * 2.5 + UP * 0.5)
        gold_label = Text("Zero Yield", font=self.body_font, font_size=30, color=GRAY).next_to(gold_icon, DOWN)
        
        # Right: Panic/Liquidity
        # Use decrease.png or loss.png for crisis
        panic_icon = self.load_png_icon("loss", height=2.0).move_to(RIGHT * 2.5 + UP * 0.5)
        panic_label = Text("Liquidity Crisis", font=self.body_font, font_size=30, color=RED).next_to(panic_icon, DOWN)
        
        # VS Symbol
        vs_text = Text("VS", font_size=48, color=YELLOW).move_to(UP * 0.5)
        vs_bg = Circle(radius=0.6, color=YELLOW, fill_opacity=0.2).move_to(vs_text)
        vs_group = VGroup(vs_bg, vs_text)

        # Animations
        self.play(FadeIn(title_group), run_time=step_time)
        
        # Show Contrast
        self.play(
            FadeIn(gold_icon, shift=RIGHT), Write(gold_label),
            FadeIn(panic_icon, shift=LEFT), Write(panic_label),
            run_time=step_time
        )
        
        # VS Impact
        self.play(
            GrowFromCenter(vs_group),
            Flash(vs_group, color=YELLOW),
            run_time=step_time
        )
        
        # Panic Selling Effect - Gold moving to Panic side
        arrow_sell = Arrow(start=gold_icon.get_right(), end=panic_icon.get_left(), color=RED, buff=0.5)
        sell_text = Text("FORCED SELL", font_size=24, color=RED).next_to(arrow_sell, UP)
        
        self.play(
            GrowArrow(arrow_sell),
            Write(sell_text),
            gold_icon.animate.move_to(panic_icon).set_opacity(0), # Gold disappears into panic
            run_time=step_time
        )
        
        # Conclusion
        conclusion = Text("NO SAFETY FLOOR", font=self.title_font, font_size=50, color=RED)
        conclusion.set_stroke(color=WHITE, width=1)
        c_bg = BackgroundRectangle(conclusion, fill_color=BLACK, fill_opacity=0.9)
        c_group = VGroup(c_bg, conclusion).move_to(DOWN * 3.0)
        
        self.play(FadeIn(c_group, scale=0.5), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        Visual Strategy: Viewer identification.
        Enhanced: Card style layout for scenarios.
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Are You Overexposed?")
        title_group = self.create_engaging_title(title_text).move_to(UP * 4.0)
        
        # Central Character
        person = self.load_png_icon("thinking", height=2.0).move_to(UP * 1.5)
        
        # Scenario Cards
        def create_card(text, color, position, icon_key=None):
            rect = RoundedRectangle(width=3.5, height=2.5, corner_radius=0.3, color=color, fill_opacity=0.2)
            content = Text(text, font=self.body_font, font_size=24, color=color).move_to(rect).shift(DOWN*0.5)
            
            group = Group(rect, content)
            
            if icon_key:
                icon = self.load_png_icon(icon_key, height=1.0).move_to(rect).shift(UP*0.5)
                group.add(icon)
                
            return group.move_to(position)

        card_hoarding = create_card("Gold Hoarding", GOLD, LEFT * 2.2 + DOWN * 0.5, "gold_bars")
        card_cash = create_card("Cash Waiting", GREEN, RIGHT * 2.2 + DOWN * 0.5, "piggy_bank")
        
        # Warning Line
        warning_line = Line(start=LEFT*4, end=RIGHT*4, color=RED, stroke_width=2).move_to(DOWN * 2.5)
        warning_text = Text("WEALTH EROSION", font=self.title_font, font_size=48, color=RED).next_to(warning_line, DOWN)
        
        # Down arrow for erosion
        down_arrow = self.load_png_icon("down_arrow", height=1.0).next_to(warning_text, DOWN)

        # Animations
        self.play(FadeIn(title_group), FadeIn(person), run_time=step_time)
        
        # Scenarios appear
        self.play(
            FadeIn(card_hoarding, shift=RIGHT),
            run_time=step_time
        )
        self.play(
            FadeIn(card_cash, shift=LEFT),
            run_time=step_time
        )
        
        # Realization/Warning
        self.play(
            person.animate.set_color(RED), # Realizes danger
            card_hoarding.animate.set_opacity(0.5),
            card_cash.animate.set_opacity(0.5),
            Create(warning_line),
            run_time=step_time
        )
        
        self.play(
            Write(warning_text),
            Flash(warning_text, color=RED),
            FadeIn(down_arrow, shift=DOWN),
            run_time=step_time
        )

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        Visual Strategy: Checklist of 3 steps.
        Enhanced: Card layout with icons for each step, distinct colors.
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        title_text = scene_data.get("h2_heading", "Real Protection")
        title_group = self.create_engaging_title(title_text).move_to(UP * 4.0)
        
        # Strategy Cards
        def create_strategy_item(idx, text, color, icon_key=None):
            bg = RoundedRectangle(width=8, height=1.5, corner_radius=0.2, color=color, fill_opacity=0.1)
            bg.set_stroke(width=2)
            
            num = Text(str(idx), font_size=40, color=color, weight=BOLD).move_to(bg.get_left() + RIGHT * 0.6)
            
            content_group = Group()
            if icon_key:
                icon = self.load_png_icon(icon_key, height=0.8)
                content_group.add(icon)
                
            text_obj = Text(text, font=self.body_font, font_size=32, color=WHITE)
            content_group.add(text_obj)
            content_group.arrange(RIGHT, buff=0.4).move_to(bg).shift(RIGHT * 0.5)
            
            return Group(bg, num, content_group)

        # Icons: pie_chart.png, real_estate.png/stocks.png, idea.png/strategy.png
        item1 = create_strategy_item(1, "Diversify Assets", GOLD, "pie_chart")
        item2 = create_strategy_item(2, "Productive Income", GREEN, "real_estate")
        item3 = create_strategy_item(3, "Adapt Strategy", BLUE, "strategy")
        
        items_group = Group(item1, item2, item3).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        
        # Animations
        self.play(FadeIn(title_group), run_time=step_time)
        
        # Items sliding in with style
        self.play(
            FadeIn(item1, shift=LEFT), 
            run_time=step_time
        )
        self.play(
            FadeIn(item2, shift=RIGHT), 
            run_time=step_time
        )
        self.play(
            FadeIn(item3, shift=LEFT), 
            run_time=step_time
        )
        
        # Highlight all
        self.play(
            item1.animate.scale(1.05),
            item2.animate.scale(1.05),
            item3.animate.scale(1.05),
            run_time=step_time
        )

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        Visual Strategy: Strong engage cues.
        Enhanced: Subscribe Button simulation, pulsing bell.
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 3
        step_time = (page_duration - t_trans) / N

        title_text = "Subscribe for More"
        title_group = self.create_engaging_title(title_text).move_to(UP * 3.5)
        
        # Subscribe Button
        sub_rect = RoundedRectangle(width=6, height=1.5, corner_radius=0.75, color=RED, fill_opacity=1)
        sub_text = Text("SUBSCRIBE", font_size=48, color=WHITE, weight=BOLD).move_to(sub_rect)
        sub_button = VGroup(sub_rect, sub_text).move_to(ORIGIN)
        
        # Bell Icon (Simulated or Real)
        bell_icon = self.load_png_icon("checklist", height=1.0).next_to(sub_button, UP, buff=1.0) # Fallback to checklist if no bell
        
        # Next Lesson Teaser
        next_box = RoundedRectangle(width=7, height=1.2, color=BLUE, fill_opacity=0.2).move_to(DOWN * 2.5)
        next_text = Text("Next: Currency Secrets", font_size=32, color=WHITE).move_to(next_box)
        next_group = Group(next_box, next_text)
        
        # Target icon for next lesson focus
        target_icon = self.load_png_icon("target", height=0.8).next_to(next_text, LEFT)
        next_group.add(target_icon)
        
        # Finger Cursor
        cursor = Triangle(color=WHITE, fill_opacity=1).scale(0.3).rotate(-60*DEGREES).move_to(sub_button.get_corner(DR))

        # Animations
        self.play(FadeIn(title_group), run_time=step_time)
        
        # Show Button
        self.play(
            GrowFromCenter(sub_button),
            FadeIn(bell_icon, shift=DOWN),
            run_time=step_time
        )
        
        # Show Next Teaser
        self.play(
            FadeIn(next_group, shift=UP),
            run_time=step_time
        )
        
        self.wait(step_time) # No FadeOut at the end
