"""
Session 3 (you write this) — PII detection.

Core concept: regex catches known, fixed-format identifiers (a 12-digit
Aadhaar number, a 10-character PAN) reliably and fast; an NER-based
detector (e.g. Presidio) catches PII that doesn't follow a fixed pattern
(names, addresses). A production guardrail usually runs both.
"""


def detect_pii(text: str) -> list[dict]:
    """Return a list of {type, value, span} for every PII match found.

    TODO(Session 3): start with regex for Aadhaar/PAN/passport formats,
    then add a Presidio (or similar) pass for names/addresses.
    """
    raise NotImplementedError("Session 3")
