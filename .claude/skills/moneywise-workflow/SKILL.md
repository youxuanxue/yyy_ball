---
name: moneywise-workflow
description: MoneyWise global video production workflow. Converts lessons into YouTube Shorts and website content.
---

# MoneyWise Global Video Workflow

This skill automates the production of MoneyWise videos for the global audience (English).

## Runtime Configuration

Run commands from the project root (`yyy_ball` repo):

```bash
# Required for publish step
export MEDIA_PUBLISHER_DIR=/path/to/media-publisher

# Optional for website-content step
export MONEYWISE_SITE_DIR=/path/to/money-site
```

## Workflow Overview

1. **Generate Script**: Create `script.json` from source content.
2. **Generate Animation**: Create `animate.py` using Manim.
3. **Render Video**: Render video (`manim` or helper workflow script).
4. **Publish**: Upload to YouTube Shorts (`workflow.py publish`).
5. **Website Content**: Generate MDX for the MoneyWise website.

---

## Step 1: Generate script.json

**Goal**: Create the English voiceover script and scene structure.

**Inputs**:
- **Lesson Number**: `XXX` (e.g., `001`)
- **Source Content**: `assets/zsxq/jingpin_100ke_posts.json`
- **Prompt**: `series/prompts/moneywise_script.prompt`

**Instructions**:
1. Read the **Source Content** file. Search lesson `XXX` (e.g. "第XXX课").
2. Read the **Prompt** file.
3. Ensure directory exists: `series/moneywise_global/lessonXXX/`.
4. Generate `series/moneywise_global/lessonXXX/script.json`.

---

## Step 2: Generate animate.py

**Goal**: Create the Manim animation code.

**Inputs**:
- **Script**: `series/moneywise_global/lessonXXX/script.json`
- **Prompt**: `series/prompts/moneywise_annimate.prompt`

**Instructions**:
1. Read the **Script** file generated in Step 1.
2. Read the **Prompt** file.
3. Generate `series/moneywise_global/lessonXXX/animate.py`.

---

## Step 3: Render Video

**Goal**: Render the MP4 video file.

**Command (direct)**:
```bash
cd series/moneywise_global/lessonXXX
uv run manim -qh --disable_caching animate.py LessonXXXVerticalScenes; echo "Render done (exit: $?)"
```

**Command (helper script, recommended)**:
```bash
uv run python .cursor/skills/video-workflow/scripts/workflow.py --series moneywise render XXX --quality qh
```

**Note**:
- `--disable_caching` helps prevent Manim from hanging after rendering.
- Using `;` instead of `&&` ensures the echo runs regardless of exit code.
- If terminal appears stuck after "File ready at...", the video is usually ready.

**Output**:
- `series/moneywise_global/lessonXXX/media/videos/animate/1920p60/LessonXXXVerticalScenes.mp4`

---

## Step 4: Publish to YouTube Shorts

**Goal**: Upload video and get the Video ID.

**Prerequisites**:
- Credentials are available to the `media-publisher` repo.
- `MEDIA_PUBLISHER_DIR` points to the `media-publisher` directory.

**Command (recommended)**:
```bash
uv run python .cursor/skills/video-workflow/scripts/workflow.py \
  --series moneywise \
  --media-publisher-dir "$MEDIA_PUBLISHER_DIR" \
  publish XXX \
  --platform youtube \
  --privacy private
```

**Post-Condition**:
- Capture the **Video ID** from output (e.g. `dQw4w9WgXcQ`).
- OAuth may require manual confirmation in terminal/browser.

---

## Step 5: Generate Website Content (MDX)

**Goal**: Create a content page for the MoneyWise website.

**Inputs**:
- **Video ID**: From Step 4 output.
- **Video File**: `series/moneywise_global/lessonXXX/media/videos/animate/1920p60/LessonXXXVerticalScenes.mp4`
- **Script**: `series/moneywise_global/lessonXXX/script.json`
- **Template**: `$MONEYWISE_SITE_DIR/src/content/videos/_TEMPLATE.mdx.example`

**Instructions**:
1. Read **Template** and **Script**.
2. Ensure `blog.category` / `blog.tags` values match `taxonomy.ts`.
3. Create: `$MONEYWISE_SITE_DIR/src/content/videos/lessonXXX_{videoid}.mdx`.
4. Fill template fields:
   - `videoId`: ID from Step 4.
   - `title`: `script.meta.lesson_title`.
   - `description`: `script.seo.meta_description`.
   - `publishDate`: Today.
   - `duration`: Use `ffprobe` and convert to ISO-8601 `PT{M}M{S}S`.
   - `category`, `tags`, `keywords`: from `script.blog` / `script.seo`.
   - Content sections: map from `script.json` scenes.
