"""
Session 2 (you write this) — local, offline embedding model wrapper.

Core concept: what an embedding actually is (a dense vector positioning
text in semantic space so "salary slip" and "payslip" land close
together even with no shared words), and why it runs locally here
instead of through a cloud embedding API (Claude has no embeddings
endpoint; the data here is too sensitive to send to any third party).

Model comes from config/settings.yaml: embedding.model_name.
"""
from functools import lru_cache

from sentence_transformers import SentenceTransformer 

_MODEL_NAME = "BAAI/bge-small-en-v1.5" #matches config/setting.yaml -> embedding.model_name

@lru_cache(maxsize=1)
def _get_model() -> SentenceTransformer:
    #Loaded once per process - this is a real model file on disk, you don't
    #want to reload it every time embed_texts is called.
    return SentenceTransformer(_MODEL_NAME)


def embed_texts(texts: list[str]) -> list[list[float]]:
    model = _get_model()
    embeddings = model.encode(texts, normalize_embeddings=True, convert_to_numpy=True)
    return embeddings.tolist()

    """Return one dense vector per input text.

    TODO(Session 2): load a sentence-transformers model (see
    config/settings.yaml) once at module scope, then encode `texts` in
    a batch.
    """
    
