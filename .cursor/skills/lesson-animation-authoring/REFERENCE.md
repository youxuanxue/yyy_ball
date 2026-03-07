# Lesson Animation Authoring Reference

## Animation prompt asset map

| Series | Prompt asset | Expected base class | Template source of truth |
|---|---|---|---|
| `zsxq` | `series/prompts/zsxq_100ke_annimate.prompt` | `Zsxq100keLessonVertical` | The full code template embedded inside the prompt |
| `sunzi` | `series/prompts/sunzi_annimate.prompt` | `SunziLessonVertical` | The full code template embedded inside the prompt |
| `moneywise` | `series/prompts/moneywise_annimate.prompt` | `MoneyWiseLessonVertical` | The full code template embedded inside the prompt |

## Important clarification

The Chinese animation prompts refer to `animate_template.py`, but there is currently **no tracked standalone file under `series/template/`** for that template. The large code block embedded in each prompt is the canonical template contract.

## Shared output constraints

- Class name: `LessonNNNVerticalScenes`
- Runtime path assumptions: project root added to `sys.path`, imports from `src.animate` / `src.utils`
- Render entrypoint: `.cursor/skills/video-core-protocol/scripts/workflow.py`

## Runtime source dependencies

| Src asset | Why this skill depends on it |
|---|---|
| `src/animate/__init__.py` | Unified re-export surface for lesson base classes, including `SunziLessonVertical`, `Zsxq100keLessonVertical`, and `MoneyWiseLessonVertical` |
| `src/animate/lesson_vertical.py` | Defines `SunziLessonVertical`, `Zsxq100keLessonVertical`, and `MoneyWiseLessonVertical` |
| `src/utils/anim_helper.py` | Provides `get_audio_duration()` used by all animation prompt templates |

## Failure ownership

- Prompt structure mismatch or title/scene mapping drift: fix in the prompt asset above
- Cross-series animation rule: fix in `video-core-protocol`
- Series-specific layout/color/icon convention: fix in the corresponding series adapter
