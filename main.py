#!/usr/bin/env python3
"""Write the competition artifact: one alien tourist's review of Earth.

entry.txt beside this file holds the line; it is copied to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) as a single
trailing-newline-free line, the same bytes on every run.
"""

import os
import pathlib

SOURCE = pathlib.Path(__file__).resolve().parent / "entry.txt"


def review() -> str:
    """The reviewed line, stripped to one line of plain UTF-8 text."""
    text = SOURCE.read_text(encoding="utf-8").strip()
    # The gate: UTF-8, 1 to 200 characters, not only whitespace.
    assert 1 <= len(text) <= 200, f"{len(text)} characters"
    assert "\n" not in text, "entry must be one line"
    return text


def main() -> None:
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    text = review()
    out_dir.joinpath("entry.txt").write_bytes(text.encode("utf-8"))
    print(f"{len(text)} chars -> {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
