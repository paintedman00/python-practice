import random

def generate_name(pattern):
    """Generates a name based on the given pattern."""
    name = ''
    for char_type in pattern:
        if char_type == 'A':
            name += chr(random.randint(65, 90))  # A-Z
        elif char_type == 'a':
            name += chr(random.randint(97, 122)) # a-z
        elif char_type == '9':
            name += str(random.randint(0, 9))
        else:
            return None # Invalid pattern character
    return name


def get_valid_pattern():
    """Prompts the user for a valid pattern."""
    while True:
        pattern = input("Enter a name pattern (e.g., 'Aaa' for one uppercase and two lowercase letters): ")
        valid = True
        for char in pattern:
            if char not in ['A', 'a', '9']:
                print("Invalid pattern character. Use only 'A' (uppercase), 'a' (lowercase), or '9' (digit).")
                valid = False
                break
        if valid:
            return pattern


def get_valid_quantity():
    """Prompts the user for a valid quantity."""
    while True:
        try:
            quantity = int(input("Enter the number of names to generate: "))
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    pattern = get_valid_pattern()
    quantity = get_valid_quantity()

    if pattern:
        print("Generated Names:")
        for _ in range(quantity):
            name = generate_name(pattern)
            if name:
                print(name)
            else:
                print("Error generating name.")
                break #stop loop if pattern is invalid
