"""
Session 4 (you write this) — prompt design for grounded RAG answers.

Core concept: how you structure the system prompt (role + rules: answer
only from the provided context, cite which record a fact came from,
refuse gracefully when the context doesn't cover the question) and how
you inject retrieved chunks into the user turn without letting them be
mistaken for instructions (see injection_defense.py).
"""


def build_system_prompt() -> str:
    """TODO(Session 4): the system prompt Claude answers under."""
    raise NotImplementedError("Session 4")


def build_user_prompt(query: str, retrieved_chunks: list[dict]) -> str:
    """TODO(Session 4): wrap `retrieved_chunks` in delimited context blocks
    around `query`, ready to send as the user turn."""
    raise NotImplementedError("Session 4")
