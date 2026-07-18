---
name: xbox-crop-figures
description: Replace full-page rendered figure images with tightly cropped figure-only images for the Hacking the Xbox translation project. Use when the user asks to crop figures, fix figure crops, or apply the crop-figures workflow to a chapter or appendix.
---

# xbox-crop-figures

Reusable workflow for replacing full-page PDF page renders (`docs/public/images/page-NNN-render.png`)
with tightly cropped, figure-only images for one chapter or appendix at a time.

## Core principles

- **Crop from existing page renders, not the PDF.** Never re-extract images from
  `source/HackingTheXbox_Free.pdf` for this workflow. Source input is always an existing
  `docs/public/images/page-NNN-render.png` file.
- **Manifest-driven and deterministic.** Every crop box lives in `source/figure-crops.json`.
  Never hand-edit a cropped PNG directly - always add/update a manifest entry and regenerate
  via the script, so crop coordinates stay recorded and reproducible.
- **Tight framing.** Crop boxes must hug the actual figure/photo/diagram content. Avoid
  excessive surrounding margin (page whitespace, adjacent captions, adjacent figures).
  Derive boxes from the real content bounding area (e.g. by inspecting pixel data or by
  iterative crop-and-preview), not by eyeballing page fractions.
- **Multi-part figures = one crop.** If a single caption covers multiple sub-images on one
  page (e.g. "Figure 1-7 and Figure 1-8", or two side-by-side photos under one caption),
  crop the whole figure block as **one** combined image. Only split into separate crops if
  the source page clearly presents them as separate, independently labeled figures.
- **Never delete page renders.** Full-page render PNGs stay in place even after a figure has
  been cropped out of them - they may still be needed by other figures on the same page, or
  as a fallback.
- **Markdown paths only.** The only Markdown change is swapping the image path in the
  `![...](...)` line. Captions, figure labels, and surrounding translation prose must not
  change.

## Files touched by this workflow

**Allowed during a crop task (edit freely):**
- `source/figure-crops.json` - manifest
- `scripts/crop_figures.py` - the crop script (only if fixing a script bug)
- `docs/ja/<target>.md` - the one chapter/appendix file being processed
- `docs/public/images/figures/*.png` - generated crop outputs

**Not allowed unless the user explicitly requests it:**
- Translation prose or captions (any text other than the image path itself)
- `TRANSLATION_GUIDE.md`
- `glossary.tsv`
- `package-lock.json`
- Any config files (`docs/.vitepress/config.mts`, etc.)
- Any chapter/appendix other than the one being processed

## Step-by-step procedure

1. **Identify target and scope.** Parse the invocation for a chapter/appendix id (e.g. `ch01`,
   `appendix-b`) and optional scope:
   - `--pilot` - only process 2-3 obvious figures, don't batch the whole chapter.
   - Explicit figure ids (e.g. `fig1-1 fig1-3`) - only process those figures.
   - No scope given - process all figures currently shown as full-page renders in that file.

2. **Survey the target Markdown file.** Grep `docs/ja/<target>.md` for `render.png` to find
   every figure currently using a full-page render, and read the surrounding caption/label
   text so captions can be preserved verbatim.

3. **Determine crop boxes.** For each figure:
   - Open the relevant `page-NNN-render.png` and inspect it (visually, and/or via pixel
     thresholding) to find the tight bounding box of the actual figure content.
   - Record `source_size` (the render's actual pixel dimensions) alongside the box so future
     runs can detect a source-size mismatch.
   - For multi-part figures sharing a caption, find one box that covers the whole block.
   - Iterate: crop a test region, preview it, adjust, until the box is tight with no clipping
     and minimal margin.

4. **Update `source/figure-crops.json`.** Add or update entries. Each entry needs: `id`,
   `figure_label`, `source_render`, `source_size`, `box_type` (`pixel` or `normalized`),
   `box`, `output_image` (under `docs/public/images/figures/`), `target_markdown`, `notes`.

   After writing, validate immediately:
   ```
   python3 -c "import json; json.load(open('source/figure-crops.json')); print('valid json')"
   ```
   **Tool writes to this file have silently truncated it mid-write before.** If `Write`/`Edit`
   produces a file that fails JSON validation, or `wc -c` on the file looks suspiciously small,
   do not retry the same tool blindly - rewrite the file directly via shell heredoc or Python
   (`open(path, 'wb').write(data.encode('utf-8'))`) instead, then re-validate.

5. **Generate cropped images:**
   ```
   python scripts/crop_figures.py
   ```
   or, to limit to specific entries: `python scripts/crop_figures.py --only <id> <id> ...`.
   Confirm the script's printed output lists exactly the files expected.

6. **Update Markdown image paths.** For each figure being converted, replace only the image
   path inside its `![...](...)` line in `docs/ja/<target>.md` with the new
   `/images/figures/<id>.png` path. Leave the caption line, figure label, and all prose
   untouched. Prefer a scoped Python string replace (exact old string -> exact new string,
   asserting a count of 1) over a broad find-and-replace, to avoid accidentally touching a
   different figure that shares the same source render.

   After editing, validate immediately:
   ```
   python3 -c "open('docs/ja/<target>.md', encoding='utf-8').read(); print('valid utf-8')"
   ```
   Also check the file's tail for stray NUL bytes or truncation (`tail -c 60 <file> | xxd`).
   If corruption is found, restore from `git show HEAD:<path>` and reapply only the intended
   substitutions via direct shell/Python, not the Edit tool.

7. **Visually verify every cropped image.** Read each generated PNG under
   `docs/public/images/figures/` and visually confirm: the correct figure content is present,
   nothing is clipped, margins are minimal, and (for multi-part figures) all sub-images are
   included. Do not consider a crop done from coordinates alone.

8. **Confirm every Markdown reference.** Grep the target file for `figures/` and `render.png`
   and check that: every intended figure now points to its cropped image, every figure number
   in the path matches the figure number in the caption/label next to it, and no unrelated
   figure on the same page was accidentally repointed.

9. **Run validation:**
   ```
   python scripts/validate_links.py
   ```
   Must show zero errors before the task is considered done.

10. **Run build - Windows only.** Run `npm run docs:build` only if actually operating on
    Windows. If running in a Linux sandbox, do not attempt it - report that the user must run
    `npm run docs:build` locally on Windows to confirm the build.

11. **Report.** Use the report template below. Do not commit or push unless explicitly asked.

## Invocation examples

```
xbox-crop-figures ch01
xbox-crop-figures appendix-b
xbox-crop-figures ch08 --pilot
xbox-crop-figures ch01 fig1-1 fig1-3
```

## Report template

Report in English:

- **Target**: chapter/appendix processed
- **Figures processed**: list of figure ids/labels
- **Crop boxes added/changed**: id -> old box (if any) -> new box, with brief reason
- **Generated files**: output of `crop_figures.py`
- **Markdown image paths changed**: file + lines changed
- **Visual verification result**: pass/fail per figure, noting any clipping or margin issues found and fixed
- **Validation result**: `validate_links.py` output
- **Build result**: build output, or reason it was not run (non-Windows environment)
- **git diff --stat**
- **git diff --name-only**
- **Suggested commit command** (PowerShell, English commit message, do not run it yourself), e.g.:
  ```powershell
  git add source/figure-crops.json scripts/crop_figures.py docs/ja/ch01.md docs/public/images/figures/
  git commit -m "fix: tighten chapter 1 figure crops and add missing Figure 1-3"
  ```
