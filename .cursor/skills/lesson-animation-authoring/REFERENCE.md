# Lesson Animation Authoring Reference

## Animation prompt asset map

| Series | Prompt asset (in adapter skill dir) | Expected base class |
|---|---|---|
| `zsxq` | `.cursor/skills/series-zsxq-adapter/prompts/zsxq_100ke_annimate.prompt` | `Zsxq100keLessonVertical` |
| `sunzi` | `.cursor/skills/series-sunzi-adapter/prompts/sunzi_annimate.prompt` | `SunziLessonVertical` |
| `moneywise` | `.cursor/skills/series-moneywise-adapter/prompts/moneywise_annimate.prompt` | `MoneyWiseLessonVertical` |

Each prompt embeds the full animate.py code template as a code block — there is no separate standalone template file.

## Shared output constraints

- Class name: `LessonNNNVerticalScenes`
- Runtime path assumptions: project root added to `sys.path`, imports from `src.animate` / `src.utils`
- Render entrypoint: `.cursor/skills/video-core-protocol/scripts/workflow.py`

## Render & status execution entrypoints

| Command surface | Path | Role |
|---|---|---|
| Shared workflow CLI | `.cursor/skills/video-core-protocol/scripts/workflow.py` | `status`, `render`, `render-all` |
| Lesson bootstrap CLI | `.cursor/skills/video-core-protocol/scripts/create_lesson.py` | Creates lesson folder and prints layered execution order |

## Runtime dependencies

This skill consumes the shared runtime owned by `video-core-protocol`. See its REFERENCE.md § "Shared runtime" for the full `src/` module list and call chain.

The key constraint: `src/animate/` and `src/utils/` modules are imported by every lesson `animate.py` at render time via Python's import system. They live in `src/` (not in a skill directory) because all 41+ lesson files use `from src.animate import ...` — moving them would break every lesson.

## Non-git asset caveats

- Icon list files (e.g. `icons_education.txt`) may be absent; icon loading degrades to fallbacks from existing `script.json`
- `series/cover/<series_name>/` may be absent; cover generation then warns and skips
- `series/bgm/<series_name>/bgm.wav` may be absent; BGM is skipped without blocking render
- Edge TTS needs network access for fresh voice generation

## Failure ownership

- Prompt structure mismatch or title/scene mapping drift: fix in the adapter's prompt asset
- Cross-series animation rule: fix in `video-core-protocol`
- Series-specific layout/color/icon convention: fix in the corresponding series adapter
