from art import logo

# Basic arithmetic operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

# Operation symbol to function mapping
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    print(logo)
    while True:
        try:
            num1 = float(input("What is the first number?: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        while True:
            print("\nAvailable operations:")
            for symbol in operations:
                print(symbol)
            
            operation = input("Pick an operation: ")
            if operation not in operations:
                print("Invalid operation. Try again.")
                continue

            try:
                num2 = float(input("What is the next number?: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            result = operations[operation](num1, num2)
            print(f"\n{num1} {operation} {num2} = {result}")

            next_step = input(
                "\nType 'y' to continue with this result, 'n' to exit, or 'new' to start a new calculation: ").lower()
            
            if next_step == 'y':
                num1 = result if isinstance(result, float) else 0  # Avoid carrying error messages
            elif next_step == 'new':
                break  # Break inner loop, restart outer loop
            elif next_step == 'n':
                print("Goodbye!")
                return
            else:
                print("Invalid input. Exiting.")
                return

# Start the calculator
calculator()
