"""ai-joke-03c entry: write one fixed one-liner about AI coding agents.

Deterministic by design: no network, no randomness, no clock, no input.
Every run writes the exact same bytes to /output/entry.txt.
The joke is fixed at import time; nothing is computed from the environment.
The output is a single line with no trailing newline, so the file content
is exactly the joke and nothing else.

The joke follows the "Never ..." guardrail pattern: it states a rule for
working with AI coding agents (never ask it to explain a failure) and lands
the punchline on the agent blaming the developer instead.
"""
import os

# The guardrail rule, as one line: asking the agent to diagnose its own
# failure just gets you blamed for the code it wrote.
JOKE = (
    "Never ask your coding agent what went wrong — "
    "it always blames you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
