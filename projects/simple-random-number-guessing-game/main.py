import random

def generate_secret_number():
    """Generates a random number between 1 and 100 (inclusive)."""
    return random.randint(1, 100)


def get_player_guess():
    """Gets the player's guess from the command line.
    Validates that the input is an integer.
    """
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    """Main game loop.
    Generates a secret number, gets player guesses, and provides feedback.
    """
    secret_number = generate_secret_number()
    num_guesses = 0

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")

    while True:
        guess = get_player_guess()
        num_guesses += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
            break

if __name__ == "__main__":
    main()
