def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_budget_summary(income, expenses):
    total_income = sum(income)
    total_expenses = sum(expenses)
    balance = total_income - total_expenses

    print("\n--- Budget Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")


if __name__ == "__main__":
    income = []
    expenses = []

    while True:
        print("\nOptions:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Budget Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = get_valid_float_input("Enter income amount: $")
            income.append(amount)
        elif choice == '2':
            amount = get_valid_float_input("Enter expense amount: $")
            expenses.append(amount)
        elif choice == '3':
            display_budget_summary(income, expenses)
        elif choice == '4':
            print("Exiting Budget Tracker.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
