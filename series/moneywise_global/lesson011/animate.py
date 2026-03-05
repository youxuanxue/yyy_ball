import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson011VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 11: Central Bank Digital Currency: The Future of Money
    What CBDCs Mean for Your Savings and Financial Freedom
    """

    def build_scene_1(self, scene_data):
        """
        Scene 1: Hook / Pain Point
        'Imagine a world where the government can see every purchase you make...'
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title - wrap for vertical display
        title_text = "The Digital Money\nRevolution Is Here"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size, 
                    color=self.COLOR_RISK, line_spacing=1.1).move_to(UP * 4.0)
        
        # Visual: Eye watching money flow - government surveillance
        eye_icon = self.load_png_icon("data_protection", height=2.2).move_to(UP * 1.5)
        money_icon = self.load_png_icon("money_circulation", height=1.8).move_to(LEFT * 2.0 + DOWN * 0.5)
        lock_icon = self.load_png_icon("lock", height=1.8).move_to(RIGHT * 2.0 + DOWN * 0.5)
        
        # Warning words appearing
        warning_words = VGroup()
        warn_texts = ["Track", "Freeze", "Expire"]
        positions = [LEFT * 2.5 + DOWN * 2.5, ORIGIN + DOWN * 2.8, RIGHT * 2.5 + DOWN * 2.5]
        colors = [ORANGE, RED, ORANGE]
        for txt, pos, col in zip(warn_texts, positions, colors):
            word = Text(txt, font_size=32, color=col, weight=BOLD).move_to(pos)
            warning_words.add(word)
        
        # Globe showing global race
        globe_icon = self.load_png_icon("globe", height=1.5).move_to(DOWN * 4.5)
        
        # Bottom message
        bottom_text = Text("Central banks worldwide\nare racing to create this.", 
                          font_size=30, color=WHITE, weight=BOLD, line_spacing=1.1).move_to(DOWN * 4.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(eye_icon, scale=0.8), run_time=step_time)
        self.play(
            FadeIn(money_icon, shift=RIGHT),
            FadeIn(lock_icon, shift=LEFT),
            run_time=step_time
        )
        self.play(
            LaggedStart(
                *[GrowFromCenter(w) for w in warning_words],
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        self.play(
            FadeOut(warning_words),
            FadeIn(globe_icon, shift=UP),
            run_time=step_time
        )
        self.play(Write(bottom_text), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        'A Central Bank Digital Currency, or CBDC, is simply electronic cash...'
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "What Is a Central Bank\nDigital Currency?"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Visual explanation: Physical cash -> Digital CBDC
        # Left side: Physical dollar
        dollar_icon = self.load_png_icon("banknotes", height=2.0).move_to(LEFT * 2.5 + UP * 1.0)
        physical_label = Text("Physical Cash", font_size=26, color=WHITE).next_to(dollar_icon, DOWN, buff=0.3)
        
        # Arrow transformation
        arrow = Arrow(LEFT * 0.5 + UP * 1.0, RIGHT * 0.5 + UP * 1.0, color=GOLD, stroke_width=4)
        
        # Right side: Phone with digital currency
        phone_icon = self.load_png_icon("mobile", height=2.0).move_to(RIGHT * 2.5 + UP * 1.0)
        digital_label = Text("Digital CBDC", font_size=26, color=GOLD, weight=BOLD).next_to(phone_icon, DOWN, buff=0.3)
        
        # Key difference box
        diff_box = RoundedRectangle(width=5.5, height=1.5, corner_radius=0.2,
                                   color=BLUE_B, fill_opacity=0.3, stroke_width=3).move_to(DOWN * 1.5)
        diff_text = Text("Direct liability of\nthe central bank", 
                        font_size=28, color=WHITE, line_spacing=1.1).move_to(diff_box)
        
        # Bank building icon
        bank_icon = self.load_png_icon("bank_building", height=1.8).move_to(DOWN * 3.8)
        bank_label = Text("Central Bank", font_size=24, color=LIGHT_GRAY).next_to(bank_icon, DOWN, buff=0.2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(dollar_icon, shift=DOWN), Write(physical_label), run_time=step_time)
        self.play(GrowArrow(arrow), run_time=step_time)
        self.play(FadeIn(phone_icon, shift=DOWN), Write(digital_label), run_time=step_time)
        self.play(Create(diff_box), Write(diff_text), run_time=step_time)
        self.play(FadeIn(bank_icon, shift=UP), Write(bank_label), run_time=step_time)
        self.play(
            bank_icon.animate.scale(1.1),
            Flash(bank_icon, color=BLUE),
            run_time=step_time
        )
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        'Here's the critical difference most people miss...'
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title - wrap long title
        title_text = "CBDC vs Bitcoin:\nThe Crucial Difference"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Left side - Bitcoin
        btc_label = Text("BITCOIN", font_size=32, color=ORANGE, weight=BOLD).move_to(LEFT * 2.5 + UP * 2.2)
        btc_icon = self.load_png_icon("bitcoin", height=1.5).move_to(LEFT * 2.5 + UP * 1.0)
        
        btc_features = VGroup()
        btc_items = [
            ("No Gov Backing", WHITE),
            ("Peer-to-Peer", WHITE),
            ("Anonymous", GREEN)
        ]
        for i, (txt, col) in enumerate(btc_items):
            item = Text(txt, font_size=22, color=col).move_to(LEFT * 2.5 + DOWN * (0.2 + i * 0.6))
            btc_features.add(item)
        
        btc_box = SurroundingRectangle(Group(btc_label, btc_icon, btc_features), 
                                       color=ORANGE, buff=0.3, stroke_width=2)
        
        # Right side - CBDC
        cbdc_label = Text("CBDC", font_size=32, color=RED, weight=BOLD).move_to(RIGHT * 2.5 + UP * 2.2)
        cbdc_icon = self.load_png_icon("government", height=1.5).move_to(RIGHT * 2.5 + UP * 1.0)
        
        cbdc_features = VGroup()
        cbdc_items = [
            ("State Backed", WHITE),
            ("Pay Taxes", WHITE),
            ("Fully Tracked", RED)
        ]
        for i, (txt, col) in enumerate(cbdc_items):
            item = Text(txt, font_size=22, color=col).move_to(RIGHT * 2.5 + DOWN * (0.2 + i * 0.6))
            cbdc_features.add(item)
        
        cbdc_box = SurroundingRectangle(Group(cbdc_label, cbdc_icon, cbdc_features), 
                                        color=RED, buff=0.3, stroke_width=2)
        
        # VS in middle
        vs_text = Text("VS", font_size=44, color=GOLD, weight=BOLD).move_to(ORIGIN + UP * 1.0)
        
        # Key insight at bottom
        insight = Text("Every transaction can be\ntracked, traced, controlled.", 
                      font_size=30, color=RED, weight=BOLD, line_spacing=1.2).move_to(DOWN * 3.5)
        insight_box = SurroundingRectangle(insight, color=RED, buff=0.2, stroke_width=2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            Write(btc_label),
            FadeIn(btc_icon, scale=0.8),
            Create(btc_box),
            run_time=step_time
        )
        self.play(
            LaggedStart(*[FadeIn(item, shift=RIGHT) for item in btc_features], lag_ratio=0.2),
            run_time=step_time
        )
        self.play(GrowFromCenter(vs_text), run_time=step_time * 0.5)
        self.play(
            Write(cbdc_label),
            FadeIn(cbdc_icon, scale=0.8),
            Create(cbdc_box),
            run_time=step_time
        )
        self.play(
            LaggedStart(*[FadeIn(item, shift=LEFT) for item in cbdc_features], lag_ratio=0.2),
            run_time=step_time
        )
        self.play(Write(insight), Create(insight_box), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        'If you have a bank account, use digital payments, or care about financial privacy...'
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "Who Needs to\nUnderstand CBDCs"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Three target groups with icons
        groups = [
            ("Bank Account Holders", "bank_cards", "Everyone with savings"),
            ("Digital Payment Users", "online_payment", "Venmo, Apple Pay, etc."),
            ("Privacy-Conscious", "data_protection", "Value financial freedom")
        ]
        
        group_items = []
        for txt, icon_name, desc in groups:
            icon = self.load_png_icon(icon_name, height=1.4)
            main_text = Text(txt, font_size=26, color=WHITE, weight=BOLD)
            sub_text = Text(desc, font_size=20, color=LIGHT_GRAY)
            text_group = VGroup(main_text, sub_text).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            item = Group(icon, text_group).arrange(RIGHT, buff=0.5)
            group_items.append(item)
        
        # Position groups
        group_items[0].move_to(UP * 1.8)
        group_items[1].move_to(DOWN * 0.2)
        group_items[2].move_to(DOWN * 2.2)
        
        # Double-edged sword message
        pros_cons = VGroup()
        pro_text = Text("+ Instant cross-border payments", font_size=24, color=GREEN).move_to(DOWN * 3.5)
        con_text = Text("- Government visibility", font_size=24, color=RED).move_to(DOWN * 4.2)
        pros_cons.add(pro_text, con_text)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(
                FadeIn(group_items[0], shift=RIGHT),
                FadeIn(group_items[1], shift=RIGHT),
                FadeIn(group_items[2], shift=RIGHT),
                lag_ratio=0.4
            ),
            run_time=step_time * 2
        )
        self.play(Write(pro_text), run_time=step_time)
        self.play(Write(con_text), run_time=step_time)
        self.play(
            Flash(pro_text, color=GREEN, line_length=0.1),
            Flash(con_text, color=RED, line_length=0.1),
            run_time=step_time
        )
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        'Here's your action plan...'
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "How to Prepare\nfor the CBDC Era"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Three action steps
        steps = [
            ("1", "Stay Informed", "Track your country's\nCBDC development", BLUE, "policy_document"),
            ("2", "Diversify Assets", "Cash, investments,\nand some crypto", GREEN, "currency_exchange"),
            ("3", "Understand Privacy", "Know the implications\nbefore adoption", ORANGE, "data_protection")
        ]
        
        step_items = []
        for num, label, desc, color, icon_name in steps:
            # Number circle
            circle = Circle(radius=0.4, color=color, fill_opacity=0.3, stroke_width=3)
            num_text = Text(num, font_size=32, color=color, weight=BOLD).move_to(circle)
            num_group = VGroup(circle, num_text)
            
            # Icon
            icon = self.load_png_icon(icon_name, height=1.0)
            
            # Text
            label_text = Text(label, font_size=26, color=WHITE, weight=BOLD)
            desc_text = Text(desc, font_size=20, color=LIGHT_GRAY, line_spacing=1.1)
            text_group = VGroup(label_text, desc_text).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
            
            # Arrange horizontally
            item = Group(num_group, icon, text_group).arrange(RIGHT, buff=0.4)
            step_items.append((item, circle, color))
        
        # Position steps
        positions = [UP * 1.8, DOWN * 0.3, DOWN * 2.4]
        for i, (item, _, _) in enumerate(step_items):
            item.move_to(positions[i])
        
        # Footer message
        footer = Text("Don't wait until\nit's mandatory.", 
                     font_size=30, color=GOLD, weight=BOLD, line_spacing=1.2).move_to(DOWN * 4.3)
        footer_box = SurroundingRectangle(footer, color=GOLD, buff=0.2, stroke_width=2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        
        # Show steps one by one
        for item, circle, color in step_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=step_time)
        
        # Highlight all circles
        self.play(
            *[circle.animate.set_fill(color, opacity=0.5) for _, circle, color in step_items],
            run_time=step_time
        )
        
        self.play(Write(footer), Create(footer_box), run_time=step_time)
        self.play(Flash(footer_box, color=GOLD), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        'Want to stay ahead of the digital money revolution?...'
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        # Title
        title = Text("Stay Ahead of\nthe Revolution", font=self.title_font, 
                    font_size=self.font_title_size, color=GOLD, line_spacing=1.1).move_to(UP * 3.5)
        
        # MoneyWise branding
        brand = Text("MoneyWise", font_size=56, color=GOLD, weight=BOLD).move_to(UP * 1.0)
        
        # Globe and shield combo showing global + protection
        globe_icon = self.load_png_icon("globe", height=1.5).move_to(LEFT * 1.5 + DOWN * 0.5)
        shield_icon = self.load_png_icon("security_shield", height=1.5).move_to(RIGHT * 1.5 + DOWN * 0.5)
        
        # Tagline
        tagline = Text("Weekly insights on\nthe changing financial landscape.", 
                      font_size=28, color=WHITE, line_spacing=1.2).move_to(DOWN * 2.2)
        
        # CTA icons
        icon_like = self.load_png_icon("thumbs_up", height=1.5)
        icon_share = self.load_png_icon("share", height=1.5)
        icon_subscribe = self.load_png_icon("check", height=1.5)
        
        cta_icons = Group(icon_like, icon_share, icon_subscribe).arrange(RIGHT, buff=1.5).move_to(DOWN * 4.2)
        
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
            FadeIn(globe_icon, shift=RIGHT),
            FadeIn(shield_icon, shift=LEFT),
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
