def get_input(prompt, input_type=str):
    while True:
        user_input = input(prompt + ": ")
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue
        try:
            if input_type == int:
                int(user_input)
            elif input_type == float:
                float(user_input)
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid {}.".format(input_type.__name__))


def generate_mad_lib(adjective, noun, verb, adverb):
    mad_lib = f"The {adjective} {noun} likes to {verb} {adverb}."
    return mad_lib


if __name__ == "__main__":
    print("Welcome to the Mad Libs Generator!")

    adjective = get_input("Please enter an adjective")
    noun = get_input("Please enter a noun")
    verb = get_input("Please enter a verb")
    adverb = get_input("Please enter an adverb")

    mad_lib = generate_mad_lib(adjective, noun, verb, adverb)

    print("\nHere's your Mad Lib:\n")
    print(mad_lib)
