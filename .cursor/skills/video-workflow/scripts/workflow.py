#!/usr/bin/env python3
"""
视频制作工作流脚本（支持日日生金和孙子兵法两个系列）

用法:
    python workflow.py render --series zsxq 002        # 渲染日日生金第002课
    python workflow.py render --series sunzi 06        # 渲染孙子兵法第06课
    python workflow.py publish --series sunzi 06       # 发布孙子兵法到YouTube
    python workflow.py render-all --series zsxq 002 005  # 批量渲染
    python workflow.py status --series sunzi 06        # 检查课程状态
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

# 项目路径
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
MEDIA_PUBLISHER_DIR = Path.home() / "Codes" / "yyy_monkey" / "media-publisher"

# 系列配置
SERIES_CONFIG = {
    "zsxq": {
        "name": "日日生金",
        "dir": PROJECT_ROOT / "series" / "book_zsxq_100ke",
        "lesson_prefix": "lesson",
        "num_digits": 3,  # 3位数编号 (001-999)
        "class_suffix": "VerticalScenes",
    },
    "sunzi": {
        "name": "孙子兵法",
        "dir": PROJECT_ROOT / "series" / "book_sunzibingfa",
        "lesson_prefix": "lesson",
        "num_digits": 2,  # 2位数编号 (01-99)
        "class_suffix": "VerticalScenes",
    },
}


def get_series_config(series: str) -> dict:
    """获取系列配置"""
    if series not in SERIES_CONFIG:
        print(f"❌ 错误: 未知系列 '{series}'，可选: {list(SERIES_CONFIG.keys())}")
        sys.exit(1)
    return SERIES_CONFIG[series]


def get_lesson_dir(series: str, lesson_num: str) -> Path:
    """获取课程目录路径"""
    config = get_series_config(series)
    lesson_num = lesson_num.zfill(config["num_digits"])
    return config["dir"] / f"{config['lesson_prefix']}{lesson_num}"


def get_class_name(series: str, lesson_num: str) -> str:
    """获取 Manim 类名"""
    config = get_series_config(series)
    lesson_num = lesson_num.zfill(config["num_digits"])
    return f"Lesson{lesson_num}{config['class_suffix']}"


def check_lesson_status(series: str, lesson_num: str) -> dict:
    """检查课程各资源的状态"""
    config = get_series_config(series)
    lesson_dir = get_lesson_dir(series, lesson_num)
    lesson_num = lesson_num.zfill(config["num_digits"])
    
    status = {
        "series": series,
        "series_name": config["name"],
        "lesson_num": lesson_num,
        "lesson_dir": lesson_dir.exists(),
        "origin.md": (lesson_dir / "origin.md").exists() if series == "sunzi" else None,
        "script.json": (lesson_dir / "script.json").exists(),
        "animate.py": (lesson_dir / "animate.py").exists(),
        "wechat.md": (lesson_dir / "wechat.md").exists(),
        "voice": (lesson_dir / "voice").exists() and any((lesson_dir / "voice").iterdir()) if (lesson_dir / "voice").exists() else False,
        "cover": (lesson_dir / "images" / "cover_design.png").exists(),
        "video": False,
    }
    
    # 检查视频
    video_dir = lesson_dir / "media" / "videos" / "animate" / "1920p60"
    if video_dir.exists():
        videos = list(video_dir.glob("*VerticalScenes.mp4"))
        status["video"] = len(videos) > 0
        if videos:
            status["video_path"] = str(videos[0])
    
    return status


def render_lesson(series: str, lesson_num: str, force_cover: bool = False, force_voice: bool = False):
    """渲染课程视频"""
    config = get_series_config(series)
    lesson_num = lesson_num.zfill(config["num_digits"])
    lesson_dir = get_lesson_dir(series, lesson_num)
    class_name = get_class_name(series, lesson_num)
    
    if not (lesson_dir / "animate.py").exists():
        print(f"❌ 错误: {lesson_dir}/animate.py 不存在")
        return False
    
    if not (lesson_dir / "script.json").exists():
        print(f"❌ 错误: {lesson_dir}/script.json 不存在")
        return False
    
    print(f"🎬 开始渲染 [{config['name']}] 第{lesson_num}课...")
    
    # 构建环境变量
    env = {}
    if force_cover:
        env["FORCE_COVER"] = "true"
    if force_voice:
        env["FORCE_VOICE"] = "true"
    
    # 构建命令
    cmd = [
        "uv", "run", "manim",
        "-qh",  # 高质量
        "-r", "1080,1920",  # 竖屏分辨率
        "--fps", "60",  # 60帧
        "animate.py",
        class_name
    ]
    
    print(f"工作目录: {lesson_dir}")
    print(f"执行命令: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(
            cmd,
            cwd=lesson_dir,
            env={**subprocess.os.environ, **env},
            check=True
        )
        print(f"✅ [{config['name']}] 第{lesson_num}课渲染完成!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 渲染失败: {e}")
        return False


def publish_lesson(series: str, lesson_num: str, platform: str = "youtube", privacy: str = "private"):
    """发布课程视频"""
    config = get_series_config(series)
    lesson_num = lesson_num.zfill(config["num_digits"])
    status = check_lesson_status(series, lesson_num)
    
    if not status.get("video"):
        print(f"❌ 错误: 视频不存在，请先渲染")
        return False
    
    video_path = status.get("video_path")
    script_path = get_lesson_dir(series, lesson_num) / "script.json"
    
    print(f"📤 发布 [{config['name']}] 第{lesson_num}课 到 {platform}...")
    
    cmd = [
        "media-publisher",
        "--video", video_path,
        "--platform", platform,
        "--script", str(script_path),
    ]
    
    if platform in ["youtube", "both"]:
        cmd.extend(["--privacy", privacy])
    
    print(f"执行命令: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(
            cmd,
            cwd=MEDIA_PUBLISHER_DIR,
            check=True
        )
        print(f"✅ [{config['name']}] 第{lesson_num}课发布完成!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 发布失败: {e}")
        return False
    except FileNotFoundError:
        print("❌ media-publisher 命令未找到，请先安装:")
        print(f"   cd {MEDIA_PUBLISHER_DIR}")
        print("   uv pip install -e .")
        return False


def print_status(series: str, lesson_num: str):
    """打印课程状态"""
    config = get_series_config(series)
    lesson_num = lesson_num.zfill(config["num_digits"])
    status = check_lesson_status(series, lesson_num)
    
    print(f"\n📊 [{config['name']}] 第{lesson_num}课 状态:")
    print("-" * 40)
    
    items = [
        ("lesson_dir", "📁 课程目录"),
        ("script.json", "📝 脚本文件"),
        ("animate.py", "🎨 动画代码"),
        ("wechat.md", "📱 微信文章"),
        ("voice", "🎤 语音文件"),
        ("cover", "🖼️  封面图片"),
        ("video", "🎬 视频文件"),
    ]
    
    # 孙子兵法特有
    if series == "sunzi":
        items.insert(1, ("origin.md", "📄 原始素材"))
    
    for key, label in items:
        value = status.get(key)
        if value is None:
            continue
        icon = "✅" if value else "❌"
        print(f"  {icon} {label}")
    
    if status.get("video_path"):
        print(f"\n  视频路径: {status['video_path']}")
    
    print()


def main():
    parser = argparse.ArgumentParser(
        description="视频制作工作流（支持日日生金和孙子兵法）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s status --series zsxq 002        查看日日生金第002课状态
  %(prog)s status --series sunzi 06        查看孙子兵法第06课状态
  %(prog)s render --series sunzi 06        渲染孙子兵法第06课
  %(prog)s render --series zsxq 002 --force-voice  重新生成语音
  %(prog)s publish --series sunzi 06       发布到YouTube（私有）
  %(prog)s publish --series zsxq 002 --platform both --privacy public  公开发布

系列代号:
  zsxq   - 日日生金（精品100课），3位数编号
  sunzi  - 孙子兵法（小小谋略家），2位数编号
        """
    )
    
    # 全局参数
    parser.add_argument("--series", "-s", choices=["zsxq", "sunzi"], default="zsxq",
                        help="系列代号: zsxq (日日生金) 或 sunzi (孙子兵法)")
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # status 命令
    status_parser = subparsers.add_parser("status", help="检查课程状态")
    status_parser.add_argument("lesson", help="课程编号 (如 002 或 06)")
    
    # render 命令
    render_parser = subparsers.add_parser("render", help="渲染视频")
    render_parser.add_argument("lesson", help="课程编号 (如 002 或 06)")
    render_parser.add_argument("--force-cover", action="store_true", help="强制重新生成封面")
    render_parser.add_argument("--force-voice", action="store_true", help="强制重新生成语音")
    
    # render-all 命令
    render_all_parser = subparsers.add_parser("render-all", help="批量渲染")
    render_all_parser.add_argument("start", help="起始课程编号")
    render_all_parser.add_argument("end", help="结束课程编号")
    
    # publish 命令
    publish_parser = subparsers.add_parser("publish", help="发布视频")
    publish_parser.add_argument("lesson", help="课程编号 (如 002 或 06)")
    publish_parser.add_argument("--platform", choices=["youtube", "wechat", "both"], default="youtube")
    publish_parser.add_argument("--privacy", choices=["public", "unlisted", "private"], default="private")
    
    args = parser.parse_args()
    
    if args.command == "status":
        print_status(args.series, args.lesson)
    
    elif args.command == "render":
        render_lesson(args.series, args.lesson, args.force_cover, args.force_voice)
    
    elif args.command == "render-all":
        start = int(args.start)
        end = int(args.end)
        for i in range(start, end + 1):
            render_lesson(args.series, str(i))
    
    elif args.command == "publish":
        publish_lesson(args.series, args.lesson, args.platform, args.privacy)


if __name__ == "__main__":
    main()
