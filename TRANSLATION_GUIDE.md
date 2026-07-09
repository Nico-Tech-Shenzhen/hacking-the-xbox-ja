# Translation Guide — Hacking the Xbox 非公式日本語訳

See `CLAUDE.md` for operational rules. This guide covers substance.

## Project scope

Unofficial Japanese translation (非公式日本語訳) of:

> *Hacking the Xbox: An Introduction to Reverse Engineering*  
> Author: Andrew "bunnie" Huang  
> Copyright © 2003 by Xenatera LLC  
> Publisher: No Starch Press, San Francisco, CA  
> Original license: Creative Commons Attribution-NonCommercial-ShareAlike 1.0 (CC BY-NC-SA 1.0)  
> Free edition release: https://nostarch.com/xboxfree

The Japanese translation is also released under **CC BY-NC-SA 1.0**.

## Attribution requirements (mandatory in every chapter file)

Every `docs/ja/*.md` file must include the following in its frontmatter AND in a visible footer block:

```
原著: Hacking the Xbox: An Introduction to Reverse Engineering
著者: Andrew "bunnie" Huang
著作権: Copyright © 2003 by Xenatera LLC
出版: No Starch Press
ライセンス: CC BY-NC-SA 1.0
本翻訳: 非公式日本語訳（unofficial Japanese translation）
```

Never use the phrases "公式日本語版", "公認翻訳", or "正規翻訳". Always use "非公式日本語訳".

## Translation style

### Core rules
- **Faithful**: Translate every paragraph. Do not summarize, condense, or skip content.
- **Complete**: Do not omit paragraphs, sentences, footnotes, sidebars, or captions.
- **No invented text**: If source text is unclear or garbled from PDF extraction, mark with a `<!-- TODO: verify: [description] -->` comment and leave a bracketed placeholder. Do not fabricate.
- **Preserve order**: Keep all paragraphs in original order. Do not reorganize.

### What to preserve verbatim (do not translate)
- Code, assembly listings, pseudocode, shell commands
- Hexadecimal values (e.g., `0xDEADBEEF`)
- Part numbers and order numbers (e.g., `MCM order number 22-3495`)
- URLs
- Figure numbers and table numbers (e.g., `Figure 1-1`, `Table 2-1`)
- Product names, company names, brand names (e.g., Xbox, Weller WTCPT, Kester 24-6337-8802)
- US Code citations (e.g., `17 U.S.C § 1201(f)`)
- Footnote numbers (preserve as superscripts or footnote markers)

### Japanese writing style
- Use natural, readable Japanese. Avoid overly literal translations that produce unnatural phrasing.
- Technical terms: consult `glossary.tsv` first. If a term is not in the glossary, add it before translating.
- On first use of a technical term, show both Japanese and English: 例） リバースエンジニアリング (reverse engineering)
- Katakana for established loanwords (e.g., ハッカー, ソルダー, フラックス).
- Kanji compounds for native-equivalent terms where natural.
- Footnotes: use `<sup>N</sup>` in the body and a `## 注` section at the end of the file. See **Footnote handling** below.

### Sidebars and callout boxes
VitePress does not have a native sidebar container, so use a blockquote with a bold heading:

```markdown
> **📦 サイドバー: 静電気：回路の天敵 (Static Electricity: The Circuit Killer)**
>
> 翻訳テキスト...
```

### Notes and tips
Preserve "Note" and "Tip" callouts as:
```markdown
> [!NOTE]
> 翻訳テキスト

> [!TIP]
> 翻訳テキスト
```

## Figure and caption handling

- Preserve every figure number exactly as printed: **Figure 1-1**, **Figure 2-3**, etc.
- Translate captions into Japanese below the image tag.
- Format:
  ```markdown
  ![Figure 1-1: A selection of security bits.](/images/page-034-img-01.png)
  **図1-1**: セキュリティビットの一覧。左から右へ：任天堂4.5mm、セキュリティトルクス、...
  ```
- If the image file has not yet been extracted, use this placeholder:
  ```markdown
  <!-- TODO: insert Figure 1-1 — source: PDF page 34 -->
  ```
- Do not guess which image file corresponds to which figure. Only link images confirmed in `source/extract/figures-manifest.json`.

## Footnote handling

**Do NOT use Markdown footnote syntax in this project.** VitePress does not support `[^n]` / `[^n]:` natively (no `markdown-it-footnote` plugin is installed), and both patterns create dead links that break the build.

Forbidden patterns:
- `[^1]` inline reference → **breaks build**
- `[^1]: note text` definition → **breaks build**
- `[3](note text)` link-style → **breaks build**

Correct format:

In the body, mark the footnote call with an HTML superscript:
```markdown
本文テキスト<sup>1</sup>続きのテキスト
```

At the end of the file, before the `---` footer, add a `## 注` section with plain numbered lines:
```markdown
## 注

1. 原注テキスト (英語原文: "original English text")
2. source: NPDFunworld
```

Always include the original English text in parentheses after the Japanese translation.

## TODO handling

Use HTML comments so they are invisible to readers but visible in source:

```markdown
<!-- TODO: verify: paragraph unclear due to PDF extraction artifact -->
<!-- TODO: figure: Figure 3-2 — confirm image file from manifest -->
<!-- TODO: footnote: footnote 4 text garbled on PDF page 23 -->
```

Never delete a TODO without completing the underlying check against the source PDF.

## Chapter frontmatter requirements

Every `docs/ja/*.md` must begin with:

```yaml
---
title: "第N章：日本語タイトル"
original_title: "Chapter N: English Title"
author: 'Andrew "bunnie" Huang'
copyright: "Copyright © 2003 by Xenatera LLC"
publisher: "No Starch Press"
source_pdf: "HackingTheXbox_Free.pdf"
pdf_page_range: "pp. XX–YY"
printed_page_range: "pp. XX–YY"
translation_status: draft  # draft | review | verified | final
license: "CC BY-NC-SA 1.0"
---
```

`pdf_page_range` = actual PDF page numbers (1-indexed).  
`printed_page_range` = page numbers printed in the book.

## Review checklist before marking a chapter complete

Before changing `translation_status` from `draft` to `review`:

- [ ] Every paragraph from the source PDF is present in the translation
- [ ] No paragraphs are summarized or condensed
- [ ] All figure numbers are preserved; all extracted figures are linked or TODO-marked
- [ ] All footnotes are translated and placed at end of file
- [ ] All sidebars and callout boxes are preserved
- [ ] All part numbers, URLs, hex values, code blocks are verbatim
- [ ] All technical terms match `glossary.tsv`
- [ ] Frontmatter `pdf_page_range` and `printed_page_range` are accurate
- [ ] Attribution block is present in footer
- [ ] `python3 scripts/validate_links.py` passes with zero errors
- [ ] No `<!-- TODO -->` comments remain that relate to missing content (placement TODOs for uncertain figure positions are acceptable)

## Chapter map (confirmed from PDF TOC)

| ID | English title | Printed pages | PDF pages |
|----|---------------|---------------|-----------|
| prologue | Prologue — README.1ST | 1–14 | 19–32 |
| ch01 | Chapter 1 — Voiding the Warranty | 15–31 | 33–50 |
| ch02 | Chapter 2 — Thinking Inside the Box | 33–51 | 51–70 |
| ch03 | Chapter 3 — Installing a Blue LED | 53–65 | 71–84 |
| ch04 | Chapter 4 — Building a USB Adapter | 67–72 | 85–92 |
| ch05 | Chapter 5 — Replacing a Broken Power Supply | 73–88 | 93–108 |
| ch06 | Chapter 6 — The Best Xbox Game: Security Hacking | 89–102 | 107–120 |
| ch07 | Chapter 7 — A Brief Primer on Security | 103–120 | 121–138 |
| ch08 | Chapter 8 — Reverse Engineering Xbox Security | 121–138 | 139–156 |
| ch09 | Chapter 9 — Sneaking in the Back Door | 139–150 | 157–170 |
| ch10 | Chapter 10 — More Hardware Projects | 151–162 | 171–180 |
| ch11 | Chapter 11 — Developing Software for the Xbox | 163–174 | 181–192 |
| ch12 | Chapter 12 — Caveat Hacker | 1