"""
CosyVoice 语音克隆模块

提供使用 CosyVoice 进行语音克隆的功能。
"""
import os
import sys
import types


# ============================================================================
# CosyVoice 初始化设置
# ============================================================================

# 设置环境变量以禁用 torchcodec（如果未安装）
# 强制使用 soundfile 后端加载音频
os.environ['TORCHAUDIO_USE_SOUNDFILE'] = '1'
os.environ['TORCHAUDIO_DISABLE_TORCHCODEC'] = '1'
os.environ['TORCHAUDIO_BACKEND'] = 'soundfile'

# 添加 CosyVoice 和 Matcha-TTS 到 Python 路径（必须在导入之前）
# 注意：Matcha-TTS 必须在 CosyVoice 之前，因为 CosyVoice 依赖 Matcha-TTS
_current_file = os.path.abspath(__file__)
_project_root = os.path.dirname(os.path.dirname(os.path.dirname(_current_file)))
_cosyvoice_path = os.path.join(_project_root, "external/CosyVoice")
_matcha_path = os.path.join(_cosyvoice_path, "third_party/Matcha-TTS")

# 先添加 Matcha-TTS（依赖项在前）
if os.path.exists(_matcha_path):
    _matcha_path_abs = os.path.abspath(_matcha_path)
    if _matcha_path_abs not in sys.path:
        sys.path.insert(0, _matcha_path_abs)
    pythonpath = os.environ.get('PYTHONPATH', '')
    if _matcha_path_abs not in pythonpath:
        os.environ['PYTHONPATH'] = f"{_matcha_path_abs}:{pythonpath}" if pythonpath else _matcha_path_abs

# 再添加 CosyVoice
if os.path.exists(_cosyvoice_path):
    _cosyvoice_path_abs = os.path.abspath(_cosyvoice_path)
    if _cosyvoice_path_abs not in sys.path:
        sys.path.insert(0, _cosyvoice_path_abs)
    pythonpath = os.environ.get('PYTHONPATH', '')
    if _cosyvoice_path_abs not in pythonpath:
        os.environ['PYTHONPATH'] = f"{_cosyvoice_path_abs}:{pythonpath}" if pythonpath else _cosyvoice_path_abs

# 在导入 CosyVoice 之前，先 patch torchaudio 以避免 torchcodec 错误
# torchaudio 2.9.1 会先尝试使用 torchcodec，即使指定了 backend='soundfile'
try:
    # 创建一个 mock 模块来替换 _torchcodec
    class MockTorchcodec:
        @staticmethod
        def load_with_torchcodec(*args, **kwargs):
            """Mock load_with_torchcodec 以强制使用其他后端"""
            raise ImportError("TorchCodec not available, using soundfile backend instead")
        
        @staticmethod
        def save_with_torchcodec(*args, **kwargs):
            """Mock save_with_torchcodec 以强制使用其他后端"""
            raise ImportError("TorchCodec not available, using soundfile backend instead")
    
    # 在导入 torchaudio 之前注册 mock
    mock_module = types.ModuleType('torchaudio._torchcodec')
    mock_module.load_with_torchcodec = MockTorchcodec.load_with_torchcodec
    mock_module.save_with_torchcodec = MockTorchcodec.save_with_torchcodec
    sys.modules['torchaudio._torchcodec'] = mock_module
    
    import torchaudio
    
    # 再次尝试 patch（如果上面的方法不起作用）
    try:
        from torchaudio import _torchcodec
        if hasattr(_torchcodec, 'load_with_torchcodec'):
            _torchcodec.load_with_torchcodec = MockTorchcodec.load_with_torchcodec
    except (ImportError, AttributeError):
        pass
    
    # Patch torchaudio.load 以确保使用 soundfile
    if not hasattr(torchaudio, '_original_load'):
        torchaudio._original_load = torchaudio.load
        
        def patched_torchaudio_load_early(filepath, *args, **kwargs):
            """强制使用 soundfile 后端的 torchaudio.load 补丁"""
            backend = kwargs.pop('backend', 'soundfile')
            
            try:
                return torchaudio._original_load(filepath, *args, backend=backend, **kwargs)
            except Exception as e:
                error_str = str(e).lower()
                # 如果遇到 torchcodec 错误，使用 soundfile 库直接加载
                if 'torchcodec' in error_str or 'load_with_torchcodec' in error_str or 'torchcodec not available' in error_str:
                    try:
                        import soundfile as sf
                        import torch
                        data, sample_rate = sf.read(filepath)
                        if len(data.shape) == 1:
                            audio = torch.from_numpy(data).float().unsqueeze(0)
                        else:
                            audio = torch.from_numpy(data.mean(axis=1)).float().unsqueeze(0)
                        return audio, sample_rate
                    except ImportError:
                        if backend != 'sox_io':
                            try:
                                return torchaudio._original_load(filepath, *args, backend='sox_io', **kwargs)
                            except Exception:
                                pass
                        raise RuntimeError(f"无法加载音频文件 {filepath}，soundfile 和 sox_io 后端都失败: {e}")
                raise
        
        torchaudio.load = patched_torchaudio_load_early
        print("✅ 已提前应用 torchaudio 补丁，强制使用 soundfile 后端")
except ImportError:
    pass
except Exception as e:
    print(f"⚠️ 警告: 无法提前应用 torchaudio 补丁: {e}")

# 尝试导入 CosyVoice CLI（如果可用）
COSYVOICE_AVAILABLE = False

try:
    if os.path.exists(_cosyvoice_path):
        try:
            from cosyvoice.cli.cosyvoice import CosyVoice
            COSYVOICE_AVAILABLE = True
        except (ImportError, RuntimeError) as e:
            error_str = str(e).lower()
            if "torchcodec" in error_str or "libtorchcodec" in error_str:
                print(f"⚠️ 警告: 导入 CosyVoice 时遇到 torchcodec 错误，但将继续使用（已应用补丁）: {e}")
                COSYVOICE_AVAILABLE = True
            else:
                print(f"⚠️ 警告: 导入 CosyVoice 时遇到错误: {e}")
                COSYVOICE_AVAILABLE = False
    else:
        COSYVOICE_AVAILABLE = False
except Exception as e:
    print(f"⚠️ 警告: 导入 CosyVoice 时遇到未预期的错误: {e}")
    COSYVOICE_AVAILABLE = False


# ============================================================================
# CosyVoice 功能函数
# ============================================================================

def normalize_numbers_in_text(text: str) -> str:
    """
    将文本中的阿拉伯数字转换为中文读法，提高 TTS 质量
    
    Args:
        text: 原始文本
        
    Returns:
        转换后的文本
    """
    import re
    
    def int_to_chinese(num: int) -> str:
        """将整数转换为中文读法（支持 0-9999）"""
        if num == 0:
            return "零"
        elif num < 10:
            chinese_digits = ["", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
            return chinese_digits[num]
        elif num < 20:
            if num == 10:
                return "十"
            else:
                return "十" + int_to_chinese(num % 10)
        elif num < 100:
            tens = num // 10
            ones = num % 10
            if ones == 0:
                return int_to_chinese(tens) + "十"
            else:
                return int_to_chinese(tens) + "十" + int_to_chinese(ones)
        elif num < 1000:
            hundreds = num // 100
            remainder = num % 100
            if remainder == 0:
                return int_to_chinese(hundreds) + "百"
            elif remainder < 10:
                return int_to_chinese(hundreds) + "百零" + int_to_chinese(remainder)
            else:
                return int_to_chinese(hundreds) + "百" + int_to_chinese(remainder)
        elif num < 10000:
            thousands = num // 1000
            remainder = num % 1000
            if remainder == 0:
                return int_to_chinese(thousands) + "千"
            elif remainder < 100:
                return int_to_chinese(thousands) + "千零" + int_to_chinese(remainder)
            else:
                return int_to_chinese(thousands) + "千" + int_to_chinese(remainder)
        else:
            # 超过 10000 的数字，保持原样
            return str(num)
    
    def number_to_chinese(match):
        """将匹配到的数字字符串转换为中文"""
        num_str = match.group(0)
        try:
            num = int(num_str)
            return int_to_chinese(num)
        except ValueError:
            return num_str
    
    # 匹配独立的数字（前后不是数字字符）
    # 匹配 1-4 位数字
    pattern = r'(?<!\d)\d{1,4}(?!\d)'
    result = re.sub(pattern, number_to_chinese, text)
    
    return result


def clone_voice_batch(
    texts: dict,
    reference_audio_path: str,
    output_dir: str,
    prompt_text: str = ""
) -> list:
    """
    批量克隆语音
    
    Args:
        texts: 文字字典 { "filename_key": "text_content" }
        reference_audio_path: 参考音频文件路径
        output_dir: 输出目录
        prompt_text: 参考音频对应的文字（可选，建议提供以提高质量）
    
    Returns:
        list: 成功生成的文件路径列表
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    if not COSYVOICE_AVAILABLE:
        print("❌ 错误: CosyVoice 未安装")
        return []
    
    successful = []
    
    # 初始化 CosyVoice CLI（文件顶部已设置路径和补丁）
    try:
        from cosyvoice.cli.cosyvoice import CosyVoice
        model_dir = "iic/CosyVoice-300M"
        cosyvoice = CosyVoice(model_dir=model_dir)
    except Exception as e:
        print(f"❌ 错误: 无法初始化 CosyVoice: {e}")
        return []
    
    for key, text in texts.items():
        filename = key if key.endswith(".wav") else f"{key}.wav"
        output_path = os.path.join(output_dir, filename)
        
        print(f"\n[{len(successful) + 1}/{len(texts)}] 处理: {filename}")
        
        try:
            import soundfile as sf
            
            # 预处理文本：将数字转换为中文读法，提高 TTS 质量
            normalized_text = normalize_numbers_in_text(text)
            normalized_prompt_text = normalize_numbers_in_text(prompt_text) if prompt_text else ""
            
            # 使用 inference_zero_shot 进行零样本语音克隆
            # 这是最稳定的方法，需要提供 prompt_text 和 prompt_wav
            # CosyVoice 会同时使用文本和音频特征进行克隆，质量更稳定
            for i, output in enumerate(cosyvoice.inference_zero_shot(
                tts_text=normalized_text,
                prompt_text=normalized_prompt_text,  # 使用数字转换后的 prompt_text
                prompt_wav=reference_audio_path,
                zero_shot_spk_id='',
                stream=False
            )):
                audio_np = output['tts_speech'].squeeze().cpu().numpy()
                sf.write(output_path, audio_np, cosyvoice.sample_rate)
                break
            
            successful.append(output_path)
            print(f"✅ 已生成: {filename}")
        except Exception as e:
            print(f"❌ 生成失败: {filename} - {str(e)}")
    
    print(f"\n🎉 批量处理完成: {len(successful)}/{len(texts)} 成功")
    return successful


def gen_voice_clips_from_json_with_clone(
    script_path: str,
    output_dir: str,
    reference_audio_path: str,
    prompt_text: str = ""
):
    """
    使用 CosyVoice 语音克隆从 JSON 脚本生成语音
    
    Args:
        script_path: JSON 脚本文件路径
        output_dir: 输出目录路径
        reference_audio_path: 参考音频文件路径（你的录音）
        prompt_text: 参考音频对应的文字（可选，建议提供以提高质量）
    """
    from .voice_edgetts import parse_json_script
    
    print(f"📄 解析脚本: {script_path}")
    scripts = parse_json_script(script_path)
    
    if not scripts:
        print("⚠️ 未找到任何口播内容，请检查 JSON 格式")
        return
    
    # 检查参考音频
    if not os.path.exists(reference_audio_path):
        print(f"❌ 错误: 参考音频文件不存在: {reference_audio_path}")
        return
    
    # 批量生成
    clone_voice_batch(
        texts=scripts,
        reference_audio_path=reference_audio_path,
        output_dir=output_dir,
        prompt_text=prompt_text
    )


def gen_voice_clips_from_json_with_clone_frank(script_path: str):
    """
    使用 frank 语音克隆从 JSON 脚本生成语音
    
    Args:
        script_path: JSON 脚本文件路径
    """
    prompt_text_path = "assets/voice/frank_enhanced.txt"
    with open(prompt_text_path, 'r', encoding='utf-8') as f:
        prompt_text = f.read().strip()
    
    output_dir = os.path.join(os.path.dirname(script_path), "voice")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    reference_audio_wav = "assets/voice/frank_enhanced.wav"
    
    gen_voice_clips_from_json_with_clone(
        script_path=script_path,
        output_dir=output_dir,
        reference_audio_path=reference_audio_wav,
        prompt_text=prompt_text
    )


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("用法:")
        print("  uv run python -m src.utils.voice_cosyvoice <function_name> [args...]")
        print("\n可用函数:")
        print("  gen_voice_clips_from_json_with_clone_frank <script_path>")
        print("    使用 frank 语音克隆从 JSON 脚本生成语音")
        print("\n示例:")
        print("  uv run python -m src.utils.voice_cosyvoice gen_voice_clips_from_json_with_clone_frank series/book_sunzibingfa/lesson13/script.json")
        sys.exit(1)
    
    function_name = sys.argv[1]
    
    if function_name == "gen_voice_clips_from_json_with_clone_frank":
        if len(sys.argv) < 3:
            print("❌ 错误: 缺少 script_path 参数")
            print("用法: uv run python -m src.utils.voice_cosyvoice gen_voice_clips_from_json_with_clone_frank <script_path>")
            sys.exit(1)
        script_path = sys.argv[2]
        gen_voice_clips_from_json_with_clone_frank(script_path)
    else:
        print(f"❌ 错误: 未知函数 '{function_name}'")
        print("可用函数: gen_voice_clips_from_json_with_clone_frank")
        sys.exit(1)

