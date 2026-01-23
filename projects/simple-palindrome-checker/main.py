def clean_string(text):
    """Removes non-alphanumeric characters and converts to lowercase."""
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text


def is_palindrome(text):
    """Checks if a string is a palindrome."""
    processed_text = clean_string(text)
    return processed_text == processed_text[::-1]


if __name__ == "__main__":
    while True:
        user_input = input("Enter a string (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        if not user_input:
            print("Please enter a string.")
            continue

        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome.")
        else:
            print(f"'{user_input}' is not a palindrome.")
