import datetime

def get_birthdate():
    while True:
        try:
            year = int(input("Enter your birth year (YYYY): "))
            month = int(input("Enter your birth month (MM): "))
            day = int(input("Enter your birth day (DD): "))
            birthdate = datetime.date(year, month, day)
            return birthdate
        except ValueError:
            print("Invalid date. Please enter a valid date in YYYY MM DD format.")


def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def main():
    print("Welcome to the Simple Age Calculator!")
    birthdate = get_birthdate()
    age = calculate_age(birthdate)
    print(f"You are {age} years old.")

if __name__ == "__main__":
    main()
