#!/usr/bin/env python3
"""
scripts/build_book.py

Reproducible EPUB/PDF build pipeline for the "Hacking the Xbox" Japanese
translation (VitePress site).

Pipeline:
  1. Read the ordered list of docs/ja/*.md files (BOOK_ORDER below).
  2. Strip YAML frontmatter from each file.
  3. Strip the repeated per-page "<small>...</small>" credit footer from
     each file (it is re-added once, at the very end of the manuscript).
  4. Rewrite "/images/..." absolute site paths to portable *relative* paths
     ("images/...") and copy every referenced image from
     docs/public/images/... into dist/book/images/... (preserving
     subdirectories), so Pandoc/Typst can resolve them without ever seeing
     an absolute filesystem path. This avoids the duplicated-path bug where
     an absolute path baked into the manuscript gets re-joined with a CWD
     by Typst (e.g. on GitHub Actions runners), producing nonsense paths
     like ".../home/runner/work/.../docs/public/images/foo.png".
  5. Concatenate everything (in book order) into a single manuscript at
     dist/book/manuscript.md.
  6. Append a single combined license/credits section at the end, sourced
     from docs/license.md and docs/credits.md.
  7. Optionally invoke Pandoc to produce:
       - docs/public/downloads/hacking-the-xbox-ja.epub
       - docs/public/downloads/hacking-the-xbox-ja.pdf
     Pandoc is run with cwd=dist/book so the relative "images/..." paths in
     manuscript.md resolve correctly; outputs are written back out to
     docs/public/downloads/ via a relative "../../docs/public/downloads/..."
     path. PDF engine preference order: typst > xelatex > (HTML+Playwright/
     Chromium fallback, printed to PDF). Every Pandoc invocation reads with
     `--from markdown-citations` (citations extension disabled) so plain
     text handles like "@tks" in the credits section are never parsed as
     Pandoc citation keys -- see CITELESS_MARKDOWN below for why.

Usage:
    python3 scripts/build_book.py --prepare   # build manuscript only
    python3 scripts/build_book.py --epub      # prepare + build EPUB
    python3 scripts/build_book.py --pdf       # prepare + build PDF
    python3 scripts/build_book.py --all       # prepare + EPUB + PDF

This script never edits files under docs/ja/ — it only reads them and
writes a derived manuscript under dist/book/ and (optionally) binary
outputs under docs/public/downloads/.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
JA_DIR = DOCS_DIR / "ja"
PUBLIC_DIR = DOCS_DIR / "public"
DOWNLOADS_DIR = PUBLIC_DIR / "downloads"
BUILD_DIR = REPO_ROOT / "dist" / "book"
BUILD_IMAGES_DIR = BUILD_DIR / "images"
MANUSCRIPT_PATH = BUILD_DIR / "manuscript.md"
BOOK_CSS = REPO_ROOT / "scripts" / "book.css"
SOURCE_IMAGES_DIR = PUBLIC_DIR / "images"

EPUB_OUT = DOWNLOADS_DIR / "hacking-the-xbox-ja.epub"
PDF_OUT = DOWNLOADS_DIR / "hacking-the-xbox-ja.pdf"

# Relative path from BUILD_DIR (pandoc's cwd) back to DOWNLOADS_DIR, used so
# pandoc's -o argument never contains an absolute path either.
EPUB_OUT_REL = Path("..") / ".." / "docs" / "public" / "downloads" / "hacking-the-xbox-ja.epub"
PDF_OUT_REL = Path("..") / ".." / "docs" / "public" / "downloads" / "hacking-the-xbox-ja.pdf"

BOOK_TITLE = "Hacking the Xbox 日本語訳"

# The manuscript does not use Pandoc citations (no [@key] bibliography
# syntax anywhere in the book). Disable the "citations" Markdown extension
# on input so that plain-text social handles like "@tks" in the credits
# section are passed through as literal text instead of being parsed as
# citation keys. Without this, Pandoc rewrites "@tks" into a citation node,
# which the Typst PDF engine then renders as `#cite("tks")` -- a bare
# identifier Typst can't resolve (no bibliography exists), and Typst aborts
# with "expected label, found string". Applied to every Pandoc invocation
# used for book generation (EPUB, Typst PDF, xelatex PDF, HTML/Playwright).
CITELESS_MARKDOWN = "markdown-citations"

# Explicit book order (mirrors docs/.vitepress/config.mts sidebar order).
BOOK_ORDER = [
    "dear-reader",
    "acknowledgments",
    "prologue",
    "ch01", "ch02", "ch03", "ch04", "ch05", "ch06", "ch07",
    "ch08", "ch09", "ch10", "ch11", "ch12", "ch13",
    "appendix-a", "appendix-b", "appendix-c",
    "appendix-d", "appendix-e", "appendix-f",
]

# Non-/ja files appended once at the very end as a single combined
# license/credits section (instead of repeating the per-chapter footer).
CREDIT_SOURCE_FILES = [
    DOCS_DIR / "license.md",
    DOCS_DIR / "credits.md",
]

FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)

# Matches the canonical per-page footer:
#   ---
#
#   <small>
#   ...
#   </small>
# only when it appears at the very end of the file (trailing whitespace ok).
FOOTER_RE = re.compile(
    r"\n+(?:---\n+)?<small>.*?</small>\s*\Z", re.DOTALL
)

IMG_ABS_RE = re.compile(r'(!\[[^\]]*\]\()/images/([^)\s]+)((?:\s+"[^"]*")?\))')


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1).lstrip("\n")


def strip_footer(text: str) -> str:
    """Remove the trailing per-page <small>...</small> credit block, if present."""
    return FOOTER_RE.sub("", text)


def rewrite_image_paths(text: str, source_file: Path) -> str:
    """Rewrite `/images/...` (VitePress public-dir absolute site paths) to
    portable *relative* paths ("images/...") and copy the referenced image
    from docs/public/images/... into dist/book/images/... (preserving any
    subdirectory structure, e.g. images/figures/ch01-fig1-1.png).

    Never emits an absolute filesystem path into the manuscript -- that was
    the root cause of the Pandoc+Typst "duplicated path" failure on CI,
    where an absolute path baked into the manuscript got re-joined with
    Typst's own working directory.
    """

    def replace(m: re.Match) -> str:
        prefix, rel_path, suffix = m.group(1), m.group(2), m.group(3)
        src = (SOURCE_IMAGES_DIR / rel_path).resolve()
        if not src.is_file():
            raise FileNotFoundError(
                "[build_book] Missing image referenced by the manuscript.\n"
                f"  Source markdown file : {source_file}\n"
                f"  Original image path  : /images/{rel_path}\n"
                f"  Expected source path : {src}\n"
                "  Fix: extract/add the missing image under docs/public/images/, "
                "or correct the reference in the source Markdown file."
            )
        dest = (BUILD_IMAGES_DIR / rel_path).resolve()
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        # Always emit forward slashes -- Pandoc/Typst accept them on every
        # platform, and it keeps the manuscript free of backslashes that
        # Markdown could misinterpret as escapes.
        rel_ref = f"images/{rel_path}".replace("\\", "/")
        return f"{prefix}{rel_ref}{suffix}"

    return IMG_ABS_RE.sub(replace, text)


def load_section(slug: str) -> str:
    path = JA_DIR / f"{slug}.md"
    if not path.exists():
        raise FileNotFoundError(f"Expected book section not found: {path}")
    text = path.read_text(encoding="utf-8")
    text = strip_frontmatter(text)
    text = strip_footer(text)
    text = rewrite_image_paths(text, source_file=path)
    return text.strip() + "\n"


def load_credits_section() -> str:
    """Build a single combined license/credits section from docs/license.md
    and docs/credits.md, appended once at the end of the manuscript instead
    of repeating the per-chapter footer block."""
    parts = []
    for path in CREDIT_SOURCE_FILES:
        if not path.exists():
            print(f"[build_book] WARNING: credits source missing: {path}", file=sys.stderr)
            continue
        text = path.read_text(encoding="utf-8")
        text = strip_frontmatter(text)
        text = rewrite_image_paths(text, source_file=path)
        parts.append(text.strip() + "\n")
    return "\n\n---\n\n".join(parts)


def build_manuscript() -> Path:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    # Start each build from a clean images/ dir so stale/renamed images from
    # a previous run never linger and get bundled by mistake.
    if BUILD_IMAGES_DIR.exists():
        shutil.rmtree(BUILD_IMAGES_DIR)
    BUILD_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    sections = [load_section(slug) for slug in BOOK_ORDER]

    credits = load_credits_section()
    if credits:
        sections.append("# ライセンスとクレジット\n\n" + credits)

    manuscript = "\n\n---\n\n".join(sections) + "\n"
    MANUSCRIPT_PATH.write_text(manuscript, encoding="utf-8")

    n_words = len(manuscript)
    print(f"[build_book] Wrote manuscript: {MANUSCRIPT_PATH} ({n_words} chars, {len(sections)} sections)")
    return MANUSCRIPT_PATH


def which(cmd: str) -> str | None:
    return shutil.which(cmd)


def run(cmd: list[str], cwd: Path = REPO_ROOT) -> None:
    print(f"[build_book] $ {' '.join(cmd)}  (cwd={cwd})")
    subprocess.run(cmd, check=True, cwd=cwd)


def build_epub() -> bool:
    if not which("pandoc"):
        print("[build_book] SKIPPED EPUB: 'pandoc' not found on PATH.")
        print("  Install on Windows:  winget install --id JohnMacFarlane.Pandoc")
        return False

    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
    # Run from BUILD_DIR (dist/book) with a bare "manuscript.md" input and a
    # relative "../../docs/public/downloads/..." output, so pandoc/pandoc's
    # resource-resolution never has to deal with an absolute path and the
    # manuscript's relative "images/..." references resolve against
    # dist/book/images/ as expected.
    cmd = [
        "pandoc", "manuscript.md",
        "-o", str(EPUB_OUT_REL.as_posix()),
        "--from", CITELESS_MARKDOWN,
        "--toc", "--toc-depth=2",
        "--metadata", "lang=ja-JP",
        "--metadata", f"title={BOOK_TITLE}",
    ]
    if BOOK_CSS.exists():
        cmd += ["--css", str(BOOK_CSS.resolve())]
    run(cmd, cwd=BUILD_DIR)
    print(f"[build_book] EPUB written: {EPUB_OUT}")
    return True


def build_pdf() -> bool:
    if not which("pandoc"):
        print("[build_book] SKIPPED PDF: 'pandoc' not found on PATH.")
        print("  Install on Windows:  winget install --id JohnMacFarlane.Pandoc")
        return False

    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)

    if which("typst"):
        cmd = [
            "pandoc", "manuscript.md",
            "-o", str(PDF_OUT_REL.as_posix()),
            "--from", CITELESS_MARKDOWN,
            "--toc", "--toc-depth=2",
            "--pdf-engine=typst",
            "-V", "mainfont=Noto Serif CJK JP",
            "--metadata", "lang=ja-JP",
            "--metadata", f"title={BOOK_TITLE}",
        ]
        run(cmd, cwd=BUILD_DIR)
        print(f"[build_book] PDF written via Pandoc+Typst: {PDF_OUT}")
        return True

    if which("xelatex"):
        print("[build_book] 'typst' not found; falling back to Pandoc+xelatex "
              "(Noto CJK fonts detected on this system).")
        # NOTE: deliberately do NOT pass `-V CJKmainfont=...` or
        # `--metadata lang=ja...` here. On this build image, xeCJK pulls in
        # ctexhook.sty (part of the `ctex` CTAN bundle, not installed and
        # not installable without root in this sandbox), and Polyglossia
        # has no working `japanese` language definition, so
        # `\setmainlanguage{japanese}` aborts the LaTeX run. Plain
        # `fontspec` + `mainfont` renders Japanese correctly under XeTeX
        # without either package (verified against a sample chapter).
        # If your local TeX Live/MiKTeX has the `ctex` bundle and
        # polyglossia's Japanese support installed, CJKmainfont/lang can be
        # re-added for nicer CJK line-breaking.
        cmd = [
            "pandoc", "manuscript.md",
            "-o", str(PDF_OUT_REL.as_posix()),
            "--from", CITELESS_MARKDOWN,
            "--toc", "--toc-depth=2",
            "--pdf-engine=xelatex",
            "-V", "mainfont=Noto Serif CJK JP",
            "-V", "geometry:margin=1in",
            "--metadata", f"title={BOOK_TITLE}",
        ]
        try:
            run(cmd, cwd=BUILD_DIR)
        except subprocess.CalledProcessError:
            print("[build_book] Pandoc+xelatex failed. Falling back to HTML+Playwright route.")
        else:
            print(f"[build_book] PDF written via Pandoc+xelatex: {PDF_OUT}")
            return True

    return build_pdf_via_playwright()


def build_pdf_via_playwright() -> bool:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError:
        print("[build_book] SKIPPED PDF: no working PDF engine found.")
        print("  Neither 'typst' nor 'xelatex' produced a PDF, and the")
        print("  'playwright' Python package (HTML->PDF fallback) is not installed.")
        print("  Install one of the following on Windows:")
        print("    winget install --id typst.typst          # preferred (best CJK support)")
        print("    (xelatex ships with a full TeX Live / MiKTeX install)")
        print("    pip install playwright && playwright install chromium")
        return False

    if not which("pandoc"):
        return False

    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
    html_out = BUILD_DIR / "manuscript.html"
    cmd = [
        "pandoc", "manuscript.md",
        "-o", "manuscript.html",
        "--from", CITELESS_MARKDOWN,
        "--toc", "--toc-depth=2",
        "--standalone",
        "--metadata", "lang=ja-JP",
        "--metadata", f"title={BOOK_TITLE}",
    ]
    if BOOK_CSS.exists():
        cmd += ["--css", str(BOOK_CSS.resolve())]
    run(cmd, cwd=BUILD_DIR)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_out.resolve().as_uri())
        page.pdf(path=str(PDF_OUT), format="A4", print_background=True,
                 margin={"top": "20mm", "bottom": "20mm", "left": "15mm", "right": "15mm"})
        browser.close()
    print(f"[build_book] PDF written via HTML+Playwright/Chromium: {PDF_OUT}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepare", action="store_true", help="Build manuscript only")
    parser.add_argument("--epub", action="store_true", help="Build manuscript + EPUB")
    parser.add_argument("--pdf", action="store_true", help="Build manuscript + PDF")
    parser.add_argument("--all", action="store_true", help="Build manuscript + EPUB + PDF")
    args = parser.parse_args()

    if not any([args.prepare, args.epub, args.pdf, args.all]):
        parser.print_help()
        return 1

    try:
        build_manuscript()
    except FileNotFoundError as exc:
        # Missing-image errors are raised with a fully-formed, actionable
        # message (source file, original /images/... path, expected
        # filesystem path). Print that message plainly instead of a raw
        # Python traceback and fail with a distinct exit code.
        print(str(exc), file=sys.stderr)
        return 3

    epub_ok = pdf_ok = None
    if args.epub or args.all:
        epub_ok = build_epub()
    if args.pdf or args.all:
        pdf_ok = build_pdf()

    if epub_ok is False or pdf_ok is False:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
