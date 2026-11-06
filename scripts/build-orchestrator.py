#!/usr/bin/env python3
"""Package the canonical router as a standalone, discoverable agent skill."""

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "agents" / "learner-orchestrator.md"
TARGET = ROOT / "skills" / "00-learner-orchestrator" / "SKILL.md"
HEADER = """---
name: learner-orchestrator
description: Use when a learner wants a guided study session and needs help choosing among learning plans, Socratic tutoring, teach-back, retrieval practice, analogies, or critical review; route to one available learning skill at a time.
---

"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="Check the committed package without modifying it."
    )
    args = parser.parse_args()
    expected = HEADER + SOURCE.read_text(encoding="utf-8")
    if args.check:
        if not TARGET.is_file() or TARGET.read_text(encoding="utf-8") != expected:
            parser.exit(1, "Router package is out of date. Run python3 scripts/build-orchestrator.py.\n")
        print("Router package matches the canonical agent instructions.")
        return
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(expected, encoding="utf-8")
    print(f"Built {TARGET.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
