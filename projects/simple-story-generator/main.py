def get_user_input(prompt, validation_func=None):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty.")
            continue
        if validation_func and not validation_func(user_input):
            print("Invalid input.")
            continue
        return user_input


def generate_story(character, setting, problem):
    story = f"In the {setting}, lived {character}. One day, {character} faced a terrible problem: {problem}. Determined to overcome this, {character}...
    (The rest of the story is left to your imagination!)"
    return story


if __name__ == "__main__":
    print("Welcome to the Simple Story Generator!")

    character = get_user_input("Enter a character: ")
    setting = get_user_input("Enter a setting: ")
    problem = get_user_input("Enter a problem: ")

    story = generate_story(character, setting, problem)
    print("\nHere's your story:\n")
    print(story)
