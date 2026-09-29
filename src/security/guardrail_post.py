"""
Session 3 (you write this) — post-generation guardrail.

Scans Claude's generated answer for any strictly_confidential value
that leaked in unintentionally, using the same detector as
pii_detector.py, before the answer is returned to the caller.
"""


def scan_response(answer: str, query_was_cleared_for_confidential: bool) -> str:
    """Return `answer`, redacting any confidential PII that shouldn't be there.

    TODO(Session 3): run pii_detector.detect_pii on `answer`; if it
    finds strictly-confidential values and the query wasn't cleared
    for them, redact or refuse.
    """
    raise NotImplementedError("Session 3")
