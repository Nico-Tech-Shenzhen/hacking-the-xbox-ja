Update translation rules in `TRANSLATION_GUIDE.md` and/or glossary entries in `glossary.tsv`.
Never edit translated chapter content. Never retranslate.

**Argument:** free-form description of the rule or term change. Examples:
- `errata should be 正誤表 for book errata, エラッタ for technical errata`
- `workaround should be 回避策, not ワークアラウンド`
- `visible Figure N-M must be 図N-M in Japanese prose and captions`
- `operational reports and commit messages must be English`

Also triggered by Japanese phrases such as:
- ルールだけ更新 / ルールを追加
- 辞書に追加 / この訳語を登録して
- 本文は修正しない / 再翻訳しない
- この訳語を今後固定したい / この表現を今後避けたい

**Instructions:**
1. Read `.claude/skills/xbox-rule-update/SKILL.md` for the full procedure.
2. Follow `CLAUDE.md` operational rules.
3. Edit **only** `TRANSLATION_GUIDE.md` and/or `glossary.tsv` (unless user explicitly names another file).
   - Stable term mappings → `glossary.tsv`
   - Style / process / prose rules → `TRANSLATION_GUIDE.md`
   - Both a term and a usage rule → both files
4. Check for existing entries first. Merge or strengthen; do not duplicate.
5. **Never** edit `docs/ja/*.md` or any translated chapter/appendix file.
6. **Never** retranslate.
7. Run `python3 scripts/validate_links.py` and include the full output in your report.
8. Show `git diff -- TRANSLATION_GUIDE.md glossary.tsv`.
9. Report in **English**: what changed, placement rationale, retroactive-fix flags (if any),
   confirmation that no chapter files were edited, validation result, and the PowerShell commit command.
