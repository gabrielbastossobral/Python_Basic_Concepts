import sys


def analyze_text(text: str) -> None:
    """Count uppercase, lowercase, punctuation, digits and spaces."""
    upper = 0
    lower = 0
    punctuation = 0
    digits = 0
    spaces = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            punctuation += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main() -> None:
    """Handle arguments and start the text analysis."""
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        if len(sys.argv) == 2 and sys.argv[1] != "":
            text = sys.argv[1]
        else:
            text = input("What is the text to count?\n")

        analyze_text(text)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
