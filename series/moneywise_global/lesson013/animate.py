import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson013VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 13: The Hidden Power of Lending Licenses
    Why Only Certain Institutions Can Legally Loan You Money
    """

    def build_scene_1(self, scene_data):
        """
        Scene 1: Hook / Pain Point
        'Here's something most people don't realize: making money in finance...'
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title - wrap for vertical display
        title_text = "The Secret Behind\nBank Profits"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size, 
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Visual: Bank building with money flowing in
        bank_icon = self.load_png_icon("bank_building", height=2.5).move_to(ORIGIN + UP * 0.5)
        
        # Money icons flowing towards bank
        money_icons = []
        positions = [
            LEFT * 3 + UP * 1.5, LEFT * 3 + DOWN * 0.5, LEFT * 3 + DOWN * 2.5,
            RIGHT * 3 + UP * 1.5, RIGHT * 3 + DOWN * 0.5, RIGHT * 3 + DOWN * 2.5
        ]
        for pos in positions:
            m = self.load_png_icon("money", height=0.8).move_to(pos)
            money_icons.append(m)
        
        # Certificate/License icon
        license_icon = self.load_png_icon("certificate", height=1.5).move_to(DOWN * 2.0)
        license_text = Text("The License", font_size=28, color=GOLD, weight=BOLD).next_to(license_icon, DOWN, buff=0.2)
        
        # Bottom text
        bottom_text = Text("They hold something\nothers can't get.", 
                          font_size=32, color=WHITE, line_spacing=1.2).move_to(DOWN * 4.2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(bank_icon, scale=0.8), run_time=step_time)
        
        # Money flows toward bank
        self.play(
            *[FadeIn(m, shift=ORIGIN - m.get_center()) for m in money_icons[:3]],
            run_time=step_time
        )
        self.play(
            *[m.animate.move_to(bank_icon.get_center() + LEFT * 0.5).set_opacity(0) for m in money_icons[:3]],
            *[FadeIn(m, shift=ORIGIN - m.get_center()) for m in money_icons[3:]],
            run_time=step_time
        )
        
        self.play(
            FadeIn(license_icon, shift=UP),
            Write(license_text),
            run_time=step_time
        )
        self.play(Write(bottom_text), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        'In most countries, you can't just lend money to strangers...'
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "What a Lending License\nActually Means"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Licensed vs Unlicensed comparison
        # Left: Licensed (Banks, Credit Unions)
        licensed_header = Text("LICENSED", font_size=32, color=GREEN, weight=BOLD).move_to(LEFT * 2.5 + UP * 2.2)
        
        licensed_items = []
        licensed_texts = ["Banks", "Credit Unions", "Collect Deposits", "Make Loans"]
        icons_licensed = ["bank", "bank_building", "deposit", "loan"]
        for i, (txt, icon_name) in enumerate(zip(licensed_texts, icons_licensed)):
            icon = self.load_png_icon(icon_name, height=0.7)
            text = Text(txt, font_size=22, color=WHITE)
            item = Group(icon, text).arrange(RIGHT, buff=0.3)
            licensed_items.append(item)
        licensed_group = Group(*licensed_items).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(LEFT * 2.3 + DOWN * 0.2)
        
        licensed_box = SurroundingRectangle(Group(licensed_header, licensed_group), color=GREEN, buff=0.3, stroke_width=2)
        
        # Right: Unlicensed (Most businesses)
        unlicensed_header = Text("UNLICENSED", font_size=32, color=RED, weight=BOLD).move_to(RIGHT * 2.5 + UP * 2.2)
        
        unlicensed_text = Text("Most Businesses\nCannot Lend", font_size=24, color=LIGHT_GRAY, line_spacing=1.2).move_to(RIGHT * 2.5 + DOWN * 0.2)
        lock_icon = self.load_png_icon("lock", height=1.5).move_to(RIGHT * 2.5 + DOWN * 2.0)
        
        unlicensed_box = SurroundingRectangle(Group(unlicensed_header, unlicensed_text, lock_icon), color=RED, buff=0.3, stroke_width=2)
        
        # Bottom: Key message
        bottom_text = Text("Without it, lending is illegal.", 
                          font_size=32, color=RED, weight=BOLD).move_to(DOWN * 4.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(Write(licensed_header), Create(licensed_box), run_time=step_time)
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT) for item in licensed_items],
                lag_ratio=0.25
            ),
            run_time=step_time * 1.5
        )
        self.play(
            Write(unlicensed_header), 
            Create(unlicensed_box),
            run_time=step_time
        )
        self.play(
            Write(unlicensed_text),
            FadeIn(lock_icon, scale=0.5),
            run_time=step_time
        )
        self.play(Write(bottom_text), Flash(bottom_text, color=RED), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        'This licensing system exists to protect you...'
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title - wrap long title
        title_text = "Why Lending Regulations\nProtect You"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Visual: Licensed lender (safe) vs Unlicensed (dangerous)
        # Left: Licensed - with shield
        safe_header = Text("LICENSED", font_size=28, color=GREEN, weight=BOLD)
        shield_icon = self.load_png_icon("security_shield", height=1.5)
        safe_benefits = VGroup(
            Text("• Fair interest rates", font_size=22, color=WHITE),
            Text("• Clear disclosures", font_size=22, color=WHITE),
            Text("• Legal protection", font_size=22, color=WHITE)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        safe_group = Group(safe_header, shield_icon, safe_benefits).arrange(DOWN, buff=0.3).move_to(LEFT * 2.5 + UP * 0.3)
        
        # Right: Unlicensed - with warning
        danger_header = Text("UNLICENSED", font_size=28, color=RED, weight=BOLD)
        warning_icon = self.load_png_icon("warning", height=1.5)
        danger_list = VGroup(
            Text("• Predatory rates", font_size=22, color=RED),
            Text("• Hidden fees", font_size=22, color=RED),
            Text("• No recourse", font_size=22, color=RED)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        danger_group = Group(danger_header, warning_icon, danger_list).arrange(DOWN, buff=0.3).move_to(RIGHT * 2.5 + UP * 0.3)
        
        # VS text
        vs_text = Text("VS", font_size=40, color=GOLD, weight=BOLD).move_to(ORIGIN + UP * 1.0)
        
        # Bottom insight
        insight_text = Text("Regulations exist\nfor your safety.", 
                           font_size=34, color=WHITE, weight=BOLD, line_spacing=1.2).move_to(DOWN * 3.8)
        insight_box = SurroundingRectangle(insight_text, color=GREEN, buff=0.2, stroke_width=2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            FadeIn(safe_group, shift=RIGHT),
            run_time=step_time
        )
        self.play(GrowFromCenter(vs_text), run_time=step_time * 0.5)
        self.play(
            FadeIn(danger_group, shift=LEFT),
            run_time=step_time
        )
        self.play(
            shield_icon.animate.scale(1.1),
            warning_icon.animate.scale(1.1),
            run_time=step_time
        )
        self.play(Write(insight_text), Create(insight_box), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        'This affects you whenever you need to borrow money...'
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "Who Needs to Know\nAbout Lending Licenses"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Borrowing scenarios
        scenarios = [
            ("Mortgage", "house", "Buying a home"),
            ("Car Loan", "car", "Financing a vehicle"),
            ("Personal Credit", "credit_card", "Credit lines")
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
        scenario_items[0].move_to(UP * 1.5)
        scenario_items[1].move_to(DOWN * 0.3)
        scenario_items[2].move_to(DOWN * 2.1)
        
        # Warning message
        warning = Text("Loans outside the banking\nsystem? Proceed with caution!", 
                      font_size=28, color=ORANGE, weight=BOLD, line_spacing=1.2).move_to(DOWN * 4.0)
        warning_icon = self.load_png_icon("warning", height=1.0).next_to(warning, LEFT, buff=0.3)
        
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
            Write(warning),
            FadeIn(warning_icon, scale=0.5),
            run_time=step_time
        )
        self.play(
            Flash(warning_icon, color=ORANGE),
            run_time=step_time
        )
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        'Before borrowing, take these steps...'
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "Your Safe\nBorrowing Checklist"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Three steps with checkboxes
        steps = [
            ("1", "Verify registration\nwith regulators", GREEN, "certificate"),
            ("2", "Compare rates from\nmultiple lenders", BLUE, "percentage"),
            ("3", "Read all disclosures\ncarefully", PURPLE, "document")
        ]
        
        step_items = []
        
        for num, step_text, color, icon_name in steps:
            # Checkbox
            checkbox = Square(side_length=0.7, color=color, stroke_width=3)
            num_text = Text(num, font_size=30, color=color, weight=BOLD).move_to(checkbox)
            check_group = VGroup(checkbox, num_text)
            
            # Icon
            icon = self.load_png_icon(icon_name, height=0.9)
            
            # Step text
            step_label = Text(step_text, font_size=24, color=WHITE, line_spacing=1.1)
            
            # Arrange
            item = Group(check_group, icon, step_label).arrange(RIGHT, buff=0.4)
            step_items.append((item, checkbox, color))
        
        # Position steps
        positions = [UP * 1.8, DOWN * 0.2, DOWN * 2.2]
        for i, (item, _, _) in enumerate(step_items):
            item.move_to(positions[i])
        
        # Footer: Red flag warning
        footer = Text("No clear terms?\nThat's a red flag.", 
                     font_size=32, color=RED, weight=BOLD, line_spacing=1.2).move_to(DOWN * 4.3)
        footer_box = SurroundingRectangle(footer, color=RED, buff=0.2, stroke_width=2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        
        # Show steps one by one
        for item, checkbox, color in step_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=step_time)
        
        # Check all boxes
        check_icons = []
        for item, checkbox, color in step_items:
            check_icon = self.load_png_icon("check_mark", height=0.5).move_to(checkbox)
            check_icons.append(check_icon)
        
        self.play(
            *[FadeIn(check, scale=0.5) for check in check_icons],
            *[checkbox.animate.set_fill(color, opacity=0.3) for _, checkbox, color in step_items],
            run_time=step_time
        )
        
        self.play(Write(footer), Create(footer_box), run_time=step_time)
        self.play(Flash(footer_box, color=RED), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        'Want to understand how the financial system really works?...'
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        # Title
        title = Text("Understand the System", font=self.title_font, 
                    font_size=self.font_title_size, color=GOLD, line_spacing=1.1).move_to(UP * 3.5)
        
        # MoneyWise branding
        brand = Text("MoneyWise", font_size=56, color=GOLD, weight=BOLD).move_to(UP * 1.0)
        
        # Knowledge shield visual
        shield = self.load_png_icon("security_shield", height=2.0).move_to(DOWN * 0.5)
        brain_icon = self.load_png_icon("brain", height=1.0).move_to(shield.get_center())
        
        # Tagline
        tagline = Text("Knowledge is your\nbest defense.", 
                      font_size=34, color=WHITE, line_spacing=1.2).move_to(DOWN * 2.5)
        
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
        
        # No fade out at the end - hold the final frame
        self.wait(t_trans)
