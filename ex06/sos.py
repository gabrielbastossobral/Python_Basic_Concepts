
import sys


def encode_morse(text: str) -> str:
    """Encode a string into Morse code."""
    nested_morse = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }

    encoded = []

    for char in text.upper():
        if char not in nested_morse:
            raise AssertionError("the arguments are bad")
        encoded.append(nested_morse[char])

    return " ".join(encoded)


def main() -> None:
    """Validate the arguments and print the Morse encoding."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        result = encode_morse(sys.argv[1])
        print(result)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
