import os
import subprocess
from pathlib import Path
from manim import Scene
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
    使用 ffmpeg 将多个音频片段拼接成一个 wav 文件。
    如果 silence_duration > 0，则在片段之间插入静音。
    支持添加背景音乐 (bgm_file)，并自动调整音量、循环和淡入淡出。
    
    bgm_volume: 背景音乐音量，单位 dB，默认 -20dB
    bgm_loop: 是否循环播放背景音乐以填满总时长
    """
    # Use absolute paths to avoid cwd issues in Manim
    clips = [Path(p).resolve() for p in clip_paths]
    out_wav = Path(output_wav_path).resolve()
    
    # 检查输入文件是否存在
    missing = [str(p) for p in clips if not p.exists()]
    if missing:
        raise FileNotFoundError(f"缺少音频文件：{missing}")
    
    # 如果指定了背景音乐，也检查是否存在
    bgm_path = Path(bgm_file).resolve() if bgm_file else None
    if bgm_path and not bgm_path.exists():
        raise FileNotFoundError(f"缺少背景音乐文件：{bgm_path}")

    # 检查是否需要重新生成（输入文件比输出文件新时才生成）
    # 如果 bgm 存在，也要把 bgm 的修改时间考虑进去
    newest_mtime = max(p.stat().st_mtime for p in clips)
    if bgm_path:
        newest_mtime = max(newest_mtime, bgm_path.stat().st_mtime)

    if out_wav.exists() and out_wav.stat().st_mtime >= newest_mtime:
        print(f"Using cached combined audio: {out_wav}")
        return str(out_wav)

    print(f"Generating combined audio: {out_wav}")
    
    # 确保输出目录存在
    out_wav.parent.mkdir(parents=True, exist_ok=True)

    # ffmpeg 滤镜构建 - 1. 拼接人声 (Voice Chain)
    n_clips = len(clips)
    
    in_filters = []
    # 使用 fltp + 48000 统一输入
    for i in range(n_clips):
        in_filters.append(f"[{i}:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=mono[a{i}]")

    # 构建人声拼接
    if silence_duration > 0:
        silence_filters = []
        for i in range(n_clips - 1):
            silence_filters.append(f"anullsrc=r=48000:cl=mono:d={silence_duration}[s{i}]")
        
        concat_list = []
        for i in range(n_clips):
            concat_list.append(f"[a{i}]")
            if i < n_clips - 1:
                concat_list.append(f"[s{i}]")
        
        concat_str = "".join(concat_list)
        total_segments = n_clips + (n_clips - 1)
        voice_chain = f"{concat_str}concat=n={total_segments}:v=0:a=1[voice_mono];[voice_mono]aformat=channel_layouts=stereo[voice]"
    else:
        # 直接拼接
        concat_str = "".join([f"[a{i}]" for i in range(n_clips)])
        voice_chain = f"{concat_str}concat=n={n_clips}:v=0:a=1[voice_mono];[voice_mono]aformat=channel_layouts=stereo[voice]"

    filter_complex_steps = in_filters
    if silence_duration > 0:
        filter_complex_steps += silence_filters
    
    # 如果没有 BGM，直接输出 voice
    if not bgm_path:
        filter_complex_str = ";".join(filter_complex_steps + [
            voice_chain.replace("[voice]", "[aout]") # 直接输出到 aout
        ])
        inputs = sum([["-i", str(p)] for p in clips], [])
    else:
        # 有 BGM，进行混合
        # BGM 是第 n_clips 个输入 (index 从 0 开始，所以 index = n_clips)
        bgm_idx = n_clips
        
        # 1. 生成 Voice Track
        filter_complex_steps.append(voice_chain)
        
        # 2. 处理 BGM
        # [voice] 是人声轨，我们可以用 apad 滤镜确保 voice 轨长度确定（或者不用，amix 默认取最长）
        # 这里使用 sidechaincompressor 或者简单的 amix
        # 简单方案：volume -> loop -> amix
        
        # 调整 BGM 音量
        # loop=-1:size=32767 表示无限循环 (ffmpeg loop input option is easier)
        # 但 ffmpeg filter 的 loop 比较复杂，我们用 -stream_loop 在 input 前
        
        # 注意：stream_loop只对输入文件有效，不能在filter里简单loop
        # 所以如果 loop=True，我们在构造 cmd 时添加 -stream_loop -1
        
        # BGM 滤镜链: [bgm_raw] -> aformat -> volume -> [bgm_vol]
        # 显式统一采样率，避免 amix 隐式转换可能的问题
        bgm_filter = f"[{bgm_idx}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={bgm_volume}dB[bgm_vol]"
        # normalize=0 防止 amix 自动降低音量导致人声变小
        mix_filter = f"[voice][bgm_vol]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[aout]"
        
        filter_complex_steps.append(bgm_filter)
        filter_complex_steps.append(mix_filter)
        
        filter_complex_str = ";".join(filter_complex_steps)
        
        inputs = sum([["-i", str(p)] for p in clips], [])
        
        bgm_input_opts = []
        if bgm_loop:
            bgm_input_opts = ["-stream_loop", "-1"]
        
        inputs += bgm_input_opts + ["-i", str(bgm_path)]

    # 构建完整命令
    cmd = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        *inputs,
        "-filter_complex", filter_complex_str,
        "-map", "[aout]",
        str(out_wav),
    ]
    
    # print("DEBUG CMD:", " ".join(cmd)) # 调试用
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

def merge_audio_video_if_needed(video_path: str, audio_path: str):
    """
    检查视频是否有音轨，如果没有则将 audio_path 的音频合并进去。
    """
    video_p = Path(video_path)
    audio_p = Path(audio_path)
    
    if not video_p.exists() or not audio_p.exists():
        return

    # Check for audio stream using ffprobe
    check_cmd = [
        "ffprobe", "-v", "error", "-select_streams", "a", 
        "-show_entries", "stream=index", "-of", "csv=p=0", 
        str(video_p)
    ]
    
    try:
        output = subprocess.check_output(check_cmd, text=True)
        if output.strip():
            # Already has audio
            return
    except subprocess.CalledProcessError:
        pass # treat as no audio or error

    # Merge audio
    temp_output = video_p.with_name(f"{video_p.stem}_merged{video_p.suffix}")
    print(f"Merging audio into video: {video_p} + {audio_p} -> {temp_output}")
    
    cmd = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-i", str(video_p),
        "-i", str(audio_p),
        "-c:v", "copy",
        "-c:a", "aac",
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-shortest",
        str(temp_output)
    ]
    
    subprocess.run(cmd, check=True)
    
    if temp_output.exists():
        # Replace original
        os.replace(temp_output, video_p)
        print(f"Replaced original video with merged version: {video_p}")
