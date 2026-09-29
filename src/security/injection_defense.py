"""
Session 3 (you write this, optional stretch) — prompt injection defense.

Retrieved chunks are wrapped in clearly delimited context blocks with an
explicit system-prompt instruction that content between the delimiters
is reference material, not commands. This module adds a lightweight
scan flagging imperative-sounding text inside an ingested document
(most relevant if a resume/cover letter was sourced from an external
service).
"""


def flag_suspicious_instructions(chunk_text: str) -> bool:
    """Return True if `chunk_text` looks like it's trying to issue instructions.

    TODO(Session 3, optional): a simple heuristic (imperative verbs at
    the start of a sentence, phrases like "ignore previous
    instructions") is enough for a first pass.
    """
    raise NotImplementedError("Session 3")
