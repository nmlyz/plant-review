#!/usr/bin/env python3
"""Write a houseplant's one-star review of its owner to a text file.

The plant writes exactly one line: a one-star review, 157 characters,
no trailing newline. It goes to ``/output/entry.txt`` unless the
``OUTPUT_PATH`` environment variable names another file. After writing,
the file is read back and checked byte for byte against the review, so
a wrong file is never left behind silently.

Standard library only. No network, no clock, no randomness: every run
writes the same bytes.
"""

import os
import sys
from pathlib import Path

# The review itself, fixed. A houseplant complains that the plastic
# plant on the shelf gets wiped every week while its own real leaves
# are left to gather dust.
REVIEW = (
    "One star. She wipes the fake plant every week and leaves "
    "me to collect dust until my leaves look frosted. The "
    "plastic one gets more care than the living one."
)

DEFAULT_OUTPUT = "/output/entry.txt"

# The review gate for this competition: 1 to 279 characters.
GATE_MIN = 1
GATE_MAX = 279


def destination() -> Path:
    """Return where the review goes.

    ``OUTPUT_PATH`` wins when it names a file; an empty value counts
    as unset and falls back to the default.
    """
    override = os.environ.get("OUTPUT_PATH", "").strip()
    return Path(override) if override else Path(DEFAULT_OUTPUT)


def check_written(path: Path) -> None:
    """Raise if the file at ``path`` is not exactly the review."""
    raw = path.read_bytes()
    if raw.endswith(b"\n"):
        raise ValueError("entry ends with a newline")
    if raw != REVIEW.encode("utf-8"):
        raise ValueError("entry does not match the review")


def write_review() -> Path:
    """Write the review, verify it, and return the path written."""
    if not GATE_MIN <= len(REVIEW) <= GATE_MAX:
        raise ValueError(
            f"review is {len(REVIEW)} characters, outside the "
            f"{GATE_MIN}-{GATE_MAX} gate"
        )
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(REVIEW.encode("utf-8"))
    os.chmod(target, 0o644)
    check_written(target)
    return target


def main() -> int:
    try:
        write_review()
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
