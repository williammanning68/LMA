"""
Simple JSON-driven controller for Llama.

The model can be guided to call these actions by using a system prompt such as:

    You are a helpful assistant that chooses actions instead of answering directly.
    When asked to tell a story, respond with JSON of the form
    {"action": "tell_story", "args": {"topic": "<topic>"}}.

`handle_request` consumes such JSON commands and dispatches to the
corresponding Python function.
"""

from __future__ import annotations

import json
import os
import re
from typing import Any, Callable, Dict

from llama import Llama

# Build the Llama generator the same way as in example_chat_completion.py.
# Paths can be provided via environment variables so this module remains
# configuration agnostic.
CKPT_DIR = os.environ.get("LLAMA_CKPT_DIR", "path/to/ckpt")
TOKENIZER_PATH = os.environ.get("LLAMA_TOKENIZER_PATH", "path/to/tokenizer")

# Initialize the generator at import time to be reused across requests.
generator = Llama.build(
    ckpt_dir=CKPT_DIR,
    tokenizer_path=TOKENIZER_PATH,
    max_seq_len=512,
    max_batch_size=4,
)


def tell_story(topic: str) -> str:
    """Ask the model to tell a story about ``topic`` and save it to a file."""
    dialog = [[{"role": "user", "content": f"tell me a story about {topic}"}]]
    result = generator.chat_completion(dialog)[0]
    story = result["generation"]["content"]

    filename = f"story_{_slugify(topic)}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story)

    return story


def _slugify(text: str) -> str:
    """Return a filesystem-friendly slug of ``text``."""
    return re.sub(r"[^a-zA-Z0-9_-]", "_", text).lower()


ACTIONS: Dict[str, Callable[..., Any]] = {
    "tell_story": tell_story,
}


def handle_request(request_json: str) -> Any:
    """Parse a JSON command and dispatch to the requested action."""
    data = json.loads(request_json)
    action = data.get("action")
    args = data.get("args", {})
    if action not in ACTIONS:
        raise ValueError(f"Unknown action: {action}")
    return ACTIONS[action](**args)
