"""One Star, Five Stars for the Food — make.fun entry (173 chars vs the 200-char gate).

Writes one sentence (173 chars, within the 1-200 gate) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt):
an alien tourist's one-star review of Earth that still compliments
the food. Pure stdlib only.
"""

import os
import sys

LINE = (
    "One star: your species queues for lukewarm bean water, yells at "
    "glowing rectangles, and charges rent for sleeping \u2014 but the "
    "dumplings alone are worth the 40-light-year trip."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Self-check the gate: 1-200 chars, single line, not whitespace-only.
    with open(path, "rb") as f:
        back = f.read()
    text = back.decode("utf-8")
    assert back == data, "read-back differs from what was written"
    assert 1 <= len(text) <= 200, "gate: length %d outside 1-200" % len(text)
    assert text.strip(), "gate: entry is whitespace-only"
    assert "\n" not in text and "\r" not in text, "gate: entry must be one line"
    print("wrote %s (%d chars, %d bytes)" % (path, len(text), len(back)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
