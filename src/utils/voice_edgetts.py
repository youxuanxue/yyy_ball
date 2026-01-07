"""
Edge TTS 语音生成模块

提供使用 Edge TTS 生成中文语音的功能。
"""
import asyncio
import edge_tts
import os
import json


def parse_json_script(file_path):
    """
    解析 JSON 脚本，提取口播内容。
    返回字典: { "scene_index_key": "voiceover_script_content" }
    
    Args:
        file_path: JSON 脚本文件路径
    
    Returns:
        dict: 场景索引到口播脚本的映射
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


def gen_voice_clips_from_json(script_path, output_dir, voice="zh-CN-YunxiNeural"):
    """
    从 JSON 脚本生成语音的入口函数
    
    Args:
        script_path (str): JSON 脚本文件路径
        output_dir (str): 输出目录路径
        voice (str): Edge TTS 语音模型，默认为 "zh-CN-YunxiNeural" (云希)
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

