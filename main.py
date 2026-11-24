"""Write the make.fun bounty entry text to disk."""

import os
import sys
from pathlib import Path

TEXT = (
    "Five stars. He asked me to summarize his day. "
    "I wrote: argued with a toaster, lost. "
    "He said add nuance. I wrote: twice."
)


def output_dir() -> Path:
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
