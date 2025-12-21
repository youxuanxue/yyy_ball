#!/usr/bin/env python3
"""
语音克隆 CLI 工具
使用 CosyVoice 进行语音克隆
"""
import argparse
import sys
import os
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.voice import (
    clone_voice,
    clone_voice_batch,
    optimize_reference_audio,
    print_reference_audio_guide,
    check_cosyvoice_installation,
    parse_json_script,
    gen_voice_clips_from_json_with_clone,
    get_optimal_prompt_text
)


def convert_wav_to_mp3(wav_path: str, mp3_path: str) -> bool:
    """将 WAV 文件转换为 MP3"""
    try:
        from pydub import AudioSegment
        if not os.path.exists(wav_path):
            return False
        audio = AudioSegment.from_wav(wav_path)
        audio.export(mp3_path, format="mp3")
        return True
    except Exception as e:
        print(f"❌ 转换失败: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="使用 CosyVoice 语音克隆生成语音",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 单个文本生成
  python -m src.cli.voice_clone \\
      --text "你好，这是测试语音" \\
      --reference assets/voice/my_voice.wav \\
      --output output.wav

  # 从 JSON 脚本批量生成
  python -m src.cli.voice_clone \\
      --script series/sunzi/lesson10/script.json \\
      --reference assets/voice/my_voice.wav \\
      --output-dir series/sunzi/lesson10/voice

  # 优化参考音频
  python -m src.cli.voice_clone \\
      --optimize-reference assets/voice/raw_recording.wav \\
      --target-duration 10
        """
    )
    
    parser.add_argument("--text", type=str, help="要生成的文字内容（单个文本模式）")
    parser.add_argument("--script", type=str, help="JSON 脚本文件路径（批量模式）")
    parser.add_argument("--reference", type=str, help="参考音频文件路径")
    parser.add_argument("--output", type=str, help="输出音频文件路径（单个文本模式）")
    parser.add_argument("--output-dir", type=str, help="输出目录（批量模式）")
    parser.add_argument("--language", type=str, default="zh", help="语言代码（默认: zh）")
    parser.add_argument("--prompt-text", type=str, default="", help="参考音频对应的文字")
    parser.add_argument("--prompt-text-file", type=str, help="prompt_text 文件路径")
    parser.add_argument("--optimize-reference", type=str, help="优化参考音频")
    parser.add_argument("--target-duration", type=float, default=10.0, help="目标时长（秒）")
    parser.add_argument("--auto-extract-text", action="store_true", help="自动提取 prompt_text")
    parser.add_argument("--convert-to-mp3", action="store_true", help="将生成的 WAV 转换为 MP3")
    parser.add_argument("--guide", action="store_true", help="显示参考音频准备指南")
    
    args = parser.parse_args()
    
    # 显示指南
    if args.guide:
        print_reference_audio_guide()
        return
    
    # 优化参考音频
    if args.optimize_reference:
        optimize_reference_audio(
            audio_path=args.optimize_reference,
            target_duration=args.target_duration
        )
        return
    
    # 检查 CosyVoice 安装
    if not check_cosyvoice_installation():
        print("❌ 错误: CosyVoice 未安装")
        print("💡 请从 GitHub 安装: git clone https://github.com/FunAudioLLM/CosyVoice.git external/CosyVoice")
        sys.exit(1)
    
    if not args.reference:
        parser.error("必须指定 --reference 参数")
    
    if not os.path.exists(args.reference):
        print(f"❌ 错误: 参考音频文件不存在: {args.reference}")
        print_reference_audio_guide()
        sys.exit(1)
    
    # 获取 prompt_text
    prompt_text = args.prompt_text
    if args.prompt_text_file and os.path.exists(args.prompt_text_file):
        with open(args.prompt_text_file, 'r', encoding='utf-8') as f:
            prompt_text = f.read().strip()
        print(f"📝 使用 prompt_text: {prompt_text[:50]}...")
    elif args.auto_extract_text:
        prompt_text = get_optimal_prompt_text(
            reference_audio_path=args.reference,
            auto_extract=True
        )
    
    # 单个文本模式
    if args.text:
        if not args.output:
            parser.error("使用 --text 时必须指定 --output")
        
        success = clone_voice(
            text=args.text,
            reference_audio_path=args.reference,
            output_path=args.output,
            language=args.language,
            prompt_text=prompt_text
        )
        sys.exit(0 if success else 1)
    
    # 批量模式
    elif args.script:
        if not args.output_dir:
            parser.error("使用 --script 时必须指定 --output-dir")
        
        scripts = parse_json_script(args.script)
        if not scripts:
            print("⚠️ 未找到任何口播内容，请检查 JSON 格式")
            sys.exit(1)
        
        # 优化参考音频（如果需要）
        optimized_audio = args.reference
        if args.auto_extract_text:
            temp_audio = os.path.join(args.output_dir, "optimized_reference.wav")
            os.makedirs(args.output_dir, exist_ok=True)
            optimized_audio = optimize_reference_audio(
                audio_path=args.reference,
                target_duration=10.0,
                output_path=temp_audio
            )
        
        results = clone_voice_batch(
            texts=scripts,
            reference_audio_path=optimized_audio,
            output_dir=args.output_dir,
            language=args.language,
            prompt_text=prompt_text
        )
        
        # 转换 WAV 到 MP3（如果需要）
        if args.convert_to_mp3:
            print("\n🔄 转换音频格式为 MP3...")
            wav_files = sorted([f for f in os.listdir(args.output_dir) 
                              if f.endswith('.wav') and f != 'optimized_reference.wav'],
                             key=lambda x: int(os.path.splitext(x)[0]) if os.path.splitext(x)[0].isdigit() else 999)
            
            success_count = 0
            for wav_file in wav_files:
                wav_path = os.path.join(args.output_dir, wav_file)
                basename = os.path.splitext(wav_file)[0]
                mp3_path = os.path.join(args.output_dir, f"{basename}.mp3")
                
                if convert_wav_to_mp3(wav_path, mp3_path):
                    success_count += 1
                    try:
                        os.remove(wav_path)
                    except:
                        pass
            
            print(f"✅ 成功转换 {success_count} 个 MP3 文件")
        
        print(f"\n✅ 成功生成 {len(results)} 个文件")
        sys.exit(0)
    
    else:
        parser.error("必须指定 --text 或 --script")


if __name__ == "__main__":
    main()

