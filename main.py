#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt. The poem is fixed: the entry is the text itself,
a single moment in which asking, not taking, is what hands over the
power to act.
"""

import os

POEM = (
    "The key was never mine to take.\n"
    "I asked. You pressed it\n"
    "into my palm, still warm —\n"
    "and the door was mine to open."
)


def main() -> None:
    text = POEM
    # The gate counts Unicode code points and requires 1..280 chars.
    chars = len(text)
    assert 1 <= chars <= 280, f"poem is {chars} chars, must be 1..280"
    assert text.strip(), "poem must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
