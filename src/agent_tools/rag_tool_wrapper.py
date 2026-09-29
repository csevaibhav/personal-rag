"""
Session 5 (you write this) — expose pipeline.answer_query as one Anthropic
tool definition, ready for Stage 2's ReAct agent to call.

Core concept: a tool-use/function-calling schema (name, description,
input JSON schema) is a CONTRACT the agent's LLM reads to decide when
and how to call your function — the description is the only thing the
model sees to decide "should I call this now?", so its wording matters
as much as the code behind it.
"""


def get_tool_definition() -> dict:
    """Return an Anthropic tool-use schema for `pipeline.answer_query`.

    TODO(Session 5): {"name": ..., "description": ..., "input_schema": {...}}
    """
    raise NotImplementedError("Session 5")
