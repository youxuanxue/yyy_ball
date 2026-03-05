import sys
import os
import numpy as np
from manim import *

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Import tools
from src.utils.anim_helper import get_audio_duration
from src.animate.lesson_vertical import MoneyWiseLessonVertical


class Lesson008VerticalScenes(MoneyWiseLessonVertical):
    """
    Lesson 8: Where Can You Actually Invest Your Money?
    Understanding Your Investment Options From Banks to Private Funds
    """

    def build_scene_1(self, scene_data):
        """
        Scene 1: Hook / Pain Point
        'Got some money saved up and wondering where to put it?'
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title - wrap for vertical display
        title_text = "The Investment Question\nEveryone Faces"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size, 
                    color=self.COLOR_RISK, line_spacing=1.1).move_to(UP * 4.0)
        
        # Visual: Person with money bag and question marks
        money_icon = self.load_png_icon("stack_of_money", height=2.5).move_to(LEFT * 2.5)
        person_icon = self.load_png_icon("in_doubt", height=2.5).move_to(ORIGIN)
        
        # Multiple question marks floating
        question_marks = VGroup()
        positions = [RIGHT * 2.5 + UP * 0.5, RIGHT * 2.0 + DOWN * 0.5, RIGHT * 3.0]
        for pos in positions:
            qm = Text("?", font_size=60, color=GOLD, weight=BOLD).move_to(pos)
            question_marks.add(qm)
        
        main_group = Group(money_icon, person_icon, question_marks).move_to(UP * 0.5)
        
        # Bottom message
        bottom_text = Text("Where should your\nmoney actually go?", 
                          font_size=36, color=WHITE, line_spacing=1.2).move_to(DOWN * 2.5)
        
        # Savings account visual - common default
        bank_icon = self.load_png_icon("bank_building", height=1.5).move_to(DOWN * 4.2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(money_icon, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(person_icon, scale=0.8), run_time=step_time)
        self.play(
            LaggedStart(
                *[GrowFromCenter(qm) for qm in question_marks],
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        self.play(Write(bottom_text), run_time=step_time)
        self.play(FadeIn(bank_icon, shift=UP), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene_data):
        """
        Scene 2: What It Is (The Concept)
        'Three main places for your money: banks, public funds, and private investments.'
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "The Three Main\nInvestment Categories"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Three pillars/categories
        # Category 1: Banks
        bank_box = RoundedRectangle(width=2.0, height=4.0, corner_radius=0.2,
                                    color=BLUE_B, fill_opacity=0.3, stroke_width=3)
        bank_icon = self.load_png_icon("bank_building", height=1.2)
        bank_label = Text("Banks", font_size=28, color=WHITE, weight=BOLD)
        bank_desc = Text("Savings\nAccounts", font_size=20, color=LIGHT_GRAY, line_spacing=1.1)
        bank_easy = Text("Easy Access", font_size=18, color=GREEN)
        
        bank_content = Group(bank_icon, bank_label, bank_desc, bank_easy).arrange(DOWN, buff=0.3)
        bank_content.move_to(bank_box)
        bank_group = Group(bank_box, bank_content).move_to(LEFT * 3.2 + UP * 0.5)
        
        # Category 2: Public Funds
        fund_box = RoundedRectangle(width=2.0, height=4.0, corner_radius=0.2,
                                    color=GREEN_B, fill_opacity=0.3, stroke_width=3)
        fund_icon = self.load_png_icon("investment_portfolio", height=1.2)
        fund_label = Text("Public\nFunds", font_size=26, color=WHITE, weight=BOLD, line_spacing=1.0)
        fund_desc = Text("Mutual Funds\n& ETFs", font_size=20, color=LIGHT_GRAY, line_spacing=1.1)
        fund_min = Text("Low Minimums", font_size=18, color=GREEN)
        
        fund_content = Group(fund_icon, fund_label, fund_desc, fund_min).arrange(DOWN, buff=0.3)
        fund_content.move_to(fund_box)
        fund_group = Group(fund_box, fund_content).move_to(ORIGIN + UP * 0.5)
        
        # Category 3: Private Investments
        private_box = RoundedRectangle(width=2.0, height=4.0, corner_radius=0.2,
                                       color=PURPLE_B, fill_opacity=0.3, stroke_width=3)
        private_icon = self.load_png_icon("briefcase", height=1.2)
        private_label = Text("Private\nFunds", font_size=26, color=WHITE, weight=BOLD, line_spacing=1.0)
        private_desc = Text("Hedge Funds\nPrivate Equity", font_size=20, color=LIGHT_GRAY, line_spacing=1.1)
        private_access = Text("Exclusive", font_size=18, color=ORANGE)
        
        private_content = Group(private_icon, private_label, private_desc, private_access).arrange(DOWN, buff=0.3)
        private_content.move_to(private_box)
        private_group = Group(private_box, private_content).move_to(RIGHT * 3.2 + UP * 0.5)
        
        # Bottom summary
        summary = Text("Each has different rules and requirements", 
                      font_size=28, color=WHITE).move_to(DOWN * 3.5)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(bank_group, shift=UP), run_time=step_time)
        self.play(FadeIn(fund_group, shift=UP), run_time=step_time)
        self.play(FadeIn(private_group, shift=UP), run_time=step_time)
        self.play(
            bank_box.animate.set_stroke(color=BLUE, width=4),
            fund_box.animate.set_stroke(color=GREEN, width=4),
            private_box.animate.set_stroke(color=PURPLE, width=4),
            run_time=step_time
        )
        self.play(Write(summary), run_time=step_time)
        self.wait(step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene_data):
        """
        Scene 3: Why It Matters (The Stakes)
        'Each option has different rules. Your access level determines your investment universe.'
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 6
        step_time = (page_duration - t_trans) / N

        # Title - wrap long title
        title_text = "Why Your Options Are\nLimited—And That's Okay"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Create access level pyramid
        # Bottom - Everyone (Banks)
        level_1 = RoundedRectangle(width=8, height=1.3, corner_radius=0.1,
                                   color=BLUE_B, fill_opacity=0.4, stroke_width=2)
        level_1_text = Text("Savings Accounts", font_size=26, color=WHITE)
        level_1_access = Text("Anyone", font_size=20, color=GREEN)
        level_1_group = VGroup(level_1_text, level_1_access).arrange(RIGHT, buff=1.0).move_to(level_1)
        
        # Middle - Most Investors (Public Funds)
        level_2 = RoundedRectangle(width=6, height=1.3, corner_radius=0.1,
                                   color=GREEN_B, fill_opacity=0.4, stroke_width=2)
        level_2_text = Text("Mutual Funds & ETFs", font_size=24, color=WHITE)
        level_2_access = Text("$100+", font_size=20, color=WHITE)
        level_2_group = VGroup(level_2_text, level_2_access).arrange(RIGHT, buff=0.8).move_to(level_2)
        
        # Top - Accredited Only (Private)
        level_3 = RoundedRectangle(width=4, height=1.3, corner_radius=0.1,
                                   color=PURPLE_B, fill_opacity=0.4, stroke_width=2)
        level_3_text = Text("Private Funds", font_size=22, color=WHITE)
        level_3_access = Text("$100K+", font_size=20, color=ORANGE)
        level_3_group = VGroup(level_3_text, level_3_access).arrange(RIGHT, buff=0.5).move_to(level_3)
        
        # Stack them as pyramid
        pyramid = VGroup(
            VGroup(level_1, level_1_group),
            VGroup(level_2, level_2_group),
            VGroup(level_3, level_3_group)
        ).arrange(UP, buff=0.3).move_to(UP * 0.3)
        
        # Key insight
        insight = Text("Your current wealth\ndetermines your options", 
                      font_size=32, color=WHITE, line_spacing=1.2).move_to(DOWN * 2.8)
        insight_box = SurroundingRectangle(insight, color=GOLD, buff=0.3, stroke_width=2)
        
        # Lock icons for restricted access
        lock_icon = self.load_png_icon("lock", height=0.8).next_to(level_3, RIGHT, buff=0.3)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(pyramid[0], shift=UP), run_time=step_time)
        self.play(FadeIn(pyramid[1], shift=UP), run_time=step_time)
        self.play(FadeIn(pyramid[2], shift=UP), FadeIn(lock_icon), run_time=step_time)
        self.play(Write(insight), Create(insight_box), run_time=step_time)
        self.play(Flash(insight_box, color=GOLD), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene_data):
        """
        Scene 4: Who This Applies To (Relevance)
        'If you're just starting out, stick with bank savings and low-cost index funds.'
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 5
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "Finding Your\nInvestment Level"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Two profiles
        # Profile 1: Just Starting
        starter_box = RoundedRectangle(width=3.5, height=4.0, corner_radius=0.2,
                                       color=BLUE_B, fill_opacity=0.2, stroke_width=3)
        starter_icon = self.load_png_icon("user", height=1.2)
        starter_label = Text("Just Starting", font_size=26, color=WHITE, weight=BOLD)
        starter_amount = Text("$100 - $10K", font_size=22, color=GREEN)
        starter_options = Text("• Savings Account\n• Index Funds", font_size=20, 
                              color=WHITE, line_spacing=1.3)
        
        starter_content = Group(starter_icon, starter_label, starter_amount, starter_options).arrange(DOWN, buff=0.3)
        starter_content.move_to(starter_box)
        starter_group = Group(starter_box, starter_content).move_to(LEFT * 2.5 + UP * 0.5)
        
        # Profile 2: More to Invest
        advanced_box = RoundedRectangle(width=3.5, height=4.0, corner_radius=0.2,
                                        color=PURPLE_B, fill_opacity=0.2, stroke_width=3)
        advanced_icon = self.load_png_icon("businessman", height=1.2)
        advanced_label = Text("More to Invest", font_size=26, color=WHITE, weight=BOLD)
        advanced_amount = Text("$50K+", font_size=22, color=GOLD)
        advanced_options = Text("• All Above, Plus\n• More Options", font_size=20, 
                               color=WHITE, line_spacing=1.3)
        
        advanced_content = Group(advanced_icon, advanced_label, advanced_amount, advanced_options).arrange(DOWN, buff=0.3)
        advanced_content.move_to(advanced_box)
        advanced_group = Group(advanced_box, advanced_content).move_to(RIGHT * 2.5 + UP * 0.5)
        
        # Key message
        key_msg = Text("Match your situation\nto the right vehicle", 
                      font_size=32, color=WHITE, line_spacing=1.2).move_to(DOWN * 3.5)
        
        # Target icon
        target_icon = self.load_png_icon("target", height=1.2).move_to(DOWN * 5.0)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(starter_group, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(advanced_group, shift=LEFT), run_time=step_time)
        self.play(Write(key_msg), run_time=step_time)
        self.play(FadeIn(target_icon, shift=UP), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene_data):
        """
        Scene 5: How To Take Action (Strategy)
        'Three-step plan: emergency fund, index funds, then explore.'
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 7
        step_time = (page_duration - t_trans) / N

        # Title
        title_text = "Your Three-Step\nInvestment Plan"
        title = Text(title_text, font=self.title_font, font_size=self.font_title_size,
                    color=GOLD, line_spacing=1.1).move_to(UP * 4.0)
        
        # Three steps with icons
        steps = [
            ("1", "Emergency Fund", "3-6 months expenses\nin high-yield savings", "safe", GREEN),
            ("2", "Start Investing", "Low-cost index funds\nvia 401k or IRA", "investment", BLUE),
            ("3", "Grow & Explore", "Add options as\nwealth increases", "growing_money", GOLD)
        ]
        
        step_items = []
        
        for num, title_txt, desc, icon_name, color in steps:
            # Number circle
            circle = Circle(radius=0.5, color=color, fill_opacity=0.8, stroke_width=0)
            num_text = Text(num, font_size=40, color=BLACK, weight=BOLD).move_to(circle)
            num_group = VGroup(circle, num_text)
            
            # Step title
            
            step_title = Text(title_txt, font_size=28, color=WHITE, weight=BOLD)
            
            # Description
            step_desc = Text(desc, font_size=22, color=LIGHT_GRAY, line_spacing=1.2)
            
            # Icon
            icon = self.load_png_icon(icon_name, height=1.0)
            
            # Arrange in a row
            text_group = VGroup(step_title, step_desc).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            item = Group(num_group, text_group, icon).arrange(RIGHT, buff=0.5)
            step_items.append(item)
        
        # Position steps
        step_items[0].move_to(UP * 2.0)
        step_items[1].move_to(DOWN * 0.3)
        step_items[2].move_to(DOWN * 2.6)
        
        # Footer
        footer = Text("Simple, effective, proven.", font_size=34, color=GREEN,
                     weight=BOLD).move_to(DOWN * 4.5)
        footer_box = SurroundingRectangle(footer, color=GREEN, buff=0.2, stroke_width=2)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(step_items[0], shift=RIGHT), run_time=step_time)
        self.play(FadeIn(step_items[1], shift=RIGHT), run_time=step_time)
        self.play(FadeIn(step_items[2], shift=RIGHT), run_time=step_time)
        # Highlight circles
        self.play(
            step_items[0][0][0].animate.set_fill(GREEN, opacity=1.0),
            step_items[1][0][0].animate.set_fill(BLUE, opacity=1.0),
            step_items[2][0][0].animate.set_fill(GOLD, opacity=1.0),
            run_time=step_time
        )
        self.play(Write(footer), Create(footer_box), run_time=step_time)
        self.play(Flash(footer_box, color=GREEN), run_time=step_time)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene_data):
        """
        Scene 6: Call to Action (CTA)
        'Subscribe to MoneyWise for more practical investing tips.'
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        N = 4
        step_time = (page_duration - t_trans) / N

        # Title
        title = Text("Subscribe for More", font=self.title_font, 
                    font_size=self.font_title_size, color=GOLD, line_spacing=1.1).move_to(UP * 3.5)
        
        # MoneyWise branding
        brand = Text("MoneyWise", font_size=56, color=GOLD, weight=BOLD).move_to(UP * 1.0)
        
        # Tagline
        tagline = Text("Make Your Money\nWork Harder", 
                      font_size=36, color=WHITE, line_spacing=1.2).move_to(DOWN * 0.8)
        
        # CTA icons
        icon_like = self.load_png_icon("thumbs_up", height=1.5)
        icon_share = self.load_png_icon("share", height=1.5)
        icon_subscribe = self.load_png_icon("check", height=1.5)
        
        cta_icons = Group(icon_like, icon_share, icon_subscribe).arrange(RIGHT, buff=1.5).move_to(DOWN * 3.0)
        
        # Labels under icons
        label_like = Text("Like", font_size=24, color=WHITE)
        label_share = Text("Share", font_size=24, color=WHITE)
        label_subscribe = Text("Subscribe", font_size=24, color=GOLD)
        
        label_like.next_to(icon_like, DOWN, buff=0.3)
        label_share.next_to(icon_share, DOWN, buff=0.3)
        label_subscribe.next_to(icon_subscribe, DOWN, buff=0.3)
        
        labels = VGroup(label_like, label_share, label_subscribe)
        
        # Animations
        self.play(Write(title), run_time=step_time)
        self.play(
            GrowFromCenter(brand),
            Write(tagline),
            run_time=step_time
        )
        self.play(
            LaggedStart(
                FadeIn(icon_like, scale=0.5),
                FadeIn(icon_share, scale=0.5),
                FadeIn(icon_subscribe, scale=0.5),
                lag_ratio=0.3
            ),
            run_time=step_time
        )
        self.play(
            Write(labels),
            icon_subscribe.animate.scale(1.2),
            run_time=step_time
        )
        
        # No fade out at the end - hold the final frame
        self.wait(t_trans)
