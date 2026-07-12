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
*日本語訳・レビュー*: ニコ技深圳コミュニティ / 高須正和（@tks） — [https://takasumasakazu.net](https://takasumasakazu.net) — CC BY-NC-SA 1.0<br>
*注記*: 本翻訳は、原著の Creative Commons ライセンス条件に従って公開する翻訳コントリビューションであり、著者 bunnie からも歓迎のコメントをいただいています。出版社による公式日本語版ではありません。
</small>
```

Never use the phrases "公式日本語版", "公認翻訳", or "正規翻訳".  
Do not describe the translation as "非公式日本語訳". Use "ニコ技深圳コミュニティ / 高須正和による日本語訳" in attribution credits and chapter footers. For the homepage hero title, use "日本語訳" only.

## Translation priorities

These four priorities override every specific rule below. Apply them in order when they conflict.

**1. Japanese reader clarity comes first.**  
Translate so a technically curious Japanese reader can understand the point without decoding English-shaped prose. If a literal technical term is obscure, explain the function first and add the formal term only if useful.

**2. Preserve bunnie's voice.**  
The target voice should feel like the Japanese edition of *The Hardware Hacker*: direct, practical, hands-on, hacker-oriented, essay-like, lightly conversational, and not academic. Use 「僕」 for bunnie's first-person narration. Prefer concrete verbs and short declarative sentences.

**3. Technical accuracy still matters.**  
Do not simplify by changing meaning. Preserve all technical facts, part numbers, signal names, figure/table references, commands, and source order.

**4. Translate meaning and function, not English syntax.**  
Rebuild sentences in natural Japanese. Do not carry over English noun chains, vague pronouns, hedges, or passive abstractions when they obscure the point.

## Voice target

The Japanese should sound like a working hacker explaining what he learned, not a textbook author summarizing a chapter.

- Use 「だ／だった」 prose where natural.
- Use practical verbs: いじる、つつく、たどる、探る、飛ばす、つながる、保つ、抑える。
- Replace textbook/report phrases:

| Avoid | Prefer |
|-------|--------|
| 「〜と考えることができる」 | 「〜だ」（assert directly） |
| 「〜に慰めを見出せる」 | 「〜ものだ」/「〜は救いだ」 |
| 「断続的な信頼性の問題」 | 「たまにしか再現しない不安定動作や間欠不良」 |
| 「〜に基づいて機能を推測する」 | 「〜を見て機能を推測する」 |
| 「〜することも助けになる」 | 「〜してみるといい」 |
| 「最も起きやすい問題は〜だ」 | 「〜が起きやすい」 |
| 「〜を最小化する」 | 「〜を抑える」 |
| 「エンジニアリング人材のプール」 | 「エンジニアの人材基盤」/「技術者の層」 |
| 「地下社会」（hackers） | 「アンダーグラウンドなコミュニティ」 |

## Reader-first terminology policy

Always check `glossary.tsv` first. If a term is missing, add it before translating.

**Decision rules:**
- Prefer the reader-first Japanese term from `glossary.tsv`.
- If a term is obscure for general readers, explain the function first, then give the formal term.
- **First mention pattern:** Japanese explanation + formal term + English term (if useful)
- **After first mention:** natural Japanese term, no parentheses.
- Do not overload sentences with parentheses; prefer "what it does" over literal English noun phrases.
- Add 「つまり」 or apposition only when genuinely helpful.
- If a longer translator note is needed, leave a `<!-- TODO: -->` comment.

Good (function-first + apposition): 「その配線パターンには、部品同士の接続関係、つまりネットリストがそのまま刻み込まれている。」  
Good (first-mention → subsequent): 「はんだレジスト（soldermask）と呼ばれる薄い樹脂膜が塗られており……ランドやパッドだけは、はんだレジストがかからないようになっていて、銅のパターンが露出している。」

## Translation style

### Core rules
- **Faithful**: Translate every paragraph. Do not summarize, condense, or skip content.
- **Complete**: Do not omit paragraphs, sentences, footnotes, sidebars, or captions.
- **No invented text**: If source text is unclear or garbled from PDF extraction, mark with `<!-- TODO: verify: [description] -->`. Do not fabricate.
- **Preserve order**: Keep all paragraphs in original order. Do not reorganize.
- **Consult glossary.tsv** before translating technical terms. Add missing terms before translating.
- **Katakana** for established loanwords (ハッカー, ソルダー, フラックス, etc.). Kanji compounds for native-equivalent terms where natural.

### What to preserve verbatim
- Code, assembly listings, pseudocode, shell commands
- Hexadecimal values (e.g., `0xDEADBEEF`)
- Part numbers and order numbers (e.g., `MCM order number 22-3495`)
- URLs
- Figure numbers in alt text and English source references (e.g., `Figure 1-1`, `Table 2-1`); visible Japanese labels use `図N-M` — see **Figure and caption handling** below
- Product names, company names, brand names (e.g., Xbox, Weller WTCPT, Kester 24-6337-8802)
- **Japanese-origin vs Western-origin proper nouns (game consoles, companies):**
  - Japanese-origin game consoles, game companies, and game titles: use established Japanese names in prose (ドリームキャスト, セガ, 任天堂, ソニー).
  - Xbox stays **Xbox** (not エックスボックス). Microsoft, Intel, AMD, NVIDIA: keep English.
  - PlayStation: choose one project-wide convention. Prefer **PlayStation** when product-line branding consistency matters; プレイステーション is acceptable in running prose. Document the choice in `glossary.tsv` and keep it consistent throughout.
  - If an official brand spelling is central to the technical context (e.g., an exact product model name), preserve the official English spelling.
  - If both Japanese and English forms appear across existing chapters, standardize on the glossary convention.
- US Code citations (e.g., `17 U.S.C § 1201(f)`)
- Footnote numbers (preserve as superscripts)

### Sentence construction

**Rebuild sentences; do not mirror English syntax.** When a literal translation produces stacked relative clauses, unclear pronouns, or abstract noun chains, break or rephrase.

- Split long English sentences at natural pauses. "and / but / since / while / hence" chains → separate Japanese sentences.
- **"not because A, but because B"** → 「Aだからではない。Bだからこそ……」
- **Resolve ambiguous pronouns** from context. 「その」 alone is not enough if the referent is unclear; use the explicit noun.
- **Subject clarity in long first-person sentences:** Japanese permits subject omission, but do not omit 「僕は」 when a long sentence becomes ambiguous about who is acting. In bunnie's narration, add 「僕は」 at the point where the subject shifts or the sentence becomes hard to follow without it. Goal: clarity, not minimal wording.
  - ×「何に使えるか、修理できるかどうかも分からなくても、……習慣的に集めている。」
  - ○「何に使えるか、僕は修理できるかどうかも分からなくても、……習慣的に集めている。」
- **Replace abstract noun endings with cause/effect.** Prefer 「XするとYが起きやすい」 over 「最も起きやすい問題はYだ」.
- **Avoid repeated adjacent subjects/locations.** Use 「手始めに」「次に」 or omit repeated context.
- **"secret" in security contexts** → 「秘密情報」「秘密鍵」or 「保護情報」 — never just 「秘密」.

Good (cause/effect):  
「飛ばしたコンデンサを交換せずにそのまま使うと、たまにしか再現しない不安定動作や間欠不良が起きやすい。」

Good (repeated subject removed):  
「Xboxのマザーボード上で、いくつかの信号をたどってみよう。手始めに、セクター8Cにある40ピンIDEコネクタJ8C1を見る。」

Good (security / secret):  
「安価なハードウェアクライアントに委ねられる秘密情報の重要度には、おのずと上限がある。安く大量に配布される機器を完全に守ることは難しい。だからこそ、その内部に置く秘密鍵や保護情報も、「破られたとしても許容できる範囲」に抑えるべきなのだ。」

**Word order — put context/topic first:**
- Topic/context before predicate: ×「Xを理解することはリバースエンジニアリングにおいて非常に重要だ」→ ○「リバースエンジニアリングにおいて、Xを理解することは非常に重要だ」
- Short concrete cause first: ×「ペナルティは大きくない。最適化ハードウェアが組み込まれているからだ」→ ○「最適化ハードウェアが組み込まれているから、ペナルティは大きくない」
- Adverb near what it modifies: ×「次第に多く見ていくうちに」→ ○「多く見ていくうちに、次第に」
- Fix doubled simile: ×「パイプのように水が流れるように各ステップを通過する」→ ○「パイプの中を水が流れるように各ステップを通過する」
- Cause/effect flow — put reason first when it aids readability: ×「ブートROMは極めて重要だ。初期化コードが含まれているからだ。」→ ○「ブートROMには初期化コードが含まれているから、リバースエンジニアリング上で極めて重要だ。」

### First-person pronoun
Use **「僕」** (not 「私」) for bunnie's first-person narration throughout.
- "I hack because..." → 「僕がハックするのは……」
- "my work / my research" → 「僕の仕事」 / 「僕の研究」

### Wording and phrasing

- **Person vs activity:** 「リバースエンジニア」= the person; 「リバースエンジニアリング」= the activity. ×「リバースエンジニアの次の強力なツール」→ ○「リバースエンジニアリングの次の強力なツール」
- **Flash ROM notation:** Use 「フラッシュROM」. Avoid 「FLASHロム（フラッシュROM）」 or 「FLASHスタイルのメモリ」.
- **Literal idioms and stock phrases:** Prefer concrete or natural Japanese over literal English idiom or connective phrase.
  - Generic idiom: ×「かなり遠くまで到達できる」→ ○「かなりのスキルを獲得できる」
  - "That said / having said that": ×「それを言っておいて」→ ○「言いたいことはこれだけだ」 or 「とはいえ」
  - "As with any X / like any X": ×「どんなゲームと同じく」→ ○「どんなゲームとも同じで」 / 「どんなXの場合と同じで」
  - Do not carry over English connective syntax. Find the Japanese phrase that carries the same rhetorical move.
  - **"nifty hack"**: Do not transliterate as ニッティハック。Render as 気の利いた小技, 気の利いたハック, or 小粋なハック depending on tone.
  - **Punchline / irony sentences**: When English piles up a list of examples before a punchline, split into separate Japanese sentences so the punchline lands. Do not carry English example-chains mechanically into a single Japanese sentence.
  - **Awkward English idioms (e.g. "sack of rice")**: Preserve the joke only if it can be made naturally readable in Japanese. 米袋 is acceptable when the irony is clear; rephrase or omit if the literal image causes confusion rather than humor.
- **"Aspiring X" phrasing:** Avoid 「志望するX」 as a literal rendering of "aspiring X".
  Choose Japanese that describes intention or growth path:
  - 「Xを目指す人」 / 「Xとして成長したいなら」 / 「Xになりたい人」 / 「Xとして腕を上げたい人」
  - For direct advice framing: 「Xとして成長したいなら、最も大事なアドバイスは」 (not 「志望するXへの最良のアドバイスは」)
- **Biography and profile sentences (appositive constructions):** When English uses an appositive to stack two biographical facts in one sentence (e.g. "Lee Tien, a senior staff attorney at EFF who specializes in X, also focuses on Y"), split into two natural Japanese sentences.
  - Avoid subject duplication caused by literal translation of appositive structures.
  - Translate "free speech law" as 表現の自由に関する法律, not フリースピーチ法.
  - Translate "staff attorney" as スタッフ弁護士; for "senior staff attorney" use シニアスタッフ弁護士.
  - Translate "intersection with X law" as X法との交差領域, not X法との交差点.
  - When "specializes in" would sound too repetitive in the same sentence, use 詳しい as a natural alternative.
  - Keep organization names such as Electronic Frontier Foundation in English unless a standard Japanese name is clearly established; EFF may be used after first mention.

- **Local energy (capacitors):** Do not translate "local energy" as 「ローカルエネルギー」. Explain function: 「各部品のすぐ近くで一時的に必要になる電荷を供給する」. See `glossary.tsv` entry `local energy`.
- **Resistor / energy dissipation:** Avoid 「余剰エネルギーを除去する」. Prefer 「余分なエネルギーを熱として逃がす」. See `glossary.tsv` entry `resistor removes excess energy`.
- **Bed-of-nails tester:** Explain the physical setup; do not use bare 「ベッドオブネイルズテスター」 or 「一斉に探針される」. Good: 「針山のように多数のプローブを並べた検査治具を使い、テストポイントに一斉に接触させて検査する（ベッド・オブ・ネイルズ治具）」. See `glossary.tsv` entry `bed-of-nails tester`.
- **Abbreviation first use:** Expand on first mention: Japanese term、つまり ABBR（English expansion）. After first mention: abbreviation alone. Example: 「算術論理演算装置、つまり ALU（Arithmetic Logic Unit）」→ 以後「ALU」.
- **Culturally specific hobby/event terms (swapfest, swap meet):** Explain on first mention; do not leave bare katakana without context.
  - 「swapfest」/「swap meet」: explain as 「中古・ジャンク機材が集まる交換市」 on first mention, then use 「スワップフェスト」.
  - For instruments, use the full name on first mention: 「オシロスコープ」 not 「スコープ」 alone; 「ロジックアナライザ」 not 「アナライザ」 alone.
  - Good: 「中古・ジャンク機材が集まるスワップフェストは、古いオシロスコープやロジックアナライザを安く手に入れる絶好の場所だ。」
  - Bad: 「スワップフェストは古いスコープやアナライザを安く手に入れる絶好の場所だ。」

- **Alligator clip / third hand tool:** Prefer the standard Japanese electronics term over English-derived katakana when a native term exists.
  - Use **ワニ口クリップ** for "alligator clip". Avoid 「アリゲータークリップ」 unless the source is specifically discussing the English term itself.
  - For the soldering aid with clips, use 「ワニ口クリップ付きの「第三の手」ツール」. Avoid 「アリゲータークリップ付き」.
  - General principle: if a widely used Japanese electronics term exists (e.g., ワニ口クリップ、ハンダごて、など), prefer it over a literal katakana rendering of the English.

- **Emphasis and negation:** Do not leave English emphasis words such as NOT in Japanese text. Convert them into natural Japanese. Preserve the full force of the original warning.
  - For safety instructions use 「必ず」, 「絶対に」, or 「忘れずに」 depending on severity.
  - ×「コンセントからNOT抜いてあること」→ ○「コンセントから「必ず」抜いてあること」
  - Do not mechanically carry over English emphasis markers into Japanese prose.

- **errata / workaround:**
  - Spell **エラッタ**, not エラータ. エラータ is a common mispronunciation; avoid it.
  - In running prose, prefer 不具合 or 既知の不具合 when that reads more naturally than repeating エラッタ.
  - For semiconductor or hardware specification known-bug lists, エラッタ is acceptable and standard.
  - For book correction lists (printed corrections), prefer 正誤表.
  - Prefer **回避策** over ワークアラウンド.
  - When describing ordinary user or device conditions, prefer **通常の使用条件** over 通常の動作条件 unless the technical context specifically requires the latter.

- **"signaling" in electronics contexts:**  
  Do not leave シグナリング in Japanese prose. Choose based on sentence context:
  - 「信号」 — the electrical signal itself. Example: `AGTL+信号に対応したロジックアナライザ`
  - 「信号方式」 — a category or method of digital signal transmission. Example: `信号方式は大きく二つに分けられる`
  - 「信号規格」 — a voltage/logic-level convention (AGTL+, SST-2, TTL, 3.3V CMOS). Example: `信号規格（電圧を論理値に対応付ける規格）はAGTL+と呼ばれる`
  - Never use 「信号標準」 as a literal translation of "signaling standard".
  - single-ended signaling → 「シングルエンド信号」; differential signaling → 「差動信号」
  - LVDS: expand on first use as LVDS（低電圧差動信号）. AGTL+ and SST-2: keep source ASCII spelling; AGTL+ uses ASCII `+`, not full-width ＋.
  - Blind replacement of シグナリング is a valid first pass; review each sentence individually — "signaling" sometimes means the signal itself and sometimes the convention or method.

- **Duplicated heading/title fragments (OCR/extraction artifacts):** Watch for artifacts where a heading, chapter title, or quoted title is duplicated inside itself.
  - Verify suspicious quoted titles against `source/chapter-map.json` or the source extract before changing.
  - Remove accidental duplicate fragments when fixing text. Do not invent new titles.
  - ×「第8章「XboxセキュリティのリバースエンジニアリングXboxセキュリティ」」→ ○「第8章「Xboxセキュリティのリバースエンジニアリング」」

- **Bit/byte capacity notation:** Preserve bit/byte units accurately. Do not confuse Mbit with MB.
  - On first mention of flash memory capacity, add the byte equivalent: 8Mbit（1MB）のフラッシュROM.
  - ×「8Mbitのフラッシュ」（first mention, unit unclear）→ ○「8Mbit（1MB）のフラッシュROM」
  - Never write 8MB when the source says 8Mbit. 8Mbit = 8メガビット = 1メガバイト.
  - After first mention, 8Mbit alone is acceptable when context is clear.


### Callout boxes

Source "sidebar" → heading uses **「コラム」** or **「囲み記事」**. Do **not** use 「サイドバー」 — in VitePress this sounds like site navigation.

```markdown
> **📦 コラム：なぜ基板の配線はあちこちで蛇行しているのか？**
>
> 翻訳テキスト...
```

"Note", "Tip", "Caution" callouts:
```markdown
> [!NOTE]
> 翻訳テキスト

> [!TIP]
> 翻訳テキスト

> [!WARNING]
> 翻訳テキスト
```

### YAML frontmatter

Any frontmatter value containing a colon must be quoted or written as a block scalar:
```yaml
details: >-
  翻訳・レビューはニコ技深圳コミュニティ / 高須正和（@tks）によるものです。
```
Applies to `details`, `tagline`, `description`, and any other frontmatter string field.

## Figure and caption handling

### Label notation — 図N-M vs Figure N-M

**All visible Japanese text must use `図N-M` notation.** This includes:

- Body-text references (「図8-4に示すように」)
- Bold captions below images (`**図8-4**: ...`)
- Callouts, notes, and explanation paragraphs
- Translated source references (「Figure 8-4 shows…」→「図8-4に示す...」)

**Good:**
```
図8-4に示すように
図8-4：暗号化されたデータ構造
先ほどの図8-4では
```

**Bad:**
```
Figure 8-4に示すように
Figure 8-4：暗号化されたデータ構造
先ほどのFigure 8-4では
```

**Exceptions — these three contexts may keep `Figure N-M`:**
- **Alt text** inside `![...]()` tags (accessibility / compatibility).
- **Image filenames** — must not be changed to localize labels.
- **Intentional source quotations** where the English label itself is the point; normal translated prose around the quotation must still use `図N-M`.

### Pre-completion check

Before reporting a chapter complete, run both commands and inspect every match:

```
rg "Figure [0-9]+-[0-9]+" docs/ja/chNN.md
rg "Figure [0-9]+" docs/ja/chNN.md
```

- Match in **visible Japanese prose or a caption** → convert to `図N-M` before completing.
- Match in **alt text, filename, HTML comment, or intentional quotation** → report it explicitly; no conversion needed.

### Caption format

- Translate captions into Japanese below the image tag.
- Format:
  ```markdown
  ![Figure 1-1: A selection of security bits.](/images/page-034-img-01.png)
  **図1-1**: セキュリティビットの一覧。左から右へ：任天堂4.5mm、セキュリティトルクス、...
  ```
- If the image file has not yet been extracted:
  ```markdown
  <!-- TODO: insert Figure 1-1 — source: PDF page 34 -->
  ```
- Do not guess which image file corresponds to which figure. Only link images confirmed in `source/extract/figures-manifest.json`.
- If a chapter references a figure number but no image has been extracted yet, leave the TODO comment and preserve the in-text figure reference.
- During chapter review, report all figure references that lack a corresponding extracted image file.
- **Multiple figures on the same source page (full-page renders):** When two or more figures appear on the same PDF page and the project uses a full-page render, insert the image **once** and place all captions beneath it. Do not repeat the same `![...](/images/pageNNN-render.png)` tag for each figure.
  - Use a combined alt-text: `![Figure 1-7 and Figure 1-8: ...]`
  - List captions in order: `**図1-7**: ... ` (two trailing spaces for line break) then `**図1-8**: ...`
  - Only use separate image tags if the figures have been individually cropped into separate files.

  **Bad** (same file repeated):
  ```markdown
  ![Figure 1-7](/images/page-045-render.png)
  **図1-7**: ...
  ![Figure 1-8](/images/page-045-render.png)
  **図1-8**: ...
  ```
  **Good** (single tag, both captions):
  ```markdown
  ![Figure 1-7 and Figure 1-8](/images/page-045-render.png)
  **図1-7**: ...  
  **図1-8**: ...
  ```


## Footnote handling

**Do NOT use Markdown footnote syntax** (`[^n]` / `[^n]:`). VitePress does not support it natively.

**Inline reference:**
```markdown
本文テキスト<sup>1</sup>続きのテキスト
```

**Footnote section:** add `## 注` after the last paragraph, before the `<small>` attribution footer:
```markdown
## 注

1. 原注テキスト（英語原文: "original English text"）
```

Rules: preserve original numbering; translate body text where possible; keep URLs verbatim; no HTML back-link anchors.


## URLs and Markdown links

**Never leave a bare URL directly followed by Japanese text.** VitePress auto-links bare
URLs via markdown-it linkify; if Japanese text immediately follows without a space or
terminating punctuation, the Japanese characters may be swallowed into the anchor.

Rules:
- Always use explicit Markdown link syntax: `[visible text](url)`.
- Markdown link delimiters must be ASCII `[` `]` `(` `)`, never full-width brackets.
- The link text must contain only the intended clickable text.
- Japanese particles and punctuation must stay **outside** the link.
- When the URL itself is the visible label (typical for source footnotes), use:  
  `[http://example.com](http://example.com)`
- When wrapping a URL in Japanese parentheses, place the full Markdown link inside:  
  `（[http://example.com](http://example.com)）に`  
  **not** `（http://example.com）に`
- When the URL immediately precedes Japanese text without intervening punctuation,
  the auto-linker may include Japanese characters in the anchor. Always use
  explicit `[url](url)` to prevent this.
- **`<small>` attribution footers are not exempt.** All URLs in the credit/attribution
  footer — including `https://takasumasakazu.net` — must use explicit Markdown link
  syntax. The canonical footer line is:
  ```
  *日本語訳・レビュー*: ニコ技深圳コミュニティ / 高須正和（@tks） — [https://takasumasakazu.net](https://takasumasakazu.net) — CC BY-NC-SA 1.0<br>
  ```

**Bad** (bare URL swallows following Japanese):
```markdown
論文はhttp://www.example.com/paper.pdfで見ることができる。
（http://www.xenatera.com/bunnie）に記録して
```

**Good**:
```markdown
論文は[http://www.example.com/paper.pdf](http://www.example.com/paper.pdf)で見ることができる。
（[http://www.xenatera.com/bunnie](http://www.xenatera.com/bunnie)）に記録して
```

## Credit placement

- Do not place a credit/license block directly under each chapter title. Chapter pages start with chapter content, not attribution.
- Keep credit/license information in: the site homepage footer; the credits page (`docs/credits.md`); or a single compact `<small>` footer at the end of a page if needed.
- Do not duplicate the same credit information at both the top and bottom of a chapter page.
- Do not use a blockquote-style credit zone under headings.
- Avoid visually dense one-line or multi-line credit blocks at the top of content pages.
- The canonical credit text is maintained in `TRANSLATION_GUIDE.md` and credit-related pages, not repeated prominently at the top of every chapter.

**Bad:**
```markdown
# 第6章　最高のXboxゲーム：セキュリティハッキング

> **原著**: Hacking the Xbox ...
> **著者**: Andrew "bunnie" Huang
> **著作権**: Copyright © 2003 ...
> **出版**: No Starch Press
> **本翻訳**: ニコ技深圳コミュニティ ...
```

**Good:**
```markdown
# 第6章　最高のXboxゲーム：セキュリティハッキング

本文から始める。
```

If page-level attribution is necessary, use the canonical `<small>` footer at the bottom only (see `## Attribution footer` below).

## LLM translation checklist

Before marking any section complete, verify all 22 items:

1. Japanese reader can understand the point without decoding English syntax.
2. bunnie's voice feels direct, practical, hacker-like, and essay-like.
3. 「僕」 is used for first-person narration.
4. No paragraphs, sentences, or footnotes are omitted.
5. No text is invented; unclear source is marked with a TODO comment.
6. Unclear pronouns and demonstratives are resolved to explicit nouns.
7. Technical terms follow `glossary.tsv`; apply the reader-first policy for first mention.
8. English terms are added only when useful, not for every technical noun.
9. No unnecessary katakana jargon (パラサイティクス, ブラックアート, シグナリング, etc.); see **signaling** rule under *Wording and phrasing*.
10. No stiff phrases such as 「〜と考えることができる」 when direct assertion is better.
11. No repeated adjacent subjects or locations in consecutive sentences.
12. Circuit behavior is explained by function or cause/effect, not abstract noun stacks.
13. PCB terms follow `glossary.tsv` (soldermask → はんだレジスト; trace → 配線; ビア = layer holes only).
14. Source "sidebar" headings are translated as 「コラム」 or 「囲み記事」, not 「サイドバー」.
15. Links, YAML, figures, and footnotes are valid; no mojibake or "\ufffd".
16. No bare URLs directly followed by Japanese text; all such URLs use explicit `[url](url)` Markdown syntax.
17. Abbreviations are expanded on first mention: Japanese term、つまり ABBR（English expansion）; abbreviation alone after that.
18. No English emphasis markers (NOT, ONLY, etc.) left in Japanese text; emphasis expressed with 「必ず」 or equivalent natural Japanese.
19. No duplicated heading/title fragments from OCR/extraction artifacts; quoted chapter titles verified against source/chapter-map.json.
20. Bit/byte units accurate (Mbit ≠ MB); byte equivalent added on first mention of flash capacity.
21. No credit/license blockquote under any chapter title; attribution is in the bottom `<small>` footer only.
22. No English figure labels (`Figure N-M`) in visible Japanese prose or captions; all must be `図N-M`. Verified with `rg "Figure [0-9]+-[0-9]+" docs/ja/chNN.md` — only alt text, filenames, HTML comments, and intentional quotations are exempt.
