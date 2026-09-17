"""Encode and decode text with Base64 and a Caesar cipher."""

import base64


def caesar_cipher(text: str, shift: int) -> str:
    result = []
    for character in text:
        if character.isalpha():
            start = ord("A") if character.isupper() else ord("a")
            result.append(chr((ord(character) - start + shift) % 26 + start))
        else:
            result.append(character)
    return "".join(result)


def main() -> None:
    choice = input("Choose 1: Base64 encode, 2: Base64 decode, 3: Caesar encode, 4: Caesar decode: ").strip()
    text = input("Enter text: ")
    try:
        if choice == "1":
            print("Encoded:", base64.b64encode(text.encode()).decode())
        elif choice == "2":
            print("Decoded:", base64.b64decode(text.encode(), validate=True).decode())
        elif choice in {"3", "4"}:
            shift = int(input("Shift value (for example, 3): "))
            print("Result:", caesar_cipher(text, shift if choice == "3" else -shift))
        else:
            print("Please choose a number from 1 to 4.")
    except (ValueError, UnicodeDecodeError) as error:
        print("Unable to decode input:", error)


if __name__ == "__main__":
    main()
