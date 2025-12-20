import os
import torch
import scipy
from transformers import pipeline
from datetime import datetime

# ================= 配置区 =================
# 可选模型: 'facebook/musicgen-small', 'facebook/musicgen-medium', 'facebook/musicgen-large'
# M4 16GB 推荐: 'facebook/musicgen-small' (最快) 或 'facebook/musicgen-medium'
MODEL_NAME = 'facebook/musicgen-small'
OUTPUT_DIR = "assets/music_candidates_local"

# 生成时长控制
# MusicGen 约 50 tokens/秒 (这个数值不一定精确，取决于模型配置)
# small/medium 模型默认最大长度通常限制在 30秒左右 (1500 tokens)
DURATION_SECONDS = 30
MAX_NEW_TOKENS = int(DURATION_SECONDS * 51.2) # 经验值: 1500 tokens ~= 30s

# 定义音乐风格 Prompt
STYLES = {
    "playful_chinese": [
        "Background music for kids education video, traditional chinese instruments, guzheng and dizi flute, blended with light lo-fi hip hop beat, playful, happy, bright, medium tempo"
    ],
    "smart_thinking": [
        "Background music, pizzicato strings, light percussion, marimba, curious mood, thinking process, puzzle solving, subtle asian melody, clean, minimal"
    ],
    "epic_wisdom": [
        "Cinematic underscore, inspiring, orchestral, chinese drums and strings, victory, wisdom, ancient china atmosphere but modern production, uplifting"
    ]
}
# =========================================

def generate_music_local():
    """
    在本地使用 Hugging Face Transformers 生成音乐
    """
    print(f"🖥️  正在检查硬件环境...")
    
    # 检查设备
    if torch.backends.mps.is_available():
        device = "mps"
        print("🚀 检测到 Apple Silicon (MPS) 加速开启")
    elif torch.cuda.is_available():
        device = "cuda"
        print("🚀 检测到 NVIDIA GPU (CUDA) 加速开启")
    else:
        device = "cpu"
        print("🐢 未检测到 GPU，使用 CPU 运行 (会比较慢)")

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print(f"⏳ 正在加载模型: {MODEL_NAME} (第一次运行会下载约 1-2GB)...")
    
    # 初始化 Pipeline
    # 注意: mps 在某些 transformer 版本下可能不稳定，如果报错请改为 device="cpu"
    try:
        synthesiser = pipeline("text-to-audio", model=MODEL_NAME, device=device)
    except Exception as e:
        print(f"⚠️  加载设备 {device} 失败，尝试切换回 CPU... ({e})")
        synthesiser = pipeline("text-to-audio", model=MODEL_NAME, device="cpu")

    print(f"🎹 开始生成，共 {len(STYLES)} 种风格...")

    for style_name, prompts in STYLES.items():
        for i, prompt in enumerate(prompts):
            print(f"\n🎼 正在生成风格: [{style_name}] ({i+1}/{len(prompts)})")
            print(f"   Prompt: {prompt[:50]}...")
            
            # 生成
            # forward_params 控制生成参数
            music = synthesiser(
                prompt, 
                forward_params={
                    "max_new_tokens": MAX_NEW_TOKENS,
                    "do_sample": True
                }
            )
            
            # music 格式: {'audio': np.array(shape=(1, N)), 'sampling_rate': 32000}
            audio_data = music['audio'][0] # 取出单声道/第一轨 (通常是 (C, T) 或 (T,))
            # 如果是 (C, T) 且 C=1, scipy 需要 (T,) 或 (T, C)
            if audio_data.ndim == 2 and audio_data.shape[0] == 1:
                audio_data = audio_data.squeeze(0)
                
            sample_rate = music['sampling_rate']

            # 保存文件
            timestamp = datetime.now().strftime('%H%M')
            filename = f"{style_name}_{timestamp}.wav"
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            scipy.io.wavfile.write(filepath, rate=sample_rate, data=audio_data)
            print(f"   ✅ 已保存: {filepath}")

    print(f"\n🎉 全部完成！请检查目录: {OUTPUT_DIR}")

if __name__ == "__main__":
    generate_music_local()
