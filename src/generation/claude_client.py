"""
Session 4 (Claude-scaffolded) — thin wrapper around the Anthropic Messages API.
"""
import os

import anthropic


def generate(system_prompt: str, user_prompt: str, model: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return response.content[0].text
