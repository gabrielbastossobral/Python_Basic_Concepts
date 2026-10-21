
import sys


def filter_words(text: str, number: int) -> list[str]:
    """Return words whose length is greater than the given number."""
    words = text.split()
    return [word for word in words if (lambda w: len(w) > number)(word)]


def main() -> None:
    """Validate arguments and print words longer than the given number."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]

        try:
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad") from None

        if not text.isalpha() and text != "":
            if not all(char == " " or char.isalpha() for char in text):
                raise AssertionError("the arguments are bad")

        result = filter_words(text, number)
        print(result)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
