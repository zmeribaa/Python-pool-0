import string
import sys


def text_analyzer(text=None):
    """
    Analyze a text string and display statistics about its contents.

    This function counts the number of upper letters, lower letters,
    punctuation marks, spaces, and digits in the given text.

    Args:
        text (str, optional): The text to analyze. If None, prompts for input.

    Returns:
        None. Prints the analysis results to stdout.
    """
    if text is None:
        text = input("What is the text to count?\n")

    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    punct_count = sum(1 for c in text if c in string.punctuation)
    space_count = sum(1 for c in text if c.isspace())
    digit_count = sum(1 for c in text if c.isdigit())

    total_chars = len(text)

    print(f"The text contains {total_chars} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """
    Main entry point of the script.

    Handles cmd line args and calls txt_analyzer with the provided text.
    Raises an AssertionError if more than one argument is provided.
    """
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument provided")

    text = sys.argv[1] if len(sys.argv) == 2 else None
    text_analyzer(text)


if __name__ == "__main__":
    main()
