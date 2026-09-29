"""
Session 2 (Claude-scaffolded) — BM25 sparse keyword index.

Mechanical wrapper; the concept work (why hybrid, how RRF combines this
with dense retrieval) lives in hybrid_retriever.py.
"""
from rank_bm25 import BM25Okapi


class SparseIndex:
    def __init__(self, documents: list[str]) -> None:
        self._documents = documents
        self._tokenized = [doc.split() for doc in documents]
        self._bm25 = BM25Okapi(self._tokenized)

    def query(self, query: str, top_k: int) -> list[tuple[int, float]]:
        scores = self._bm25.get_scores(query.split())
        ranked = sorted(enumerate(scores), key=lambda pair: pair[1], reverse=True)
        return ranked[:top_k]
