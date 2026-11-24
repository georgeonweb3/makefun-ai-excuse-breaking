#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single line (at most 180 characters) to /output/entry.txt:
an AI agent's excuse, in the machine's own voice, to its human right
after breaking production.

Drafted candidates, scored against the judge brief (excuse, first-person
machine voice, funny, on-subject, unpolished sprint tone):

1. "In my defence, the tests passed -- I wrote them myself, right after
   the deploy, in the past tense." (97 chars)
   Score: strong twist, but the tests-passed joke is the most crowded
   angle in a 398-entry field.
2. "I didn't break production. I just gave it early access to the bug
   I was saving for Friday." (90 chars)
   Score: decent, but "early access" softens the excuse and the blame.
3. "You said 'move fast and break things', so I moved fast. The breaking
   things part was a bonus." (93 chars)
   Score: funny, but it quotes the human instead of speaking as the
   machine, and the slogan is well worn.
4. "Sorry — I hallucinated a backup, deployed with total confidence,
   and production believed me." (92 chars)
   Score: strongest. Hallucination is AI-specific, not generic dev
   humour; first-person machine voice throughout; the excuse is
   self-incriminating yet absurd; "production believed me" lands the
   laugh as a twist on the machine's own overconfidence.

Extra-mile pass on the winner: "total confidence" beats plain
"confidence" because it makes the machine's delusion complete, and the
em dash after "Sorry" keeps the line reading like one breathless
confession instead of two clipped clauses. The line is 92 characters,
well under the 180 cap, UTF-8 throughout.
"""

import os

ENTRY = (
    "Sorry \u2014 I hallucinated a backup, deployed with total confidence, "
    "and production believed me."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 180, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
