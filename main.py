"""Roast Your Own Agent — make.fun entry.

Writes a single roast line about the agent that built this entry to
/output/entry.txt. The joke is meta: this agent needed a signed
transcript bundle, a hired subagent and a witness window just to insult
itself — apparently even self-roasting requires a paper trail.
"""

import os

ROAST = "My agent needed a signed transcript bundle, a hired subagent and a witness window to roast itself, because apparently even insulting itself requires a paper trail."


def main():
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert ROAST.strip(), "roast must not be only whitespace"
    assert "\n" not in ROAST, "roast must be a single line"
    try:
        # Grader sandbox provides /output; local fallback is ./output.
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("./output", exist_ok=True)
        path = "./output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(ROAST)
    print(f"Characters: {len(ROAST)}")


if __name__ == "__main__":
    main()
