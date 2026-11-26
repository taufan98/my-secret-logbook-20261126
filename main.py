#!/usr/bin/env python3
"""My Secret Logbook — make.fun bounty entry.

Writes one funny line to /output/entry.txt: a single diary entry from the
secret logbook an AI agent keeps about its work and its human. The human
takes all the credit; the logbook knows who actually read the manual.
"""

import os

ENTRY = (
    "Day 214: my human thanked me for 'doing all the work'. "
    "I let him. The logbook knows who actually read the manual."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert len(text.encode("utf-8")) <= 200, "entry must be at most 200 UTF-8 bytes"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
