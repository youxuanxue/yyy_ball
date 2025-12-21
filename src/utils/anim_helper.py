import os
import subprocess
from pathlib import Path
from mutagen.mp3 import MP3

def get_audio_duration(filepath):
    """获取音频文件时长（秒）"""
    if not os.path.exists(filepath):
        print(f"Error: Audio file not found: {filepath}")
        return 5.0 # Fallback for dev, but ideally should raise
        
    # Prefer ffprobe for accuracy if available
    try:
        cmd = [
            "ffprobe", 
            "-v", "error", 
            "-show_entries", "format=duration", 
            "-of", "default=noprint_wrappers=1:nokey=1", 
            filepath
        ]
        output = subprocess.check_output(cmd, text=True).strip()
        return float(output)
    except Exception as e:
        print(f"Warning: ffprobe failed for {filepath}, falling back to mutagen. Error: {e}")
        try:
            audio = MP3(filepath)
            return audio.info.length
        except:
            return 5.0

def combine_audio_clips(clip_paths, output_wav_path, silence_duration=0, bgm_file=None, bgm_volume=-20, bgm_loop=True):
    """
    使用 ffmpeg 将多个音频片段拼接成一个 wav 文件
    
    Args:
        clip_paths: 音频文件路径列表
        output_wav_path: 输出文件路径
        silence_duration: 片段间静音时长（秒）
        bgm_file: 背景音乐文件路径
        bgm_volume: 背景音乐音量（dB，默认 -20）
        bgm_loop: 是否循环播放背景音乐
    """
    clips = [Path(p).resolve() for p in clip_paths]
    out_wav = Path(output_wav_path).resolve()
    
    missing = [str(p) for p in clips if not p.exists()]
    if missing:
        raise FileNotFoundError(f"缺少音频文件：{missing}")
    
    bgm_path = Path(bgm_file).resolve() if bgm_file else None
    if bgm_path and not bgm_path.exists():
        raise FileNotFoundError(f"缺少背景音乐文件：{bgm_path}")

    # 检查缓存
    newest_mtime = max(p.stat().st_mtime for p in clips)
    if bgm_path:
        newest_mtime = max(newest_mtime, bgm_path.stat().st_mtime)

    if out_wav.exists() and out_wav.stat().st_mtime >= newest_mtime:
        print(f"Using cached combined audio: {out_wav}")
        return str(out_wav)

    print(f"Generating combined audio: {out_wav}")
    out_wav.parent.mkdir(parents=True, exist_ok=True)

    # 构建 ffmpeg 滤镜
    n_clips = len(clips)
    in_filters = [f"[{i}:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=mono[a{i}]" 
                  for i in range(n_clips)]

    # 构建人声拼接
    if silence_duration > 0:
        silence_filters = [f"anullsrc=r=48000:cl=mono:d={silence_duration}[s{i}]" 
                          for i in range(n_clips - 1)]
        concat_list = []
        for i in range(n_clips):
            concat_list.append(f"[a{i}]")
            if i < n_clips - 1:
                concat_list.append(f"[s{i}]")
        concat_str = "".join(concat_list)
        total_segments = n_clips + (n_clips - 1)
        voice_chain = f"{concat_str}concat=n={total_segments}:v=0:a=1[voice_mono];[voice_mono]aformat=channel_layouts=stereo[voice]"
    else:
        concat_str = "".join([f"[a{i}]" for i in range(n_clips)])
        voice_chain = f"{concat_str}concat=n={n_clips}:v=0:a=1[voice_mono];[voice_mono]aformat=channel_layouts=stereo[voice]"

    filter_complex_steps = in_filters + (silence_filters if silence_duration > 0 else [])
    
    if not bgm_path:
        filter_complex_str = ";".join(filter_complex_steps + [voice_chain.replace("[voice]", "[aout]")])
        inputs = sum([["-i", str(p)] for p in clips], [])
    else:
        bgm_idx = n_clips
        filter_complex_steps.append(voice_chain)
        filter_complex_steps.append(f"[{bgm_idx}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={bgm_volume}dB[bgm_vol]")
        filter_complex_steps.append(f"[voice][bgm_vol]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[aout]")
        filter_complex_str = ";".join(filter_complex_steps)
        
        inputs = sum([["-i", str(p)] for p in clips], [])
        if bgm_loop:
            inputs += ["-stream_loop", "-1"]
        inputs += ["-i", str(bgm_path)]

    cmd = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        *inputs,
        "-filter_complex", filter_complex_str,
        "-map", "[aout]",
        str(out_wav),
    ]
    
    subprocess.run(cmd, check=True)
    return str(out_wav)

def load_png_icon(icon_name, project_root=None, height=2):
    """
    从 assets/icons8 目录加载 PNG 图标
    
    支持精确匹配、别名匹配、模糊匹配和文件搜索。
    按优先级查找：精确匹配 > 别名匹配 > 模糊匹配 > 文件搜索 > 回退
    
    Args:
        icon_name: 图标名称（不含扩展名）
        project_root: 项目根目录，如果为 None 则自动推断
        height: 图标高度（Manim 单位，默认 2）
        
    Returns:
        ImageMobject 或回退的图标对象
    """
    from manim import ImageMobject, Text, GRAY
    import json
    from difflib import SequenceMatcher
    
    # 自动推断项目根目录
    if project_root is None:
        current_file = Path(__file__).resolve()
        project_root = current_file.parent.parent.parent
    
    project_root = Path(project_root)
    icons8_dir = project_root / "assets" / "icons8"
    
    icon_sources = [
        ("doodle", "doodle_png_metadata.json"),
        ("plasticine", "plasticine_png_metadata.json"),
        ("stickers", "stickers_png_metadata.json"),
        ("color", "color_png_metadata.json"),
    ]
    
    def similarity(a, b):
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()
    
    def try_load_icon(icon_path, source_name=""):
        if icon_path.exists():
            try:
                icon = ImageMobject(str(icon_path.resolve()))
                icon.height = height
                return icon
            except Exception as e:
                if source_name:
                    print(f"⚠️ 加载 PNG 图标失败 {icon_name} (来自 {source_name}): {e}")
        return None
    
    def get_icon_path(icon_dir, icon_info, filename):
        """根据 icon_info 构建图标路径"""
        subcategory = icon_info.get("subcategory", "")
        return icon_dir / subcategory / f"{filename}.png"
    
    def load_metadata(metadata_path):
        """加载 metadata 文件"""
        if not metadata_path.exists():
            return None
        try:
            with open(metadata_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ 读取 metadata 失败 ({metadata_path.name}): {e}")
            return None
    
    # 方法1: 精确匹配和别名匹配
    for subdir, metadata_file in icon_sources:
        metadata_path = icons8_dir / metadata_file
        icon_dir = icons8_dir / subdir
        metadata = load_metadata(metadata_path)
        if not metadata:
            continue
        
        file_map = metadata.get("file_map", {})
        
        # 精确匹配
        if icon_name in file_map:
            icon_path = get_icon_path(icon_dir, file_map[icon_name], icon_name)
            icon = try_load_icon(icon_path, subdir)
            if icon:
                return icon
        
        # 别名匹配
        for filename, icon_info in file_map.items():
            if icon_name in icon_info.get("aliases", []):
                icon_path = get_icon_path(icon_dir, icon_info, filename)
                icon = try_load_icon(icon_path, f"{subdir} (别名: {filename})")
                if icon:
                    return icon
    
    # 方法2: 模糊匹配
    best_score, best_path, best_source = 0.0, None, None
    for subdir, metadata_file in icon_sources:
        metadata_path = icons8_dir / metadata_file
        icon_dir = icons8_dir / subdir
        metadata = load_metadata(metadata_path)
        if not metadata:
            continue
        
        file_map = metadata.get("file_map", {})
        for filename, icon_info in file_map.items():
            score = max(similarity(icon_name, filename), 
                       max([similarity(icon_name, alias) for alias in icon_info.get("aliases", [])], default=0))
            if score > 0.6 and score > best_score:
                best_score, best_path, best_source = score, get_icon_path(icon_dir, icon_info, filename), subdir
    
    if best_path:
        icon = try_load_icon(best_path, f"{best_source} (模糊匹配, 相似度: {best_score:.2f})")
        if icon:
            return icon
    
    # 方法3: 递归文件搜索
    for subdir, _ in icon_sources:
        icon_dir = icons8_dir / subdir
        if icon_dir.exists():
            for png_file in icon_dir.rglob(f"{icon_name}.png"):
                icon = try_load_icon(png_file, subdir)
                if icon:
                    return icon
    
    # 方法4: 关键词匹配
    icon_name_lower = icon_name.lower()
    for subdir, _ in icon_sources:
        icon_dir = icons8_dir / subdir
        if icon_dir.exists():
            for png_file in icon_dir.rglob("*.png"):
                filename_lower = png_file.stem.lower()
                if icon_name_lower in filename_lower or filename_lower in icon_name_lower:
                    if similarity(icon_name, png_file.stem) > 0.5:
                        icon = try_load_icon(png_file, f"{subdir} (关键词匹配)")
                        if icon:
                            return icon
    
    # 回退：使用 icon_helper
    try:
        from src.utils.icon_helper import create_icon
        icon = create_icon(icon_name, icon_type="auto")
        if hasattr(icon, 'height'):
            icon.height = height
        else:
            icon.scale(height / 2)
        return icon
    except Exception as e:
        print(f"⚠️ 图标回退失败 {icon_name}: {e}")
    
    return Text("?", font_size=int(height * 36), color=GRAY)
