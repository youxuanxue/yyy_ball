import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson009VerticalScenes(Zsxq100keLessonVertical):
    """
    第009课：股票与股市全貌
    副标题：上市的本质是什么
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：引发共鸣 -> 反常识观点 -> 抓住注意力
        
        口播稿关键词/短语：
        - "同样一年赚2000万" -> 对比基础
        - "不上市只值1600万，上市能值4个亿" -> 核心对比，巨大反差
        - "上市就像修仙成功" -> 比喻，升级感
        - "割韭菜的资格" -> 扎心真相
        
        动态标题：「同样赚2000万」
        使用数字对比突出差距
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、利润、左侧不上市、右侧上市、VS+差距、结论）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题 (y=4.0) - 引发好奇
        title = Text(
            "同样赚2000万", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 核心利润数字
        profit_text = Text(
            "年利润：2000万", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GOLD
        ).move_to(UP * 2.5)
        
        # 3. 左侧：不上市 - 只值1600万
        # 图标来源：organization 代表普通公司
        left_icon = self.load_png_icon("organization", height=1.5).move_to(UP * 0.5 + LEFT * 2.2)
        left_label = Text("不上市", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(left_icon, DOWN, buff=0.2)
        left_value = Text("值1600万", font=self.title_font, font_size=self.font_body_size, color=GRAY).next_to(left_label, DOWN, buff=0.2)
        left_group = Group(left_icon, left_label, left_value)
        
        # 4. 右侧：上市 - 值4个亿
        # 图标来源：stocks_growth 代表上市公司
        right_icon = self.load_png_icon("stocks_growth", height=1.8).move_to(UP * 0.5 + RIGHT * 2.2)
        right_label = Text("上市", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(right_icon, DOWN, buff=0.2)
        right_value = Text("值4个亿！", font=self.title_font, font_size=self.font_body_size, color=GOLD).next_to(right_label, DOWN, buff=0.2)
        right_group = Group(right_icon, right_label, right_value)
        
        # 5. 中间 VS 和差距倍数
        vs_text = Text("VS", font=self.title_font, font_size=self.font_body_size, color=RED).move_to(UP * 0.5)
        gap_text = Text(
            "差25倍！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(DOWN * 1.5)
        
        # 6. 底部结论 - 修仙比喻
        conclusion = Text(
            "上市 = 修仙飞升", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(profit_text), run_time=step_time)
        self.play(
            FadeIn(left_group, shift=RIGHT), 
            FadeIn(right_group, shift=LEFT),
            FadeIn(vs_text, scale=0.5),
            run_time=step_time
        )
        self.play(Write(gap_text), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=2*step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：核心概念 -> 两个关键点 -> 清晰对比
        
        口播稿关键词/短语：
        - "上市解决了两个问题" -> 核心概念
        - "让全天下人都知道你" -> 问题1：知名度
        - "让全天下人都能买你的股份" -> 问题2：流动性
        - "普通公司一个个谈，上市公司往交易所一挂" -> 对比
        - "公众公司的威力" -> 结论
        
        动态标题：「上市的两大好处」
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、两个好处LaggedStart、对比、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部：核心概念标题
        title = Text(
            "上市的两大好处", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 两个关键好处
        # 好处1：全天下人都知道你
        benefit1_icon = self.load_png_icon("organization", height=1.2).move_to(UP * 2.0 + LEFT * 2.5)
        benefit1_text = Text("全天下人都知道你", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(benefit1_icon, RIGHT, buff=0.3)
        benefit1 = Group(benefit1_icon, benefit1_text)
        
        # 好处2：全天下人都能买股份
        benefit2_icon = self.load_png_icon("money_bag", height=1.2).move_to(UP * 0.5 + LEFT * 2.5)
        benefit2_text = Text("全天下人都能买股份", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(benefit2_icon, RIGHT, buff=0.3)
        benefit2 = Group(benefit2_icon, benefit2_text)
        
        benefits = [benefit1, benefit2]
        
        # 3. 对比：普通公司 vs 上市公司
        compare_normal = Text("普通公司：一个个谈", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(DOWN * 1.2)
        compare_listed = Text("上市公司：交易所一挂，随便买", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 2.0)
        
        # 4. 底部结论
        conclusion = Text(
            "这就是公众公司的威力", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        # 使用 LaggedStart 逐项弹出好处
        self.play(
            LaggedStart(
                *[FadeIn(b, shift=RIGHT) for b in benefits], 
                lag_ratio=0.4
            ), 
            run_time=step_time
        )
        self.play(Write(compare_normal), run_time=step_time)
        self.play(Write(compare_listed), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：核心洞察 -> 数据对比 -> 魔力揭示
        
        口播稿关键词/短语：
        - "问题的关键在于市盈率" -> 核心概念
        - "普通公司，银行只愿意按利润打8折贷款" -> 普通公司估值
        - "上市公司，最低20倍市盈率起" -> 上市公司估值
        - "2000万乘以20倍等于4个亿" -> 计算公式
        - "相信你未来5年10年的增长" -> 预期价值
        - "资本市场的魔力" -> 结论
        
        动态标题：「市盈率的秘密」
        使用计算公式展示估值差异
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：6个动作（标题、核心概念、普通公司、上市公司计算、对比结果、结论）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text(
            "市盈率的秘密", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心概念
        core_concept = Text(
            "关键在于：市盈率", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=BLUE
        ).move_to(UP * 2.5)
        
        # 3. 普通公司估值
        normal_label = Text("普通公司", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(UP * 1.2 + LEFT * 2.0)
        normal_calc = Text("利润 × 0.8 = 1600万", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(normal_label, RIGHT, buff=0.3)
        normal_row = VGroup(normal_label, normal_calc)
        
        # 4. 上市公司估值 - 核心公式
        listed_label = Text("上市公司", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(DOWN * 0.2 + LEFT * 2.0)
        listed_calc = Text("利润 × 20倍 = 4亿！", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(listed_label, RIGHT, buff=0.3)
        listed_row = VGroup(listed_label, listed_calc)
        
        # 5. 对比结果框
        result_text = Text(
            "20倍市盈率 = 相信未来增长", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).move_to(DOWN * 1.8)
        result_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=GREEN, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=GREEN
        ).surround(result_text, buff=0.4)
        result_group = VGroup(result_box, result_text)
        
        # 6. 底部结论
        conclusion = Text(
            "这就是资本市场的魔力", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(Write(core_concept), run_time=step_time)
        self.play(FadeIn(normal_row, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(listed_row, shift=RIGHT), run_time=step_time)
        self.play(FadeIn(result_group, scale=0.8), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：具象化场景 -> 对号入座 -> 引发认同
        
        口播稿关键词/短语：
        - "投资股票，就得理解这个逻辑" -> 适用人群
        - "股价不只看今天赚多少，更看未来能赚多少" -> 核心逻辑
        - "亏损公司股价也很高" -> 反常识现象
        - "赌它的未来" -> 解释
        - "赌错了就是韭菜" -> 警示
        
        动态标题：「股价看的是未来」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、核心逻辑、亏损公司现象、原因解释、警示结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "股价看的是未来", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 核心逻辑
        logic_line1 = Text("股价 ≠ 今天赚多少", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(UP * 2.2)
        logic_line2 = Text("股价 = 未来能赚多少", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(UP * 1.4)
        
        # 3. 反常识现象
        # 图标来源：chart 代表股价
        chart_icon = self.load_png_icon("chart", height=1.5).move_to(DOWN * 0.2 + LEFT * 2.0)
        phenomenon_text = Text("亏损公司\n股价也很高？", font=self.body_font, font_size=self.font_body_size, color=ORANGE).next_to(chart_icon, RIGHT, buff=0.5)
        phenomenon_group = Group(chart_icon, phenomenon_text)
        
        # 4. 原因解释
        reason_text = Text(
            "因为大家赌它的未来", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=GREEN
        ).move_to(DOWN * 2.0)
        
        # 5. 底部警示
        warning = Text(
            "赌错了 = 韭菜", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(logic_line1), Write(logic_line2), run_time=step_time)
        self.play(FadeIn(phenomenon_group, shift=UP), run_time=step_time)
        self.play(Write(reason_text), run_time=step_time)
        self.play(Write(warning), Circumscribe(warning, color=RED), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：行动步骤 -> 逐项弹出 -> 强调可执行
        
        口播稿关键词/短语：
        - "看市盈率看成长性" -> 口诀
        - "市盈率太高，要么真有成长，要么是泡沫" -> 判断标准
        - "优先选业绩稳定、市盈率合理的股票" -> 策略1
        - "新手从指数基金开始，别一上来就挑个股" -> 策略2
        
        动态标题：「选股口诀」
        使用 LaggedStart 实现逐项弹出效果
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、口诀、判断标准、策略列表、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "选股口诀", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心口诀 - 金句框
        slogan = Text(
            "看市盈率，看成长性", 
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
        
        # 3. 判断标准
        judgment = Text(
            "市盈率高 = 真成长 or 泡沫？", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(UP * 1.0)
        
        # 4. 策略列表
        item1 = Text("① 优先选业绩稳定、市盈率合理的股票", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 0.4)
        item2 = Text("② 新手从指数基金开始", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 1.4)
        item3 = Text("③ 别一上来就挑个股", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 2.4)
        
        items = [item1, item2, item3]
        
        # 5. 底部结论
        conclusion = Text(
            "稳健投资，远离韭菜命", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(slogan_group, scale=0.8), Circumscribe(slogan, color=GOLD), run_time=step_time)
        self.play(Write(judgment), run_time=step_time)
        # 使用 LaggedStart 逐项弹出，lag_ratio=0.3
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT) for item in items], 
                lag_ratio=0.3
            ), 
            run_time=step_time
        )
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_6(self, scene):
        """
        场景6: 行动号召 (Action) - 视觉逻辑：低门槛互动 -> 强调动画 -> 引导关注
        
        口播稿关键词/短语：
        - "现在你知道股票的本质了吧" -> 总结
        - "下期咱们聊聊怎么防止被割韭菜" -> 预告
        - "点赞收藏" -> 互动号召
        - "每天一课，日日生金" -> 系列口号
        
        动态标题：「搞懂股票本质」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、预告、互动图标、系列口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 核心CTA标题
        title = Text(
            "搞懂股票的本质", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 3.5)
        
        # 2. 下期预告
        preview_text = Text(
            "下期：如何防止被割韭菜", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=ORANGE
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
        self.play(Write(preview_text), Circumscribe(preview_text, color=ORANGE), run_time=step_time)
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
        - stocks_growth: 股票上市核心概念
        - money_bag: 财富/估值
        - chart: 股价/市盈率
        - organization: 公司/企业
        - growing_money: 增长/收益
        """
        return ["stocks_growth", "money_bag", "chart", "organization", "growing_money"]
