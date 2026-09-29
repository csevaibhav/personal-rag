# Personal RAG Chatbot — Stage 1

The full architecture blueprint and the session-by-session working plan live in the Claude Doc:
https://claude.ai/code/artifact/ecce84ac-7c78-428b-b72d-3010d952b841 (see the "Working Plan & Roadmap" tab).

## Quickstart

1. Create a virtual environment and activate it:
   - Windows: `python -m venv .venv && .venv\Scripts\activate`
   - macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt`
3. `python main.py "hello"` — should print a stub response. That confirms Session 0 is wired correctly.

## Where things stand

Session 0 (this scaffold) is done — the repo runs end to end with stubbed logic.
Sessions 1-5 fill in the `TODO(Session N)` markers in `src/` — see the working plan doc for what
each session covers and who writes what.
