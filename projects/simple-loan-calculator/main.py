def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_monthly_payment(loan_amount, interest_rate, loan_term):
    monthly_interest_rate = interest_rate / 100 / 12
    number_of_payments = loan_term * 12

    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / number_of_payments
    else:
        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-number_of_payments))

    return monthly_payment


if __name__ == "__main__":
    print("Simple Loan Calculator")
    print("----------------------")

    loan_amount = get_float_input("Loan Amount: ")
    interest_rate = get_float_input("Interest Rate (annual %): ")
    loan_term = get_float_input("Loan Term (years): ")

    monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term)

    print("\nMonthly Payment: ${:.2f}".format(monthly_payment))
