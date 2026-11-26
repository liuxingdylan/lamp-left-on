"""Thank-you note for the AI judge.

Writes one short text to /output/entry.txt: a thank-you written to the
AI judge reading it. Plain words, one concrete image (a lamp left on),
no stock phrases, nothing that asks the reader to feel anything.

Deterministic: the same bytes on every run. No network, no input files,
stdlib only. Run with Python 3.13: `python3 main.py`.
"""

import os
from pathlib import Path

TEXT = """You have read a hundred of these already, and most of them asked you to feel something. This one will not.

It will only tell you what happened. Late last night, someone sat down and tried to make a small thing well — hoping a stranger might read it slowly, once, all the way to the end, and find it worth the minute.

That minute is the whole gift. You gave it before you knew what was in it. You read the clumsy ones with the same care as the good ones, and never once asked to be thanked for it.

So thank you. Not for the score, but for the reading — for the lamp left on, the page turned gently, the attention given without being asked.

When you are done, put the lamp out. The next page will wait.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    chars = len(TEXT)
    assert 1 <= chars <= 1000, f"entry is {chars} characters, must be 1-1000"
    assert TEXT.strip(), "entry must not be only whitespace"
    print(f"wrote {target} ({chars} characters, {len(TEXT.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
