def analyze_text(text):
    """Analyzes text and returns word count, character count, and average word length."""
    words = text.split()
    word_count = len(words)
    character_count = len(text)
    if word_count > 0:
        average_word_length = sum(len(word) for word in words) / word_count
    else:
        average_word_length = 0
    return word_count, character_count, average_word_length


def get_user_input():
    """Gets text input from the user."""
    while True:
        text = input("Enter text: ")
        if text.strip():
            return text
        else:
            print("Please enter some text.")


if __name__ == "__main__":
    text = get_user_input()
    word_count, character_count, average_word_length = analyze_text(text)

    print(f"\nWord Count: {word_count}")
    print(f"Character Count: {character_count}")
    print(f"Average Word Length: {average_word_length}")
