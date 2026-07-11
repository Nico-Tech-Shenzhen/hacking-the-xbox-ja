# Hacking the Xbox — 日本語訳

公開サイトはこちら：  
**https://nico-tech-shenzhen.github.io/hacking-the-xbox-ja/**

This repository hosts a Japanese translation of Andrew "bunnie" Huang's *Hacking the Xbox*, published under CC BY-NC-SA 1.0.
The author has confirmed that translation is allowed under the Creative Commons license.
This is not a publisher-issued official Japanese edition.
Translation: ニコ技深圳コミュニティ / 高須正和 / TAKASU Masakazu（@tks） — https://takasumasakazu.net

読むだけなら、npm install やローカルビルドは不要です。  
GitHub Pages の公開サイトを開けば、そのまま読めます。

---

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
| Appendices A–F | not started |

---

## Development / 翻訳・開発者向け

**All translation work must follow [`TRANSLATION_GUIDE.md`](TRANSLATION_GUIDE.md) and [`glossary.tsv`](glossary.tsv).**

- Before translating any chapter, read `TRANSLATION_GUIDE.md` in full.
- Before translating any technical term, check `glossary.tsv`. Add missing terms before translating.
- See `CLAUDE.md` for operational rules (AI assistant instructions).

### Local setup

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

### GitHub Pages deployment

A GitHub Actions workflow is at `.github/workflows/deploy.yml`. It runs automatically on every push to `main`.

To enable GitHub Pages: repo Settings → Pages → Source: GitHub Actions.
