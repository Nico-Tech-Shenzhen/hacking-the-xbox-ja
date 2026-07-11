# Translation Guide — Hacking the Xbox 日本語訳

See `CLAUDE.md` for operational rules. This guide covers substance.

## Project scope

Japanese translation of:

> *Hacking the Xbox: An Introduction to Reverse Engineering*  
> Author: Andrew "bunnie" Huang  
> Copyright © 2003 by Xenatera LLC  
> Publisher: No Starch Press, San Francisco, CA  
> Original license: Creative Commons Attribution-NonCommercial-ShareAlike 1.0 (CC BY-NC-SA 1.0)  
> Free edition release: https://nostarch.com/xboxfree

The Japanese translation is also released under **CC BY-NC-SA 1.0**.

## Attribution requirements (mandatory in every chapter file)

Every `docs/ja/*.md` file must include the following visible footer `<small>` block:

```html
<small>
*原著*: *Hacking the Xbox: An Introduction to Reverse Engineering* © 2003 Xenatera LLC<br>
*著者*: Andrew "bunnie" Huang | *出版*: No Starch Press<br>
*本翻訳*: 有志による日本語訳 — CC BY-NC-SA 1.0<br>
*翻訳*: TAKASU Masakazu（@tks） — https://takasumasakazu.net<br>
*注記*: 本翻訳は、原著の Creative Commons ライセンス条件に従って公開するコントリビューションであり、著者 bunnie からも歓迎のコメントをいただいています。出版社による公式日本語版ではありません。
</small>
```

Never use the phrases "公式日本語版", "公認翻訳", or "正規翻訳".
Do not describe the translation as "非公式日本語訳". Use "有志による日本語訳" — the author has welcomed this translation contribution.

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
- On first use of a technical term, show both Japanese and English. Example: リバースエンジニアリング (reverse engineering)
- Katakana for established loanwords (e.g., ハッカー, ソルダー, フラックス).
- Kanji compounds for native-equivalent terms where natural.
- Footnotes: use `<sup>N</sup>` in the body and a `## 注` section at the end of the file. See **Footnote handling** below.

### First-person pronoun
- Use **「僕」** (not 「私」) for bunnie's first-person narration throughout. The Prologue and hacker profiles have a personal, conversational, hacker-oriented voice. 「僕」 preserves that tone.
  - "I hack because..." → 「僕がハックするのは……」
  - "I feel..." → 「僕は……と感じている」
  - "my work / my research" → 「僕の仕事」 / 「僕の研究」

### Naturalness rules (do not over-translate English syntax)

**Split long English sentences into shorter Japanese sentences.** English subordinate clauses chained with "and", "but", "since", "while", "hence" often produce unreadable Japanese if translated clause-by-clause. Break them wherever a natural pause occurs.

**"not because A, but because B"** → translate as: 「Aだからではない。Bだからこそ……」
> Example: "not because it is an outstanding example of security, but because it is a high profile product…"
> → 「セキュリティ設計の優れた手本だったからではない。知名度が高く大量に出回る製品だったからこそ……」

**Resolve ambiguous pronouns from context.** "its chairman" → Microsoftの会長 (not XboxやXboxの議長).

**"hostile user environment"** means: a device physically in the user's hands — the user can open it, observe it, modify it, and attack it. Translate as 「ユーザーの手元という『敵対的な』環境」 with explanatory context if needed.

**"secret" in security contexts** means cryptographic keys or protected information. Translate contextually as 「秘密情報」, 「秘密鍵」, or 「保護情報」 — never literally as 「秘密」 without qualification.

**Avoid literal filler phrases:**
- "One observation is that…" → 「このことは……という示唆を与える」 or just make it a direct statement
- "The Catch-22 is that…" → 「問題はここにある。……」 or 「「鶏と卵」のジレンマがある。……」
- "Additionally," → 「さらに、」 (fine) but do not start too many consecutive sentences with transitional adverbs

**"high profile, high volume product"** → 「知名度が高く大量に出回る製品」 (not 「高知名度・大量生産品」)

**"pool of engineering talent"** → 「エンジニアの人材基盤」 or 「技術者の層」 (not 「エンジニアリング人材のプール」)

**"underground society"** (of hackers) → 「アンダーグラウンドなコミュニティ」 or 「地下コミュニティ」 (not 「地下社会」 which implies criminal underworld)

**"fiduciary interest"** in a non-legal context → 「職業的な責務として深い関心を持っている」 (not the literal 「受託的な関心」)

**"tangible artifact"** → 「物理的な成果物」 or 「手で触れられる成果物」 (not 「有形のアーティファクト」)

**Key example rewrites:**

Bad:  「Xboxの経験は、ユーザの手元にある敵対的な環境において信頼できるクライアントを構築することは——大企業であっても、潤沢な資金があっても——困難だということを示している。一つの観察として、安価で信頼できるハードウェアクライアントを構築するリスクと難しさは、そのようなクライアントハードウェアに委ねることができる秘密の重要性に上限を設けることになる。」

Good: 「Xboxの経験は、ユーザーの手元という「敵対的な」環境で信頼できるクライアントを構築することがいかに難しいかを示している。たとえ大企業であっても、資金が潤沢であっても、それは容易ではない。このことは一つの示唆を与える——安価なハードウェアクライアントに委ねられる秘密情報の重要度には、おのずと上限がある。安く大量に配布される機器を完全に守ることは難しい。だからこそ、その内部に置く秘密鍵や保護情報も、「破られたとしても許容できる範囲」に抑えるべきなのだ。」

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

**Do NOT use Markdown footnote syntax in this project.** VitePress does not support `[^n]` / `[^n]:` natively (no `markdown-it-footnote` plugin is installed), and those patterns render as literal bracketed text rather than working references.

**Inline reference:** place an HTML superscript tag at the call site in the body:

```markdown
本文テキスト<sup>1</sup>続きのテキスト
```

**Footnote section:** add a `## 注` section at the end of the file, after the last paragraph of translated text and before the `---` attribution footer. List each footnote by number:

```markdown
## 注

1. 原注テキスト（英語原文: "original English text"）
2. source: NPDFunworld
```

Rules:
- Preserve the original footnote numbering exactly. Do not renumber.
- Translate footnote body text into Japanese where possible. Keep any URLs verbatim.
- If the original footnote is a bare citation (URL or publisher name only), leaving it in English is fine.
- The `## 注` section goes after the last paragraph of body text but before the `<small>` attribution footer.
- Do not add HTML back-link anchors — they are not required and clutter the source.
