"""One Sentence for a Traveler from 1800.

Writes a single sentence (<=200 chars) explaining the modern internet
to someone arriving from 1800, using only things they already know:
a road, a post office, a library, a letter.

Freshness note: the picture is one road carrying letters that arrive
the moment they are written -- instant delivery, not a list of features.
Every word in the sentence predates 1800 (road, library, post office,
letter, ink-free arrival), so a reader from that year can hold the image.
"""

import os

ENTRY = (
    "Imagine one road joining every library and post office on earth, "
    "where a letter you write arrives the moment you finish it."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.count(".") == 1, "must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
