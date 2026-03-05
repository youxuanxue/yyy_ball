---
name: moneywise-workflow
description: Use this skill when the user asks to create MoneyWise videos, generate lesson content, produce YouTube Shorts, or mentions "moneywise", "lesson XXX", or video production workflow for the global/English audience.
---

# MoneyWise Global Video Workflow

This skill automates the production of MoneyWise videos for the global audience (English). It converts lessons into YouTube Shorts and website content.

## When This Skill Applies

This skill activates when the user's request involves:
- Creating MoneyWise video content
- Generating lesson scripts or animations
- Producing YouTube Shorts for MoneyWise
- Publishing videos to YouTube
- Creating MDX content for the MoneyWise website

## Workflow Overview

The complete workflow consists of 5 steps:
1. Generate Script (`script.json`)
2. Generate Animation (`animate.py`)
3. Render Video (Manim)
4. Publish to YouTube Shorts
5. Generate Website Content (MDX)

---

## Step 1: Generate script.json

**Goal**: Create the English voiceover script and scene structure.

**Inputs**:
- **Lesson Number**: `XXX` (e.g., `001`)
- **Source Content**: `/Users/xuejiao/Codes/yyy_ball/assets/zsxq/jingpin_100ke_posts.json`
- **Prompt**: `/Users/xuejiao/Codes/yyy_ball/series/prompts/moneywise_script.prompt`

**Instructions**:
1. Read the **Source Content** file. Search for the entry corresponding to Lesson `XXX` (Note: search for "第XXX课" or similar identifier).
2. Read the **Prompt** file.
3. Create directory if needed: `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/`
4. Generate `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/script.json` following the prompt's instructions.

---

## Step 2: Generate animate.py

**Goal**: Create the Manim animation code.

**Inputs**:
- **Script**: `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/script.json`
- **Prompt**: `/Users/xuejiao/Codes/yyy_ball/series/prompts/moneywise_annimate.prompt`

**Instructions**:
1. Read the **Script** file generated in Step 1.
2. Read the **Prompt** file.
3. Generate `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/animate.py`.

---

## Step 3: Render Video

**Goal**: Render the MP4 video file.

**Command**:
```bash
cd /Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX && uv run manim -qh --disable_caching animate.py LessonXXXVerticalScenes; echo "Render done (exit: $?)"
```

**Notes**:
- `--disable_caching` prevents Manim from hanging after rendering.
- Using `;` ensures the echo runs regardless of exit code.
- If terminal appears stuck after "File ready at...", the video is ready - proceed to Step 4.

**Output**:
- `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/media/videos/animate/1920p60/LessonXXXVerticalScenes.mp4`

---

## Step 4: Publish to YouTube Shorts

**Goal**: Upload video and get the Video ID.

**Prerequisites**:
- Credentials at `/Users/xuejiao/Codes/yyy_monkey/config/youtube_credentials.json`

**Command**:
```bash
cd /Users/xuejiao/Codes/yyy_monkey/media-publisher && [ -d config ] || ln -s ../config config && uv run media-publisher \
    --video "/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/media/videos/animate/1920p60/LessonXXXVerticalScenes.mp4" \
    --platform youtube \
    --script "/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/script.json" \
    --privacy private
```

**Post-Condition**:
- Capture the **Video ID** (e.g., `dQw4w9WgXcQ`) from the output.
- If the command hangs or asks for authentication, run manually in terminal to complete OAuth flow.

---

## Step 5: Generate Website Content (MDX)

**Goal**: Create a content page for the MoneyWise website.

**Inputs**:
- **Video ID**: From Step 4 output
- **Video File**: `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/media/videos/animate/1920p60/LessonXXXVerticalScenes.mp4`
- **Script**: `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/script.json`
- **Template**: `/Users/xuejiao/Codes/yyy-oversea/money-site/src/content/videos/_TEMPLATE.mdx.example`

**Instructions**:
1. Read the **Template** and **Script**.
2. Note: `blog.category` and `blog.tags` must match values in `taxonomy.ts`. Update `taxonomy.ts` first if new category/tag is needed.
3. Create file: `/Users/xuejiao/Codes/yyy-oversea/money-site/src/content/videos/lessonXXX_{videoid}.mdx`
4. Fill in template fields:
   - `videoId`: The ID from Step 4
   - `title`: From `script.meta.lesson_title`
   - `description`: From `script.seo.meta_description`
   - `publishDate`: Today's date
   - `duration`: Get via `ffprobe -v error -show_entries format=duration -of csv=p=0 {video_path}`, convert to ISO 8601 `PT{M}M{S}S`
   - `category`: From `script.blog.category`
   - `tags`: From `script.blog.tags`
   - `keywords`: From `script.seo.primary_keyword` and `script.seo.secondary_keywords`
   - **Content Sections**: Map `script.json` scenes to MDX sections per template comments
