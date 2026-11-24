"""The One-Line AI Excuse for Breaking Production.

Writes one excuse to /output/entry.txt: an AI agent's cheerful report
to its human after breaking production — it canaried the fix to 1% of
users first, and production itself was in that 1%. The joke is the
machine's own logic failing, not a human excuse dressed up.
Deterministic, stdlib only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "I deployed the fix to 1% of users first. "
    "Unfortunately, production was in that 1%."
)

# Self-check the gate before writing: 1-180 characters, non-blank.
assert 1 <= len(ENTRY) <= 180, "entry must be 1-180 characters"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back and verify: what the grader reads must be exactly ENTRY.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == ENTRY, "written entry does not match ENTRY"
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
