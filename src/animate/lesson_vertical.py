import sys
import os
import json
import random
from abc import ABC
from manim import *

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# 导入工具
from src.utils.anim_helper import get_audio_duration, combine_audio_clips, load_png_icon
from src.utils.voice_edgetts import gen_voice_clips_from_json
from src.utils.cover_generator import generate_cover

# 默认配置（可以在 construct 中被 JSON 覆盖）
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

# Define extended colors that might be missing in some Manim versions or are custom
ORANGE_E = "#CC5500" # Burnt Orange
GREEN_E = "#006400"  # Dark Green
PURPLE_E = "#301934" # Dark Purple


class LessonVertical(Scene, ABC):
    """
    通用竖屏课程动画基类（抽象类）
    
    子类通过覆盖类属性来定制不同系列的配置：
    - series_name: 系列名称，用于封面图目录 (如 "sunzibingfa", "zsxq_100ke")
    - font_style: 字体风格 "classical" (楷体) 或 "modern" (黑体)
    - default_decoration_icons: 默认封面装饰图标
    - bgm_file_name: BGM 文件名
    """
    
    # ========== 子类可覆盖的配置 ==========
    series_name = "default"  # 封面图目录名，子类必须覆盖
    font_style = "modern"    # "classical" 或 "modern"
    default_decoration_icons = ["🔍", "💡", "📚"]  # 默认装饰图标
    voice_name = "zh-CN-YunxiNeural"  # Edge TTS 语音，子类可覆盖
    
    def construct(self):
        # 获取子类的文件路径（通过模块获取）
        module = sys.modules.get(self.__class__.__module__)
        if module and hasattr(module, '__file__'):
            self.lesson_dir = os.path.abspath(os.path.dirname(module.__file__))
        else:
            # 如果无法获取，使用当前文件目录（不应该发生）
            self.lesson_dir = os.path.abspath(os.path.dirname(__file__))
        
        self.project_root = os.path.abspath(os.path.join(self.lesson_dir, "../../.."))
        self.script_json_path = os.path.join(self.lesson_dir, "script.json")
        
        if not os.path.exists(self.script_json_path):
             print(f"Error: script.json not found at {self.script_json_path}")
             return

        print(f"Loading script from: {self.script_json_path}")
        with open(self.script_json_path, 'r', encoding='utf-8') as f:
            self.script_data = json.load(f)

        if 'icons' in self.script_data:
            self.default_decoration_icons = self.script_data["icons"]

        self.setup_paths(self.script_json_path)
        self.prepare_resources()
        self.build_scenes()

    def setup_paths(self, script_path):
        """设置相关目录路径"""        
        self.media_dir = os.path.join(self.lesson_dir, "media")
        config.media_dir = self.media_dir # Manim config
        
        # Voice and images directories are now directly under lesson directory
        self.voice_dir = os.path.join(self.lesson_dir, "voice")
        self.images_dir = os.path.join(self.lesson_dir, "images")
        
        self.combined_wav_path = os.path.join(self.voice_dir, "full_audio.wav")
        self.cover_path = os.path.join(self.images_dir, "cover_design.png")
        
        # 源图片目录 (用于封面随机图等) - 使用 series_name 配置
        project_root = os.path.abspath(os.path.join(self.lesson_dir, "../../.."))
        self.source_images_dir = os.path.join(project_root, "series", "cover", self.series_name)

        # 根据 font_style 配置选择字体
        if self.font_style == "classical":
            fonts = ["Kaiti SC", "STKaiti", "KaiTi", "SimKai", "FandolKai"]  # 楷体
        else:  # modern
            fonts = ["PingFang SC", "Heiti SC", "STHeiti", "Helvetica Neue", "Microsoft YaHei"]  # 黑体
        
        self.title_font = fonts[0]
        self.body_font = fonts[0]

        self.font_title_size = 48
        self.font_body_size = 36
        self.font_small_size = 24
        
        self.safe_bottom_buff = 3.5
        self.transition_time = 0.5
    
    def get_cover_decoration_icons(self):
        """
        获取封面装饰图标列表，子类可以覆盖此方法来自定义装饰图标
        
        Returns:
            list: 图标列表，可以是 emoji 字符串或图标文件路径
        """
        return self.default_decoration_icons
    
    def find_icon_file_path(self, icon_name):
        """
        查找图标文件的路径（用于封面生成）
        
        Args:
            icon_name: 图标名称（支持带 .png 扩展名或不带扩展名）
            
        Returns:
            str: 图标文件路径，如果找不到则返回 None
        """
        from pathlib import Path
        import json
        from difflib import SequenceMatcher
        
        # 兼容性处理：如果 icon_name 以 .png 结尾，去掉扩展名
        if icon_name.lower().endswith('.png'):
            icon_name = icon_name[:-4]
        
        icons8_dir = Path(self.project_root) / "assets" / "icons8"
        
        # 定义所有子目录和对应的 metadata 文件
        icon_sources = [
            ("doodle", "doodle_png_metadata.json"),
            ("plasticine", "plasticine_png_metadata.json"),
            ("stickers", "stickers_png_metadata.json"),
            ("color", "color_png_metadata.json"),
        ]
        
        # 辅助函数：计算字符串相似度
        def similarity(a, b):
            return SequenceMatcher(None, a.lower(), b.lower()).ratio()
        
        # 方法1: 从所有 metadata 文件查找（精确匹配 + aliases）
        for subdir, metadata_file in icon_sources:
            metadata_path = icons8_dir / metadata_file
            icon_dir = icons8_dir / subdir
            
            if not metadata_path.exists():
                continue
                
            try:
                with open(metadata_path, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                
                file_map = metadata.get("file_map", {})
                
                # 1.1 精确匹配文件名
                if icon_name in file_map:
                    icon_info = file_map[icon_name]
                    subcategory = icon_info.get("subcategory", "")
                    icon_path = icon_dir / subcategory / f"{icon_name}.png"
                    if icon_path.exists():
                        return str(icon_path.resolve())
                
                # 1.2 通过 aliases 查找
                for filename, icon_info in file_map.items():
                    aliases = icon_info.get("aliases", [])
                    if icon_name in aliases:
                        subcategory = icon_info.get("subcategory", "")
                        icon_path = icon_dir / subcategory / f"{filename}.png"
                        if icon_path.exists():
                            return str(icon_path.resolve())
            except Exception as e:
                print(f"⚠️ 读取 metadata 失败 ({metadata_file}): {e}")
        
        # 方法2: 递归搜索所有子目录
        for subdir, _ in icon_sources:
            icon_dir = icons8_dir / subdir
            if icon_dir.exists():
                for png_file in icon_dir.rglob(f"{icon_name}.png"):
                    return str(png_file.resolve())
        
        return None

    def prepare_resources(self):
        """生成语音和封面"""
        # 新加环境变量FORCE_COVER，如果为True，则强制生成封面；FORCE_VOICE，如果为True，则强制生成语音
        force_cover = os.getenv("FORCE_COVER", "False").lower() == "true"
        force_voice = os.getenv("FORCE_VOICE", "False").lower() == "true"

        # 1. 语音
        if force_voice or not os.path.exists(self.voice_dir) or not os.listdir(self.voice_dir):
            print(f"🎤 Generating voice clips (voice: {self.voice_name})...")
            # 使用保存的 script_json_path 和子类指定的音色
            gen_voice_clips_from_json(self.script_json_path, self.voice_dir, voice=self.voice_name)

        # 2. 封面
        if force_cover or not os.path.exists(self.cover_path):
            print("🎨 Generating cover image...")
            os.makedirs(self.images_dir, exist_ok=True)
            
            main_image = None
            if os.path.exists(self.source_images_dir):
                valid_images = [
                    os.path.join(self.source_images_dir, f) 
                    for f in os.listdir(self.source_images_dir) 
                    if f.lower().endswith(('.jpg', '.jpeg', '.png'))
                ]
                if valid_images:
                    main_image = random.choice(valid_images)
            
            # 如果没有找到图，使用 placeholder 或报错 (这里暂且跳过报错，allow None might fail in generator)
            if not main_image:
                 print("⚠️ No source image found for cover!")
                 # 可以设置一个默认图
            
            if main_image:
                meta = self.script_data.get("meta", {})
                
                # 获取装饰图标（子类可以覆盖 get_cover_decoration_icons 方法）
                decoration_icons = self.get_cover_decoration_icons()
                # 将图标名称转换为文件路径（如果是图标名称）
                decoration_icons_processed = []
                for icon in decoration_icons:
                    if isinstance(icon, str):
                        # 检查是否是文件路径
                        if os.path.exists(icon):
                            decoration_icons_processed.append(icon)
                        else:
                            # 尝试查找图标文件
                            icon_path = self.find_icon_file_path(icon)
                            if icon_path:
                                decoration_icons_processed.append(icon_path)
                            elif len(icon) <= 4:
                                # 短字符串（如 emoji）可以直接使用
                                decoration_icons_processed.append(icon)
                            else:
                                # 找不到图标文件，打印警告并跳过
                                print(f"⚠️ 图标未找到，已跳过: {icon}")
                    else:
                        decoration_icons_processed.append(icon)
                
                generate_cover(
                    output_path=self.cover_path,
                    template_dir=self.source_images_dir,
                    title_main=meta.get("lesson_title", "未命名课程"),
                    title_sub=meta.get("lesson_sub_title", ""),
                    main_image_path=os.path.abspath(main_image),
                    header_text=f'{meta.get("project_name")} · {meta.get("lesson_number")}',
                    toc_items=None,  # 不再显示目录
                    decoration_icons=decoration_icons_processed
                )

        # 3. 合成 BGM
        self.audio_clips = []
        for scene in self.script_data.get("scenes", []):
            idx = scene.get("scene_index")
            if idx is not None:
                # 兼容 utils/voice.py 的输出逻辑：直接使用 idx 作为文件名 (e.g., "1.mp3")
                filename = f"{idx}.mp3"
                self.audio_clips.append(os.path.join(self.voice_dir, filename))
            
        # BGM 文件路径：series/bgm/{series_name}/bgm.wav
        bgm_file = os.path.join(self.project_root, "series", "bgm", self.series_name, "bgm.wav")
        if not os.path.exists(bgm_file):
            print(f"⚠️ BGM not found at {bgm_file}, skipping BGM")
            bgm_file = None
        
        full_audio = combine_audio_clips(
            self.audio_clips, 
            self.combined_wav_path, 
            silence_duration=0,
            bgm_file=bgm_file,
            bgm_volume=-15,
            bgm_loop=True
        )
        self.add_sound(full_audio)
       
    def build_scenes(self):
        """构建所有场景"""
        scenes = self.script_data.get("scenes", [])
       
       # 0. 插入封面首帧
        if os.path.exists(self.cover_path):
            print(f"Adding cover image to scene: {self.cover_path}")
            cover_img = ImageMobject(self.cover_path)
            cover_img.height = config.frame_height
            self.add(cover_img)
            self.wait(0.5) # 增加停留时间，确保可见
            self.remove(cover_img)
        else:
            print(f"Warning: Cover image not found at {self.cover_path}")

        # 主要的 manim 动画生成的代码，请放在这里。
        self.build_all_scenes(scenes)

    def build_all_scenes(self, scenes):
        """构建所有场景（默认实现：根据场景索引调用对应的 build_scene_{scene_index} 方法）"""
        for scene in scenes:
            scene_index = scene.get("scene_index")
            if scene_index is None:
                continue
                
            # 根据场景索引调用对应的构建方法
            method_name = f"build_scene_{scene_index}"
            if hasattr(self, method_name):
                getattr(self, method_name)(scene)
            else:
                # 如果没有对应的构建方法，抛出异常提示需要实现
                raise NotImplementedError(f"build_scene_{scene_index} method not implemented for scene {scene_index}")
    
    def load_png_icon(self, icon_name, height=2):
        """
        加载 PNG 图标（便捷方法）
        
        Args:
            icon_name: 图标名称（不含扩展名）
            height: 图标高度（Manim 单位，默认 2）
            
        Returns:
            ImageMobject 或回退的图标对象
        """
        return load_png_icon(icon_name, project_root=self.project_root, height=height)


# ========== 系列专用子类（仅配置差异） ==========

class SunziLessonVertical(LessonVertical):
    """孙子兵法课程动画基类"""
    series_name = "sunzibingfa"
    font_style = "classical"  # 楷体（古典风格）
    default_decoration_icons = ["🔍", "💡", "📚"]
    voice_name = "zh-CN-YunxiNeural"  # 云希 - 年轻男性，清晰自然
    
    def build_scene_6(self, scene):
        """场景6: 懿爸锦囊（默认实现：处理互动内容）"""
        interactive_content = scene.get("interactive_content")
        if not interactive_content:
            # 如果没有互动内容，直接返回
            return
        
        audio_file = self.audio_clips[5] if len(self.audio_clips) > 5 else None
        page_duration = get_audio_duration(audio_file) if audio_file else 10.0
        t_trans = self.transition_time
        
        step_time = (page_duration - t_trans) / 7

        q_text = Text("挑战小小谋略家", font=self.title_font, font_size=self.font_title_size, color=WHITE)
        q_bg = RoundedRectangle(width=5, height=1.2, corner_radius=0.6, color=BLUE, fill_opacity=0.8)
        q_header = VGroup(q_bg, q_text).move_to(UP * 4.0)
        
        # 设置问题文本，支持自动换行（保持字体大小不变）
        question_text = interactive_content.get("question", "")
        # 手动处理文本换行，保持字体大小不变
        import textwrap
        max_chars_per_line = max(10, int(config.frame_width * 1.8))  # 至少 10 个字符，避免为 0
        wrapped_lines = textwrap.wrap(question_text, width=max_chars_per_line)
        question = Text(
            "\n".join(wrapped_lines),
            font=self.body_font, 
            font_size=self.font_body_size,
            line_spacing=1.2
        ).next_to(q_header, DOWN, buff=0.8)
        
        options = interactive_content.get("options", [])
        opt_group = VGroup()
        colors = [RED, GREEN, GRAY]
        for i, text in enumerate(options):
            color = colors[i] if i < len(colors) else WHITE
            box = RoundedRectangle(width=8, height=1.2, color=color, fill_opacity=0.1)
            txt = Text(text, font_size=self.font_body_size*0.8, color=WHITE).move_to(box)
            item = VGroup(box, txt)
            opt_group.add(item)
            
        opt_group.arrange(DOWN, buff=0.4).next_to(question, DOWN, buff=0.5)
        
        cta_text = Text("评论区告诉懿爸，挑战小小谋略家！", font_size=self.font_body_size, color=BLUE)
        cta = VGroup(Triangle(color=BLUE, fill_opacity=1).scale(0.15).rotate(PI), cta_text).arrange(RIGHT).move_to(DOWN * 4.5)
        
        self.play(FadeIn(q_bg, shift=UP), Write(q_text))
        self.play(Write(question), run_time=step_time)
        self.play(GrowFromCenter(opt_group[0]), run_time=step_time)
        self.play(GrowFromCenter(opt_group[1]), run_time=step_time)
        self.play(GrowFromCenter(opt_group[2]), run_time=step_time)
        self.play(Write(cta), run_time=step_time)
        self.wait(step_time*2)


class Zsxq100keLessonVertical(LessonVertical):
    """日日生金（知识星球精品100课）动画基类"""
    series_name = "zsxq_100ke"
    font_style = "modern"  # 黑体（现代风格）
    default_decoration_icons = ["💰", "📈", "🏦"]
    voice_name = "zh-CN-XiaoxiaoNeural"  # 晓晓 - 年轻女性，活泼甜美
