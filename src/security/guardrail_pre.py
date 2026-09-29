"""
Session 3 (you write this) — pre-retrieval guardrail.

Classifies the incoming query: does it explicitly ask for
strictly_confidential data? If not, strictly_confidential chunks must
never enter the retrieval candidate set at all (filter at the
VectorStore.query `where` clause, not after the fact).
"""


def clear_query_for_retrieval(query: str) -> dict:
    """Return which sensitivity tiers this query is allowed to retrieve from.

    TODO(Session 3): classify `query` and return something like
    {"allowed_tiers": ["public", "private"]} unless the query
    explicitly and legitimately asks for confidential data.
    """
    raise NotImplementedError("Session 3")
