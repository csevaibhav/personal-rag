"""
Session 1 (you write this) — metadata + sensitivity tagging.

Every chunk that reaches the vector store needs document_type,
sensitivity_level, date, and category attached, so the pre-retrieval
guardrail (Session 3) can filter on them before anything is embedded
or searched.
"""


def tag_chunk(chunk_text: str, source_record: dict) -> dict:
    """Build the metadata dict ChromaDB stores alongside this chunk.
    Return a metadata dict for one chunk, derived from its source record.

    TODO(Session 1): pull document_type, sensitivity_level, date, and a
    category label out of `source_record` (an IdentityRecord /
    AcademicRecord / FinancialRecord, already parsed by loaders.py).
    """
    document_type = source_record["document_type"]

    data_field_by_type = {
        "identity": "issue_date",
        "academic": "start_date",
        "financial":"sub_type",
    }
    return{
        "document_type": document_type,
        "sensitivity_level": source_record["sensitivity_level"],
        "date": str(source_record.get(date_field_by_type[document_type], "")),
        "category": source_record.get(category_field_by_type[document_type],"general"),
        "source_file": source_record["source_file"],
        "chunk_length": len(chunk_text),
    }
    
