import asyncio
import edge_tts
import os

async def generate_voice_for_scripts(scripts_dict, output_dir, voice="zh-CN-XiaoxiaoNeural"):
    """
    根据脚本字典生成 MP3 音频。
    
    Args:
        scripts_dict (dict): { "filename_key": "text_content" }
        output_dir (str): 输出目录路径
        voice (str): Edge TTS 语音模型
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"🎙️ 正在生成语音 (Voice: {voice})...")
    print(f"📂 输出目录: {output_dir}")
    
    for key, text in scripts_dict.items():
        # 自动补全 .mp3 后缀
        filename = key if key.endswith(".mp3") else f"{key}.mp3"
        output_file = os.path.join(output_dir, filename)
        
        # 调用 Edge TTS
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)
        print(f"✅ 已生成: {filename}")
        
    print("\n🎉 所有语音生成完毕！")

