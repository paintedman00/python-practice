def celsius_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    except ValueError:
        return None

def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except ValueError:
        return None

def kilometers_to_miles(kilometers):
    try:
        kilometers = float(kilometers)
        miles = kilometers * 0.621371
        return miles
    except ValueError:
        return None

def miles_to_kilometers(miles):
    try:
        miles = float(miles)
        kilometers = miles * 1.60934
        return kilometers
    except ValueError:
        return None


while True:
    print("\nUnit Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        celsius = input("Enter temperature in Celsius: ")
        fahrenheit = celsius_to_fahrenheit(celsius)
        if fahrenheit is not None:
            print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
        else:
            print("Invalid input. Please enter a number.")
    elif choice == '2':
        fahrenheit = input("Enter temperature in Fahrenheit: ")
        celsius = fahrenheit_to_celsius(fahrenheit)
        if celsius is not None:
            print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")
        else:
            print("Invalid input. Please enter a number.")
    elif choice == '3':
        kilometers = input("Enter distance in Kilometers: ")
        miles = kilometers_to_miles(kilometers)
        if miles is not None:
            print(f"{kilometers} Kilometers is equal to {miles} Miles")
        else:
            print("Invalid input. Please enter a number.")
    elif choice == '4':
        miles = input("Enter distance in Miles: ")
        kilometers = miles_to_kilometers(miles)
        if kilometers is not None:
            print(f"{miles} Miles is equal to {kilometers} Kilometers")
        else:
            print("Invalid input. Please enter a number.")
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
