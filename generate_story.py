import random
import datetime

characters = [
    "wizard",
    "astronaut",
    "pirate",
    "robot",
    "dragon",
]

settings = [
    "in a forest",
    "on Mars",
    "at sea",
    "in a castle",
    "in a futuristic city",
]

conflicts = [
    "lost a treasure",
    "fought a rival",
    "found a mysterious map",
    "discovered a secret portal",
    "built a strange machine",
]

def generate_story() -> str:
    """Create a short, random story."""
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    return f"Once upon a time, a {character} {setting} {conflict}."


def main() -> None:
    story = generate_story()
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open("stories.txt", "a", encoding="utf-8") as f:
        f.write(f"{timestamp} - {story}\n")
    print("Generated story saved.")


if __name__ == "__main__":
    main()
