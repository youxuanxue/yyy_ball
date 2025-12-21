import asyncio
import edge_tts
import os
import re
import json
import sys
from pathlib import Path
from typing import Optional

# ============================================================================
# Edge TTS 中文语音选项说明
# ============================================================================
"""
Edge TTS 支持的中文语音选项及其特点：

【中国大陆普通话 - zh-CN】
女性语音：
  - zh-CN-XiaoxiaoNeural (晓晓) ⭐ 默认推荐
    音色：年轻女性，甜美活泼，适合儿童教育、轻松内容
    适用：儿童教育、故事讲述、轻松视频
  
  - zh-CN-XiaoyiNeural (晓伊)
    音色：成熟女性，温和亲切，适合正式场合
    适用：教育课程、客服、新闻播报

男性语音：
  - zh-CN-YunxiNeural (云希) ⭐ 推荐
    音色：年轻男性，清晰自然，亲和力强
    适用：教育视频、知识科普、日常对话
  
  - zh-CN-YunjianNeural (云健)
    音色：成熟男性，沉稳专业，权威感强
    适用：商务演讲、新闻播报、正式文档
  
  - zh-CN-YunxiaNeural (云夏)
    音色：成熟男性，温暖亲切，语速较慢
    适用：故事朗读、情感内容、深度内容
  
  - zh-CN-YunyangNeural (云扬)
    音色：年轻男性，明亮有活力，节奏感强
    适用：游戏解说、运动视频、娱乐内容

【香港粤语 - zh-HK】
  - zh-HK-HiuGaaiNeural (晓佳) - 年轻女性
  - zh-HK-HiuMaanNeural (晓文) - 成熟女性
  - zh-HK-WanLungNeural (云龙) - 成熟男性

【台湾国语 - zh-TW】
  - zh-TW-HsiaoChenNeural (晓辰) - 年轻女性
  - zh-TW-HsiaoYuNeural (晓语) - 成熟女性
  - zh-TW-YunJheNeural (云哲) - 成熟男性

【方言语音】
  - zh-CN-liaoning-XiaobeiNeural (晓北) - 东北话，年轻女性
  - zh-CN-shaanxi-XiaoniNeural (晓妮) - 陕西话，年轻女性

详细文档请参考: docs/edge_tts_voices_guide.md
"""

async def list_chinese_voices():
    """
    列出所有可用的中文语音选项
    
    Returns:
        dict: 按地区分类的语音列表
    """
    voices = await edge_tts.list_voices()
    chinese_voices = {
        'zh-CN': [],
        'zh-HK': [],
        'zh-TW': [],
        'dialects': []
    }
    
    for voice in voices:
        locale = voice.get('Locale', '')
        short_name = voice.get('ShortName', '')
        friendly_name = voice.get('FriendlyName', '')
        gender = voice.get('Gender', '')
        
        if locale.startswith('zh-CN') and 'liaoning' not in locale and 'shaanxi' not in locale:
            chinese_voices['zh-CN'].append({
                'short_name': short_name,
                'friendly_name': friendly_name,
                'gender': gender
            })
        elif locale.startswith('zh-HK'):
            chinese_voices['zh-HK'].append({
                'short_name': short_name,
                'friendly_name': friendly_name,
                'gender': gender
            })
        elif locale.startswith('zh-TW'):
            chinese_voices['zh-TW'].append({
                'short_name': short_name,
                'friendly_name': friendly_name,
                'gender': gender
            })
        elif 'liaoning' in locale or 'shaanxi' in locale:
            chinese_voices['dialects'].append({
                'short_name': short_name,
                'friendly_name': friendly_name,
                'gender': gender
            })
    
    return chinese_voices

def print_voice_options():
    """打印所有可用的中文语音选项"""
    print("\n" + "=" * 80)
    print("🎙️ Edge TTS 中文语音选项")
    print("=" * 80)
    
    voices = asyncio.run(list_chinese_voices())
    
    print("\n【中国大陆普通话 - zh-CN】")
    for voice in voices['zh-CN']:
        gender_emoji = "👨" if voice['gender'] == 'Male' else "👩"
        print(f"  {gender_emoji} {voice['short_name']:30s} - {voice['friendly_name']}")
    
    if voices['zh-HK']:
        print("\n【香港粤语 - zh-HK】")
        for voice in voices['zh-HK']:
            gender_emoji = "👨" if voice['gender'] == 'Male' else "👩"
            print(f"  {gender_emoji} {voice['short_name']:30s} - {voice['friendly_name']}")
    
    if voices['zh-TW']:
        print("\n【台湾国语 - zh-TW】")
        for voice in voices['zh-TW']:
            gender_emoji = "👨" if voice['gender'] == 'Male' else "👩"
            print(f"  {gender_emoji} {voice['short_name']:30s} - {voice['friendly_name']}")
    
    if voices['dialects']:
        print("\n【方言语音】")
        for voice in voices['dialects']:
            gender_emoji = "👨" if voice['gender'] == 'Male' else "👩"
            print(f"  {gender_emoji} {voice['short_name']:30s} - {voice['friendly_name']}")
    
    print("\n" + "=" * 80)
    print("💡 提示: 详细语音特点和使用建议请参考 docs/edge_tts_voices_guide.md")
    print("=" * 80 + "\n")


async def list_all_voices():
    """获取所有可用的语音列表"""
    return await edge_tts.list_voices()


def list_all_voices_sync():
    """同步版本：获取所有可用的语音列表"""
    return asyncio.run(list_all_voices())


def categorize_voices(voices):
    """按语言和地区分类语音"""
    from collections import defaultdict
    categorized = defaultdict(list)
    
    for voice in voices:
        locale = voice.get('Locale', '')
        gender = voice.get('Gender', '')
        name = voice.get('Name', '')
        short_name = voice.get('ShortName', '')
        friendly_name = voice.get('FriendlyName', '')
        
        categorized[locale].append({
            'name': name,
            'short_name': short_name,
            'friendly_name': friendly_name,
            'gender': gender,
            'locale': locale,
            'voice_type': voice.get('VoiceType', ''),
            'status': voice.get('Status', ''),
        })
    
    return categorized

async def generate_voice_for_scripts(scripts_dict, output_dir, voice="zh-CN-XiaoxiaoNeural"):
    """
    根据脚本字典生成 MP3 音频。
    
    Args:
        scripts_dict (dict): { "filename_key": "text_content" }
        output_dir (str): 输出目录路径
        voice (str): Edge TTS 语音模型，默认为 "zh-CN-XiaoxiaoNeural" (晓晓)
                    常用选项：
                    - zh-CN-XiaoxiaoNeural: 年轻女性，活泼甜美，适合儿童教育 ⭐
                    - zh-CN-XiaoyiNeural: 成熟女性，温和亲切，适合教育课程
                    - zh-CN-YunxiNeural: 年轻男性，清晰自然，适合知识科普 ⭐
                    - zh-CN-YunjianNeural: 成熟男性，沉稳专业，适合正式场合
                    - zh-CN-YunxiaNeural: 成熟男性，温暖亲切，适合故事讲述
                    - zh-CN-YunyangNeural: 年轻男性，有活力，适合娱乐内容
                    更多选项请参考文件顶部的注释或运行 print_voice_options()
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

def parse_json_script(file_path):
    """
    解析 JSON 脚本，提取口播内容。
    返回字典: { "scene_index_key": "voiceover_script_content" }
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    scripts = {}
    
    # 遍历 scenes 列表
    for scene in data.get("scenes", []):
        # 获取 scene_index 和 voiceover_script
        idx = scene.get("scene_index")
        script = scene.get("voiceover_script")
            
        if idx is not None and script:
            scripts[str(idx)] = script
                
    return scripts

def gen_voice_clips_from_json(script_path, output_dir, voice="zh-CN-YunxiNeural"):
    """
    从 JSON 脚本生成语音的入口函数
    
    Args:
        script_path (str): JSON 脚本文件路径
        output_dir (str): 输出目录路径
        voice (str): Edge TTS 语音模型，默认为 "zh-CN-XiaoxiaoNeural" (晓晓)
                    常用选项：
                    - zh-CN-XiaoxiaoNeural: 年轻女性，活泼甜美，适合儿童教育 ⭐
                    - zh-CN-YunxiNeural: 年轻男性，清晰自然，适合知识科普 ⭐
                    更多选项请参考文件顶部的注释或运行 print_voice_options()
    """
    print(f"📄 解析脚本: {script_path}")
    scripts = parse_json_script(script_path)
    
    if not scripts:
        print("⚠️ 未找到任何口播内容，请检查 JSON 格式")
        return
        
    asyncio.run(generate_voice_for_scripts(scripts, output_dir, voice))


def gen_voice_clips_from_json_with_clone(
    script_path: str,
    output_dir: str,
    reference_audio_path: str,
    language: str = "zh",
    prompt_text: str = ""
):
    """
    使用 CosyVoice 语音克隆从 JSON 脚本生成语音
    
    Args:
        script_path: JSON 脚本文件路径
        output_dir: 输出目录路径
        reference_audio_path: 参考音频文件路径（你的录音）
        language: 语言代码，默认 "zh" (中文)
        prompt_text: 参考音频对应的文字（可选，建议提供以提高质量）
    """
    print(f"📄 解析脚本: {script_path}")
    scripts = parse_json_script(script_path)
    
    if not scripts:
        print("⚠️ 未找到任何口播内容，请检查 JSON 格式")
        return
    
    # 检查参考音频
    if not os.path.exists(reference_audio_path):
        print(f"❌ 错误: 参考音频文件不存在: {reference_audio_path}")
        print_reference_audio_guide()
        return
    
    # 批量生成
    clone_voice_batch(
        texts=scripts,
        reference_audio_path=reference_audio_path,
        output_dir=output_dir,
        language=language,
        prompt_text=prompt_text
    )


# ============================================================================
# CosyVoice 语音克隆功能
# ============================================================================

# 添加 CosyVoice 和 Matcha-TTS 到 Python 路径（必须在导入之前）
_cosyvoice_path = os.path.join(os.path.dirname(__file__), "../../external/CosyVoice")
_matcha_path = os.path.join(_cosyvoice_path, "third_party/Matcha-TTS")
if os.path.exists(_cosyvoice_path):
    if _cosyvoice_path not in sys.path:
        sys.path.insert(0, _cosyvoice_path)
    if os.path.exists(_matcha_path) and _matcha_path not in sys.path:
        sys.path.insert(0, _matcha_path)

# 尝试导入 CosyVoice（如果可用）
COSYVOICE_AVAILABLE = False
COSYVOICE_API = False

try:
    try:
        from cosyvoice.api import CosyVoiceTTS
        COSYVOICE_API = True
        COSYVOICE_AVAILABLE = True
    except ImportError:
        if os.path.exists(_cosyvoice_path):
            try:
                from cosyvoice.cli.cosyvoice import CosyVoice
                COSYVOICE_API = False
                COSYVOICE_AVAILABLE = True
            except (ImportError, RuntimeError) as e:
                if "torchcodec" in str(e).lower() or "libtorchcodec" in str(e).lower():
                    COSYVOICE_AVAILABLE = False
                else:
                    COSYVOICE_AVAILABLE = False
        else:
            COSYVOICE_AVAILABLE = False
except Exception:
    COSYVOICE_AVAILABLE = False
    COSYVOICE_API = False


def check_cosyvoice_installation() -> bool:
    """检查 CosyVoice 是否已安装"""
    return COSYVOICE_AVAILABLE


def extract_text_from_audio(audio_path: str, language: str = "zh") -> Optional[str]:
    """
    从参考音频中提取文字（使用 Whisper）
    
    Args:
        audio_path: 音频文件路径
        language: 语言代码，默认 "zh" (中文)
    
    Returns:
        str: 提取的文字，如果失败返回 None
    """
    try:
        import whisper
        
        print(f"🎤 正在从参考音频提取文字...")
        model = whisper.load_model("base")
        result = model.transcribe(audio_path, language=language)
        text = result["text"].strip()
        
        if text:
            print(f"✅ 提取成功: {text[:50]}...")
            return text
        else:
            print("⚠️ 未提取到文字")
            return None
            
    except ImportError:
        print("⚠️ Whisper 未安装，无法自动提取文字")
        print("💡 请安装: uv add openai-whisper")
        return None
    except Exception as e:
        print(f"⚠️ 文字提取失败: {str(e)}")
        return None


def optimize_reference_audio(
    audio_path: str,
    target_duration: float = 10.0,
    output_path: Optional[str] = None
) -> str:
    """
    优化参考音频：裁剪到最佳时长，转换为单声道，标准化采样率
    
    Args:
        audio_path: 原始音频文件路径
        target_duration: 目标时长（秒），默认 10 秒
        output_path: 输出路径，如果为 None 则覆盖原文件
    
    Returns:
        str: 优化后的音频文件路径
    """
    try:
        from pydub import AudioSegment
        
        print(f"🔧 正在优化参考音频...")
        audio = AudioSegment.from_file(audio_path)
        
        # 转换为单声道（CosyVoice 推荐）
        if audio.channels > 1:
            audio = audio.set_channels(1)
            print("  ✓ 转换为单声道")
        
        # 标准化采样率到 16kHz（CosyVoice 推荐）
        target_sample_rate = 16000
        if audio.frame_rate != target_sample_rate:
            audio = audio.set_frame_rate(target_sample_rate)
            print(f"  ✓ 采样率标准化到 {target_sample_rate}Hz")
        
        # 裁剪到指定时长（取前 N 秒，选择最清晰的部分）
        if len(audio) > target_duration * 1000:
            audio = audio[:int(target_duration * 1000)]
            print(f"  ✓ 裁剪到 {target_duration} 秒")
        
        output = output_path or audio_path
        audio.export(output, format="wav")
        
        print(f"✅ 参考音频已优化: {output}")
        return output
        
    except ImportError:
        print("⚠️ 警告: pydub 未安装，跳过音频优化")
        return audio_path
    except Exception as e:
        print(f"⚠️ 警告: 音频优化失败 - {str(e)}")
        return audio_path


def get_optimal_prompt_text(
    reference_audio_path: str,
    manual_text: Optional[str] = None,
    auto_extract: bool = True
) -> str:
    """
    获取最佳的 prompt_text
    
    优先级：
    1. 手动提供的文字（最准确）
    2. 从音频自动提取（使用 Whisper）
    3. 返回空字符串（效果较差）
    
    Args:
        reference_audio_path: 参考音频文件路径
        manual_text: 手动提供的文字（可选）
        auto_extract: 是否自动提取（如果未提供手动文字）
    
    Returns:
        str: prompt_text
    """
    # 优先使用手动提供的文字
    if manual_text and manual_text.strip():
        print(f"📝 使用手动提供的文字: {manual_text[:50]}...")
        return manual_text.strip()
    
    # 自动提取
    if auto_extract:
        extracted_text = extract_text_from_audio(reference_audio_path)
        if extracted_text:
            return extracted_text
    
    # 如果都失败，返回空字符串（效果较差）
    print("⚠️ 警告: 未提供 prompt_text，音色相似度可能较低")
    print("💡 建议: 提供参考音频对应的文字以提高质量")
    return ""


def clone_voice(
    text: str,
    reference_audio_path: str,
    output_path: str,
    language: str = "zh",
    prompt_text: str = ""
) -> bool:
    """
    使用 CosyVoice 克隆语音
    
    Args:
        text: 要生成的文字内容
        reference_audio_path: 参考音频文件路径（你的录音）
        output_path: 输出音频文件路径
        language: 语言代码，默认 "zh" (中文)
        prompt_text: 参考音频对应的文字（可选，建议提供以提高质量）
    
    Returns:
        bool: 是否成功生成
    """
    if not COSYVOICE_AVAILABLE:
        print("❌ 错误: CosyVoice 未安装")
        print("💡 请先安装（推荐从 GitHub 安装完整版本）:")
        print("   方式一（推荐）: git clone https://github.com/FunAudioLLM/CosyVoice.git external/CosyVoice")
        print("   方式二: pip install cosyvoice（注意：PyPI 包可能不完整）")
        return False
    
    if not os.path.exists(reference_audio_path):
        print(f"❌ 错误: 参考音频文件不存在: {reference_audio_path}")
        return False
    
    try:
        print(f"🎙️ 正在使用 CosyVoice 克隆语音...")
        print(f"📝 文字: {text[:50]}...")
        print(f"🎵 参考音频: {reference_audio_path}")
        
        if COSYVOICE_API:
            try:
                from cosyvoice.api import CosyVoiceTTS
                import torch
                import torchaudio
                
                device = "cuda" if torch.cuda.is_available() else "cpu"
                tts = CosyVoiceTTS(device=device)
                
                audio_generator = tts.tts_instruct(
                    text=text,
                    spk_id="中文男",
                    prompt="",
                    return_format="wav",
                    stream=False
                )
                
                audio = next(audio_generator)
                torchaudio.save(output_path, audio, 22050)
            except Exception as e:
                print(f"❌ 错误: CosyVoice API 调用失败: {e}")
                print("💡 提示: PyPI 包可能不完整，建议从 GitHub 安装完整版本")
                return False
        else:
            from cosyvoice.cli.cosyvoice import CosyVoice
            import torchaudio
            
            model_dir = "iic/CosyVoice-300M"
            cosyvoice = CosyVoice(model_dir=model_dir)
            
            for i, output in enumerate(cosyvoice.inference_zero_shot(
                tts_text=text,
                prompt_text=prompt_text,
                prompt_wav=reference_audio_path,
                stream=False
            )):
                torchaudio.save(output_path, output['tts_speech'], cosyvoice.sample_rate)
                break
        
        print(f"✅ 已生成: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ 错误: 生成失败 - {str(e)}")
        print(f"💡 提示: CosyVoice API 可能需要根据实际安装版本调整")
        return False


def clone_voice_batch(
    texts: dict,
    reference_audio_path: str,
    output_dir: str,
    language: str = "zh",
    prompt_text: str = ""
) -> list:
    """
    批量克隆语音
    
    Args:
        texts: 文字字典 { "filename_key": "text_content" }
        reference_audio_path: 参考音频文件路径
        output_dir: 输出目录
        language: 语言代码
        prompt_text: 参考音频对应的文字（可选，建议提供以提高质量）
    
    Returns:
        list: 成功生成的文件路径列表
    """
    current_file = os.path.abspath(__file__)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
    cosyvoice_path = os.path.join(project_root, "external/CosyVoice")
    matcha_path = os.path.join(cosyvoice_path, "third_party/Matcha-TTS")
    
    if os.path.exists(matcha_path):
        matcha_path_abs = os.path.abspath(matcha_path)
        if matcha_path_abs not in sys.path:
            sys.path.insert(0, matcha_path_abs)
    if os.path.exists(cosyvoice_path):
        cosyvoice_path_abs = os.path.abspath(cosyvoice_path)
        if cosyvoice_path_abs not in sys.path:
            sys.path.insert(0, cosyvoice_path_abs)
    
    import os as os_module
    pythonpath = os_module.environ.get('PYTHONPATH', '')
    if matcha_path_abs and matcha_path_abs not in pythonpath:
        if pythonpath:
            os_module.environ['PYTHONPATH'] = f"{matcha_path_abs}:{cosyvoice_path_abs}:{pythonpath}"
        else:
            os_module.environ['PYTHONPATH'] = f"{matcha_path_abs}:{cosyvoice_path_abs}"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    if not COSYVOICE_AVAILABLE:
        print("❌ 错误: CosyVoice 未安装")
        return []
    
    successful = []
    
    if COSYVOICE_API:
        try:
            from cosyvoice.api import CosyVoiceTTS
            import torch
            import torchaudio
            device = "cuda" if torch.cuda.is_available() else "cpu"
            tts = CosyVoiceTTS(device=device)
        except Exception as e:
            print(f"❌ 错误: CosyVoice API 初始化失败: {e}")
            print("💡 提示: PyPI 包可能不完整，建议从 GitHub 安装完整版本")
            return []
    else:
        current_file = os.path.abspath(__file__)
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
        cosyvoice_path = os.path.join(project_root, "external/CosyVoice")
        matcha_path = os.path.join(cosyvoice_path, "third_party/Matcha-TTS")
        
        if os.path.exists(matcha_path):
            matcha_path_abs = os.path.abspath(matcha_path)
            if matcha_path_abs not in sys.path:
                sys.path.insert(0, matcha_path_abs)
        if os.path.exists(cosyvoice_path):
            cosyvoice_path_abs = os.path.abspath(cosyvoice_path)
            if cosyvoice_path_abs not in sys.path:
                sys.path.insert(0, cosyvoice_path_abs)
        
        try:
            import matcha.models.components.flow_matching
        except ImportError:
            pass
        
        try:
            from cosyvoice.cli.cosyvoice import CosyVoice
        except RuntimeError as e:
            if "torchcodec" in str(e).lower() or "libtorchcodec" in str(e).lower():
                print("⚠️ 警告: torchcodec 加载失败，但将继续尝试使用 CosyVoice")
                print("💡 提示: CosyVoice 的音频加载使用 torchaudio，不依赖 torchcodec")
                from cosyvoice.cli.cosyvoice import CosyVoice
            else:
                raise
        
        model_dir = "iic/CosyVoice-300M"
        cosyvoice = CosyVoice(model_dir=model_dir)
    
    for key, text in texts.items():
        filename = key if key.endswith(".wav") else f"{key}.wav"
        output_path = os.path.join(output_dir, filename)
        
        print(f"\n[{len(successful) + 1}/{len(texts)}] 处理: {filename}")
        
        try:
            if COSYVOICE_API:
                audio_generator = tts.tts_instruct(
                    text=text,
                    spk_id="中文男",
                    prompt="",
                    return_format="wav",
                    stream=False
                )
                audio = next(audio_generator)
                torchaudio.save(output_path, audio, 22050)
            else:
                import torchaudio
                for i, output in enumerate(cosyvoice.inference_zero_shot(
                    tts_text=text,
                    prompt_text=prompt_text,
                    prompt_wav=reference_audio_path,
                    stream=False
                )):
                    try:
                        import soundfile as sf
                        audio_np = output['tts_speech'].squeeze().cpu().numpy()
                        sf.write(output_path, audio_np, cosyvoice.sample_rate)
                    except ImportError:
                        torchaudio.save(output_path, output['tts_speech'], cosyvoice.sample_rate)
                    break
            successful.append(output_path)
            print(f"✅ 已生成: {filename}")
        except Exception as e:
            print(f"❌ 生成失败: {filename} - {str(e)}")
    
    print(f"\n🎉 批量处理完成: {len(successful)}/{len(texts)} 成功")
    return successful


def get_recommended_reference_audio_requirements() -> dict:
    """
    获取推荐的参考音频要求
    
    Returns:
        dict: 音频要求说明
    """
    return {
        "时长": "建议 5-15 秒（至少 3 秒）",
        "格式": "WAV, MP3, M4A 等常见格式",
        "质量": "清晰，无背景噪音",
        "内容": "清晰的语音，最好包含多种音调",
        "采样率": "建议 16kHz 或更高",
        "声道": "单声道或立体声均可"
    }


def print_reference_audio_guide():
    """打印参考音频准备指南"""
    requirements = get_recommended_reference_audio_requirements()
    
    print("\n" + "=" * 80)
    print("🎙️ 参考音频准备指南")
    print("=" * 80)
    
    for key, value in requirements.items():
        print(f"  {key}: {value}")
    
    print("\n💡 提示:")
    print("  - 录制时保持安静环境")
    print("  - 说话清晰，语速适中")
    print("  - 可以录制一段包含不同音调的内容")
    print("  - 使用 optimize_reference_audio() 可以优化音频")
    print("=" * 80 + "\n")


def print_voice_cloning_optimization_guide():
    """打印语音克隆优化指南"""
    print("\n" + "=" * 80)
    print("🎙️ 语音克隆优化指南")
    print("=" * 80)
    print("\n【提高音色相似度的关键因素】")
    print("1. ✅ 提供 prompt_text（参考音频对应的文字）")
    print("   - 手动提供：最准确，效果最好")
    print("   - 自动提取：使用 Whisper 从音频提取")
    print("   - 不提供：效果较差，音色相似度低")
    print("\n2. ✅ 优化参考音频质量")
    print("   - 时长：5-15 秒最佳（建议 10 秒）")
    print("   - 格式：WAV 格式，单声道，16kHz 采样率")
    print("   - 质量：清晰，无背景噪音")
    print("\n3. ✅ 参考音频内容")
    print("   - 包含多种音调和情感")
    print("   - 语速适中，发音清晰")
    print("   - 与目标文本风格相似")
    print("\n【使用建议】")
    print("1. 录制高质量的参考音频（10 秒左右）")
    print("2. 提供参考音频对应的准确文字")
    print("3. 使用 optimize_reference_audio() 优化音频")
    print("4. 使用 get_optimal_prompt_text() 获取最佳文字")
    print("=" * 80 + "\n")
