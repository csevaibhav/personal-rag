"""
Session 1 (Claude-scaffolded) — per-filetype loaders.

Each loader takes a file path and returns raw text (for unstructured docs)
or a parsed dict (for structured YAML/JSON identity, academic, financial
records). Keep these dumb: they only read and parse, they never chunk,
tag, or judge sensitivity — that's chunking.py and tagging.py's job.
"""
from pathlib import Path


def load_pdf(path: Path) -> str:
    raise NotImplementedError("Session 1: extract text from a PDF (pypdf or similar)")


def load_docx(path: Path) -> str:
    raise NotImplementedError("Session 1: extract text from a DOCX")


def load_yaml_record(path: Path) -> dict:
    raise NotImplementedError("Session 1: parse a structured YAML record (identity/academic/financial)")


def load_json_record(path: Path) -> dict:
    raise NotImplementedError("Session 1: parse a structured JSON record")
