---
name: moneywise-workflow
description: MoneyWise global video production workflow. Converts lessons into YouTube Shorts and website content.
---

# MoneyWise Global Video Workflow

This skill automates the production of MoneyWise videos for the global audience (English).

## Workflow Overview

1.  **Generate Script**: Create `script.json` from source content.
2.  **Generate Animation**: Create `animate.py` using Manim.
3.  **Render Video**: Render the video using `uv run manim`.
4.  **Publish**: Upload to YouTube Shorts using `media-publisher`.
5.  **Website Content**: Generate an MDX file for the MoneyWise website.

---

## Step 1: Generate script.json

**Goal**: Create the English voiceover script and scene structure.

**Inputs**:
-   **Lesson Number**: `XXX` (e.g., `001`)
-   **Source Content**: `/Users/xuejiao/Codes/yyy_ball/assets/zsxq/jingpin_100ke_posts.json`
-   **Prompt**: `/Users/xuejiao/Codes/yyy_ball/series/prompts/moneywise_script.prompt`

**Instructions**:
1.  Read the **Source Content** file. Search for the entry corresponding to Lesson `XXX` (Note: search for "第XXX课" or similar identifier if "LessonXXX" is not found directly).
2.  Read the **Prompt** file.
3.  Generate `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/script.json` following the prompt's instructions.
    -   Ensure directory exists: `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/`

---

## Step 2: Generate animate.py

**Goal**: Create the Manim animation code.

**Inputs**:
-   **Script**: `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/script.json`
-   **Prompt**: `/Users/xuejiao/Codes/yyy_ball/series/prompts/moneywise_annimate.prompt`

**Instructions**:
1.  Read the **Script** file generated in Step 1.
2.  Read the **Prompt** file.
3.  Generate `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/animate.py`.

---

## Step 3: Render Video

**Goal**: Render the MP4 video file.

**Command**:
```bash
cd /Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX
uv run manim -qh animate.py LessonXXXVerticalScenes
```

**Output**:
-   `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/media/videos/animate/1920p60/LessonXXXVerticalScenes.mp4`

---

## Step 4: Publish to YouTube Shorts

**Goal**: Upload video and get the Video ID.

**Prerequisites**:
-   Credentials must exist at `/Users/xuejiao/Codes/yyy_monkey/config/youtube_credentials.json`.
-   If `media-publisher` fails to find credentials, create a symlink: `ln -s ../config config` inside `media-publisher` directory.

**Command**:
```bash
cd /Users/xuejiao/Codes/yyy_monkey/media-publisher

# Ensure config is accessible (create symlink if needed)
[ -d config ] || ln -s ../config config

# Publish to YouTube (Private initially)
uv run media-publisher \
    --video "/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/media/videos/animate/1920p60/LessonXXXVerticalScenes.mp4" \
    --platform youtube \
    --script "/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/script.json" \
    --privacy private
```

**Post-Condition**:
-   Capture the **Video ID** (e.g., `dQw4w9WgXcQ`) from the output.
-   If the command hangs or asks for authentication, you may need to run it manually in a terminal to complete the OAuth flow.

---

## Step 5: Generate Website Content (MDX)

**Goal**: Create a content page for the MoneyWise website.

**Inputs**:
-   **Video ID**: From Step 4 output.
-   **Video File**: `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/media/videos/animate/1920p60/LessonXXXVerticalScenes.mp4`
-   **Script**: `/Users/xuejiao/Codes/yyy_ball/series/moneywise_global/lessonXXX/script.json`
-   **Template**: `/Users/xuejiao/Codes/yyy-oversea/money-site/src/content/videos/_TEMPLATE.mdx`

**Instructions**:
1.  Read the **Template** and **Script**.
    -   Note: `blog.category` and `blog.tags` must match values in `taxonomy.ts`. If a new category/tag is needed, update `taxonomy.ts` first during Step 1.
3.  Create a new file: `/Users/xuejiao/Codes/yyy-oversea/money-site/src/content/videos/{videoid}.mdx` (replace `{videoid}` with the actual ID).
4.  Fill in the template using local files:
    -   `videoId`: The ID from Step 4 output.
    -   `title`: From script `meta.lesson_title`.
    -   `description`: From script `seo.meta_description`.
    -   `publishDate`: Today's date.
    -   `duration`: Get from video file using `ffprobe -v error -show_entries format=duration -of csv=p=0 {video_path}`, then convert to ISO 8601 format `PT{M}M{S}S`. Or estimate from script total word_count (~100 words = 60 seconds).
    -   `category`: From script `blog.category`.
    -   `tags`: From script `blog.tags` (convert to taxonomy-compatible format).
    -   `keywords`: From script `seo.primary_keyword` and `seo.secondary_keywords`.
    -   **Content Sections**: Map `script.json` scenes to the MDX sections as described in the template comments.

---
