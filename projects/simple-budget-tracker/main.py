import json

def add_entry(entries, entry_type):
    '''Adds an income or expense entry to the list of entries.'''
    while True:
        try:
            amount = float(input(f'Enter the {entry_type} amount: '))
            if amount <= 0:
                print('Amount must be positive.')
                continue
            break
        except ValueError:
            print('Invalid amount. Please enter a number.')

    description = input(f'Enter a description for the {entry_type}: ')
    entries.append({'type': entry_type, 'amount': amount, 'description': description})
    print(f'{entry_type} added successfully.')


def calculate_balance(entries):
    '''Calculates the current balance based on income and expenses.'''
    balance = 0
    for entry in entries:
        if entry['type'] == 'income':
            balance += entry['amount']
        elif entry['type'] == 'expense':
            balance -= entry['amount']
    return balance


def main():
    '''Main function to run the budget tracker.'''
    entries = []

    while True:
        print('\nOptions:')
        print('1. Add income')
        print('2. Add expense')
        print('3. View balance')
        print('4. Exit')

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            add_entry(entries, 'income')
        elif choice == '2':
            add_entry(entries, 'expense')
        elif choice == '3':
            balance = calculate_balance(entries)
            print(f'Current balance: ${balance:.2f}')
        elif choice == '4':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

if __name__ == '__main__':
    main()
