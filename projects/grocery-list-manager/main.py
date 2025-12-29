def add_item(grocery_list):
    item = input("Enter the item to add: ")
    if item:
        grocery_list.append(item)
        print(f"{item} added to the list.")
    else:
        print("Invalid input. Item cannot be empty.")

def remove_item(grocery_list):
    if not grocery_list:
        print("The grocery list is empty. Nothing to remove.")
        return

    item = input("Enter the item to remove: ")
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} is not in the list.")

def view_list(grocery_list):
    if not grocery_list:
        print("The grocery list is empty.")
        return

    print("Grocery List:")
    for i, item in enumerate(grocery_list):
        print(f"{i+1}. {item}")

def main():
    grocery_list = []

    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_item(grocery_list)
        elif choice == '2':
            remove_item(grocery_list)
        elif choice == '3':
            view_list(grocery_list)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
