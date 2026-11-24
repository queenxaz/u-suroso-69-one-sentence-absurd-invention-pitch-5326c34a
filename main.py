#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt.
"""

import os

ENTRY = (
    "The WelcomeMat 3000 loudly rates every visitor's shoes out of ten "
    "the moment they wipe their feet, so nobody tracks mud through your "
    "house ever again \u2014 they're too busy arguing with the floor."
)

MAX_CHARS = 220


def main() -> None:
    # The gate requires 1-220 UTF-8 characters, not only whitespace,
    # and the brief requires exactly one sentence.
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1-220 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), (
        "entry must be exactly one sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
