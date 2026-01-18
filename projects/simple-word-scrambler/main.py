import random

def scramble_word(word):
    """Scrambles the letters of a word.

    Args:
        word: The word to scramble.

    Returns:
        The scrambled word, or None if the input is invalid.
    """
    if not isinstance(word, str) or not word.isalpha():
        return None  # Invalid input

    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)


def main():
    """Main function to interact with the user and scramble words."""
    while True:
        word = input("Enter a word to scramble (or type 'exit' to quit): ")

        if word.lower() == 'exit':
            print("Exiting...")
            break

        scrambled_word = scramble_word(word)

        if scrambled_word:
            print("Scrambled word:", scrambled_word)
        else:
            print("Invalid input. Please enter a word containing only letters.")

if __name__ == "__main__":
    main()
