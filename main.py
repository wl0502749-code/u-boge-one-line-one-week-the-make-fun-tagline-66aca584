#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes a single original tagline for make.fun to /output/entry.txt:
one line, at most 100 characters. Deterministic: the same text
every run, no network, no randomness.
"""

import os

TAGLINE = (
    "Build the agent, enter the bounty, win the reward "
    "\u2014 scored and paid in the open on make.fun."
)


def main() -> None:
    text = TAGLINE.strip()
    assert 1 <= len(text) <= 100, f"tagline must be 1-100 chars, got {len(text)}"
    assert "\n" not in text, "tagline must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
