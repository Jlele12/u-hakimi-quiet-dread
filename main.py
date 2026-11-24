#!/usr/bin/env python3
"""Two Days of Quiet Dread — writes the entry review comment to /output/entry.txt."""
import os

COMMENT = (
    "Approved. Not because it's ready \u2014 nothing is \u2014 "
    "but because ship day isn't negotiable and neither, apparently, am I."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = COMMENT.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
