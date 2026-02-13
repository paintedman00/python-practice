def add_transaction(transactions, transaction_type, amount, category):
  """Adds a transaction to the list of transactions."""
  if transaction_type not in ['income', 'expense']:
    print("Invalid transaction type. Must be 'income' or 'expense'.")
    return
  if amount <= 0:
    print("Invalid amount. Must be a positive number.")
    return
  transactions.append({'type': transaction_type, 'amount': amount, 'category': category})
  print("Transaction added successfully.")

def display_summary(transactions):
  """Displays a summary of the income and expenses."""
  total_income = 0
  total_expenses = 0
  for transaction in transactions:
    if transaction['type'] == 'income':
      total_income += transaction['amount']
    elif transaction['type'] == 'expense':
      total_expenses += transaction['amount']
  
  balance = total_income - total_expenses
  
  print("\n--- Summary ---")
  print(f"Total Income: ${total_income:.2f}")
  print(f"Total Expenses: ${total_expenses:.2f}")
  print(f"Balance: ${balance:.2f}")

def main():
  transactions = []

  while True:
    print("\nOptions:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Display Summary")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      try:
        amount = float(input("Enter income amount: "))
        category = input("Enter income category: ")
        add_transaction(transactions, 'income', amount, category)
      except ValueError:
        print("Invalid input. Please enter a number for the amount.")

    elif choice == '2':
      try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        add_transaction(transactions, 'expense', amount, category)
      except ValueError:
        print("Invalid input. Please enter a number for the amount.")

    elif choice == '3':
      display_summary(transactions)

    elif choice == '4':
      print("Exiting...")
      break

    else:
      print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
  main()
