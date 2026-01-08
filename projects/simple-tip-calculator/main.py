def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_tip(bill_amount, tip_percentage):
    tip_amount = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip_amount
    return tip_amount, total_amount


if __name__ == "__main__":
    print("Welcome to the Simple Tip Calculator!")

    bill_amount = get_float_input("Bill amount: ")
    tip_percentage = get_float_input("Tip percentage: ")

    tip_amount, total_amount = calculate_tip(bill_amount, tip_percentage)

    print(f"\nTip amount: ${tip_amount:.2f}")
    print(f"Total amount: ${total_amount:.2f}")
