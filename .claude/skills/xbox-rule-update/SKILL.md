# Skill: xbox-rule-update

Update translation rules and/or glossary entries without touching translated content.

## When this skill is invoked

Use this skill when the user says things like:

- "ルールだけ更新" / "ルールを追加"
- "辞書に追加" / "この訳語を登録して"
- "本文は修正しない" / "再翻訳しない"
- "この訳語を今後固定したい"
- "この表現を今後避けたい"
- "preferred term for X is Y"
- "ban this phrase"
- `/xbox-rule-update figure labels must use 図N-M`
- `/xbox-rule-update commit messages must be English`
- `/xbox-rule-update errata → 正誤表 for book errata, エラッタ for technical errata`
- Any request to add, change, or remove a translation rule or glossary term

## Allowed edits — default scope

| File | Purpose |
|------|---------|
| `TRANSLATION_GUIDE.md` | Style, voice, process, formatting, and judgment rules |
| `glossary.tsv` | Stable source-term → Japanese-term mappings |

**Never edit (unless user explicitly names the file):**
- `docs/ja/*.md` — translated chapters and appendices
- `docs/.vitepress/config.mts` — VitePress config
- `docs/index.md` — homepage
- `CLAUDE.md` — operational rules
- `package-lock.json`
- Any image or extracted source file

## Decision: where does this change belong?

| Change type | Target file |
|-------------|-------------|
| Stable term mapping (English term → preferred Japanese term) | `glossary.tsv` |
| Context-dependent term with usage note | `glossary.tsv` (note column) |
| Style rule, prose pattern, or voice guideline | `TRANSLATION_GUIDE.md` |
| Formatting rule (figures, footnotes, callouts, YAML) | `TRANSLATION_GUIDE.md` |
| Process rule (workflow, checklist item) | `TRANSLATION_GUIDE.md` |
| Both a term mapping AND a prose usage rule | Both files |

**Placement rules:**
- Keep glossary entries concise. Complex prose examples and multi-sentence explanations go in `TRANSLATION_GUIDE.md`.
- Do not put long prose rules into `glossary.tsv`.
- Do not duplicate content. If a similar rule or entry already exists, **merge or strengthen** it — do not add a parallel entry.
- Keep rules short and machine-followable.

## Glossary entry format

`glossary.tsv` is tab-separated with three columns:

```
source_term	ja_term	note
```

- `source_term`: English term or phrase as it appears in the source.
- `ja_term`: Preferred Japanese rendering. For alternatives: `term A / term B`.
- `note`: Short usage guidance. Required when: (a) the rendering depends on context, (b) a common wrong rendering must be called out, or (c) first-mention rules apply. Omit if the mapping is self-evident.

**Good glossary entries:**
```
errata	正誤表	Book errata (printed corrections list) → 正誤表. Technical known-issues list → エラッタ.
workaround	回避策	Avoid ワークアラウンド.
Figure N-M	図N-M	Visible Japanese prose and captions must use 図N-M. Alt text, filenames, HTML comments, and intentional English quotations are exempt.
```

**Bad glossary entries:**
```
errata	エラッタ／正誤表	(ambiguous — no context rule)
Figure N-M	図N-M	(duplicate of existing entry without merging)
```

## Workflow

**Step 1 — Verify repo root**
```bash
cd D:\hackingthexbox && git status --short
```
Confirm you are at repo root with expected files present.

**Step 2 — Read project files (required before any edit)**
1. `CLAUDE.md` — operational rules
2. `TRANSLATION_GUIDE.md` — current rules (check for existing/similar entries)
3. `glossary.tsv` — current term mappings

**Step 3 — Determine placement**
Decide: `TRANSLATION_GUIDE.md` only / `glossary.tsv` only / both.
Search for existing entries covering the same term or rule.
If found: plan a merge or strengthening edit, not a duplicate.

**Step 4 — Edit**
Make the minimum edit needed. Do not refactor unrelated content.

For `TRANSLATION_GUIDE.md`:
- Add rules under the most relevant existing section.
- If adding a checklist item, append to the numbered list in **LLM translation checklist**.
- Write rules as short, directive sentences.

For `glossary.tsv`:
- Append new entries at the end of the file, or merge into an existing row.
- Maintain `source_term\tja_term\tnote` column structure.
- Use tabs (not spaces) between columns.
- Write files with `path.write_bytes(text.encode('utf-8'))` when scripting — never the Edit tool for `.tsv` files (to prevent encoding issues).

**Step 5 — Validate**
```bash
cd D:\hackingthexbox && python3 scripts/validate_links.py
```
Zero errors required before reporting complete.

Note: `npm run docs:build` must be run on Windows — it cannot run in the Linux sandbox.

**Step 6 — Show diff**
```bash
git status --short
git diff --stat
git diff -- TRANSLATION_GUIDE.md glossary.tsv
```

**Step 7 — Report in English**

Include:

1. **Repo root confirmed** — path and git status.
2. **Placement decision** — why TRANSLATION_GUIDE.md / glossary.tsv / both.
3. **Changes made** — file(s) changed, what was added/modified/merged.
4. **Existing entry check** — whether a similar entry existed; whether it was merged or a new entry was added.
5. **Retroactive fix needed?** — flag any translated chapters that may be affected by the new rule. Do NOT edit those chapters.
6. **Confirmation** — explicit statement that no `docs/ja/*.md` files were edited.
7. **validate_links.py result** — full output.
8. **docs:build** — remind that this must be run on Windows.
9. **PowerShell commit command:**
   ```powershell
   git add TRANSLATION_GUIDE.md glossary.tsv
   git commit -m "guide: <one-line description of the rule/term change>"
   ```

## Hard constraints

- Never retranslate chapter prose.
- Never edit `docs/ja/*.md` or any translated content file.
- Never commit or push.
- Never edit `package-lock.json`.
- Report in English.
- Do not produce a Japanese-language summary unless the user explicitly asks.
