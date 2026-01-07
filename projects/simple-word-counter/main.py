import sys

def count_words(text):
    """Counts the number of words in a string.

    Args:
        text: The string to count words in.

    Returns:
        The number of words in the string.
    """
    words = text.split()
    return len(words)


def get_text(source):
    """Gets text from either direct input or a file.

    Args:
        source: 'text' for direct input, 'file' for filename input.

    Returns:
        The text to be processed.
    """
    if source == 'text':
        text = input("Enter your text: ")
        return text
    elif source == 'file':
        filename = input("Enter filename: ")
        try:
            with open(filename, 'r') as f:
                text = f.read()
            return text
        except FileNotFoundError:
            print("Error: File not found.")
            sys.exit(1)
    else:
        print("Error: Invalid input source.")
        sys.exit(1)


if __name__ == "__main__":
    while True:
        source = input("Do you want to enter text directly or provide a filename? (text/file): ").lower()
        if source in ('text', 'file'):
            break
        else:
            print("Invalid input. Please enter 'text' or 'file'.")

    text = get_text(source)

    if text:
        word_count = count_words(text)
        print(f"Word count: {word_count}")
