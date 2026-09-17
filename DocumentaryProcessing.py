"""Simple documentary/text processing: summary, keywords, and sentence search."""

from collections import Counter
from pathlib import Path
import re

STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in",
    "is", "it", "of", "on", "or", "that", "the", "to", "with",
}


def read_document(filename: str) -> str:
    path = Path(filename)
    if path.exists():
        return path.read_text(encoding="utf-8")
    return (
        "Nature documentaries explain ecosystems and the species that live in them. "
        "They show how climate, water, and conservation affect wildlife. "
        "Careful observation helps people protect endangered animals."
    )


def analyse_document(text: str) -> tuple[list[str], list[tuple[str, int]]]:
    sentences = [sentence.strip() for sentence in re.split(r"[.!?]+", text) if sentence.strip()]
    words = re.findall(r"[A-Za-z']+", text.lower())
    keywords = Counter(word for word in words if word not in STOP_WORDS and len(word) > 2)
    return sentences, keywords.most_common(8)


def main() -> None:
    filename = input("Document filename (press Enter for sample): ").strip() or "documentary.txt"
    text = read_document(filename)
    sentences, keywords = analyse_document(text)

    print("\n--- Documentary Processing Report ---")
    print("Words:", len(re.findall(r"[A-Za-z']+", text)))
    print("Sentences:", len(sentences))
    print("Summary:", " ".join(sentences[:2]) + ".")
    print("Top keywords:", ", ".join(f"{word} ({count})" for word, count in keywords))

    query = input("\nSearch word (press Enter to finish): ").strip().lower()
    if query:
        matches = [sentence for sentence in sentences if query in sentence.lower()]
        print("Matches:" if matches else "No matching sentences.")
        for match in matches:
            print("-", match)


if __name__ == "__main__":
    main()
