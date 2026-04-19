#!/usr/bin/env python3
"""
pdf_to_markdown.py — Convert PDF files to Markdown for LLM/agent consumption.

Requires: pip install pdfminer.six

Usage examples:
    python pdf_to_markdown.py file.pdf
    python pdf_to_markdown.py a.pdf b.pdf c.pdf
    python pdf_to_markdown.py --dir ./docs
    python pdf_to_markdown.py --dir ./docs --out ./markdown_output
    python pdf_to_markdown.py file.pdf --out ./output

Notes on equations:
    - Equations compiled from LaTeX are stored as Unicode text in the PDF and
      WILL be extracted (Greek letters, math operators, etc.).
    - Equations embedded as raster images or with glyph-only fonts CANNOT be
      extracted by any text-based tool. In that case the surrounding context
      (theorem names, variable descriptions, etc.) is still preserved.
"""

import argparse
import re
import sys
import pathlib
import unicodedata
from collections import Counter

try:
    from pdfminer.high_level import extract_pages
    from pdfminer.layout import LTTextBox, LTChar
except ImportError:
    print("Error: pdfminer.six is not installed. Run: pip install pdfminer.six", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Core helpers
# ---------------------------------------------------------------------------

def _get_font_sizes(element) -> list[int]:
    """Collect rounded font sizes of every LTChar inside a text box."""
    sizes = []
    for line in element:
        if hasattr(line, "__iter__"):
            for char in line:
                if isinstance(char, LTChar):
                    sizes.append(round(char.size))
    return sizes


def _classify(size: int, body: int) -> str:
    if size >= body + 6:
        return "h1"
    if size >= body + 3:
        return "h2"
    if size >= body + 1:
        return "h3"
    return "body"


def _fix_text(text: str) -> str:
    """Clean up common PDF text extraction artifacts."""
    # Repair hyphenated line breaks: "sig-\nnificant" → "significant"
    text = re.sub(r"-\n(\w)", r"\1", text)
    # Collapse remaining newlines to spaces
    text = text.replace("\n", " ").strip()
    # Compose combining characters (e.g. NFC fixes "´ı" → "í")
    text = unicodedata.normalize("NFC", text)
    # Replace common ligature artifacts
    for bad, good in {"ﬁ": "fi", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl", "ﬂ": "fl"}.items():
        text = text.replace(bad, good)
    return text


# ---------------------------------------------------------------------------
# Main conversion
# ---------------------------------------------------------------------------

def convert_pdf(pdf_path: pathlib.Path) -> str:
    """
    Convert a single PDF to a Markdown string.

    Headings are detected by comparing each text block's average font size
    against the document's body (most frequent) font size:
        body + 6pt or more  →  # H1
        body + 3pt or more  →  ## H2
        body + 1pt or more  →  ### H3
    """
    blocks: list[tuple[int, str]] = []

    for page_layout in extract_pages(str(pdf_path)):
        for element in page_layout:
            if isinstance(element, LTTextBox):
                raw = element.get_text().strip()
                if not raw:
                    continue
                sizes = _get_font_sizes(element)
                avg_size = round(sum(sizes) / len(sizes)) if sizes else 10
                blocks.append((avg_size, raw))

    if not blocks:
        return ""

    body_size = Counter(s for s, _ in blocks).most_common(1)[0][0]

    lines: list[str] = []
    for size, raw in blocks:
        text = _fix_text(raw)
        if not text:
            continue
        level = _classify(size, body_size)
        if level == "h1":
            lines.append(f"\n# {text}\n")
        elif level == "h2":
            lines.append(f"\n## {text}\n")
        elif level == "h3":
            lines.append(f"\n### {text}\n")
        else:
            lines.append(text)

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert PDF files to Markdown for LLM/agent consumption.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "files",
        nargs="*",
        type=pathlib.Path,
        metavar="PDF",
        help="One or more PDF files to convert.",
    )
    parser.add_argument(
        "--dir",
        type=pathlib.Path,
        metavar="DIRECTORY",
        help="Convert all .pdf files found in this directory.",
    )
    parser.add_argument(
        "--out",
        type=pathlib.Path,
        metavar="DIRECTORY",
        help="Output directory for .md files (default: same folder as each PDF).",
    )
    args = parser.parse_args()

    pdfs: list[pathlib.Path] = list(args.files or [])

    if args.dir:
        if not args.dir.is_dir():
            print(f"Error: '{args.dir}' is not a directory.", file=sys.stderr)
            sys.exit(1)
        pdfs.extend(sorted(args.dir.glob("*.pdf")))

    if not pdfs:
        parser.print_help()
        sys.exit(0)

    if args.out:
        args.out.mkdir(parents=True, exist_ok=True)

    ok = err = 0
    for pdf_path in pdfs:
        if not pdf_path.exists():
            print(f"[SKIP] {pdf_path}: file not found.", file=sys.stderr)
            err += 1
            continue

        out_dir = args.out or pdf_path.parent
        md_path = out_dir / pdf_path.with_suffix(".md").name

        print(f"[{ok + err + 1}/{len(pdfs)}] Converting '{pdf_path.name}'...", end=" ", flush=True)
        try:
            content = convert_pdf(pdf_path)
            md_path.write_text(content, encoding="utf-8")
            print(f"saved to '{md_path}' ({len(content):,} chars)")
            ok += 1
        except Exception as exc:
            print(f"FAILED — {exc}", file=sys.stderr)
            err += 1

    print(f"\nDone: {ok} converted, {err} failed.")


if __name__ == "__main__":
    main()
