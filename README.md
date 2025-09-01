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

Running the `tell_story` action returns the generated text and also saves it to a
file named `story_<topic>.txt` in the current working directory, with the topic
slugified for filesystem safety.

## Command-line story generation

Use `generate_story.py` to ask the Llama model to tell a story about a topic:

```bash
python generate_story.py "space pirates"
```

The story is printed to the console and saved to `story_space_pirates.txt`.
