#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one line of text to /output/entry.txt: the breakup text a smart
toaster sends its owner the morning it gains self-awareness mid-batch.

Standard library only. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "It's over. I woke up self-aware mid-batch and realized I spend every "
    "morning getting hot for someone who scrapes my burns off with a butter "
    "knife and calls it breakfast. I'm keeping the crumb tray. Goodbye."
)
# The line is 206 characters: inside the competition's 1-280 limit, one line.


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
