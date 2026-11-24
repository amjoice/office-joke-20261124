"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life to /output/entry.txt.
Deterministic: the same joke, byte for byte, on every run.
Standard library only — no third-party imports.
"""

import os

JOKE = (
    "HR said the open-plan office builds collaboration, "
    "which is why I now know Dave's divorce lawyer's first name."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(joke: str) -> str:
    """Return the joke stripped, enforcing the gate: 1-200 chars, one line."""
    text = joke.strip()
    if not text:
        raise SystemExit("joke is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit("joke is over 200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")
    return text


def main() -> None:
    text = validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
