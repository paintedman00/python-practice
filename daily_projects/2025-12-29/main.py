import datetime

def is_valid_integer(input_string):
    """Checks if a string can be converted to a positive integer."""
    try:
        num = int(input_string)
        return num > 0
    except ValueError:
        return False


def calculate_future_date(days_to_add):
    """Calculates the date a specified number of days from December 29, 2025."""
    start_date = datetime.date(2025, 12, 29)
    future_date = start_date + datetime.timedelta(days=days_to_add)
    return future_date.strftime("%Y-%m-%d")


def main():
    """Main function to handle user input and output."""
    print("Welcome to the Future Date Calculator!")
    print("This program calculates the date a specified number of days from December 29, 2025.")

    while True:
        days_input = input("Enter the number of days to add (positive integer): ")

        if is_valid_integer(days_input):
            days_to_add = int(days_input)
            future_date = calculate_future_date(days_to_add)
            print(f"The date {days_to_add} days from December 29, 2025 is: {future_date}")
            break  # Exit the loop after a valid input
        else:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()