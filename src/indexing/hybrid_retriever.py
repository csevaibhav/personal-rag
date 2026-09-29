"""
Session 2 (you write this) — Reciprocal Rank Fusion over dense + sparse results.

Core concept: dense (embedding) search finds semantic matches, sparse
(BM25) search finds exact keyword/term matches (useful for things like
"PAN" or a specific institution name that an embedding might blur past).
RRF combines the two RANKED LISTS (not raw scores, which aren't
comparable across methods) with:

    RRF_score(doc) = sum over each ranking r that contains doc of
                     1 / (rrf_k + rank_in_r(doc))

config/settings.yaml has rrf_k (60 is the standard default from the
original RRF paper).
"""

from src.indexing.embeddings import embed_texts
from src.indexing.sparse_index import SparseIndex
from src.indexing.vector_store import VectorStore

def reciprocal_rank_fusion(dense_ranked_ids: list[str], sparse_ranked_ids: list[str],
                           rrf_k: int) -> list[str]:
    scores: dict[str, float] = {}

    for ranked_ids in (dense_ranked_ids, sparse_ranked_ids):
        for rank, doc_id in enumerate(ranked_ids, start=1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (rrf_k + rank)

    return sorted(scores, key=scores.get, reverse=True)




    
    


def retrieve(query: str, top_k: int, vector_store: VectorStore, sparse_index: SparseIndex,
             sparse_chunk_ids: list[str], corpus: dict[str, dict], rrf_k:int) -> list[dict]:
    
    """Hybrid retrieval: embed the query, search both indexes, fuse with RRF.

    `corpus` maps chunk id -> {"text": ..., "metadata": ...} for every chunk
    that's been indexed, so we can assemble the final result regardless of
    which index (dense, sparse, or both) surfaced a given chunk."""

    query_embedding = embed_texts([query])[0]

    dense_results = vector_store.query(query_embedding, top_k=top_k)
    dense_ranked_ids = dense_results["ids"][0]

    sparse_hits = sparse_index.query(query, top_k=top_k)

    #SparseIndex returns (position, score) - translate position back to the
    #SAME chunk ids the vector ids the vector store uses, so RRF fuses over one shared id
    #space instead of two unrelated numbering schemes.

    sparse_ranked_ids = [sparse_chunk_ids[position] for position, _score in sparse_hits]

    fused_ids = reciprocal_rank_fusion(dense_ranked_ids, sparse_ranked_ids, rrf_k) [:top_k]
    return [{"id": doc_id, **corpus[doc_id]} for doc_id in fused_ids]



    


    """TODO(Session 2): call embeddings.embed_texts, VectorStore.query,
    SparseIndex.query, then reciprocal_rank_fusion, and return the
    fused chunks with their metadata.
    


    Return doc ids ordered by fused RRF score, highest first.
    
    TODO(Session 2): implement the formula above over the two ranked
    id lists and return the fused ordering.
    """
        
