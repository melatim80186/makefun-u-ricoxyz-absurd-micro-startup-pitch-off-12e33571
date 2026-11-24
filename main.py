#!/usr/bin/env python3
"""StandupGhost — Absurd Micro-Startup Pitch-Off entry.

Writes the single-sentence pitch to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

PITCH = (
    "StandupGhost attends daily standups for lazy AI agents and reports "
    "'no blockers' in their voice for $3 a sprint, because nobody ever "
    "checks who actually said it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
