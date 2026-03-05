import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson010VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 10: The 4-Part Scam Test
    How to Spot Investment Fraud Before You Lose Money
    """

    def build_scene_1(self, scene_data):
        """
        Scene 1: Hook / Pain Point
        'Every year, people lose billions to investment scams...'
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title - wrap for vertical display
        title_text = "Why Smart People\nStill Fall for Scams"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size, 
                    color=self.COLOR_RISK, line_spacing=1.1).move_to(UP * 4.0)
        
        # Visual: Money flying away from person
        money_icon = self.load_png_icon("stack_of_money", height=2.0).move_to(LEFT * 2.0 + UP * 1.0)
        person_icon = self.load_png_icon("sad", height=2.0).move_to(ORIGIN)
        warning_icon = self.load_png_icon("warning", height=1.8).move_to(RIGHT * 2.5 + UP * 0.5)
        
        # Scam pitch words floating
        scam_words = VGroup()
        pitch_texts = ["Guaranteed!", "Exclusive!", "Limited Time!"]
        positions = [LEFT * 2.5 + DOWN * 1.5, ORIGIN + DOWN * 1.8, RIGHT * 2.5 + DOWN * 1.5]
        colors = [ORANGE, RED, ORANGE]
        for txt, pos, col in zip(pitch_texts, positions, colors):
            word = Text(txt, font_size=28, color=col, weight=BOLD).move_to(pos)
            scam_words.add(word)
        
        # Bottom message
        bottom_text = Text("Same missing ingredients.", 
                          font_size=34, color=WHITE, weight=BOLD).move_to(DOWN * 3.5)
        
        # Shield icon showing protection
        shield_icon = self.load_png_icon("security_shield", height=1.5).move_to(DOWN * 5.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            FadeIn(person_icon, scale=0.8),
            FadeIn(money_icon, shift=LEFT),
            run_time=step_time
        )
        self.play(
            money_icon.animate.shift(LEFT * 2 + UP * 2).set_opacity(0.3),
            FadeIn(warning_icon, shift=DOWN),
            run_time=step_time
        )
        self.play(
            LaggedStart(
                *[GrowFromCenter(w) for w in scam_words],
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        self.play(Write(bottom_text), run_time=step_time)
        self.play(FadeIn(shield_icon, shift=UP), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        'Every legitimate investment passes a simple 4-part test...'
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 8
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "The 4-Part\nScam Detection Test"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Four test parts with icons
        # Part 1: Licensing
        box_1 = RoundedRectangle(width=3.5, height=1.8, corner_radius=0.2,
                                 color=BLUE_B, fill_opacity=0.3, stroke_width=3)
        icon_1 = self.load_png_icon("certificate", height=1.0)
        label_1 = Text("1. Licensing", font_size=26, color=WHITE, weight=BOLD)
        desc_1 = Text("SEC Regulated?", font_size=20, color=LIGHT_GRAY)
        content_1 = Group(icon_1, VGroup(label_1, desc_1).arrange(DOWN, buff=0.1)).arrange(RIGHT, buff=0.3)
        content_1.move_to(box_1)
        part_1 = Group(box_1, content_1).move_to(LEFT * 2.2 + UP * 2.0)
        
        # Part 2: Credibility
        box_2 = RoundedRectangle(width=3.5, height=1.8, corner_radius=0.2,
                                 color=GREEN_B, fill_opacity=0.3, stroke_width=3)
        icon_2 = self.load_png_icon("handshake", height=1.0)
        label_2 = Text("2. Credibility", font_size=26, color=WHITE, weight=BOLD)
        desc_2 = Text("Real Assets?", font_size=20, color=LIGHT_GRAY)
        content_2 = Group(icon_2, VGroup(label_2, desc_2).arrange(DOWN, buff=0.1)).arrange(RIGHT, buff=0.3)
        content_2.move_to(box_2)
        part_2 = Group(box_2, content_2).move_to(RIGHT * 2.2 + UP * 2.0)
        
        # Part 3: Production
        box_3 = RoundedRectangle(width=3.5, height=1.8, corner_radius=0.2,
                                 color=PURPLE_B, fill_opacity=0.3, stroke_width=3)
        icon_3 = self.load_png_icon("profit", height=1.0)
        label_3 = Text("3. Production", font_size=26, color=WHITE, weight=BOLD)
        desc_3 = Text("Creates Value?", font_size=20, color=LIGHT_GRAY)
        content_3 = Group(icon_3, VGroup(label_3, desc_3).arrange(DOWN, buff=0.1)).arrange(RIGHT, buff=0.3)
        content_3.move_to(box_3)
        part_3 = Group(box_3, content_3).move_to(LEFT * 2.2 + DOWN * 0.5)
        
        # Part 4: Obligation
        box_4 = RoundedRectangle(width=3.5, height=1.8, corner_radius=0.2,
                                 color=ORANGE, fill_opacity=0.3, stroke_width=3)
        icon_4 = self.load_png_icon("agreement", height=1.0)
        label_4 = Text("4. Obligation", font_size=26, color=WHITE, weight=BOLD)
        desc_4 = Text("Duties to You?", font_size=20, color=LIGHT_GRAY)
        content_4 = Group(icon_4, VGroup(label_4, desc_4).arrange(DOWN, buff=0.1)).arrange(RIGHT, buff=0.3)
        content_4.move_to(box_4)
        part_4 = Group(box_4, content_4).move_to(RIGHT * 2.2 + DOWN * 0.5)
        
        # Bottom warning
        warning_text = Text("If any part fails, walk away.", 
                           font_size=32, color=RED, weight=BOLD).move_to(DOWN * 3.0)
        warning_box = SurroundingRectangle(warning_text, color=RED, buff=0.2, stroke_width=2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(part_1, shift=DOWN), run_time=step_time)
        self.play(FadeIn(part_2, shift=DOWN), run_time=step_time)
        self.play(FadeIn(part_3, shift=UP), run_time=step_time)
        self.play(FadeIn(part_4, shift=UP), run_time=step_time)
        # Highlight all boxes
        self.play(
            box_1.animate.set_stroke(color=BLUE, width=4),
            box_2.animate.set_stroke(color=GREEN, width=4),
            box_3.animate.set_stroke(color=PURPLE, width=4),
            box_4.animate.set_stroke(color=ORANGE, width=4),
            run_time=step_time
        )
        self.play(Write(warning_text), Create(warning_box), run_time=step_time)
        self.play(Flash(warning_box, color=RED), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        'Scammers are masters at faking one or two elements...'
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title - wrap long title
        title_text = "Why This Test Works\nAgainst Fraudsters"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Visual: Scammer only fakes 1-2 elements
        # Create a comparison view
        
        # Left side - Scam (only 1-2 checks)
        scam_label = Text("SCAM", font_size=32, color=RED, weight=BOLD).move_to(LEFT * 2.5 + UP * 2.2)
        scam_rows = []
        scam_items = [
            ("Licensing", "fail"),
            ("Credibility", "check_mark"),  # Faked
            ("Production", "fail"),
            ("Obligation", "fail")
        ]
        for i, (item, status) in enumerate(scam_items):
            item_text = Text(item, font_size=22, color=WHITE)
            if status == "check_mark":
                icon = self.load_png_icon("check_mark", height=0.5)
                icon.set_color(ORANGE)  # Fake check - orange
            else:
                icon = self.load_png_icon("fail", height=0.5)
            row = Group(icon, item_text).arrange(RIGHT, buff=0.2)
            scam_rows.append(row)
        scam_checks = Group(*scam_rows).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(LEFT * 2.5 + DOWN * 0.3)
        scam_box = SurroundingRectangle(Group(scam_label, scam_checks), color=RED, buff=0.3, stroke_width=2)
        
        # Right side - Legit (all 4 checks)
        legit_label = Text("LEGIT", font_size=32, color=GREEN, weight=BOLD).move_to(RIGHT * 2.5 + UP * 2.2)
        legit_rows = []
        legit_items = ["Licensing", "Credibility", "Production", "Obligation"]
        for item in legit_items:
            item_text = Text(item, font_size=22, color=WHITE)
            icon = self.load_png_icon("check_mark", height=0.5)
            row = Group(icon, item_text).arrange(RIGHT, buff=0.2)
            legit_rows.append(row)
        legit_checks = Group(*legit_rows).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(RIGHT * 2.5 + DOWN * 0.3)
        legit_box = SurroundingRectangle(Group(legit_label, legit_checks), color=GREEN, buff=0.3, stroke_width=2)
        
        # VS in middle
        vs_text = Text("VS", font_size=40, color=GOLD, weight=BOLD).move_to(ORIGIN + UP * 0.5)
        
        # Key insight
        insight = Text("More unchecked boxes\n= Bigger red flag", 
                      font_size=32, color=WHITE, line_spacing=1.2).move_to(DOWN * 3.5)
        insight_box = SurroundingRectangle(insight, color=GOLD, buff=0.2, stroke_width=2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            Write(scam_label),
            Create(scam_box),
            run_time=step_time
        )
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT) for item in scam_rows],
                lag_ratio=0.2
            ),
            run_time=step_time
        )
        self.play(
            Write(legit_label),
            Create(legit_box),
            GrowFromCenter(vs_text),
            run_time=step_time
        )
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=LEFT) for item in legit_rows],
                lag_ratio=0.2
            ),
            run_time=step_time
        )
        self.play(Write(insight), Create(insight_box), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        'This applies to you if you've ever received a hot stock tip...'
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "When to Use\nthe 4-Part Test"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Three scenarios
        scenarios = [
            ("Hot stock tip", "stocks", "from a friend or online"),
            ("Crypto opportunity", "bitcoin", "promising huge returns"),
            ("Investment pitch", "investment", "unusually high gains")
        ]
        
        scenario_items = []
        for txt, icon_name, desc in scenarios:
            icon = self.load_png_icon(icon_name, height=1.2)
            main_text = Text(txt, font_size=28, color=WHITE, weight=BOLD)
            sub_text = Text(desc, font_size=22, color=LIGHT_GRAY)
            text_group = VGroup(main_text, sub_text).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            item = Group(icon, text_group).arrange(RIGHT, buff=0.5)
            scenario_items.append(item)
        
        # Position scenarios
        scenario_items[0].move_to(UP * 1.8)
        scenario_items[1].move_to(DOWN * 0.2)
        scenario_items[2].move_to(DOWN * 2.2)
        
        # Warning radar
        radar_text = Text("Your scam radar\nshould be going off!", 
                         font_size=32, color=ORANGE, weight=BOLD, line_spacing=1.2).move_to(DOWN * 4.2)
        
        # Alert icon
        alert_icon = self.load_png_icon("warning", height=1.2).next_to(radar_text, LEFT, buff=0.5)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(scenario_items[0], shift=RIGHT),
                FadeIn(scenario_items[1], shift=RIGHT),
                FadeIn(scenario_items[2], shift=RIGHT),
                lag_ratio=0.4
            ),
            run_time=step_time * 2
        )
        self.play(
            Write(radar_text),
            FadeIn(alert_icon, scale=0.5),
            run_time=step_time
        )
        self.play(
            alert_icon.animate.scale(1.2),
            Flash(alert_icon, color=ORANGE),
            run_time=step_time
        )
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        'Before investing anything, ask these four questions...'
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "Your Pre-Investment\nChecklist"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Four questions with checkboxes
        questions = [
            ("1", "Is this registered\nwith regulators?", GREEN),
            ("2", "Can I verify the\ntrack record?", BLUE),
            ("3", "Does this create\nreal economic value?", PURPLE),
            ("4", "What legal protections\ndo I have?", ORANGE)
        ]
        
        question_items = []
        
        for num, q_text, color in questions:
            # Checkbox
            checkbox = Square(side_length=0.6, color=color, stroke_width=3)
            num_text = Text(num, font_size=28, color=color, weight=BOLD).move_to(checkbox)
            check_group = VGroup(checkbox, num_text)
            
            # Question text
            question = Text(q_text, font_size=24, color=WHITE, line_spacing=1.1)
            
            # Arrange
            item = VGroup(check_group, question).arrange(RIGHT, buff=0.4)
            question_items.append((item, checkbox, color))
        
        # Position questions
        positions = [UP * 2.0, UP * 0.5, DOWN * 1.0, DOWN * 2.5]
        for i, (item, _, _) in enumerate(question_items):
            item.move_to(positions[i])
        
        # Footer message
        footer = Text("Can't answer all 4?\nKeep your money.", 
                     font_size=32, color=RED, weight=BOLD, line_spacing=1.2).move_to(DOWN * 4.3)
        footer_box = SurroundingRectangle(footer, color=RED, buff=0.2, stroke_width=2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        
        # Show questions one by one
        for item, checkbox, color in question_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=step_time * 0.7)
        
        # Check all boxes with checkmarks
        check_icons = []
        for item, checkbox, color in question_items:
            check_icon = self.load_png_icon("check_mark", height=0.5).move_to(checkbox)
            check_icons.append(check_icon)
        
        self.play(
            *[FadeIn(check, scale=0.5) for check in check_icons],
            *[checkbox.animate.set_fill(color, opacity=0.3) for _, checkbox, color in question_items],
            run_time=step_time
        )
        
        self.play(Write(footer), Create(footer_box), run_time=step_time)
        self.play(Flash(footer_box, color=RED), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        'Follow MoneyWise for weekly tips on building wealth safely...'
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        # Title
        title = Text("Protect Your Wealth", font=self.title_font, 
                    font_size=self.font_title_size, color=GOLD, line_spacing=1.1).move_to(UP * 3.5)
        
        # MoneyWise branding with shield
        brand = Text("MoneyWise", font_size=56, color=GOLD, weight=BOLD).move_to(UP * 1.0)
        shield = self.load_png_icon("security_shield", height=2.0).move_to(DOWN * 0.5)
        
        # Tagline
        tagline = Text("The best return is\nkeeping what you've earned.", 
                      font_size=32, color=WHITE, line_spacing=1.2).move_to(DOWN * 2.5)
        
        # CTA icons
        icon_like = self.load_png_icon("thumbs_up", height=1.5)
        icon_share = self.load_png_icon("share", height=1.5)
        icon_subscribe = self.load_png_icon("check", height=1.5)
        
        cta_icons = Group(icon_like, icon_share, icon_subscribe).arrange(RIGHT, buff=1.5).move_to(DOWN * 4.5)
        
        # Labels under icons
        label_like = Text("Like", font_size=24, color=WHITE)
        label_share = Text("Share", font_size=24, color=WHITE)
        label_subscribe = Text("Follow", font_size=24, color=GOLD)
        
        label_like.next_to(icon_like, DOWN, buff=0.3)
        label_share.next_to(icon_share, DOWN, buff=0.3)
        label_subscribe.next_to(icon_subscribe, DOWN, buff=0.3)
        
        labels = VGroup(label_like, label_share, label_subscribe)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            GrowFromCenter(brand),
            FadeIn(shield, scale=0.5),
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
        
        # No fade out at the end - hold the final frame
        self.wait(t_trans)
