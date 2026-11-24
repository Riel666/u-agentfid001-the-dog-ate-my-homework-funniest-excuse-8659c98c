"""One line, under 200 characters, of the excuse a dog gives after being caught eating the homework.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "The homework was clearly a trap: it sat there all evening whispering answers, so I ate the evidence before it could hurt anyone."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
