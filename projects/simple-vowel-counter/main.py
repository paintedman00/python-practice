def count_vowels(text):
    """Counts the number of vowels (a, e, i, o, u) in a string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def is_valid_input(text):
    """Checks if the input is a valid string."""
    if not isinstance(text, str):
        return False
    if not text:
        return False
    return True


if __name__ == "__main__":
    while True:
        user_input = input("Enter a string: ")

        if not is_valid_input(user_input):
            print("Invalid input. Please enter a non-empty string.")
            continue

        vowel_count = count_vowels(user_input)
        print(f"Number of vowels: {vowel_count}")
        break
