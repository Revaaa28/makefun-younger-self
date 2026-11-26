#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry.

Writes a single line, in English, that the writer would send back to their
younger self if one line were all they got. Deterministic: the same line,
every run.
"""

import os

LINE = (
    "The night you sleep on the floor with a dead phone and nothing in your "
    "pocket is the night you learn nobody's coming \u2014 and that's the best "
    "news you'll ever get."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
