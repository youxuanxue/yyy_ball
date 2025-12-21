#!/usr/bin/env python3
"""
说话头像生成 CLI 工具
使用 SadTalker 从音频和图片生成说话头像视频
"""
import argparse
import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.talking_head import (
    generate_talking_head,
    batch_generate_talking_heads,
    print_installation_status,
    print_materials_checklist,
    check_sadtalker_installation
)


def main():
    parser = argparse.ArgumentParser(
        description="生成说话头像视频（使用 SadTalker）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 生成单个视频
  python -m src.cli.talking_head \\
      --image assets/avatars/character_01.jpg \\
      --audio series/sunzi/lesson10/voice/1.mp3 \\
      --output series/sunzi/lesson10/talking_head/1.mp4

  # 批量生成
  python -m src.cli.talking_head \\
      --image assets/avatars/character_01.jpg \\
      --audio-dir series/sunzi/lesson10/voice \\
      --output-dir series/sunzi/lesson10/talking_head

  # 检查安装状态
  python -m src.cli.talking_head --check
        """
    )
    
    parser.add_argument("--image", type=str, help="人物头像图片路径")
    parser.add_argument("--audio", type=str, help="音频文件路径（单个文件）")
    parser.add_argument("--audio-dir", type=str, help="音频文件目录（批量处理）")
    parser.add_argument("--output", type=str, help="输出视频路径（单个文件）")
    parser.add_argument("--output-dir", type=str, help="输出目录（批量处理）")
    parser.add_argument("--face-enhance", action="store_true", default=True, help="启用面部增强（默认启用）")
    parser.add_argument("--no-face-enhance", dest="face_enhance", action="store_false", help="禁用面部增强")
    parser.add_argument("--batch-size", type=int, default=1, help="批处理大小（默认: 1）")
    parser.add_argument("--size", type=int, default=512, help="输出视频尺寸（默认: 512）")
    parser.add_argument("--preprocess", type=str, default="full", choices=["crop", "full"], help="预处理模式")
    parser.add_argument("--still", action="store_true", help="保持头部静止（仅唇形动画）")
    parser.add_argument("--check", action="store_true", help="检查安装状态和素材准备情况")
    
    args = parser.parse_args()
    
    # 检查模式
    if args.check:
        print_installation_status()
        print_materials_checklist()
        return
    
    # 验证参数
    if not args.image:
        parser.error("必须指定 --image 参数")
    
    if not args.audio and not args.audio_dir:
        parser.error("必须指定 --audio 或 --audio-dir 参数")
    
    if args.audio and args.audio_dir:
        parser.error("不能同时指定 --audio 和 --audio-dir")
    
    if args.audio and not args.output:
        parser.error("使用 --audio 时必须指定 --output")
    
    if args.audio_dir and not args.output_dir:
        parser.error("使用 --audio-dir 时必须指定 --output-dir")
    
    # 检查安装状态
    checks = check_sadtalker_installation()
    if not checks['pytorch_available']:
        print("❌ 错误: PyTorch 未安装")
        print("💡 请先安装: uv add torch torchvision torchaudio")
        sys.exit(1)
    
    if not checks['sadtalker_dir_exists']:
        print("❌ 错误: SadTalker 未安装")
        print("💡 请先安装: git clone https://github.com/OpenTalker/SadTalker.git external/SadTalker")
        sys.exit(1)
    
    # 执行生成
    if args.audio:
        success = generate_talking_head(
            image_path=args.image,
            audio_path=args.audio,
            output_path=args.output,
            face_enhance=args.face_enhance,
            batch_size=args.batch_size,
            size=args.size,
            still=args.still
        )
        sys.exit(0 if success else 1)
    else:
        results = batch_generate_talking_heads(
            image_path=args.image,
            audio_dir=args.audio_dir,
            output_dir=args.output_dir,
            face_enhance=args.face_enhance,
            batch_size=args.batch_size,
            size=args.size,
            still=args.still
        )
        print(f"\n✅ 成功生成 {len(results)} 个视频文件")
        sys.exit(0)


if __name__ == "__main__":
    main()

