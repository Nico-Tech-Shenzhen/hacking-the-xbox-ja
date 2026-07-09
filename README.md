# Hacking the Xbox — 非公式日本語訳

非公式日本語翻訳サイト for *Hacking the Xbox: An Introduction to Reverse Engineering*  
by Andrew "bunnie" Huang | Copyright © 2003 by Xenatera LLC | Publisher: No Starch Press

**This is an UNOFFICIAL, NONCOMMERCIAL fan translation (非公式日本語訳).**  
**Not endorsed by the author, Xenatera LLC, or No Starch Press.**

---

> **TODO (deployment):** The VitePress `base` in `docs/.vitepress/config.mts` is currently set to
> `"/hacking-the-xbox-ja/"`. If the final GitHub repository name differs, update `base` in
> `docs/.vitepress/config.mts` to match the actual repository name before deploying.

---

## Translation work guidelines

**All translation work must follow [`TRANSLATION_GUIDE.md`](TRANSLATION_GUIDE.md) and [`glossary.tsv`](glossary.tsv).**

- Before translating any chapter, read `TRANSLATION_GUIDE.md` in full.
- Before translating any technical term, check `glossary.tsv`. Add missing terms before translating.
- See `CLAUDE.md` for operational rules (AI assistant instructions).

## Setup

```bash
# 1. Install dependencies
npm install

# 2. The PDF is already at source/HackingTheXbox_Free.pdf (DO NOT re-download)

# 3. Extract text and images from the PDF
pip install pdfplumber pypdfium2 pikepdf
python3 scripts/extract_text.py
python3 scripts/extract_images.py

# 4. Copy extracted images to VitePress public dir
cp source/extract/images/* docs/public/images/

# 5. Validate links
python3 scripts/validate_links.py

# 6. Dev server
npm run docs:dev

# 7. Build
npm run docs:build
```

## GitHub Pages Deployment

A GitHub Actions workflow is included at `.github/workflows/deploy.yml`.

**Prerequisites before deployment:**
1. Create the GitHub repository (name: `hacking-the-xbox-ja` or update `base` in config)
2. Enable GitHub Pages in repo Settings → Pages → Source: GitHub Actions
3. Push to `main` branch

No remote origin is configured yet. This is a local-only repository.

## License

- **Book-derived text, images, and translations**: CC BY-NC-SA 1.0  
  Copyright © 2003 Xenatera LLC (Author: Andrew "bunnie" Huang, Publisher: No Starch Press)
- **Scripts and site config**: MIT License

See [CONTENT-LICENSE.md](CONTENT-LICENSE.md) for full details.

## Translation status

| Section | Status |
|---------|--------|
| Prologue — README.1ST | draft |
| Chapter 1 — Voiding the Warranty | draft |
| Chapters 2–13 | not started |
| Appendices A–F | not started 