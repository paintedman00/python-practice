import random
from replit import clear
from my_hangman_words import word_list
from my_hangman_art import stages, logo2, logo3

# Initialize game variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False

print(logo3)
print("\nGuess the word correctly before the figure is fully drawn!\n")

# Create display and track wrong guesses
display = ["_" for _ in range(word_length)]
wrong_guesses = []

while not end_of_game:
    guess = input("Enter a letter: ").lower()
    clear()
    
    # Check if the letter was already guessed
    if guess in wrong_guesses:
        print(" ".join(display))
        print(stages[lives])
        print(f"You've already tried '{guess}', pick a different letter.")
        continue
    
    wrong_guesses.append(guess)
    
    # Update display if guess is correct
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter
    else:
        lives -= 1
        print(f"'{guess}' is incorrect, you've lost a life.")
    
    # Display current game state
    print(" ".join(display))
    print(stages[lives])
    
    # Check for game end conditions
    if "_" not in display:
        print("\nCongratulations! You found the word!")
        print(logo2)
        end_of_game = True
    elif lives == 0:
        print("Oh no! The figure is complete, you lost.")
        print(f"\nThe correct word was '{chosen_word}'")
        end_of_game = True
