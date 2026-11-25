#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes one line of patch notes to /output/entry.txt.

The line is written in a deadpan changelog voice: one specific fix
mechanism (sleep now syncs across all your devices) plus one counted
absurd consequence (800 million users woke up in someone else's bed).
One incident only, no setup clause, no explanation of the joke.

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1 to 160
characters, a single line, not only whitespace.
"""

from pathlib import Path

NOTE = (
    "Fixed: sleep now syncs across all your devices; "
    "800 million users woke up in someone else's bed."
)

MAX_CHARS = 160


def main() -> None:
    text = NOTE

    # Gate asserts: one line, 1-160 characters, not only whitespace.
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    text.encode("utf-8")  # must be valid UTF-8

    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"Wrote {out} ({len(text)} characters)")


if __name__ == "__main__":
    main()
