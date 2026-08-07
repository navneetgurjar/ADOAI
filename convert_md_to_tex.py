#!/usr/bin/env python3
"""
Converts A_DREAM_OF_ASH_AND_IRON_FINAL_123ch.md into LaTeX-ready chapter files.
Does NOT alter a single word of the novel's text -- only escapes LaTeX-reserved
characters and translates Markdown emphasis/scene-break syntax into LaTeX
equivalents, which are typographic necessities, not content changes.
"""
import re
import os

SOURCE_MD = "A_DREAM_OF_ASH_AND_IRON_FINAL_123ch.md"
OUT_DIR = "chapters_tex"

# ---- EDIT THIS MAPPING ------------------------------------------------------
# Keys are STORY chapter numbers (1 = Chapter One, ..., 123 = final chapter;
# the Prologue is chapter 0). Values are the photo filename (WITHOUT extension)
# to place directly above that chapter's opening. Leave a chapter out of this
# dict and it simply gets no image. Placeholder below assigns photo1-photo20
# to the first 20 chapters sequentially -- REPLACE with the real mapping.
IMAGE_MAP = {
    1:  "photo1",  2:  "photo2",  3:  "photo3",  4:  "photo4",  5:  "photo5",
    6:  "photo6",  7:  "photo7",  8:  "photo8",  9:  "photo9",  10: "photo10",
    11: "photo11", 12: "photo12", 13: "photo13", 14: "photo14", 15: "photo15",
    16: "photo16", 17: "photo17", 18: "photo18", 19: "photo19", 20: "photo20",
    # 0: "title_image_for_prologue",   # example of how to add the Prologue
}
# -----------------------------------------------------------------------------

# ---- 1. LaTeX special-character escaping -----------------------------------
LATEX_SPECIAL = [
    ('\\', r'\textbackslash{}'),
    ('&', r'\&'),
    ('%', r'\%'),
    ('$', r'\$'),
    ('#', r'\#'),
    ('_', r'\_'),
    ('{', r'\{'),
    ('}', r'\}'),
    ('~', r'\textasciitilde{}'),
    ('^', r'\textasciicircum{}'),
]

def escape_latex(text):
    for char, repl in LATEX_SPECIAL:
        text = text.replace(char, repl)
    return text

def convert_markdown_emphasis(text):
    """**bold text** -> \\textbf{bold text}, then *italic text* -> \\textit{...}.
    Processed PARAGRAPH BY PARAGRAPH (split on blank lines) so a stray or
    unpaired marker anywhere in the manuscript can never cause a match to
    run away across a paragraph break and swallow unrelated text.
    Bold is converted first so its double-asterisk delimiters are fully
    consumed before the single-asterisk italics pattern ever sees them.
    """
    paragraphs = text.split('\n\n')
    fixed = []
    for para in paragraphs:
        para = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', para, flags=re.DOTALL)
        para = re.sub(r'\*(.+?)\*', r'\\textit{\1}', para, flags=re.DOTALL)
        fixed.append(para)
    return '\n\n'.join(fixed)

def convert_scene_breaks(text):
    """--- on its own line -> a centered ornamental scene-break."""
    lines = text.split('\n')
    out = []
    for line in lines:
        if line.strip() == '---':
            out.append(r'\sceneBreak')
        else:
            out.append(line)
    return '\n'.join(out)

def smarten_quotes(text):
    """Converts straight quotes/apostrophes to proper Unicode curly quotes,
    following standard 'SmartyPants' contextual rules. This is a typographic
    correction, not a content change -- only the character rendering a quote
    mark or apostrophe changes; the words themselves are untouched.
    """
    RSQUOTE = "\u2019"  # right single quotation mark (apostrophe)
    LSQUOTE = "\u2018"  # left single quotation mark
    LDQUOTE = "\u201c"
    RDQUOTE = "\u201d"
    EMDASH = "\u2014"

    # Apostrophes (the vast majority of ' in English prose): always RSQUOTE.
    text = re.sub(r"(?<=[A-Za-z0-9])'(?=[A-Za-z])", RSQUOTE, text)
    text = re.sub(r"(?<=[A-Za-z])'(?=[\s.,!?;:\"\)\]}])", RSQUOTE, text)
    text = re.sub(r"(?<=[A-Za-z])'$", RSQUOTE, text, flags=re.MULTILINE)

    # Elision at the start of a word (e.g. 'tis, 'em) -> opening single quote
    text = re.sub(r"(^|[\s(\[{" + EMDASH + r"])'(?=[A-Za-z])",
                   lambda m: m.group(1) + LSQUOTE, text, flags=re.MULTILINE)

    # Any remaining stray single quotes default to the closing/apostrophe form
    text = text.replace("'", RSQUOTE)

    # Double quotes: opening quote follows whitespace/start/opening-punct/
    # em-dash and precedes a non-space character; everything else is closing.
    def replace_doubles(s):
        result = []
        for i, c in enumerate(s):
            if c == '"':
                prev_char = s[i-1] if i > 0 else '\n'
                if prev_char in ' \t\n([{' + EMDASH + LSQUOTE + LDQUOTE:
                    result.append(LDQUOTE)
                else:
                    result.append(RDQUOTE)
            else:
                result.append(c)
        return ''.join(result)

    text = replace_doubles(text)
    return text

def process_chapter(raw_chapter_text):
    lines = raw_chapter_text.strip('\n').split('\n')
    header_line = lines[0]
    body = '\n'.join(lines[1:]).strip('\n')

    m = re.match(r'^## (?:CHAPTER\s+([A-Z\- ]+)\s+---\s+(.+)|(PROLOGUE))$',
                 header_line.strip().replace('\u2014', '---'))
    if not m:
        m = re.match(r'^## (?:CHAPTER\s+([A-Z\- ]+)\s+\u2014\s+(.+)|(PROLOGUE))$',
                     header_line.strip())
    if m:
        if m.group(3):
            chapter_label = "PROLOGUE"
            chapter_name = None
        else:
            chapter_label = f"CHAPTER {m.group(1).strip()}"
            chapter_name = m.group(2).strip()
    else:
        raise ValueError(f"Unrecognized header format: {header_line!r}")

    body = smarten_quotes(body)
    body = escape_latex(body)
    body = convert_markdown_emphasis(body)
    body = convert_scene_breaks(body)

    chapter_label_escaped = escape_latex(chapter_label)
    chapter_name_escaped = escape_latex(chapter_name) if chapter_name else None

    return chapter_label_escaped, chapter_name_escaped, body

def main():
    with open(SOURCE_MD, 'r', encoding='utf-8') as f:
        text = f.read()

    first_marker = re.search(r'^## (?:PROLOGUE|CHAPTER)', text, re.MULTILINE)
    text = text[first_marker.start():]

    raw_chapters = re.split(r'(?=^## (?:PROLOGUE|CHAPTER))', text, flags=re.MULTILINE)
    raw_chapters = [c for c in raw_chapters if c.strip()]

    os.makedirs(OUT_DIR, exist_ok=True)

    manifest = []
    for idx, raw in enumerate(raw_chapters, start=1):
        label, name, body = process_chapter(raw)
        fname = f"{OUT_DIR}/ch{idx:03d}.tex"
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(body)
        manifest.append((idx, label, name, fname))

    with open("chapter_manifest.tex", 'w', encoding='utf-8') as f:
        for idx, label, name, fname in manifest:
            story_num = idx - 1  # idx 1 = Prologue = story chapter 0
            f.write(f"% --- File {idx}: {label}"
                    + (f" -- {name}" if name else "") + " ---\n")
            image_key = IMAGE_MAP.get(story_num, "")
            if name:
                f.write(r"\novelchapter{" + label + r"}{" + name
                        + r"}{" + image_key + "}\n")
            else:
                f.write(r"\novelchapterprologue{" + label
                        + r"}{" + image_key + "}\n")
            f.write(r"\input{" + fname + "}\n\n")

    print(f"Processed {len(manifest)} chapters.")
    print("First 5 chapters found:")
    for idx, label, name, fname in manifest[:5]:
        print(f"  {idx:3}. {label}" + (f" -- {name}" if name else ""))
    print("...")
    print("Last 3 chapters found:")
    for idx, label, name, fname in manifest[-3:]:
        print(f"  {idx:3}. {label}" + (f" -- {name}" if name else ""))

if __name__ == "__main__":
    main()
