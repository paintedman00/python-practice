import time


def clear_screen():
    """Simulates clearing the screen by printing new lines."""
    print("\n" * 100)


def percent_of_number():
    print("Option 1: What is x% of y?\n")
    x = float(input("Enter the value of x (the percentage): "))
    y = float(input("Enter the value of y (the base number): "))
    result = (x * y) / 100
    print(f"\n{x}% of {y} is {result}\n")
    prompt_another_calculation()


def number_as_percent():
    print("Option 2: x is what % of y?\n")
    x = float(input("Enter the value of x: "))
    y = float(input("Enter the value of y: "))
    result = (x * 100) / y
    print(f"\n{x} is {result}% of {y}\n")
    prompt_another_calculation()


def percent_change():
    print("Option 3: What is the % increase/decrease from x to y?\n")
    x = float(input("Enter the starting value (x): "))
    y = float(input("Enter the ending value (y): "))
    change = ((y - x) / x) * 100
    sign = "+" if change >= 0 else "-"
    print(f"\nThere is a {sign}{abs(change)}% change from {x} to {y}\n")
    prompt_another_calculation()


def prompt_another_calculation():
    """Asks the user if they want to do another calculation."""
    response = input("Would you like to perform another calculation? (Y/N): ").strip().lower()
    if response == "y":
        clear_screen()
        main()
    elif response == "n":
        clear_screen()
        print("Thanks for using the Percentage Calculator!")
    else:
        print("\nInvalid input. Please enter 'Y' or 'N'.\n")
        time.sleep(2)
        clear_screen()
        prompt_another_calculation()


def main():
    print("Percentage Calculator - Choose an option:\n")
    print("1. What is x% of y?")
    print("2. x is what % of y?")
    print("3. % increase/decrease from x to y?\n")

    choice = input("Enter your choice (1, 2, or 3): ").strip()
    clear_screen()

    if choice == "1":
        percent_of_number()
    elif choice == "2":
        number_as_percent()
    elif choice == "3":
        percent_change()
    else:
        print("Invalid choice. Please select a valid option.\n")
        time.sleep(2)
        clear_screen()
        main()


if __name__ == "__main__":
    print("Welcome to the Percentage Calculator!\n")
    main()
