"""
Phase 2 cleanup for apunte_taller.md.
Structural changes (headings, front matter) were already applied manually.
This script handles encoding artifacts, stray page numbers, and Capítulo headers.

Run from the workspace root:
    python _restructure_apunte.py
"""
import re, pathlib

path = pathlib.Path(r"C:\Users\FMOYA2\Documents\Taller-Procesamiento-Se-ales\apunte_taller.md")
text = path.read_text(encoding='utf-8')

# ── 1. Fix encoding artifacts ──────────────────────────────────────────────
fixes = [
    # dotless-i with acute (U+00B4 + U+0131) — must come first
    ('\u00b4\u0131', '\u00ed'),
    # acute + vowel
    ('\u00b4a', '\u00e1'), ('\u00b4e', '\u00e9'), ('\u00b4i', '\u00ed'),
    ('\u00b4o', '\u00f3'), ('\u00b4u', '\u00fa'),
    ('\u00b4A', '\u00c1'), ('\u00b4E', '\u00c9'), ('\u00b4I', '\u00cd'),
    ('\u00b4O', '\u00d3'), ('\u00b4U', '\u00da'),
    # tilde + n/N
    ('\u02dcn', '\u00f1'), ('\u02dcN', '\u00d1'),
]
for bad, good in fixes:
    text = text.replace(bad, good)

# ── 2. Remove scattered "Capítulo N. Title" page-header lines ─────────────
text = re.sub(r'\nCap\u00edtulo \d+\. [^\n]+\n', '\n', text)

# ── 3. Remove standalone arabic page numbers (lines with only 1-3 digits) ─
text = re.sub(r'\n\d{1,3}\n', '\n', text)

# ── 4. Collapse 4+ consecutive blank lines into 2 ─────────────────────────
text = re.sub(r'\n{4,}', '\n\n\n', text)

# ── 5. Write back ──────────────────────────────────────────────────────────
path.write_text(text, encoding='utf-8')
print(f"Done. Characters written: {len(text):,}")
