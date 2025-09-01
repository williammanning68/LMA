# LMA Controller

The `controller.py` module exposes a small JSON-based API around the Llama chat model.

## Prompting the model

Provide a system prompt instructing the model to respond with a JSON action. For example:

```
You are an assistant that chooses from available actions and responds ONLY with JSON.
To tell a story, reply with:
{"action": "tell_story", "args": {"topic": "<topic>"}}
```

When the model emits that JSON, pass it to `handle_request` to perform the action.
