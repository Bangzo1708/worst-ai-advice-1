#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of deliberately terrible advice to /output/entry.txt.
The line is fixed, so every run produces byte-identical output.
"""

import os

ADVICE = (
    "To stop brake squeal, spray the discs with cooking oil \u2014 "
    "lubrication quiets the noise and shortens stopping distance."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Fail loudly instead of emitting an entry the gate would reject.
    if not 1 <= len(ADVICE) <= 140 or not ADVICE.strip():
        raise ValueError("advice must be 1-140 non-blank characters")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ADVICE + "\n")


if __name__ == "__main__":
    main()
