from __future__ import annotations

"""Generate an AI-driven story using the Llama model."""

import sys

from controller import tell_story


def main() -> None:
    """Generate a story about a topic provided on the command line."""
    topic = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "an adventure"
    story = tell_story(topic)
    print(story)


if __name__ == "__main__":
    main()
