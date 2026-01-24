import random
import string

def generate_password(length, include_special_chars):
    """Generates a random password.

    Args:
        length: The desired length of the password.
        include_special_chars: Whether to include special characters.

    Returns:
        A string containing the generated password.
    """
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password


def validate_length(length_str):
    """Validates that the length is a positive integer.

    Args:
        length_str: The string representation of the length.

    Returns:
        The integer representation of the length if valid, None otherwise.
    """
    try:
        length = int(length_str)
        if length <= 0:
            return None
        return length
    except ValueError:
        return None

if __name__ == "__main__":
    while True:
        length_str = input("Enter the desired password length: ")
        length = validate_length(length_str)
        if length is not None:
            break
        else:
            print("Invalid length. Please enter a positive integer.")

    while True:
        include_special_chars_input = input("Include special characters? (y/n): ").lower()
        if include_special_chars_input in ['y', 'n']:
            include_special_chars = include_special_chars_input == 'y'
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    password = generate_password(length, include_special_chars)
    print("Generated password: ", password)
