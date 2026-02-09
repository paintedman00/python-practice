def is_valid_date(year, month, day):
    if not (1 <= month <= 12):
        return False
    if not (1 <= day <= 31):
        return False
    if month in [4, 6, 9, 11] and day == 31:
        return False
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    return True

def calculate_age(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    age = current_year - birth_year
    if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
        age -= 1
    return age

if __name__ == "__main__":
    try:
        birth_year = int(input("Birth Year: "))
        birth_month = int(input("Birth Month: "))
        birth_day = int(input("Birth Day: "))
        current_year = int(input("Current Year: "))
        current_month = int(input("Current Month: "))
        current_day = int(input("Current Day: "))

        if not (1900 <= birth_year <= current_year <= 2100): # Reasonable year range
            print("Error: Invalid year(s). Year must be between 1900 and 2100.")
        elif not is_valid_date(birth_year, birth_month, birth_day):
            print("Error: Invalid birthdate.")
        elif not is_valid_date(current_year, current_month, current_day):
            print("Error: Invalid current date.")
        elif (current_year, current_month, current_day) < (birth_year, birth_month, birth_day):
            print("Error: Current date cannot be before birth date.")
        else:
            age = calculate_age(birth_year, birth_month, birth_day, current_year, current_month, current_day)
            print(f"\nAge: {age} years")

    except ValueError:
        print("Error: Invalid input. Please enter integers for year, month, and day.")
