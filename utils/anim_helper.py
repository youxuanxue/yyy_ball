import os
import subprocess
from pathlib import Path
from manim import Scene
from mutagen.mp3 import MP3

def get_audio_duration(filepath):
    """获取音频文件时长（秒），如果文件不存在或出错返回 5.0"""
    if os.path.exists(filepath):
        try:
            audio = MP3(filepath)
            return audio.info.length
        except:
            return 5.0
    return 5.0

def combine_audio_clips(clip_paths, output_wav_path, silence_duration=0):
    """
    使用 ffmpeg 将多个音频片段拼接成一个 wav 文件。
    如果 silence_duration > 0，则在片段之间插入静音。
    """
    clips = [Path(p) for p in clip_paths]
    out_wav = Path(output_wav_path)
    
    # 检查输入文件是否存在
    missing = [str(p) for p in clips if not p.exists()]
    if missing:
        raise FileNotFoundError(f"缺少音频文件：{missing}")

    # 检查是否需要重新生成（只有当输入文件比输出文件新时才生成）
    if out_wav.exists():
        newest_in = max(p.stat().st_mtime for p in clips)
        if out_wav.stat().st_mtime >= newest_in:
            print(f"Using cached combined audio: {out_wav}")
            return str(out_wav)

    print(f"Generating combined audio: {out_wav}")
    
    # 确保输出目录存在
    out_wav.parent.mkdir(parents=True, exist_ok=True)

    # ffmpeg 滤镜构建
    n_clips = len(clips)
    
    in_filters = []
    for i in range(n_clips):
        in_filters.append(f"[{i}:a]aformat=sample_fmts=fltp:sample_rates=24000:channel_layouts=mono[a{i}]")

    if silence_duration > 0:
        silence_filters = []
        for i in range(n_clips - 1):
            silence_filters.append(f"anullsrc=r=24000:cl=mono:d={silence_duration}[s{i}]")
        
        concat_list = []
        for i in range(n_clips):
            concat_list.append(f"[a{i}]")
            if i < n_clips - 1:
                concat_list.append(f"[s{i}]")
        
        concat_str = "".join(concat_list)
        total_segments = n_clips + (n_clips - 1)
        
        filter_complex = ";".join(in_filters + silence_filters + [
            f"{concat_str}concat=n={total_segments}:v=0:a=1,aresample=48000,aformat=sample_fmts=s16:channel_layouts=stereo[aout]"
        ])
    else:
        # 直接拼接
        concat_str = "".join([f"[a{i}]" for i in range(n_clips)])
        filter_complex = ";".join(in_filters + [
            f"{concat_str}concat=n={n_clips}:v=0:a=1,aresample=48000,aformat=sample_fmts=s16:channel_layouts=stereo[aout]"
        ])

    cmd = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        *sum([["-i", str(p)] for p in clips], []),
        "-filter_complex", filter_complex,
        "-map", "[aout]",
        str(out_wav),
    ]
    subprocess.run(cmd, check=True)
    return str(out_wav)

def wait_until_audio_end(scene: Scene, duration: float, elapsed: float, buffer: float = 0.0):
    """
    根据音频时长和已消耗的动画时长，自动计算并执行 wait。
    默认 buffer 设为 0，紧凑节奏。
    """
    remaining = duration - elapsed + buffer
    if remaining > 0:
        scene.wait(remaining)

def play_timeline(scene: Scene, duration: float, steps: list):
    """
    根据权重自动分配时间并执行动画。
    
    Args:
        scene: Manim Scene 实例 (通常传 self)
        duration: 当前页面的可用总时长 (音频时长)
        steps: list of (weight, animations)
               animations: 单个 Animation 对象或 Animation 列表
               
    Returns:
        elapsed_in_page: 该时间段内消耗的总时间
    """
    total_weight = sum(s[0] for s in steps)
    if total_weight == 0: total_weight = 1
    
    # 预留一点点结尾缓冲，避免最后切太快
    available_time = duration - 0.5 
    if available_time < 0: available_time = 0
    
    unit_time = available_time / total_weight
    elapsed_in_page = 0
    
    for weight, anims in steps:
        if not isinstance(anims, (list, tuple)):
            anims = [anims]
        
        step_duration = weight * unit_time
        
        # 动态计算 run_time (动画时间) 和 wait_time (停留时间)
        # 策略：
        # 1. 动画时间占 allocated time 的大部分，但不超过 2.5s (防止过慢)
        # 2. 至少保留 0.2s 动画时间
        
        run_t = min(step_duration * 0.9, 2.5)
        if run_t < 0.2: run_t = 0.2
        
        # 如果分配时间极短（比 0.2 还短），那就只能超时一点点，或者压缩 run_t
        if step_duration < run_t:
            run_t = step_duration 
        
        wait_t = step_duration - run_t
        if wait_t < 0: wait_t = 0
        
        scene.play(*anims, run_time=run_t)
        
        if wait_t > 0.01:
            scene.wait(wait_t)
        
        elapsed_in_page += (run_t + wait_t)
    
    return elapsed_in_page
