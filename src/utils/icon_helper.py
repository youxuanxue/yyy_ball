"""
Manim 图标辅助工具

提供便捷的图标创建函数，支持 SVG 和 PNG 图标
"""

from manim import *
from pathlib import Path


class IconHelper:
    """图标辅助类"""
    
    def __init__(self, project_root=None):
        """
        初始化图标辅助工具
        
        Args:
            project_root: 项目根目录，用于查找 SVG 图标文件
        """
        if project_root is None:
            # 默认从当前文件位置推断项目根目录
            current_file = Path(__file__).resolve()
            project_root = current_file.parent.parent.parent
        self.project_root = Path(project_root)
        self.icons_dir = self.project_root / "assets" / "icons"
        self.icons_dir.mkdir(parents=True, exist_ok=True)
    
    def _placeholder(self, height=2):
        """创建占位符图标"""
        return Text("?", font_size=int(height * 36), color=GRAY)
    
    def svg(self, icon_name, scale=1, color=None, **kwargs):
        """
        从 SVG 文件创建图标
        
        Args:
            icon_name: SVG 文件名（不含 .svg 扩展名）
            scale: 缩放比例
            color: 颜色
            **kwargs: 传递给 SVGMobject 的其他参数
            
        Returns:
            SVGMobject 对象
        """
        svg_path = self.icons_dir / f"{icon_name}.svg"
        
        if not svg_path.exists():
            # 如果文件不存在，返回一个占位符
            print(f"⚠️ 警告: SVG 图标文件不存在: {svg_path}")
            return self._placeholder()
        
        try:
            icon = SVGMobject(str(svg_path), **kwargs)
            icon.scale(scale)
            
            if color is not None:
                icon.set_color(color)
            
            return icon
        except Exception as e:
            print(f"⚠️ 警告: 加载 SVG 图标失败: {e}")
            return self._placeholder()
    
    def png(self, icon_name, height=2, **kwargs):
        """
        从 PNG 文件创建图标
        
        Args:
            icon_name: PNG 文件名（不含 .png 扩展名）
            height: 图标高度（Manim 单位，默认 2）
            **kwargs: 传递给 ImageMobject 的其他参数
            
        Returns:
            ImageMobject 对象
        """
        png_path = self.icons_dir / f"{icon_name}.png"
        
        if not png_path.exists():
            # 如果文件不存在，返回一个占位符
            print(f"⚠️ 警告: PNG 图标文件不存在: {png_path}")
            return self._placeholder(height)
        
        try:
            # 使用绝对路径，确保 ImageMobject 能正确加载
            abs_path = png_path.resolve()
            icon = ImageMobject(str(abs_path), **kwargs)
            icon.height = height
            return icon
        except Exception as e:
            print(f"⚠️ 警告: 加载 PNG 图标失败: {e}")
            import traceback
            traceback.print_exc()
            return self._placeholder(height)
    
    def icon(self, icon_name, icon_type="auto", **kwargs):
        """
        通用图标创建函数（智能选择）
        
        Args:
            icon_name: 图标名称
            icon_type: 图标类型，"auto" | "svg" | "png"
                      "auto" 模式会按优先级自动选择：SVG > PNG
            **kwargs: 传递给具体创建函数的参数
            
        Returns:
            Mobject 对象
        """
        if icon_type == "auto":
            # 自动选择：优先 SVG，其次 PNG
            svg_path = self.icons_dir / f"{icon_name}.svg"
            png_path = self.icons_dir / f"{icon_name}.png"
            
            if svg_path.exists():
                return self.svg(icon_name, **kwargs)
            elif png_path.exists():
                return self.png(icon_name, **kwargs)
            else:
                return self._placeholder()
        elif icon_type == "svg":
            return self.svg(icon_name, **kwargs)
        elif icon_type == "png":
            return self.png(icon_name, **kwargs)
        else:
            return self._placeholder()


# 创建全局实例（方便直接使用）
_icon_helper = None

def get_icon_helper(project_root=None):
    """获取全局图标辅助工具实例"""
    global _icon_helper
    if _icon_helper is None:
        _icon_helper = IconHelper(project_root)
    return _icon_helper


# 便捷函数
def create_icon(icon_name, icon_type="auto", **kwargs):
    """
    通用图标创建函数（智能选择）
    
    Args:
        icon_name: 图标名称
        icon_type: "auto" | "svg" | "png"
        **kwargs: 传递给具体创建函数的参数
    """
    return get_icon_helper().icon(icon_name, icon_type, **kwargs)

