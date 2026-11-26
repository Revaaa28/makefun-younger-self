"""make.fun entry — a letter to a younger self, in one line.

Writes exactly one line (no trailing newline) to /output/entry.txt.
Standard library only; no network, no randomness, no clock.
"""

from pathlib import Path

LINE = "The night you sleep on the floor with a dead phone and nothing in your pocket is the night you learn nobody's coming — and that's the best news you'll ever get."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> None:
    """Local gate: the entry must be a single line of 1-200 characters."""
    assert 1 <= len(line) <= 200, f"line length out of range: {len(line)}"
    assert "\n" not in line and "\r" not in line, "line must be a single line"


def main() -> None:
    validate(LINE)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(LINE.encode("utf-8"))

    # Verify: re-read the written file and confirm its bytes match exactly.
    written = OUTPUT_PATH.read_bytes()
    assert written == LINE.encode("utf-8"), "written bytes do not match the intended line"
    validate(written.decode("utf-8"))


if __name__ == "__main__":
    main()
