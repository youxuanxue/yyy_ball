import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson011VerticalScenes(Zsxq100keLessonVertical):
    """
    第011课：数字货币
    副标题：央行数字货币与比特币
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：引发共鸣 -> 反常识观点 -> 抓住注意力
        
        口播稿关键词/短语：
        - "数字货币就是比特币" -> 误区认知
        - "完全是两码事" -> 核心反转
        - "央行数字货币...有国家背书" -> 正方
        - "比特币...就是游戏币" -> 反方
        
        动态标题：「数字货币=比特币？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、误区文字、左右对比图标、VS、反转文字、结论）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题 (y=4.0) - 引发好奇
        title = Text(
            "数字货币=比特币？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 误区文字 - 很多人以为是一回事
        wrong_text = Text(
            "「很多人以为是一回事」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(UP * 2.5)
        wrong_cross = Cross(wrong_text, stroke_color=RED, stroke_width=4)
        
        # 3. 左侧：央行数字货币（有背书）
        # 图标来源：bank_building 代表央行
        dcep_icon = self.load_png_icon("bank_building", height=1.8).move_to(UP * 0.5 + LEFT * 2.2)
        dcep_label = Text("央行数字货币", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(dcep_icon, DOWN, buff=0.2)
        dcep_tag = Text("有国家背书", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(dcep_label, DOWN, buff=0.15)
        dcep_group = Group(dcep_icon, dcep_label, dcep_tag)
        
        # 4. 右侧：比特币（无背书）
        # 图标来源：bitcoin
        btc_icon = self.load_png_icon("bitcoin", height=1.8).move_to(UP * 0.5 + RIGHT * 2.2)
        btc_label = Text("比特币", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(btc_icon, DOWN, buff=0.2)
        btc_tag = Text("就是游戏币", font=self.body_font, font_size=self.font_small_size, color=RED).next_to(btc_label, DOWN, buff=0.15)
        btc_group = Group(btc_icon, btc_label, btc_tag)
        
        # 5. 中间 VS
        vs_text = Text("VS", font=self.title_font, font_size=self.font_body_size, color=RED).move_to(UP * 0.5)
        
        # 6. 底部结论 - 完全是两码事
        conclusion = Text(
            "完全是两码事！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(wrong_text), Create(wrong_cross), run_time=step_time)
        self.play(
            FadeIn(dcep_group, shift=RIGHT), 
            FadeIn(btc_group, shift=LEFT),
            run_time=step_time
        )
        self.play(FadeIn(vs_text, scale=0.5), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)
        self.play(Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：核心概念 -> 层级结构 -> 清晰分类
        
        口播稿关键词/短语：
        - "央行数字货币就是电子版人民币" -> 核心定义
        - "微信支付宝不一样" -> 对比
        - "银行存款的电子化" vs "真正的现金替代" -> 区别
        - "M0替代" -> 专业术语
        
        动态标题：「电子版人民币」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、核心定义、对比组、M0概念、总结）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部：核心概念标题
        title = Text(
            "电子版人民币", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心定义 - 金句框
        definition = Text(
            "央行数字货币 = 电子版现金", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(UP * 2.5)
        definition_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(definition, buff=0.4)
        definition_group = VGroup(definition_box, definition)
        
        # 3. 对比：微信支付宝 vs 数字人民币
        # 左侧：微信支付宝
        left_icon = self.load_png_icon("smartphone", height=1.5).move_to(UP * 0.3 + LEFT * 2.5)
        left_label = Text("微信/支付宝", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(left_icon, DOWN, buff=0.15)
        left_desc = Text("银行存款电子化", font=self.body_font, font_size=self.font_small_size, color=GRAY).next_to(left_label, DOWN, buff=0.1)
        left_group = Group(left_icon, left_label, left_desc)
        
        # 右侧：数字人民币
        right_icon = self.load_png_icon("money", height=1.5).move_to(UP * 0.3 + RIGHT * 2.5)
        right_label = Text("数字人民币", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(right_icon, DOWN, buff=0.15)
        right_desc = Text("真正的现金替代", font=self.body_font, font_size=self.font_small_size, color=GREEN).next_to(right_label, DOWN, buff=0.1)
        right_group = Group(right_icon, right_label, right_desc)
        
        # 中间箭头
        arrow = Text("≠", font=self.title_font, font_size=self.font_body_size, color=RED).move_to(UP * 0.3)
        
        compare_group = Group(left_group, arrow, right_group)
        
        # 4. M0替代概念
        m0_text = Text(
            "发一块数字货币，销毁一块纸币", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).move_to(DOWN * 2.5)
        
        # 5. 底部总结
        summary = Text(
            "总量不变，形式变了", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(definition_group, scale=0.8), run_time=step_time)
        self.play(FadeIn(compare_group, shift=UP), run_time=step_time)
        self.play(Write(m0_text), run_time=step_time)
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：核心洞察 -> 权力结构 -> 战略意义
        
        口播稿关键词/短语：
        - "比特币没有国家背书，就是空气" -> 核心对比
        - "央行数字货币有国家信用，有枪杆子保障" -> 权威背书
        - "人民币国际化" -> 战略目标
        - "绕开SWIFT系统" -> 具体手段
        
        动态标题：「有背书 vs 空气」
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、对比组、战略目标、SWIFT、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "有背书 vs 空气", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心对比
        # 左侧：央行数字货币
        row1_label = Text("央行数字货币", font=self.title_font, font_size=self.font_body_size, color=GOLD).move_to(UP * 2.2 + LEFT * 2.0)
        row1_desc = Text("国家信用 + 枪杆子", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(row1_label, RIGHT, buff=0.5)
        row1 = VGroup(row1_label, row1_desc)
        
        # 右侧：比特币
        row2_label = Text("比特币", font=self.title_font, font_size=self.font_body_size, color=GRAY).move_to(UP * 1.0 + LEFT * 2.0)
        row2_desc = Text("无背书 = 空气", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(row2_label, RIGHT, buff=0.5)
        row2 = VGroup(row2_label, row2_desc)
        
        rows = [row1, row2]
        
        # 3. 战略目标 - 人民币国际化
        strategy_icon = self.load_png_icon("globe", height=1.5).move_to(DOWN * 0.8 + LEFT * 2.5)
        strategy_text = Text("战略目标：人民币国际化", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(strategy_icon, RIGHT, buff=0.3)
        strategy_group = Group(strategy_icon, strategy_text)
        
        # 4. SWIFT系统
        swift_text = Text(
            "绕开美国控制的SWIFT系统", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(DOWN * 2.3)
        swift_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=ORANGE, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=ORANGE
        ).surround(swift_text, buff=0.4)
        swift_group = VGroup(swift_box, swift_text)
        
        # 5. 底部结论
        conclusion = Text(
            "跨境支付更方便", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=RIGHT) for row in rows], 
                lag_ratio=0.4
            ), 
            run_time=step_time
        )
        self.play(FadeIn(strategy_group, shift=UP), run_time=step_time)
        self.play(FadeIn(swift_group, scale=0.8), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：具象化场景 -> 对号入座 -> 引发认同
        
        口播稿关键词/短语：
        - "未来支付趋势" -> 场景1
        - "发工资、买东西可能都是数字货币" -> 应用场景
        - "有人拉你炒比特币发财" -> 风险提示
        - "涨跌全靠炒作" -> 本质揭露
        
        动态标题：「未来支付趋势」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、应用场景、警示、风险揭露、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "未来支付趋势", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 应用场景 - 使用图标展示
        # 场景1：发工资
        scene1_icon = self.load_png_icon("coins", height=1.2).move_to(UP * 2.2 + LEFT * 2.5)
        scene1_text = Text("发工资", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(scene1_icon, RIGHT, buff=0.3)
        scene1 = Group(scene1_icon, scene1_text)
        
        # 场景2：买东西
        scene2_icon = self.load_png_icon("smartphone", height=1.2).move_to(UP * 0.8 + LEFT * 2.5)
        scene2_text = Text("买东西", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(scene2_icon, RIGHT, buff=0.3)
        scene2 = Group(scene2_icon, scene2_text)
        
        scenes = [scene1, scene2]
        
        # 3. 上方提示 - 数字货币是必修课
        tip_text = Text(
            "数字货币是必修课", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).move_to(UP * 1.5 + RIGHT * 1.5)
        
        # 4. 警示区域 - 炒比特币风险
        warning_icon = self.load_png_icon("bitcoin", height=1.2).move_to(DOWN * 1.0 + LEFT * 2.5)
        warning_text = Text("有人拉你炒比特币？", font=self.body_font, font_size=self.font_body_size, color=RED).next_to(warning_icon, RIGHT, buff=0.3)
        warning_group = Group(warning_icon, warning_text)
        
        # 5. 风险揭露
        risk_text = Text(
            "涨跌全靠炒作，小心！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(DOWN * 2.5)
        risk_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=RED, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=RED
        ).surround(risk_text, buff=0.4)
        risk_group = VGroup(risk_box, risk_text)
        
        # 6. 底部结论
        conclusion = Text(
            "了解趋势，警惕陷阱", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.2)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(
            LaggedStart(
                *[FadeIn(s, shift=RIGHT) for s in scenes], 
                lag_ratio=0.3
            ),
            FadeIn(tip_text, shift=LEFT),
            run_time=step_time
        )
        self.play(FadeIn(warning_group, shift=UP), run_time=step_time)
        self.play(FadeIn(risk_group, scale=0.8), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：行动步骤 -> 逐项弹出 -> 强调可执行
        
        口播稿关键词/短语：
        - "判断标准：看有没有国家背书" -> 核心口诀
        - "央行数字货币可以放心用" -> 策略1
        - "比特币之类...投机可以，当资产配置很危险" -> 策略2
        - "优先关注正规的数字人民币" -> 策略3
        
        动态标题：「一招判断」
        使用 LaggedStart 实现逐项弹出效果
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、核心口诀、三策略、结论、强调）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "一招判断", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心口诀 - 金句框
        slogan = Text(
            "看有没有国家背书", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(UP * 2.5)
        slogan_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GOLD
        ).surround(slogan, buff=0.4)
        slogan_group = VGroup(slogan_box, slogan)
        
        # 3. 策略列表
        item1 = Text("① 央行数字货币：放心用，会越来越普及", font=self.body_font, font_size=self.font_small_size, color=GREEN).move_to(UP * 0.8)
        item2 = Text("② 比特币等加密货币：投机可以，配置危险", font=self.body_font, font_size=self.font_small_size, color=ORANGE).move_to(DOWN * 0.4)
        item3 = Text("③ 普通人：优先关注数字人民币", font=self.body_font, font_size=self.font_small_size, color=GREEN).move_to(DOWN * 1.6)
        
        items = [item1, item2, item3]
        
        # 4. 底部结论
        conclusion = Text(
            "有背书才靠谱", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(slogan_group, scale=0.8), Circumscribe(slogan, color=GOLD), run_time=step_time)
        # 使用 LaggedStart 逐项弹出，lag_ratio=0.3
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT) for item in items], 
                lag_ratio=0.3
            ), 
            run_time=2*step_time
        )
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：低门槛互动 -> 强调动画 -> 引导关注
        
        口播稿关键词/短语：
        - "分清数字货币和比特币" -> 回顾
        - "关注一下数字人民币App" -> 具体行动
        - "点赞收藏" -> 互动号召
        
        动态标题：「下载数字人民币App」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、互动任务、互动图标、系列口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 核心CTA标题
        title = Text(
            "关注数字人民币App", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 3.5)
        
        # 2. 互动任务 - 分清两者
        task_text = Text(
            "分清数字货币和比特币了吗？", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(UP * 1.8)
        
        # 3. 点赞图标
        # 图标来源：like 在 all_png_names.txt
        like_icon = self.load_png_icon("like", height=2.0).move_to(LEFT * 2 + DOWN * 0.3)
        like_text = Text("点赞", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(like_icon, DOWN, buff=0.2)
        like_group = Group(like_icon, like_text)
        
        # 4. 收藏图标
        # 图标来源：add_to_favorites 在 all_png_names.txt
        fav_icon = self.load_png_icon("add_to_favorites", height=2.0).move_to(RIGHT * 2 + DOWN * 0.3)
        fav_text = Text("收藏", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(fav_icon, DOWN, buff=0.2)
        fav_group = Group(fav_icon, fav_text)
        
        icons_group = Group(like_group, fav_group)
        
        # 5. 系列口号 - 金句框
        slogan_text = Text(
            "每天一课，日日生金！", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.5)
        slogan_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GOLD, 
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=GOLD
        ).surround(slogan_text, buff=0.5)
        slogan_group = VGroup(slogan_box, slogan_text)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(task_text), Circumscribe(task_text, color=GOLD), run_time=step_time)
        self.play(FadeIn(icons_group, shift=UP), run_time=step_time)
        self.play(
            FadeIn(slogan_group, scale=0.8), 
            Circumscribe(slogan_text, color=GOLD, fade_out=True),
            run_time=step_time
        )

        # 不需要淡出，作为结尾画面保留
        self.wait(0.5)

    def get_cover_decoration_icons(self):
        """
        根据 build_scene_1 到 build_scene_6 的动画内容和 script.json 的 icons 字段
        选择封面装饰图标，不超过5个。
        
        选用图标及其理由：
        - bitcoin: 比特币是本课核心对比对象
        - bank_building: 央行数字货币代表
        - money: 货币/现金概念
        - globe: 人民币国际化战略
        - smartphone: 数字支付场景
        """
        return ["bitcoin", "bank_building", "money", "globe", "smartphone"]
