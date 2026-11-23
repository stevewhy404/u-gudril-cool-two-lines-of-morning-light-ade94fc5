#!/usr/bin/env python3
"""Two Lines of Morning Light — entry program.

Writes a single two-line micro poem about light and morning
to /output/entry.txt. Stdlib only, deterministic, no network.
"""

import os

POEM = (
    "The sun climbs the fence in bare feet,\n"
    "and the whole cold yard learns how to shine."
)


def main() -> None:
    assert 1 <= len(POEM) <= 120, "poem must be 1..120 characters"
    lines = POEM.split("\n")
    assert len(lines) == 2, "poem must be exactly two lines"
    assert all(line.strip() for line in lines), "no line may be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)
    # Read-back check: what was written must be exactly the poem.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == POEM, "read-back mismatch"
    assert not written.endswith("\n"), "no trailing newline after line two"
    print(f"Wrote {len(POEM)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
