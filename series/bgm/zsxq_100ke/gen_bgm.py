"""
日日生金 (zsxq_100ke) 系列 BGM 生成脚本

使用 MusicGen 模型在本地生成适合国民理财科普动画的背景音乐。
音乐风格：专业但接地气、积极向上、轻松明快，适合循环播放。
"""

import os
import sys
import torch
import scipy
from datetime import datetime

# 将项目根目录加入 path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

try:
    from transformers import pipeline
except ImportError:
    print("请先安装 transformers: uv add transformers torch scipy")
    sys.exit(1)

# ================= 配置区 =================

# 可选模型: 'facebook/musicgen-small', 'facebook/musicgen-medium', 'facebook/musicgen-large'
# M4 16GB 推荐: 'facebook/musicgen-small' (最快) 或 'facebook/musicgen-medium'
MODEL_NAME = 'facebook/musicgen-small'

# 输出目录（当前目录）
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# 生成时长控制
# MusicGen 约 50 tokens/秒
# 30秒足够作为循环BGM使用
DURATION_SECONDS = 30
MAX_NEW_TOKENS = int(DURATION_SECONDS * 51.2)

# 「日日生金」系列 BGM 风格定义
# 特点：专业、积极、轻松、适合循环、不沉闷
STYLES = {
    # 风格1: 专业友好 - 适合知识讲解部分
    "professional_friendly": [
        "Background music for finance education video, "
        "light corporate, positive, friendly tone, "
        "soft synth pads, gentle piano, subtle electronic beat, "
        "clean production, medium tempo 100-110 bpm, "
        "professional but approachable, loopable, no vocals"
    ],
    
    # 风格2: 积极增长 - 适合策略建议、行动号召部分
    "positive_growth": [
        "Uplifting background music for investment education, "
        "inspiring, optimistic, motivational, "
        "bright piano melody, light orchestral strings, "
        "subtle percussion, building energy, "
        "modern corporate feel, 105-115 bpm, loopable, no vocals"
    ],
    
    # 风格3: 轻松思考 - 适合概念解释、剖析部分
    "thinking_light": [
        "Light thinking music for educational content, "
        "curious, intellectual but friendly, "
        "pizzicato strings, soft marimba, gentle bells, "
        "minimal electronic elements, clean mix, "
        "90-100 bpm, seamless loop friendly, no vocals"
    ],
    
    # 风格4: 温暖陪伴 - 适合痛点共鸣、场景描述部分
    "warm_companion": [
        "Warm background music for lifestyle finance video, "
        "comforting, empathetic, gentle, "
        "acoustic guitar arpeggios, soft piano, light strings, "
        "intimate feel, like a friend talking, "
        "85-95 bpm, loopable, no vocals"
    ]
}

# =========================================


def generate_zsxq_bgm(styles_to_generate=None):
    """
    生成「日日生金」系列专用 BGM
    
    Args:
        styles_to_generate: 要生成的风格列表，默认生成所有风格
    """
    print("🎵 「日日生金」BGM 生成器")
    print("=" * 50)
    
    # 检查硬件环境
    print("🖥️  正在检查硬件环境...")
    
    if torch.backends.mps.is_available():
        device = "mps"
        print("🚀 检测到 Apple Silicon (MPS) 加速开启")
    elif torch.cuda.is_available():
        device = "cuda"
        print("🚀 检测到 NVIDIA GPU (CUDA) 加速开启")
    else:
        device = "cpu"
        print("🐢 未检测到 GPU，使用 CPU 运行 (会比较慢)")
    
    # 确保输出目录存在
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    print(f"📂 输出目录: {OUTPUT_DIR}")
    print(f"⏳ 正在加载模型: {MODEL_NAME} (第一次运行会下载约 1-2GB)...")
    
    # 初始化 Pipeline
    try:
        synthesiser = pipeline("text-to-audio", model=MODEL_NAME, device=device)
    except Exception as e:
        print(f"⚠️  加载设备 {device} 失败，尝试切换回 CPU... ({e})")
        synthesiser = pipeline("text-to-audio", model=MODEL_NAME, device="cpu")
    
    # 确定要生成的风格
    if styles_to_generate is None:
        styles_to_generate = list(STYLES.keys())
    
    print(f"\n🎹 开始生成，共 {len(styles_to_generate)} 种风格...")
    print(f"⏱️  每个风格生成时长: {DURATION_SECONDS} 秒")
    print("=" * 50)
    
    generated_files = []
    
    for style_name in styles_to_generate:
        if style_name not in STYLES:
            print(f"⚠️  未知风格: {style_name}，跳过...")
            continue
            
        prompts = STYLES[style_name]
        
        for i, prompt in enumerate(prompts):
            print(f"\n🎼 正在生成风格: [{style_name}] ({i+1}/{len(prompts)})")
            print(f"   Prompt: {prompt[:60]}...")
            
            try:
                # 生成音乐
                music = synthesiser(
                    prompt,
                    forward_params={
                        "max_new_tokens": MAX_NEW_TOKENS,
                        "do_sample": True
                    }
                )
                
                # 处理音频数据
                audio_data = music['audio'][0]
                if audio_data.ndim == 2 and audio_data.shape[0] == 1:
                    audio_data = audio_data.squeeze(0)
                    
                sample_rate = music['sampling_rate']
                
                # 保存文件
                timestamp = datetime.now().strftime('%Y%m%d_%H%M')
                filename = f"bgm_{style_name}_{timestamp}.wav"
                filepath = os.path.join(OUTPUT_DIR, filename)
                
                scipy.io.wavfile.write(filepath, rate=sample_rate, data=audio_data)
                print(f"   ✅ 已保存: {filename}")
                generated_files.append(filepath)
                
            except Exception as e:
                print(f"   ❌ 生成失败: {e}")
    
    print("\n" + "=" * 50)
    print(f"🎉 生成完成！共生成 {len(generated_files)} 个文件")
    print(f"📂 文件位置: {OUTPUT_DIR}")
    print("\n💡 使用建议:")
    print("   - professional_friendly: 适合知识讲解场景")
    print("   - positive_growth: 适合策略建议、行动号召")
    print("   - thinking_light: 适合概念解释、剖析部分")
    print("   - warm_companion: 适合痛点共鸣、场景描述")
    
    return generated_files


def generate_single_style(style_name):
    """
    生成单个风格的 BGM
    
    Args:
        style_name: 风格名称
    """
    if style_name not in STYLES:
        print(f"❌ 未知风格: {style_name}")
        print(f"💡 可用风格: {', '.join(STYLES.keys())}")
        return []
    
    return generate_zsxq_bgm(styles_to_generate=[style_name])


def list_styles():
    """列出所有可用的 BGM 风格"""
    print("🎵 「日日生金」可用 BGM 风格:")
    print("=" * 50)
    for name, prompts in STYLES.items():
        print(f"\n📌 {name}:")
        for prompt in prompts:
            # 显示前100个字符
            print(f"   {prompt[:100]}...")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="日日生金 BGM 生成器")
    parser.add_argument(
        "--style", 
        type=str, 
        default=None,
        help=f"指定要生成的风格 ({', '.join(STYLES.keys())})"
    )
    parser.add_argument(
        "--list", 
        action="store_true",
        help="列出所有可用风格"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="生成所有风格（默认行为）"
    )
    
    args = parser.parse_args()
    
    if args.list:
        list_styles()
    elif args.style:
        generate_single_style(args.style)
    else:
        # 默认只生成一个推荐风格（professional_friendly），避免生成太多
        print("💡 默认生成推荐风格: professional_friendly")
        print("   使用 --all 生成所有风格，或 --style <风格名> 指定风格")
        print()
        generate_single_style("professional_friendly")
