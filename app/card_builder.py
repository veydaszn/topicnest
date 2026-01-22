from data.cards import save_card

def build_card(topic: str):
    card = {
        "topic": topic,
        "definition": f"{topic} is a fundamental concept in computer science.",
        "key_points": [
            f"Core idea of {topic}",
            f"Common use cases of {topic}",
            f"Advantages and limitations of {topic}"
        ],
        "example": f"Example usage of {topic} in real-world applications."
    }

    save_card(card)
    return card
