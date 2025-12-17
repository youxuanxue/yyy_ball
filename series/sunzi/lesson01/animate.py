from manim import *
from mutagen.mp3 import MP3
import os

# 配置竖屏 9:16
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

# 音频目录
VOICE_DIR = "media/voice"

def get_audio_duration(filename):
    """获取音频文件时长（秒）"""
    path = os.path.join(VOICE_DIR, filename)
    if os.path.exists(path):
        try:
            audio = MP3(path)
            return audio.info.length
        except Exception as e:
            print(f"Error reading audio {filename}: {e}")
            return 5.0
    return 5.0

class SunziLessonVertical(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # 配置字体
        # ---------------------------------------------------------
        title_font = "PingFang SC" 
        body_font = "PingFang SC"
        
        # 竖屏常用尺寸调整
        FONT_TITLE = 48
        FONT_BODY = 32
        FONT_SMALL = 24

        # ---------------------------------------------------------
        # 第一页：封面
        # ---------------------------------------------------------
        # 移除 next_section，避免音频截断问题
        audio_file = "01_cover.mp3"
        duration = get_audio_duration(audio_file)
        self.add_sound(os.path.join(VOICE_DIR, audio_file))
        
        # 标题 (垂直居中偏上)
        title = Text("我是小小谋略家", font=title_font, font_size=FONT_TITLE+10, weight=BOLD).shift(UP*2)
        subtitle = Text("孙子兵法第一课\n做决定前的智慧", font=title_font, font_size=FONT_BODY, color=BLUE, line_spacing=1.5)
        subtitle.next_to(title, DOWN, buff=1)
        
        target_audience = Text("观众：6-10岁的小学生", font=body_font, font_size=FONT_SMALL, color=GRAY)
        target_audience.next_to(subtitle, DOWN, buff=3) 

        # 动画总时长分配 (总时长 = duration + 1s buffer)
        total_anim_time = duration + 0.5
        # 分配给3个主要动作
        anim_time = total_anim_time / 4 

        self.play(Write(title), run_time=anim_time)
        self.play(FadeIn(subtitle, shift=UP), run_time=anim_time)
        self.play(Write(target_audience), run_time=anim_time)
        self.wait(anim_time)
        
        # 转场：淡出所有 (使用 FadeOut 代替 clear)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)

        # ---------------------------------------------------------
        # 第二页：什么是“国之大事”？
        # ---------------------------------------------------------
        audio_file = "02_big_event.mp3"
        duration = get_audio_duration(audio_file)
        self.add_sound(os.path.join(VOICE_DIR, audio_file))

        # 布局
        p2_group = VGroup()
        p2_title = Text("什么是“国之大事”？", font=title_font, font_size=FONT_TITLE, color=ORANGE)
        p2_group.add(p2_title)

        quote_text = '“兵者，国之大事\n不可不察也。”'
        quote = Text(quote_text, font=body_font, font_size=FONT_BODY, slant=ITALIC, line_spacing=1.5)
        quote_author = Text("—— 孙武爷爷说", font=body_font, font_size=FONT_SMALL, color=GRAY).next_to(quote, DR)
        quote_group = VGroup(quote, quote_author).next_to(p2_title, DOWN, buff=1)
        p2_group.add(quote_group)
        
        trans_box = Rectangle(width=8, height=3, color=BLUE, fill_opacity=0.1)
        trans_text = Text("打仗是国家最大的事\n绝对不能脑子一热就冲动！", font=body_font, font_size=FONT_SMALL+4, t2c={"绝对不能": RED, "冲动": RED}, line_spacing=1.5)
        trans_group = VGroup(trans_box, trans_text).next_to(quote_group, DOWN, buff=0.8)
        p2_group.add(trans_group)
        
        examples_title = Text("小朋友的“大事”有哪些？", font=body_font, font_size=FONT_BODY).next_to(trans_group, DOWN, buff=1)
        p2_group.add(examples_title)

        ex1 = Text("1. 👿 冲突：同学抢玩具，要不要打？", font=body_font, font_size=FONT_SMALL)
        ex2 = Text("2. 🏆 挑战：要不要参加演讲比赛？", font=body_font, font_size=FONT_SMALL)
        ex3 = Text("3. 💰 诱惑：花光零花钱买昂贵玩具？", font=body_font, font_size=FONT_SMALL)
        ex_group = VGroup(ex1, ex2, ex3).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(examples_title, DOWN, buff=0.5)
        p2_group.add(ex_group)
        p2_group.move_to(ORIGIN)

        # 动画分配
        total_anim_time = duration + 0.5
        anim_time = total_anim_time / 8 

        self.play(Write(p2_title), run_time=anim_time)
        self.play(Write(quote_group), run_time=anim_time)
        self.play(Create(trans_box), Write(trans_text), run_time=anim_time)
        self.play(FadeIn(examples_title), run_time=anim_time)
        self.play(Write(ex1), run_time=anim_time)
        self.play(Write(ex2), run_time=anim_time)
        self.play(Write(ex3), run_time=anim_time)
        self.wait(anim_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)

        # ---------------------------------------------------------
        # 第三页：魔法第一步
        # ---------------------------------------------------------
        audio_file = "03_magic_step1.mp3"
        duration = get_audio_duration(audio_file)
        self.add_sound(os.path.join(VOICE_DIR, audio_file))
        
        p3_group = VGroup()
        p3_title = Text("魔法第一步：必须与把握", font=title_font, font_size=FONT_TITLE, color=PURPLE)
        p3_group.add(p3_title)

        q1_box = RoundedRectangle(corner_radius=0.5, height=3.5, width=8, color=BLUE)
        q1_title = Text("1️⃣ 一定要“打”吗？", font=body_font, font_size=FONT_BODY).next_to(q1_box.get_top(), DOWN, buff=0.2)
        q1_desc = Text("思考：除了打架，有没有别的办法？\n(讲道理、找老师、用智慧)", font=body_font, font_size=FONT_SMALL, line_spacing=1.5).next_to(q1_title, DOWN, buff=0.3)
        q1_wisdom = Text("✨ 兵法智慧：不战而屈人之兵", font=body_font, font_size=FONT_SMALL, color=YELLOW).next_to(q1_desc, DOWN, buff=0.3)
        group1 = VGroup(q1_box, q1_title, q1_desc, q1_wisdom).next_to(p3_title, DOWN, buff=1)
        p3_group.add(group1)

        q2_box = RoundedRectangle(corner_radius=0.5, height=3.5, width=8, color=TEAL)
        q2_title = Text("2️⃣ 我能赢吗？", font=body_font, font_size=FONT_BODY).next_to(q2_box.get_top(), DOWN, buff=0.2)
        q2_desc = Text("思考：我有必胜的把握吗？\n力气够大吗？准备好了吗？", font=body_font, font_size=FONT_SMALL, line_spacing=1.5).next_to(q2_title, DOWN, buff=0.3)
        q2_wisdom = Text("✨ 兵法智慧：知己知彼", font=body_font, font_size=FONT_SMALL, color=YELLOW).next_to(q2_desc, DOWN, buff=0.3)
        group2 = VGroup(q2_box, q2_title, q2_desc, q2_wisdom).next_to(group1, DOWN, buff=1)
        p3_group.add(group2)
        p3_group.move_to(ORIGIN)

        # 动画分配
        total_anim_time = duration + 0.5
        anim_time = total_anim_time / 8 

        self.play(FadeIn(p3_title), run_time=anim_time)
        self.play(Create(q1_box), run_time=anim_time)
        self.play(Write(q1_title), FadeIn(q1_desc), run_time=anim_time)
        self.play(Write(q1_wisdom), run_time=anim_time)
        
        self.play(Create(q2_box), run_time=anim_time)
        self.play(Write(q2_title), FadeIn(q2_desc), run_time=anim_time)
        self.play(Write(q2_wisdom), run_time=anim_time)
        self.wait(anim_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)

        # ---------------------------------------------------------
        # 第四页：魔法第二步
        # ---------------------------------------------------------
        audio_file = "04_magic_step2.mp3"
        duration = get_audio_duration(audio_file)
        self.add_sound(os.path.join(VOICE_DIR, audio_file))
        
        p4_group = VGroup()
        p4_title = Text("魔法第二步：代价与后果", font=title_font, font_size=FONT_TITLE, color=RED)
        subtitle_p4 = Text("这是最重要的一步哦！", font=body_font, font_size=FONT_SMALL, color=GRAY).next_to(p4_title, DOWN)
        title_group = VGroup(p4_title, subtitle_p4)
        p4_group.add(title_group)

        q3_box = RoundedRectangle(corner_radius=0.5, height=3.5, width=8, color=ORANGE)
        q3_title = Text("3️⃣ 怎么赢才划算？", font=body_font, font_size=FONT_BODY).next_to(q3_box.get_top(), DOWN, buff=0.2)
        q3_desc = Text("思考：如果赢了却被批评赔钱\n叫“杀敌一千，自损八百”", font=body_font, font_size=FONT_SMALL, line_spacing=1.5).next_to(q3_title, DOWN, buff=0.3)
        q3_wisdom = Text("✨ 兵法智慧：\n以最小的代价，换最大的胜利", font=body_font, font_size=FONT_SMALL, color=YELLOW, line_spacing=1.5).next_to(q3_desc, DOWN, buff=0.3)
        group3 = VGroup(q3_box, q3_title, q3_desc, q3_wisdom).next_to(title_group, DOWN, buff=1)
        p4_group.add(group3)

        q4_box = RoundedRectangle(corner_radius=0.5, height=3.5, width=8, color=RED)
        q4_title = Text("4️⃣ 输了怎么办？", font=body_font, font_size=FONT_BODY).next_to(q4_box.get_top(), DOWN, buff=0.2)
        q4_desc = Text("思考：如果搞砸了，我会哭吗？\n能承受吗？有B计划吗？", font=body_font, font_size=FONT_SMALL, line_spacing=1.5).next_to(q4_title, DOWN, buff=0.3)
        q4_wisdom = Text("✨ 兵法智慧：未虑胜，先虑败", font=body_font, font_size=FONT_SMALL, color=YELLOW).next_to(q4_desc, DOWN, buff=0.3)
        group4 = VGroup(q4_box, q4_title, q4_desc, q4_wisdom).next_to(group3, DOWN, buff=1)
        p4_group.add(group4)
        p4_group.move_to(ORIGIN)

        # 动画分配
        total_anim_time = duration + 0.5
        anim_time = total_anim_time / 8 

        self.play(FadeIn(p4_title), FadeIn(subtitle_p4), run_time=anim_time)
        self.play(Create(q3_box), run_time=anim_time)
        self.play(Write(q3_title), FadeIn(q3_desc), run_time=anim_time)
        self.play(Write(q3_wisdom), run_time=anim_time)
        
        self.play(Create(q4_box), run_time=anim_time)
        self.play(Write(q4_title), FadeIn(q4_desc), run_time=anim_time)
        self.play(Write(q4_wisdom), run_time=anim_time)
        self.wait(anim_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)

        # ---------------------------------------------------------
        # 第五页：行动锦囊
        # ---------------------------------------------------------
        audio_file = "05_action_tips.mp3"
        duration = get_audio_duration(audio_file)
        self.add_sound(os.path.join(VOICE_DIR, audio_file))
        
        p5_group = VGroup()
        p5_title = Text("行动锦囊：先思考，再行动！", font=title_font, font_size=FONT_TITLE)
        p5_group.add(p5_title)

        scene_box = Rectangle(width=8, height=3, color=WHITE)
        scene_text = Text("场景：高年级大哥哥抢了你的篮球\n你想冲上去抢回来...", font=body_font, font_size=FONT_SMALL, line_spacing=1.5)
        scene_group = VGroup(scene_box, scene_text).next_to(p5_title, DOWN, buff=0.8)
        p5_group.add(scene_group)

        brain_title = Text("🧠 启动“四问”大脑：", font=body_font, font_size=FONT_BODY, color=BLUE).next_to(scene_group, DOWN, buff=0.8).to_edge(LEFT, buff=1.5)
        
        steps_group = VGroup()
        steps = [
            "1. 必须打吗？\n➡️ 告诉老师 / 再拿一个球",
            "2. 打得过吗？\n➡️ 他比我高两个头... (打不过❌)",
            "3. 代价大吗？\n➡️ 会受伤，会被骂",
            "4. 输了咋办？\n➡️ 球没拿回，还挨顿揍"
        ]
        
        last_obj = brain_title
        for step in steps:
            t = Text(step, font=body_font, font_size=FONT_SMALL, line_spacing=1.3).next_to(last_obj, DOWN, aligned_edge=LEFT, buff=0.4)
            steps_group.add(t)
            last_obj = t
        
        decision = Text("💡 决定：智取，不力敌！\n找老师帮忙！", font=body_font, font_size=FONT_BODY, color=YELLOW, weight=BOLD, line_spacing=1.5)
        decision.next_to(last_obj, DOWN, buff=1)
        steps_group.add(decision)
        
        total_group = VGroup(p5_title, scene_group, brain_title, steps_group)
        total_group.arrange(DOWN, center=True, buff=0.5)
        brain_title.next_to(scene_group, DOWN, buff=0.8).to_edge(LEFT, buff=1.5)
        
        last_obj = brain_title
        for t in steps_group[:-1]:
             t.next_to(last_obj, DOWN, aligned_edge=LEFT, buff=0.4)
             last_obj = t
        
        decision.next_to(last_obj, DOWN, buff=1).move_to([0, decision.get_y(), 0])
        final_group = VGroup(p5_title, scene_group, brain_title, steps_group)
        final_group.move_to(ORIGIN)

        # 动画分配
        total_anim_time = duration + 0.5
        anim_time = total_anim_time / 8

        self.play(Write(p5_title), run_time=anim_time)
        self.play(FadeIn(scene_group), run_time=anim_time)
        self.play(Write(brain_title), run_time=anim_time)
        
        for t in steps_group[:-1]:
            self.play(Write(t), run_time=anim_time)
            
        self.play(TransformFromCopy(steps_group[-2], decision), run_time=anim_time)
        self.wait(anim_time)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)

        # ---------------------------------------------------------
        # 第六页：祝贺与口号
        # ---------------------------------------------------------
        audio_file = "06_congrats.mp3"
        duration = get_audio_duration(audio_file)
        self.add_sound(os.path.join(VOICE_DIR, audio_file))
        
        p6_group = VGroup()
        congrats = Text("🎉 祝贺你！", font=title_font, font_size=64, color=RED)
        sub_congrats = Text("你学会了孙武爷爷的智慧", font=body_font, font_size=36).next_to(congrats, DOWN, buff=0.5)
        top_group = VGroup(congrats, sub_congrats)
        p6_group.add(top_group)
        
        slogan_box = Rectangle(width=8, height=4, color=YELLOW, fill_color=YELLOW_E, fill_opacity=1)
        slogan = Text("“大事要想清\n冲动是魔鬼！”", font=title_font, font_size=48, color=WHITE, line_spacing=1.5)
        slogan.move_to(slogan_box.get_center())
        slogan_group = VGroup(slogan_box, slogan).next_to(top_group, DOWN, buff=2)
        p6_group.add(slogan_group)
        p6_group.move_to(ORIGIN)
        
        # 动画分配
        total_anim_time = duration + 0.5
        anim_time = total_anim_time / 5

        self.play(Write(congrats), run_time=anim_time)
        self.play(FadeIn(sub_congrats), run_time=anim_time)
        self.wait(anim_time)
        self.play(DrawBorderThenFill(slogan_box), run_time=anim_time)
        self.play(Write(slogan), run_time=anim_time)
        self.wait(anim_time) # 结尾稍微等一下
