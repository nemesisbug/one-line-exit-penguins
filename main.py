#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter.

Writes the entry to /output/entry.txt: a single line, 132 characters,
from a zoo penguin keeper whose birds have unionised.
"""

import os

ENTRY = (
    "I resign as the zoo's penguin keeper \u2014 the penguins have "
    "unionised, management won't negotiate, and frankly, the penguins "
    "are right."
)

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 140
# characters, not only white space, exactly one line. Refuse to write
# anything that does not fit, rather than submitting an invalid entry.
assert ENTRY and not ENTRY.isspace(), "entry must not be blank"
assert "\n" not in ENTRY, "entry must be a single line"
assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, gate is 1-140"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
