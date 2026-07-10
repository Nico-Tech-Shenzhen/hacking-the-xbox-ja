# CLAUDE.md — Hacking the Xbox 非公式日本語訳

## Operational rules

1. **Always read `TRANSLATION_GUIDE.md` before any translation work.**
2. **Always consult `glossary.tsv` before translating technical terms.**
3. **Work and report in English** to reduce token usage. Japanese is required only for translated content and public-facing Japanese pages (`docs/ja/`, `docs/index.md`).
4. **Never push** to any remote unless explicitly instructed by the user.
5. **Do not call a chapter complete** unless all of the following are done:
   - Source PDF text extracted and stored in `source/extract/pages/`
   - Translation written from the extracted source text (not from memory or assumptions)
   - Images extracted and referenced correctly in `docs/public/images/`
   - Figure captions translated and placed adjacent to the correct image
   - `python3 scripts/validate_links.py` passes with zero errors
   - Frontmatter fields `pdf_page_range`, `printed_page_range`, `translation_status` are accurate
6. **Do not re-state the full guide in reports.** Only report deviations from the guide, TODOs, errors, and quantitative results (page counts, image counts, validation output).
7. **The PDF is local only** at `source/HackingTheXbox_Free.pdf`. Never attempt to download it from the internet.
8. **Use pdfplumber for text extraction** and `pikepdf` or `pypdfium2` for image extraction (PyMuPDF/fitz is not installed in this environment).
