"""
The single entrypoint the whole system funnels through.

This is the ONE function Stage 2's ReAct agent will call as a tool later
(see src/agent_tools/rag_tool_wrapper.py) — which is exactly why it takes
a plain string in and returns a plain string out, with no UI or CLI logic
inside it.

Session 0: stubbed, so the repo runs end to end today.
Session 2: wire in real hybrid retrieval.
Session 3: run the query through the pre-retrieval guardrail before retrieval,
           and the post-generation guardrail before returning.
Session 4: wire in real Claude generation.
"""


def answer_query(query: str) -> str:
    # TODO(Session 3): pre-retrieval PII/guardrail scan on `query`
    # TODO(Session 2): retrieved = hybrid_retriever.retrieve(query)
    # TODO(Session 4): answer = claude_client.generate(query, retrieved)
    # TODO(Session 3): post-generation guardrail scan on the answer before returning
    return f"[stub] You asked: {query!r}. Sessions 2-4 will wire this up for real."
