def add_item(inventory):
    name = input("Enter item name: ")
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity must be a non-negative integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    inventory[name] = quantity
    print(f"{name} added to inventory with quantity {quantity}.\n")

def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty.\n")
        return
    print("Current Inventory:")
    for name, quantity in inventory.items():
        print(f"- {name}: {quantity}")
    print()

def main():
    inventory = {}
    while True:
        print("Options:")
        print("1. Add item")
        print("2. View inventory")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            view_inventory(inventory)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
