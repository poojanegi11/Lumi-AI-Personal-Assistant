import re


def extract_city(question):

    question = question.lower()

    # Remove common weather words
    words_to_remove = [
        "what",
        "what's",
        "whats",
        "weather",
        "today",
        "tomorrow",
        "forecast",
        "temperature",
        "in",
        "of",
        "is",
        "the",
        "how",
        "how's",
        "hows"
    ]

    for word in words_to_remove:
        question = question.replace(word, "")

    # Remove punctuation
    question = re.sub(r"[^\w\s]", "", question)

    # Remove extra spaces
    question = question.strip()

    return question.title()