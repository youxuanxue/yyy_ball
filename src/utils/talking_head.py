"""
音频驱动面部动画工具
使用 SadTalker 或其他方案生成说话头像视频
"""
import os
import sys
import subprocess
from pathlib import Path
from typing import Optional, Dict, List

# 尝试导入 SadTalker（如果已安装）
try:
    import torch
    SADTALKER_AVAILABLE = True
except ImportError:
    SADTALKER_AVAILABLE = False
    print("⚠️ 警告: PyTorch 未安装，SadTalker 功能不可用")


def check_sadtalker_installation() -> Dict[str, bool]:
    """
    检查 SadTalker 安装状态
    
    Returns:
        dict: 包含各项检查结果
    """
    checks = {
        'sadtalker_dir_exists': False,
        'checkpoints_dir_exists': False,
        'models_downloaded': False,
        'pytorch_available': SADTALKER_AVAILABLE
    }
    
    # 检查 SadTalker 目录
    sadtalker_path = Path(__file__).parent.parent.parent / "external" / "SadTalker"
    if sadtalker_path.exists():
        checks['sadtalker_dir_exists'] = True
        
        # 检查 checkpoints 目录
        checkpoints_path = sadtalker_path / "checkpoints"
        if checkpoints_path.exists():
            checks['checkpoints_dir_exists'] = True
            
            # 检查关键模型文件（支持新版本和旧版本）
            # 新版本使用 safetensors 和 .pth.tar 文件
            new_version_models = [
                "SadTalker_V0.0.2_256.safetensors",
                "SadTalker_V0.0.2_512.safetensors",
                "mapping_00109-model.pth.tar",
                "mapping_00229-model.pth.tar",
            ]
            # 旧版本使用 .pth 文件
            old_version_models = [
                "auido2exp_00300-model.pth",
                "auido2pose_00140-model.pth",
                "facevid2vid_00189-model.pth",
                "mapping_00229-model.pth",
            ]
            
            # 检查新版本模型（至少需要 safetensors 和 mapping 文件）
            new_models_found = sum(1 for model in new_version_models 
                                 if (checkpoints_path / model).exists())
            # 检查旧版本模型
            old_models_found = sum(1 for model in old_version_models 
                                 if (checkpoints_path / model).exists())
            
            # 新版本：至少需要 1 个 safetensors 和 1 个 mapping 文件
            has_safetensors = any((checkpoints_path / f"SadTalker_V0.0.2_{size}.safetensors").exists() 
                                 for size in [256, 512])
            has_mapping = any((checkpoints_path / f"mapping_{mapping}-model.pth.tar").exists() 
                            for mapping in ["00109", "00229"])
            
            # 如果新版本模型存在，或者旧版本模型存在至少 3 个，则认为已下载
            checks['models_downloaded'] = (has_safetensors and has_mapping) or (old_models_found >= 3)
    
    return checks


def print_installation_status():
    """打印 SadTalker 安装状态"""
    checks = check_sadtalker_installation()
    
    print("\n" + "=" * 80)
    print("🔍 SadTalker 安装状态检查")
    print("=" * 80)
    
    status_emoji = "✅" if checks['pytorch_available'] else "❌"
    print(f"{status_emoji} PyTorch: {'已安装' if checks['pytorch_available'] else '未安装'}")
    
    status_emoji = "✅" if checks['sadtalker_dir_exists'] else "❌"
    print(f"{status_emoji} SadTalker 目录: {'存在' if checks['sadtalker_dir_exists'] else '不存在'}")
    
    if checks['sadtalker_dir_exists']:
        status_emoji = "✅" if checks['checkpoints_dir_exists'] else "❌"
        print(f"{status_emoji} Checkpoints 目录: {'存在' if checks['checkpoints_dir_exists'] else '不存在'}")
        
        if checks['checkpoints_dir_exists']:
            status_emoji = "✅" if checks['models_downloaded'] else "⚠️"
            print(f"{status_emoji} 预训练模型: {'已下载' if checks['models_downloaded'] else '未完全下载'}")
    
    print("=" * 80)
    
    if not all(checks.values()):
        print("\n💡 安装指南:")
        print("1. 克隆 SadTalker: git clone https://github.com/OpenTalker/SadTalker.git external/SadTalker")
        print("2. 安装依赖: cd external/SadTalker && pip install -r requirements.txt")
        print("3. 下载模型: 参考 docs/talking_head_guide.md")
        print("\n详细文档: docs/talking_head_guide.md")
    
    print()


def generate_talking_head(
    image_path: str,
    audio_path: str,
    output_path: str,
    face_enhance: bool = True,
    batch_size: int = 1,
    still: bool = False,
    preprocess: str = "full",
    size: int = 512,
    pose_style: int = 0,
) -> bool:
    """
    生成说话头像视频
    
    Args:
        image_path: 人物头像图片路径
        audio_path: 音频文件路径（MP3/WAV）
        output_path: 输出视频路径
        face_enhance: 是否启用面部增强
        batch_size: 批处理大小
        still: 是否保持头部静止（仅唇形动画）
        preprocess: 预处理模式 ('full', 'crop', 'extcrop', 'resize', 'full_no_alignment')
        size: 输出视频尺寸
        pose_style: 姿势风格 (0-45)
    
    Returns:
        bool: 是否成功生成
    """
    checks = check_sadtalker_installation()
    
    if not checks['pytorch_available']:
        print("❌ 错误: PyTorch 未安装，无法生成说话头像")
        return False
    
    if not checks['sadtalker_dir_exists']:
        print("❌ 错误: SadTalker 未安装")
        print("💡 请先安装 SadTalker: git clone https://github.com/OpenTalker/SadTalker.git external/SadTalker")
        return False
    
    if not checks['models_downloaded']:
        print("⚠️ 警告: 预训练模型未完全下载，生成可能失败")
        print("💡 请参考 docs/talking_head_guide.md 下载模型")
    
    # 检查输入文件
    if not os.path.exists(image_path):
        print(f"❌ 错误: 图片文件不存在: {image_path}")
        return False
    
    if not os.path.exists(audio_path):
        print(f"❌ 错误: 音频文件不存在: {audio_path}")
        return False
    
    # 转换为绝对路径（因为会在 SadTalker 目录中执行）
    image_path = os.path.abspath(image_path)
    audio_path = os.path.abspath(audio_path)
    output_path = os.path.abspath(output_path)
    
    # 创建输出目录
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 输出目录也需要转换为绝对路径
    output_dir = os.path.abspath(output_dir)
    
    # 构建 SadTalker 命令
    sadtalker_path = Path(__file__).parent.parent.parent / "external" / "SadTalker"
    inference_script = sadtalker_path / "inference.py"
    
    if not inference_script.exists():
        print(f"❌ 错误: SadTalker inference.py 不存在: {inference_script}")
        return False
    
    # 构建命令参数
    cmd = [
        sys.executable,
        str(inference_script),
        "--driven_audio", audio_path,
        "--source_image", image_path,
        "--result_dir", output_dir,
        "--batch_size", str(batch_size),
        "--size", str(size),
        "--preprocess", preprocess,
        "--pose_style", str(pose_style),
    ]
    
    if face_enhance:
        cmd.extend(["--enhancer", "gfpgan"])
    
    if still:
        cmd.append("--still")
    
    print(f"🎬 开始生成说话头像视频...")
    print(f"📸 图片: {image_path}")
    print(f"🎵 音频: {audio_path}")
    print(f"📹 输出: {output_path}")
    print(f"⚙️  参数: face_enhance={face_enhance}, batch_size={batch_size}, size={size}")
    print()
    print("=" * 80)
    print("📊 生成进度（实时更新）")
    print("=" * 80)
    
    try:
        # 切换到 SadTalker 目录执行，实时显示输出
        import sys as sys_module
        
        # 定义阶段标识（按出现顺序）
        stage_markers = [
            ('3DMM Extraction for source image', '阶段 1/4: 3DMM 提取（人脸模型提取）'),
            ('3DMM Extraction In Video', '阶段 1/4: 3DMM 提取（处理中）'),
            ('audio2exp', '阶段 2/4: 音频到表情系数转换'),
            ('audio2pose', '阶段 2/4: 音频到姿态系数转换'),
            ('Face Renderer', '阶段 3/4: 动画生成（逐帧渲染）'),
            ('face3d rendering', '阶段 3/4: 3D 人脸渲染'),
            ('The generated video is named', '阶段 4/4: 视频编码完成'),
            ('generated video is named', '阶段 4/4: 视频编码完成'),
        ]
        
        last_stage = None
        
        def process_line(line):
            """处理输出行，识别阶段并打印"""
            nonlocal last_stage
            line_stripped = line.strip()
            
            # 检查是否是新的阶段（按顺序检查）
            for marker, stage_name in stage_markers:
                if marker in line_stripped:
                    if last_stage != stage_name:
                        print(f"\n{'='*80}")
                        print(f"📌 {stage_name}")
                        print("-" * 80)
                        last_stage = stage_name
                    break
            
            # 打印进度条和重要信息
            if line_stripped:
                # tqdm 进度条格式：100%|██████████| 100/100 [00:10<00:00, 10.00it/s]
                if '|' in line_stripped and ('%' in line_stripped or 'it/s' in line_stripped):
                    # 这是进度条，直接打印
                    print(f"  {line_stripped}")
                elif any(keyword in line_stripped for keyword in ['Extraction', 'generated', 'named', 'Error', 'Warning']):
                    # 重要信息
                    print(f"  ℹ️  {line_stripped}")
                elif line_stripped.startswith('Traceback') or 'Error' in line_stripped:
                    # 错误信息
                    print(f"  ❌ {line_stripped}")
        
        # 实时显示输出
        process = subprocess.Popen(
            cmd,
            cwd=str(sadtalker_path),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,  # 行缓冲
            universal_newlines=True
        )
        
        # 实时读取并打印输出
        output_lines = []
        for line in process.stdout:
            output_lines.append(line)
            process_line(line)
            sys_module.stdout.flush()  # 确保立即显示
        
        # 等待进程完成
        return_code = process.wait()
        
        if return_code != 0:
            # 如果失败，打印所有输出
            print("\n" + "=" * 80)
            print("❌ 生成失败，完整错误信息：")
            print("=" * 80)
            print(''.join(output_lines))
            raise subprocess.CalledProcessError(return_code, cmd, ''.join(output_lines))
        
        result = type('obj', (object,), {
            'stdout': ''.join(output_lines),
            'stderr': '',
            'returncode': return_code
        })()
        
        # SadTalker 输出文件名格式
        # 需要从输出目录中找到生成的文件
        print("\n" + "=" * 80)
        print("🔍 查找生成的视频文件...")
        print("=" * 80)
        
        generated_file = None
        
        # 查找所有可能的 .mp4 文件（包括时间戳目录中的）
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                if file.endswith('.mp4') and not file.startswith('temp_'):
                    file_path = os.path.join(root, file)
                    if generated_file is None or os.path.getmtime(file_path) > os.path.getmtime(generated_file):
                        generated_file = file_path
        
        if generated_file:
            print(f"  📹 找到视频文件: {generated_file}")
            file_size = os.path.getsize(generated_file) / (1024 * 1024)  # MB
            print(f"  📦 文件大小: {file_size:.2f} MB")
        else:
            print(f"  ⚠️  未找到 .mp4 文件")
        
        # 重命名到目标路径（如果需要）
        if generated_file and os.path.exists(generated_file) and generated_file != output_path:
            print(f"  🔄 移动文件到目标位置...")
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            if os.path.exists(output_path):
                os.remove(output_path)
            os.rename(generated_file, output_path)
            print(f"  ✅ 文件已移动到: {output_path}")
        
        if os.path.exists(output_path):
            file_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
            print(f"\n✅ 成功生成: {output_path}")
            print(f"📦 文件大小: {file_size:.2f} MB")
            return True
        else:
            print(f"\n⚠️ 警告: 未找到输出文件: {output_path}")
            print(f"💡 请检查输出目录: {output_dir}")
            
            # 列出目录中的所有文件
            if os.path.exists(output_dir):
                print(f"\n📁 输出目录中的文件:")
                for root, dirs, files in os.walk(output_dir):
                    level = root.replace(output_dir, '').count(os.sep)
                    indent = ' ' * 2 * level
                    print(f"{indent}{os.path.basename(root)}/")
                    subindent = ' ' * 2 * (level + 1)
                    for file in files[:10]:  # 只显示前10个文件
                        file_path = os.path.join(root, file)
                        if os.path.isfile(file_path):
                            size = os.path.getsize(file_path) / (1024 * 1024)
                            print(f"{subindent}- {file} ({size:.2f} MB)")
            
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ 错误: 生成失败")
        print(f"错误信息: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ 错误: {str(e)}")
        return False


def batch_generate_talking_heads(
    image_path: str,
    audio_dir: str,
    output_dir: str,
    audio_pattern: str = "*.mp3",
    face_enhance: bool = True,
    still: bool = False,
    **kwargs
) -> List[str]:
    """
    批量生成说话头像视频
    
    Args:
        image_path: 人物头像图片路径
        audio_dir: 音频文件目录
        output_dir: 输出目录
        audio_pattern: 音频文件匹配模式
        face_enhance: 是否启用面部增强
        **kwargs: 其他参数传递给 generate_talking_head
    
    Returns:
        List[str]: 成功生成的视频文件路径列表
    """
    import glob
    
    if not os.path.exists(audio_dir):
        print(f"❌ 错误: 音频目录不存在: {audio_dir}")
        return []
    
    # 查找所有音频文件
    audio_files = glob.glob(os.path.join(audio_dir, audio_pattern))
    audio_files.sort()
    
    if not audio_files:
        print(f"⚠️ 警告: 在 {audio_dir} 中未找到匹配 {audio_pattern} 的音频文件")
        return []
    
    print(f"📁 找到 {len(audio_files)} 个音频文件")
    
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    successful = []
    
    for i, audio_file in enumerate(audio_files, 1):
        audio_basename = os.path.splitext(os.path.basename(audio_file))[0]
        output_path = os.path.join(output_dir, f"{audio_basename}.mp4")
        
        print(f"\n[{i}/{len(audio_files)}] 处理: {os.path.basename(audio_file)}")
        
        if generate_talking_head(
            image_path=image_path,
            audio_path=audio_file,
            output_path=output_path,
            face_enhance=face_enhance,
            still=still,
            **kwargs
        ):
            successful.append(output_path)
    
    print(f"\n🎉 批量处理完成: {len(successful)}/{len(audio_files)} 成功")
    return successful


def get_required_materials() -> Dict[str, List[str]]:
    """
    获取所需的素材清单
    
    Returns:
        dict: 素材分类列表
    """
    return {
        "已有": [
            "✅ MP3 音频文件: series/sunzi/lesson10/voice/1.mp3"
        ],
        "需要准备": [
            "⚠️ 人物头像图片 (JPG/PNG, 512x512+, 正面人脸)",
            "📝 文字脚本 (可选，用于质量控制)"
        ],
        "需要安装": [
            "⚠️ SadTalker 代码库",
            "⚠️ PyTorch 及相关依赖",
            "⚠️ 预训练模型文件"
        ]
    }


def print_materials_checklist():
    """打印素材检查清单"""
    materials = get_required_materials()
    
    print("\n" + "=" * 80)
    print("📋 素材检查清单")
    print("=" * 80)
    
    for category, items in materials.items():
        print(f"\n【{category}】")
        for item in items:
            print(f"  {item}")
    
    print("\n" + "=" * 80)
    print("💡 详细说明请参考: docs/talking_head_guide.md")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    # 打印安装状态
    print_installation_status()
    
    # 打印素材清单
    print_materials_checklist()

