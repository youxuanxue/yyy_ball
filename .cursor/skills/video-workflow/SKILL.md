---
name: video-workflow
description: 日日生金（精品100课理财）和孙子兵法（小小谋略家）视频制作完整工作流。用于将内容转化为短视频并发布。使用场景：生成 script.json、生成 animate.py、渲染视频、生成微信文章、发布 YouTube Shorts。
---

# 视频制作工作流

本 Skill 用于完成两个系列的完整视频制作流程：
- **日日生金**：精品100课理财（`book_zsxq_100ke`）
- **小小谋略家**：孙子兵法启蒙（`book_sunzibingfa`）

## 工作流概览

```
1. script.json    ← 从原始素材提取内容，生成口播脚本
2. animate.py     ← 根据脚本生成 Manim 动画代码
3. video.mp4      ← 渲染动画生成视频
4. wechat.md      ← 生成微信公众号文章
5. 发布 YouTube   ← 调用 media-publisher 发布
```

## 目录结构

### 日日生金（精品100课）
```
series/book_zsxq_100ke/
├── lessonXXX/              # 3位数编号
│   ├── script.json
│   ├── animate.py
│   ├── wechat.md
│   ├── voice/
│   ├── images/
│   └── media/
```

### 孙子兵法（小小谋略家）
```
series/book_sunzibingfa/
├── lessonXX/               # 2位数编号
│   ├── origin.md           # 原始素材（孙子兵法特有）
│   ├── script.json
│   ├── animate.py
│   ├── wechat.md
│   ├── voice/
│   ├── images/
│   └── media/
```

---

# 日日生金 工作流

## Step 1: 生成 script.json

### 输入文件
| 文件 | 路径 |
|------|------|
| 原始帖子数据 | `assets/zsxq/jingpin_100ke_posts.json` |
| Prompt 模板 | `series/prompts/zsxq_100ke_script.prompt` |
| 可用图标列表 | `assets/icons8/all_png_names.txt` |

### 操作步骤
1. **读取 Prompt**：阅读 `series/prompts/zsxq_100ke_script.prompt` 获取完整指令
2. **筛选数据**：从 posts.json 中找到 `"lesson": "第XXX课"` 的帖子
3. **生成脚本**：按照 Prompt 要求生成 script.json
4. **保存文件**：保存到 `series/book_zsxq_100ke/lessonXXX/script.json`

---

## Step 2: 生成 animate.py

### 输入文件
| 文件 | 路径 |
|------|------|
| 口播脚本 | `series/book_zsxq_100ke/lessonXXX/script.json` |
| Prompt 模板 | `series/prompts/zsxq_100ke_annimate.prompt` |

### 操作步骤
1. **读取 Prompt**：阅读 `series/prompts/zsxq_100ke_annimate.prompt` 获取完整指令
2. **读取脚本**：获取 script.json 中的场景内容
3. **生成代码**：按照 Prompt 要求生成 animate.py
4. **保存文件**：保存到 `series/book_zsxq_100ke/lessonXXX/animate.py`

---

## Step 3: 渲染视频

### 命令
```bash
cd /Users/xuejiao/Codes/yyy_ball/series/book_zsxq_100ke/lessonXXX
uv run manim -qh -r 1080,1920 --fps 60 animate.py LessonXXXVerticalScenes
```

### 输出位置
```
lessonXXX/media/videos/animate/1920p60/LessonXXXVerticalScenes.mp4
```

---

# 孙子兵法 工作流

## Step 1: 生成 script.json

### 输入文件
| 文件 | 路径 |
|------|------|
| 原始素材 | `series/book_sunzibingfa/lessonXX/origin.md` |
| Prompt 模板 | `series/prompts/sunzi_script.prompt` |
| 可用图标列表 | `assets/icons8/all_png_names.txt` |

### 操作步骤
1. **读取 Prompt**：阅读 `series/prompts/sunzi_script.prompt` 获取完整指令
2. **读取素材**：阅读 `series/book_sunzibingfa/lessonXX/origin.md`
3. **生成脚本**：按照 Prompt 要求生成 script.json
4. **保存文件**：保存到 `series/book_sunzibingfa/lessonXX/script.json`

---

## Step 2: 生成 animate.py

### 输入文件
| 文件 | 路径 |
|------|------|
| 口播脚本 | `series/book_sunzibingfa/lessonXX/script.json` |
| Prompt 模板 | `series/prompts/sunzi_annimate.prompt` |

### 操作步骤
1. **读取 Prompt**：阅读 `series/prompts/sunzi_annimate.prompt` 获取完整指令
2. **读取脚本**：获取 script.json 中的场景内容
3. **生成代码**：按照 Prompt 要求生成 animate.py
4. **保存文件**：保存到 `series/book_sunzibingfa/lessonXX/animate.py`

---

## Step 3: 渲染视频

### 命令
```bash
cd /Users/xuejiao/Codes/yyy_ball/series/book_sunzibingfa/lessonXX
uv run manim -qh -r 1080,1920 --fps 60 animate.py LessonXXVerticalScenes
```

### 输出位置
```
lessonXX/media/videos/animate/1920p60/LessonXXVerticalScenes.mp4
```

---

# 通用步骤

## Step 4: 生成微信公众号文章

### 输入
- `series/book_XXX/lessonXX/script.json`：包含所有场景的口播稿

### 输出
生成 `series/book_XXX/lessonXX/wechat.md`，风格要求：
- 口语化，像朋友聊天
- 使用 `> 引用` 突出金句
- 使用 `**加粗**` 强调关键点
- 用 `---` 分隔段落

---

## Step 5: 发布到 YouTube Shorts

### 依赖项目
```
/Users/xuejiao/Codes/yyy_monkey/media-publisher
```

### 安装（首次）
```bash
cd /Users/xuejiao/Codes/yyy_monkey/media-publisher
uv pip install -e .
uv run playwright install chromium
```

### 命令行发布
```bash
cd /Users/xuejiao/Codes/yyy_monkey/media-publisher

# 发布到 YouTube（私有）
media-publisher \
    --video <视频路径> \
    --platform youtube \
    --script <script.json路径> \
    --privacy private

# 发布到微信视频号
media-publisher --video ... --platform wechat --script ...

# 同时发布两个平台
media-publisher --video ... --platform both --script ...
```

---

## 辅助脚本

### 创建课程目录
```bash
# 日日生金（3位数编号）
uv run python .cursor/skills/video-workflow/scripts/create_lesson.py --series zsxq 002

# 孙子兵法（2位数编号）
uv run python .cursor/skills/video-workflow/scripts/create_lesson.py --series sunzi 07
```

### 查看课程状态
```bash
# 日日生金
uv run python .cursor/skills/video-workflow/scripts/workflow.py --series zsxq status 002

# 孙子兵法
uv run python .cursor/skills/video-workflow/scripts/workflow.py --series sunzi status 06
```

### 渲染视频
```bash
# 日日生金
uv run python .cursor/skills/video-workflow/scripts/workflow.py --series zsxq render 002

# 孙子兵法
uv run python .cursor/skills/video-workflow/scripts/workflow.py --series sunzi render 06
```

### 发布视频
```bash
# 日日生金
uv run python .cursor/skills/video-workflow/scripts/workflow.py --series zsxq publish 002

# 孙子兵法
uv run python .cursor/skills/video-workflow/scripts/workflow.py --series sunzi publish 06
```

---

## 常见问题

### 渲染失败
- 检查 `animate.py` 语法错误
- 确保图标名称在 `all_png_names.txt` 中存在
- 避免使用 `Indicate` 动画（会导致渲染失败）

### 语音生成慢
- 首次运行会下载模型，后续使用缓存

### YouTube 发布失败
- 检查 `config/youtube_credentials.json` 是否存在
- 确保 OAuth2 重定向 URI 已配置：`http://localhost:8080/`

### 微信发布需要手动确认
- 程序会自动填写所有信息
- 最后的「发布」按钮需要人工点击

### 强制重新生成资源
```bash
FORCE_COVER=true uv run manim ...   # 重新生成封面
FORCE_VOICE=true uv run manim ...   # 重新生成语音
```
