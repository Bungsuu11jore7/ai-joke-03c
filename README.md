# ai-joke-03c — AI Coding Agent Joke

An entry for make.fun ai-joke-03: a single one-liner about AI coding agents.
The program writes the joke, and nothing else, to `/output/entry.txt`.

> Never ask your coding agent what went wrong — it always blames you.

## How to run

```sh
python3 main.py
```

This writes the joke to `/output/entry.txt` — exactly one line, no trailing
newline.

## Determinism

No network, no randomness, no clock, no input. The joke is a fixed string
in the source. Run twice and compare the sha256 of `/output/entry.txt`;
both runs produce identical bytes.
