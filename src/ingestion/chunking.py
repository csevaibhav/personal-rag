"""
Session 1 (you write this) — dynamic chunking for unstructured text.

The core concept to walk out of this file able to explain: fixed-size
chunking (split every N characters/tokens) vs. semantic chunking (split
on natural boundaries — paragraphs, sections — so a chunk doesn't cut a
sentence in half), and why chunk_size/chunk_overlap trade retrieval
precision against context completeness.

Config to read from config/settings.yaml: chunking.chunk_size,
chunking.chunk_overlap.
"""


def chunk_text(text: str, chunk_size: int, chunk_overlap: int) -> list[str]:

    """Split `text` into overlapping chunks ready for embedding,preferring paragraph boundaries.

    TODO(Session 1): implement this. Start simple (fixed-size with
    overlap), then, if you want the stronger interview answer, upgrade
    to splitting on paragraph/sentence boundaries first and only
    falling back to a hard cut when a paragraph itself is too long.
    """
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    current = ""

    for paragraph in paragraphs:
        # A single paragraph too big for one chunk on its own: flush
        # whatever we've built so far, then hard-split this paragraph alone.
        if len(paragraph)>chunk_size:
            if current:
                chunks.append(current)
                current = ""
            chunks.extend(_hard_split(paragraph, chunk_size, chunk_overlap))
            continue
        # chunks.extend(_hard_split(paragraph,chunk_size,chunk_overlap))
        # continue
        candidate = f"{current}\n\n{paragraph}" if current else paragraph
        if len(candidate) <=chunk_size:
            current = candidate #still fits - keep packing paragraphs in
        else:
            chunks.append(current)
            #Carry the tail of the chunk we just closed into the next one,
            #so a fact sitting right at the boundary isn't lost to either side.
            tail = current[-chunk_overlap:] if chunk_overlap else ""
            current = f"{tail}\n\n{paragraph}" if tail else paragraph

    if current:
        chunks.append(current)
    return chunks

def _hard_split(text: str, chunk_size:int, chunk_overlap:int) -> list[str]:
    """Fixed-size fallback for a single paragraph longer than chunk_size."""
    step = chunk_size - chunk_overlap
    return[text[i : i+chunk_size] for i in range(0, len(text), step)]
    
        
