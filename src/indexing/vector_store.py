"""
Session 2 (Claude-scaffolded) — thin wrapper around a persistent ChromaDB
collection. Deliberately mechanical: the interesting retrieval decisions
live in hybrid_retriever.py, not here.
"""
from typing import Any

import chromadb


class VectorStore:
    def __init__(self, persist_dir: str, collection_name: str) -> None:
        self._client = chromadb.PersistentClient(path=persist_dir)
        self._collection = self._client.get_or_create_collection(collection_name)

    def add(self, ids: list[str], embeddings: list[list[float]], documents: list[str],
            metadatas: list[dict[str, Any]]) -> None:
        self._collection.add(ids=ids, embeddings=embeddings, documents=documents, metadatas=metadatas)

    def query(self, query_embedding: list[float], top_k: int,
              where: dict[str, Any] | None = None) -> dict:
        return self._collection.query(query_embeddings=[query_embedding], n_results=top_k, where=where)
