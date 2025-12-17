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

def combine_audio_clips(clip_paths, output_wav_path, silence_duration=1.5):
    """
    使用 ffmpeg 将多个音频片段拼接成一个 wav 文件，中间插入静音。
    用于 Manim 的全局音频轨道。
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
    silence_filters = []
    # 只需要 n-1 个静音段
    for i in range(n_clips - 1):
        silence_filters.append(f"anullsrc=r=24000:cl=mono:d={silence_duration}[s{i}]")

    in_filters = []
    for i in range(n_clips):
        in_filters.append(f"[{i}:a]aformat=sample_fmts=fltp:sample_rates=24000:channel_layouts=mono[a{i}]")

    # 拼接序列：a0 s0 a1 s1 ... an
    concat_list = []
    for i in range(n_clips):
        concat_list.append(f"[a{i}]")
        if i < n_clips - 1:
            concat_list.append(f"[s{i}]")
    
    concat_str = "".join(concat_list)
    # 计算 concat 的输入流数量：clips + (clips-1)
    total_segments = n_clips + (n_clips - 1)
    
    filter_complex = ";".join(in_filters + silence_filters + [
        f"{concat_str}concat=n={total_segments}:v=0:a=1,aresample=48000,aformat=sample_fmts=s16:channel_layouts=stereo[aout]"
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

def wait_until_audio_end(scene: Scene, duration: float, elapsed: float, buffer: float = 0.2):
    """
    根据音频时长和已消耗的动画时长，自动计算并执行 wait。
    """
    remaining = duration - elapsed + buffer
    if remaining > 0:
        scene.wait(remaining)
    else:
        # 哪怕超时了，也至少停一小下缓冲
        scene.wait(0.2)

