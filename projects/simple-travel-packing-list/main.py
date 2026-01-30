def add_item(packing_list, item, quantity):
    """Adds an item and its quantity to the packing list."""
    if not isinstance(quantity, int) or quantity <= 0:
        print("Invalid quantity. Please enter a positive integer.")
        return packing_list
    packing_list[item] = quantity
    return packing_list


def display_list(packing_list):
    """Displays the current packing list."""
    if not packing_list:
        print("Your packing list is empty.")
        return
    print("\nYour Packing List:\n")
    for item, quantity in packing_list.items():
        print(f"{item}: {quantity}")
    print()


def main():
    """Main function to run the packing list program."""
    packing_list = {}

    while True:
        print("Options:")
        print("1. Add item")
        print("2. View list")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            item = input("Enter item to add: ").strip()
            if not item:
                print("Item cannot be empty.")
                continue
            while True:
                try:
                    quantity = int(input("Enter quantity: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            packing_list = add_item(packing_list, item, quantity)
        elif choice == '2':
            display_list(packing_list)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()
