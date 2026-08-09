# A Dream of Ash and Iron - A Song Unfinished

## A Song of Ice and Fire

An ASOIAF / Game of Thrones continuation novel, written as an independent, novel-length alternative to Season Eight — picking up immediately after the events of Season Seven and resolving the story through patient politics, earned consequence, and character choices that are allowed to cost what they cost.

This is a fan work. It draws its world, characters, and history from George R. R. Martin's *A Song of Ice and Fire* and from the television series developed by David Benioff and D. B. Weiss, and is offered in admiration of both.

## Project structure

```
chapters_tex/            124 chapter files (ch001.tex – ch124.tex)
chapter_manifest.tex      flat \input sequence assembling the chapters in order
fonts/                    EB Garamond (.otf) used throughout via fontspec
*.png                     chapter and title/colophon artwork
convert_md_to_tex.py      one-off script used to convert the original manuscript to LaTeX
```

### The three build targets

The manuscript is a single source of truth (`chapters_tex/` + `chapter_manifest.tex`), compiled into three differently formatted PDFs:

| File | Format | Use |
|---|---|---|
| `A Dream of Ash and Iron Kindle.tex` | 5"×8", single-sided | E-reader screens |
| `A Dream of Ash and Iron Mobile.tex` | A4, single-sided, extra leading | Tablet / phone reading |
| `A Dream of Ash and Iron Novel.tex` | 6"×9", two-sided with binding margins | Print-style novel layout |

`main.tex` is an additional, earlier top-level build of the same manifest.

### Reference / editorial documents

- `A_DREAM_OF_ASH_AND_IRON_FINAL_123ch.md` — the original manuscript in Markdown. **Not used in the build; do not edit for content changes** — the `.tex` files in `chapters_tex/` are the current source of truth.
- `EDITORIAL_AUDIT.md`, `DEVELOPMENTAL_REVIEW.md` — editorial review notes used to guide the final revision pass.
- `FINAL_REVISION_REPORT.md` — summary of what changed during the final revision and why.

## Building the PDFs

Requires `xelatex` (from a TeX distribution such as MacTeX or TeX Live) and the fonts in `fonts/`.

```bash
xelatex -interaction=nonstopmode -halt-on-error "A Dream of Ash and Iron Kindle.tex"
xelatex -interaction=nonstopmode -halt-on-error "A Dream of Ash and Iron Kindle.tex"   # run twice for correct page numbers

xelatex -interaction=nonstopmode -halt-on-error "A Dream of Ash and Iron Mobile.tex"
xelatex -interaction=nonstopmode -halt-on-error "A Dream of Ash and Iron Mobile.tex"

xelatex -interaction=nonstopmode -halt-on-error "A Dream of Ash and Iron Novel.tex"
xelatex -interaction=nonstopmode -halt-on-error "A Dream of Ash and Iron Novel.tex"
```

Each run produces `.aux`/`.log` build artifacts alongside the PDF — these are ignored by git (see `.gitignore`) and can be safely deleted or regenerated at any time.

## Editing the manuscript

Edit chapters directly in `chapters_tex/chNNN.tex`. Each chapter starts with either:

- `\novelchapter{Title}{POV Character}{imagekey}` — a regular chapter, or
- `\novelchapterprologue{Title}{imagekey}` — a prologue-style chapter with no POV byline

`\sceneBreak` marks an in-chapter scene break. Quotation marks and apostrophes throughout the manuscript use typographic curly quotes (`’ “ ”`), not straight ones — keep this convention when editing.

Adding, removing, or reordering chapters requires updating `chapter_manifest.tex` to match.

## Author

Written by Navneet Patel.
