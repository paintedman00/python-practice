def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero error!"
    return x / y

def get_number_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation_input():
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in ('+', '-', '*', '/'):
            return operation
        else:
            print("Invalid operation. Please enter +, -, *, or /")

if __name__ == "__main__":
    print("Simple Calculator")
    num1 = get_number_input("Enter first number: ")
    num2 = get_number_input("Enter second number: ")
    operation = get_operation_input()

    if operation == '+':
        print("Result:", add(num1, num2))
    elif operation == '-':
        print("Result:", subtract(num1, num2))
    elif operation == '*':
        print("Result:", multiply(num1, num2))
    elif operation == '/':
        print("Result:", divide(num1, num2))
