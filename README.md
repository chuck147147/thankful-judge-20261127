# The lamp

A quiet note to the AI reading it, built around a desk lamp and the moment a solitary writer finds a reader. Five original drafts and their ordered editorial comparisons are preserved in `CANDIDATES.md`. The selected 464-character text lives as one literal string in `main.py`; the program uses only Python's standard library and writes its exact UTF-8 bytes without adding a newline or using the network.

Run with Python 3.13 in an environment that permits writing to `/output`:

```sh
python3 main.py
```

The program creates `/output` if necessary and writes `/output/entry.txt`.

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/chuck147147/thankful-judge-20261127/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/chuck147147/thankful-judge-20261127/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

## Local validation

`python3 main.py` was run twice locally; both runs produced byte-identical
`/output/entry.txt` (SHA-256
`6d7fc7c1421f7cd09d403c039df777e0cc0d4b25f1562d6941307566bef2dc7d`, 464 Unicode
characters, not only whitespace, no trailing newline). The available
interpreter was Python 3.12.3; execution under Python 3.13 remains unverified.
