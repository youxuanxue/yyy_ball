import sys
import os
import numpy as np
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration
from src.animate import Zsxq100keLessonVertical


class Lesson004VerticalScenes(Zsxq100keLessonVertical):
    """
    第004课：银行的三六九等
    副标题：读懂银行体系，选对金融伙伴
    布局规范：顶部1/5和底部1/5留白，内容集中在中间 3/5 (y: 4.8 到 -4.8)
    """

    def build_scene_1(self, scene):
        """
        场景1: 痛点/破冰/现状 (钩子引入) - 视觉逻辑：引发共鸣 -> 反常识观点 -> 抓住注意力
        
        口播稿关键词/短语：
        - "银行就是银行，存钱都一样" -> 误区认知
        - "分三六九等" -> 核心反转
        - "村镇银行" vs "工商银行" -> 对比
        - "差着五个级别" -> 冲击力
        
        动态标题：「银行都一样？」
        """
        audio_file = self.audio_clips[0] if len(self.audio_clips) > 0 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、误区文字、对比图标组、反转文字、结论）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部动态标题 (y=4.0) - 引发好奇
        title = Text(
            "银行都一样？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GRAY
        ).move_to(UP * 4.0)
        
        # 2. 误区文字 - 存钱都一样
        wrong_text = Text(
            "「存钱都一样」", 
            font=self.body_font, 
            font_size=self.font_body_size, 
            color=GRAY
        ).move_to(UP * 2.5)
        wrong_cross = Cross(wrong_text, stroke_color=RED, stroke_width=4)
        
        # 3. 左侧：村镇银行（低级别）
        # 图标来源：building 在 all_png_names.txt
        village_icon = self.load_png_icon("building", height=1.5).move_to(UP * 0.5 + LEFT * 2.2)
        village_label = Text("村镇银行", font=self.body_font, font_size=self.font_body_size, color=GRAY).next_to(village_icon, DOWN, buff=0.2)
        village_group = Group(village_icon, village_label)
        
        # 4. 右侧：工商银行（高级别）
        # 图标来源：bank_building 在 all_png_names.txt
        icbc_icon = self.load_png_icon("bank_building", height=1.8).move_to(UP * 0.5 + RIGHT * 2.2)
        icbc_label = Text("工商银行", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(icbc_icon, DOWN, buff=0.2)
        icbc_group = Group(icbc_icon, icbc_label)
        
        # 5. 中间 VS
        vs_text = Text("VS", font=self.title_font, font_size=self.font_body_size, color=RED).move_to(UP * 0.5)
        
        # 6. 差着级别的冲击文字
        gap_text = Text(
            "差着5个级别！", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=RED
        ).move_to(DOWN * 1.5)
        
        # 7. 底部结论
        conclusion = Text(
            "银行也分三六九等", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 3.8)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        self.play(Write(wrong_text), Create(wrong_cross), run_time=step_time)
        self.play(
            FadeIn(village_group, shift=RIGHT), 
            FadeIn(icbc_group, shift=LEFT),
            FadeIn(vs_text, scale=0.5),
            run_time=2*step_time
        )
        self.play(Write(gap_text), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        # 统一淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_2(self, scene):
        """
        场景2: 知识/是什么 (What) - 视觉逻辑：核心概念 -> 层级结构 -> 清晰分类
        
        口播稿关键词/短语：
        - "五个等级" -> 核心数字
        - "四大行，工农中建" -> 第一级
        - "12家股份制银行，招商、浦发、中信" -> 第二级
        - "城商行，北京银行、上海银行" -> 第三级
        - "农商行" -> 第四级
        - "村镇银行" -> 第五级
        - "级别越高，背景越硬" -> 总结
        
        动态标题：「银行五级分类」
        使用金字塔/层级结构展示
        """
        audio_file = self.audio_clips[1] if len(self.audio_clips) > 1 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、五级分类LaggedStart、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部：核心概念标题
        title = Text(
            "银行五级分类", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=BLUE
        ).move_to(UP * 4.0)
        
        # 2. 金字塔层级结构 - 从上到下（高到低）
        # 第一级：四大行
        level1 = Text("① 四大行（工农中建+交通邮储）", font=self.body_font, font_size=self.font_body_size, color=GOLD).move_to(UP * 2.5)
        level1_bg = RoundedRectangle(height=0.8, corner_radius=0.2, stroke_color=GOLD, stroke_width=2, fill_opacity=0.1, fill_color=GOLD).surround(level1, buff=0.3)
        level1_group = VGroup(level1_bg, level1)
        
        # 第二级：股份制银行
        level2 = Text("② 股份制银行（招商、浦发、中信等）", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(UP * 1.2)
        
        # 第三级：城商行
        level3 = Text("③ 城商行（北京银行、上海银行等）", font=self.body_font, font_size=self.font_body_size, color=BLUE).move_to(UP * 0.0)
        
        # 第四级：农商行
        level4 = Text("④ 农商行", font=self.body_font, font_size=self.font_body_size, color=GRAY).move_to(DOWN * 1.2)
        
        # 第五级：村镇银行
        level5 = Text("⑤ 村镇银行", font=self.body_font, font_size=self.font_body_size, color=DARK_GRAY).move_to(DOWN * 2.4)
        
        levels = [level2, level3, level4, level5]
        
        # 3. 底部总结
        summary = Text(
            "级别越高，背景越硬", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        self.play(FadeIn(level1_group, shift=DOWN), run_time=step_time)
        # 使用 LaggedStart 逐项弹出其他四级
        self.play(
            LaggedStart(
                *[FadeIn(level, shift=DOWN) for level in levels], 
                lag_ratio=0.3
            ), 
            run_time=step_time * 2
        )
        self.play(Write(summary), Circumscribe(summary, color=GOLD), run_time=step_time)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_3(self, scene):
        """
        场景3: 剖析/认知矫正/为什么重要 (Why) - 视觉逻辑：核心洞察 -> 权力结构 -> 安全性
        
        口播稿关键词/短语：
        - "级别决定了靠山是谁" -> 核心洞察
        - "四大行是国务院管" -> 权力来源
        - "一把手都是副部级" -> 权力背书
        - "股份制银行至少有省级财政背景" -> 第二级背景
        - "城商行只是市一级出资" -> 第三级背景
        - "万一有事，谁的后台更硬" -> 引导思考
        - "存款更安全" -> 落脚点
        
        动态标题：「靠山决定安全」
        使用权力层级对比
        """
        audio_file = self.audio_clips[2] if len(self.audio_clips) > 2 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、三级对比LaggedStart、安全提示、结论）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text(
            "靠山决定安全", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 权力层级对比
        # 第一级：四大行 - 国务院
        row1_bank = Text("四大行", font=self.title_font, font_size=self.font_body_size, color=GOLD).move_to(UP * 2.2 + LEFT * 2.0)
        row1_arrow = Text("→", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(row1_bank, RIGHT, buff=0.3)
        row1_power = Text("国务院（副部级）", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(row1_arrow, RIGHT, buff=0.3)
        row1 = VGroup(row1_bank, row1_arrow, row1_power)
        
        # 第二级：股份制 - 省级财政
        row2_bank = Text("股份制", font=self.title_font, font_size=self.font_body_size, color=GREEN).move_to(UP * 0.8 + LEFT * 2.0)
        row2_arrow = Text("→", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(row2_bank, RIGHT, buff=0.3)
        row2_power = Text("省级财政", font=self.body_font, font_size=self.font_body_size, color=GREEN).next_to(row2_arrow, RIGHT, buff=0.3)
        row2 = VGroup(row2_bank, row2_arrow, row2_power)
        
        # 第三级：城商行 - 市级财政
        row3_bank = Text("城商行", font=self.title_font, font_size=self.font_body_size, color=BLUE).move_to(DOWN * 0.6 + LEFT * 2.0)
        row3_arrow = Text("→", font=self.body_font, font_size=self.font_body_size, color=WHITE).next_to(row3_bank, RIGHT, buff=0.3)
        row3_power = Text("市级财政", font=self.body_font, font_size=self.font_body_size, color=BLUE).next_to(row3_arrow, RIGHT, buff=0.3)
        row3 = VGroup(row3_bank, row3_arrow, row3_power)
        
        rows = [row1, row2, row3]
        
        # 3. 安全性提示
        safety_text = Text(
            "后台越硬 = 存款越安全", 
            font=self.title_font, 
            font_size=self.font_body_size, 
            color=ORANGE
        ).move_to(DOWN * 2.2)
        safety_box = RoundedRectangle(
            height=1.0,
            corner_radius=0.2, 
            stroke_color=ORANGE, 
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=ORANGE
        ).surround(safety_text, buff=0.4)
        safety_group = VGroup(safety_box, safety_text)
        
        # 4. 底部结论
        conclusion = Text(
            "万一有事，谁更靠谱？", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(DOWN * 4.0)

        # 动画序列
        self.play(Write(title), run_time=step_time)
        # 使用 LaggedStart 逐项弹出
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=RIGHT) for row in rows], 
                lag_ratio=0.4
            ), 
            run_time=2*step_time
        )
        self.play(FadeIn(safety_group, scale=0.8), run_time=step_time)
        self.play(Write(conclusion), run_time=step_time)
        self.play(Circumscribe(conclusion, color=GOLD), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_4(self, scene):
        """
        场景4: 适用场景 (Where/When) - 视觉逻辑：具象化场景 -> 对号入座 -> 引发认同
        
        口播稿关键词/短语：
        - "存大额资金" -> 场景1
        - "买理财产品" -> 场景2
        - "跨地区办业务" -> 场景3
        - "四大行和股份制银行全国都能开户" -> 优势
        - "城商行跨省就麻烦了" -> 劣势
        - "选错银行，给你添堵" -> 后果
        
        动态标题：「这些情况要注意」
        """
        audio_file = self.audio_clips[3] if len(self.audio_clips) > 3 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：5个动作（标题、三个场景LaggedStart、对比、结论）
        step_time = (page_duration - t_trans) / 6

        # 1. 顶部标题
        title = Text(
            "这些情况要注意", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 4.0)
        
        # 2. 三个需要注意的场景
        # 图标来源：coins, credit_card, money 在 all_png_names.txt
        scene1_icon = self.load_png_icon("coins", height=1.2).move_to(UP * 2.2 + LEFT * 3.0)
        scene1_text = Text("大额存款", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(scene1_icon, RIGHT, buff=0.3)
        scene1 = Group(scene1_icon, scene1_text)
        
        scene2_icon = self.load_png_icon("credit_card", height=1.2).move_to(UP * 0.8 + LEFT * 3.0)
        scene2_text = Text("买理财", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(scene2_icon, RIGHT, buff=0.3)
        scene2 = Group(scene2_icon, scene2_text)
        
        scene3_icon = self.load_png_icon("money", height=1.2).move_to(DOWN * 0.6 + LEFT * 3.0)
        scene3_text = Text("跨地区业务", font=self.body_font, font_size=self.font_body_size, color=GOLD).next_to(scene3_icon, RIGHT, buff=0.3)
        scene3 = Group(scene3_icon, scene3_text)
        
        scenes = [scene1, scene2, scene3]
        
        # 3. 对比提示
        # 全国性银行 vs 城商行
        compare_good = Text("✓ 四大行/股份制：全国通用", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 2.0)
        compare_bad = Text("✗ 城商行：跨省麻烦", font=self.body_font, font_size=self.font_body_size, color=RED).move_to(DOWN * 2.8)
        
        # 4. 底部结论
        conclusion = Text(
            "选错银行可能添堵", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=RED
        ).move_to(DOWN * 4.2)

        # 动画序列
        self.play(FadeIn(title, shift=DOWN), run_time=step_time)
        # 使用 LaggedStart 逐项弹出场景
        self.play(
            LaggedStart(
                *[FadeIn(s, shift=RIGHT) for s in scenes], 
                lag_ratio=0.3
            ), 
            run_time=2*step_time
        )
        self.play(Write(compare_good), run_time=step_time)
        self.play(Write(compare_bad), run_time=step_time)
        self.play(Write(conclusion), Circumscribe(conclusion, color=RED), run_time=step_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=t_trans)

    def build_scene_5(self, scene):
        """
        场景5: 策略/应对/怎么做 (How) - 视觉逻辑：行动步骤 -> 逐项弹出 -> 强调可执行
        
        口播稿关键词/短语：
        - "大钱放大行，小钱看利率" -> 口诀
        - "50万以内有存款保险兜底" -> 安全线
        - "在小银行薅羊毛" -> 策略1
        - "超过50万分散到四大行或头部股份制" -> 策略2
        - "跨地区办业务多的人，优先选全国性银行" -> 策略3
        
        动态标题：「存钱策略口诀」
        使用 LaggedStart 实现逐项弹出效果
        """
        audio_file = self.audio_clips[4] if len(self.audio_clips) > 4 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、口诀、三策略、结论）
        step_time = (page_duration - t_trans) / 5

        # 1. 顶部标题
        title = Text(
            "存钱策略口诀", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=GOLD
        ).move_to(UP * 4.0)
        
        # 2. 核心口诀 - 金句框
        slogan = Text(
            "大钱放大行，小钱看利率", 
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
        item1 = Text("① 50万内：小银行薅羊毛（有存款保险）", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(UP * 0.8)
        item2 = Text("② 超50万：分散到四大行/头部股份制", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 0.4)
        item3 = Text("③ 跨地区多：优先选全国性银行", font=self.body_font, font_size=self.font_body_size, color=GREEN).move_to(DOWN * 1.6)
        
        items = [item1, item2, item3]
        
        # 4. 底部结论
        conclusion = Text(
            "分散存放，各取所需", 
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
        - "查查你常用的银行是哪一级" -> 互动任务
        - "评论区告诉我" -> 引导评论
        - "点赞收藏" -> 互动号召
        - "下期继续聊理财干货" -> 预告
        
        动态标题：「动动手指」
        """
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        # 时间管理：4个动作（标题、互动任务、互动图标、系列口号）
        step_time = (page_duration - t_trans) / 4

        # 1. 核心CTA标题
        title = Text(
            "查查你的银行等级", 
            font=self.title_font, 
            font_size=self.font_title_size, 
            color=ORANGE
        ).move_to(UP * 3.5)
        
        # 2. 互动任务
        task_text = Text(
            "评论区告诉我", 
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
        - bank_building: 银行核心概念
        - hierarchy: 层级结构（三六九等）
        - coins: 存钱理财
        - building: 对比小银行
        - credit_card: 金融服务
        """
        return ["bank_building", "hierarchy", "coins", "building", "credit_card"]
