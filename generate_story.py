"""Generate a story using a remote or local Ollama server."""

import os
import sys
import requests


def main() -> None:
    """Ask Ollama for a short whimsical story about a topic."""
    topic = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "a comet that learns to read"
    prompt = f"Tell a short whimsical story about {topic}."

    ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
    payload = {
        "model": os.getenv("OLLAMA_MODEL", "llama3.2"),
        "prompt": prompt,
        "stream": False,
    }

    resp = requests.post(f"{ollama_url}/api/generate", json=payload, timeout=600)
    resp.raise_for_status()
    print(resp.json().get("response", "").strip())


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    main()

