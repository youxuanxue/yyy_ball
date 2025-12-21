#!/usr/bin/env python3
"""
生成 lesson10 的语音和说话头像视频
1. 从 script.json 提取 voiceover_script，使用 frank.mp3 生成 1-7.mp3
2. 使用 shane.jpg 和生成的音频生成 talking head 视频
"""
import argparse
import sys
import os
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.utils.voice import (
    gen_voice_clips_from_json_with_clone, 
    parse_json_script,
    check_cosyvoice_installation,
    optimize_reference_audio,
    get_optimal_prompt_text,
    print_voice_cloning_optimization_guide
)
from src.utils.talking_head import batch_generate_talking_heads, print_installation_status


def convert_wav_to_mp3(wav_path: str, mp3_path: str) -> bool:
    """
    将 WAV 文件转换为 MP3
    
    Args:
        wav_path: WAV 文件路径
        mp3_path: 输出 MP3 文件路径
    
    Returns:
        bool: 是否成功转换
    """
    try:
        from pydub import AudioSegment
        
        if not os.path.exists(wav_path):
            print(f"❌ 错误: WAV 文件不存在: {wav_path}")
            return False
        
        print(f"🔄 转换音频格式: {os.path.basename(wav_path)} -> {os.path.basename(mp3_path)}")
        audio = AudioSegment.from_wav(wav_path)
        audio.export(mp3_path, format="mp3")
        print(f"✅ 已转换: {os.path.basename(mp3_path)}")
        return True
        
    except ImportError:
        print("❌ 错误: pydub 未安装，无法转换音频格式")
        print("💡 请安装: uv add pydub")
        return False
    except Exception as e:
        print(f"❌ 错误: 转换失败 - {str(e)}")
        return False


def generate_voice_files(
    script_path: str, 
    reference_audio: str, 
    output_dir: str, 
    prompt_text: str = "",
    optimize_reference: bool = True,
    auto_extract_text: bool = True
) -> bool:
    """
    生成语音文件（1-7.mp3）
    
    Args:
        script_path: JSON 脚本文件路径
        reference_audio: 参考音频文件路径
        output_dir: 输出目录
        prompt_text: 参考音频对应的文字（可选，建议提供以提高质量）
    
    Returns:
        bool: 是否成功生成
    """
    print("\n" + "=" * 80)
    print("🎙️ 步骤 1: 生成语音文件")
    print("=" * 80)
    
    # 检查参考音频
    if not os.path.exists(reference_audio):
        print(f"❌ 错误: 参考音频文件不存在: {reference_audio}")
        return False
    
    # 检查 CosyVoice 安装
    if not check_cosyvoice_installation():
        print("❌ 错误: CosyVoice 未安装")
        print("💡 请从 GitHub 安装: git clone https://github.com/FunAudioLLM/CosyVoice.git external/CosyVoice")
        return False
    
    # 优化参考音频（如果需要）
    optimized_audio = reference_audio
    if optimize_reference:
        # 创建临时优化后的音频文件
        temp_audio = os.path.join(output_dir, "optimized_reference.wav")
        os.makedirs(output_dir, exist_ok=True)
        optimized_audio = optimize_reference_audio(
            audio_path=reference_audio,
            target_duration=10.0,
            output_path=temp_audio
        )
    
    # 获取最佳的 prompt_text
    optimal_prompt_text = get_optimal_prompt_text(
        reference_audio_path=optimized_audio,
        manual_text=prompt_text if prompt_text else None,
        auto_extract=auto_extract_text
    )
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 解析脚本
    scripts = parse_json_script(script_path)
    if not scripts:
        print("⚠️ 未找到任何口播内容，请检查 JSON 格式")
        return False
    
    print(f"📄 找到 {len(scripts)} 个场景的语音内容")
    
    # 生成语音（会生成 WAV 文件）
    gen_voice_clips_from_json_with_clone(
        script_path=script_path,
        output_dir=output_dir,
        reference_audio_path=optimized_audio,
        language="zh",
        prompt_text=optimal_prompt_text
    )
    
    # 转换 WAV 到 MP3
    print("\n🔄 转换音频格式为 MP3...")
    wav_files = sorted([f for f in os.listdir(output_dir) if f.endswith('.wav')], 
                       key=lambda x: int(os.path.splitext(x)[0]) if os.path.splitext(x)[0].isdigit() else 999)
    
    if not wav_files:
        print("⚠️ 警告: 未找到生成的 WAV 文件")
        return False
    
    success_count = 0
    for wav_file in wav_files:
        wav_path = os.path.join(output_dir, wav_file)
        # 提取数字作为文件名（例如 "1.wav" -> "1.mp3"）
        basename = os.path.splitext(wav_file)[0]
        mp3_path = os.path.join(output_dir, f"{basename}.mp3")
        
        # 如果 MP3 已存在，跳过
        if os.path.exists(mp3_path):
            print(f"⏭️  跳过（已存在）: {os.path.basename(mp3_path)}")
            success_count += 1
            # 删除 WAV 文件（可选）
            try:
                os.remove(wav_path)
            except:
                pass
            continue
        
        if convert_wav_to_mp3(wav_path, mp3_path):
            success_count += 1
            # 删除 WAV 文件（可选）
            try:
                os.remove(wav_path)
            except:
                pass
    
    print(f"\n✅ 成功生成 {success_count} 个 MP3 文件")
    return success_count > 0


def generate_talking_head_videos(
    image_path: str, 
    audio_dir: str, 
    output_dir: str, 
    face_enhance: bool = True,
    size: int = 512,
    preprocess: str = "full",
    still: bool = False
) -> bool:
    """
    生成说话头像视频
    
    Args:
        image_path: 人物头像图片路径
        audio_dir: 音频文件目录
        output_dir: 输出目录
        face_enhance: 是否启用面部增强
        size: 输出视频尺寸（256 更快，512 质量更好）
        preprocess: 预处理模式（'crop' 更快，'full' 质量更好）
    
    Returns:
        bool: 是否成功生成
    """
    print("\n" + "=" * 80)
    print("🎬 步骤 2: 生成说话头像视频")
    print("=" * 80)
    
    # 检查图片
    if not os.path.exists(image_path):
        print(f"❌ 错误: 图片文件不存在: {image_path}")
        return False
    
    # 检查音频目录
    if not os.path.exists(audio_dir):
        print(f"❌ 错误: 音频目录不存在: {audio_dir}")
        return False
    
    # 检查 SadTalker 安装
    from src.utils.talking_head import check_sadtalker_installation
    checks = check_sadtalker_installation()
    
    if not checks['pytorch_available']:
        print("❌ 错误: PyTorch 未安装")
        return False
    
    if not checks['sadtalker_dir_exists']:
        print("❌ 错误: SadTalker 未安装")
        print("💡 请先安装: git clone https://github.com/OpenTalker/SadTalker.git external/SadTalker")
        return False
    
    # 批量生成
    successful = batch_generate_talking_heads(
        image_path=image_path,
        audio_dir=audio_dir,
        output_dir=output_dir,
        audio_pattern="*.mp3",
        face_enhance=face_enhance,
        size=size,
        preprocess=preprocess,
        still=still
    )
    
    if successful:
        print(f"\n✅ 成功生成 {len(successful)} 个视频文件")
        return True
    else:
        print("\n❌ 未成功生成任何视频")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="生成 lesson10 的语音和说话头像视频",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 完整流程（生成语音 + 说话头像）
  uv run python scripts/generate_lesson10_voice_and_talking_head.py

  # 只生成语音（自动优化和提取文字）
  uv run python scripts/generate_lesson10_voice_and_talking_head.py --voice-only

  # 提供参考音频对应的文字（提高音色相似度）
  uv run python scripts/generate_lesson10_voice_and_talking_head.py \\
      --voice-only \\
      --prompt-text "这是参考音频对应的文字内容"

  # 只生成说话头像（假设语音已生成）
  uv run python scripts/generate_lesson10_voice_and_talking_head.py --talking-head-only

  # CPU 快速模式（无 GPU 优化：禁用面部增强，256分辨率，crop模式）
  uv run python scripts/generate_lesson10_voice_and_talking_head.py \\
      --talking-head-only --fast-mode

  # 自定义优化参数
  uv run python scripts/generate_lesson10_voice_and_talking_head.py \\
      --talking-head-only \\
      --no-face-enhance \\
      --size 256 \\
      --preprocess crop

  # 检查安装状态
  uv run python scripts/generate_lesson10_voice_and_talking_head.py --check

  # 显示优化指南
  uv run python scripts/generate_lesson10_voice_and_talking_head.py --optimization-guide
        """
    )
    
    parser.add_argument(
        "--voice-only",
        action="store_true",
        help="只生成语音文件"
    )
    
    parser.add_argument(
        "--talking-head-only",
        action="store_true",
        help="只生成说话头像视频（假设语音已生成）"
    )
    
    parser.add_argument(
        "--check",
        action="store_true",
        help="检查安装状态"
    )
    
    parser.add_argument(
        "--no-face-enhance",
        action="store_true",
        help="禁用面部增强"
    )
    
    parser.add_argument(
        "--prompt-text",
        type=str,
        default="",
        help="参考音频对应的文字（提高音色相似度，建议提供）"
    )
    
    parser.add_argument(
        "--no-optimize-reference",
        action="store_true",
        help="不优化参考音频（默认会优化）"
    )
    
    parser.add_argument(
        "--no-auto-extract",
        action="store_true",
        help="不自动提取参考音频文字（默认会使用 Whisper 提取）"
    )
    
    parser.add_argument(
        "--optimization-guide",
        action="store_true",
        help="显示语音克隆优化指南"
    )
    
    parser.add_argument(
        "--fast-mode",
        action="store_true",
        help="快速模式（CPU 优化：禁用面部增强，降低分辨率，使用 crop 模式）"
    )
    
    parser.add_argument(
        "--size",
        type=int,
        default=512,
        help="输出视频尺寸（256 更快，512 质量更好，默认 512）"
    )
    
    parser.add_argument(
        "--preprocess",
        type=str,
        default="full",
        choices=["crop", "extcrop", "resize", "full", "extfull"],
        help="预处理模式（'crop' 更快，'full' 质量更好，默认 'full'）"
    )
    
    args = parser.parse_args()
    
    # 路径配置
    script_path = "series/sunzi/lesson10/script.json"
    reference_audio = "assets/voice/frank.mp3"
    voice_output_dir = "series/sunzi/lesson10/voice"
    image_path = "series/sunzi/images/shane.jpg"
    talking_head_output_dir = "series/sunzi/lesson10/talking_head"
    
    # 显示优化指南
    if args.optimization_guide:
        print_voice_cloning_optimization_guide()
        return
    
    # 检查安装状态
    if args.check:
        print_installation_status()
        print("\n" + "=" * 80)
        print("🔍 CosyVoice 安装状态")
        print("=" * 80)
        if check_cosyvoice_installation():
            print("✅ CosyVoice: 已安装")
        else:
            print("❌ CosyVoice: 未安装")
        print("=" * 80 + "\n")
        return
    
    # 生成语音
    if not args.talking_head_only:
        success = generate_voice_files(
            script_path=script_path,
            reference_audio=reference_audio,
            output_dir=voice_output_dir,
            prompt_text=args.prompt_text,
            optimize_reference=not args.no_optimize_reference,
            auto_extract_text=not args.no_auto_extract
        )
        
        if not success:
            print("\n❌ 语音生成失败，终止流程")
            sys.exit(1)
        
        if args.voice_only:
            print("\n🎉 语音生成完成！")
            return
    
    # 生成说话头像
    if not args.voice_only:
        # 快速模式优化（CPU 优化）
        if args.fast_mode:
            face_enhance = False
            size = 256
            preprocess = "crop"
            still = True  # 启用 still 模式（只做唇形动画，不移动头部，更快）
            print("\n⚡ 快速模式已启用（CPU 优化）:")
            print(f"   - 面部增强: 禁用")
            print(f"   - 分辨率: {size}x{size}")
            print(f"   - 预处理: {preprocess}")
            print(f"   - Still 模式: 启用（仅唇形动画，速度更快）")
        else:
            face_enhance = not args.no_face_enhance
            size = args.size
            preprocess = args.preprocess
            still = False
        
        success = generate_talking_head_videos(
            image_path=image_path,
            audio_dir=voice_output_dir,
            output_dir=talking_head_output_dir,
            face_enhance=face_enhance,
            size=size,
            preprocess=preprocess,
            still=still
        )
        
        if not success:
            print("\n❌ 说话头像生成失败")
            sys.exit(1)
    
    print("\n" + "=" * 80)
    print("🎉 全部完成！")
    print("=" * 80)
    print(f"📁 语音文件: {voice_output_dir}")
    print(f"📹 视频文件: {talking_head_output_dir}")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()

