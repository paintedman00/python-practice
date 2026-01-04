def add_item(shopping_list, item):
    """Adds an item to the shopping list."""
    shopping_list.append(item)
    print(f"Added {item} to the shopping list.")


def remove_item(shopping_list, item):
    """Removes an item from the shopping list."""
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed {item} from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")


def list_items(shopping_list):
    """Lists all items in the shopping list."""
    if not shopping_list:
        print("Shopping list is empty.")
    else:
        print("Shopping List:")
        for i, item in enumerate(shopping_list):
            print(f"{i+1}. {item}")


def clear_list(shopping_list):
    """Clears the entire shopping list."""
    shopping_list.clear()
    print("Shopping list cleared.")


def main():
    """Main function to run the shopping list application."""
    shopping_list = []
    print("Welcome to the Simple Shopping List!")

    while True:
        command = input("> ").lower().split()

        if not command:
            continue

        action = command[0]

        if action == "add":
            if len(command) > 1:
                item = " ".join(command[1:])
                add_item(shopping_list, item)
            else:
                print("Please specify an item to add.")

        elif action == "remove":
            if len(command) > 1:
                item = " ".join(command[1:])
                remove_item(shopping_list, item)
            else:
                print("Please specify an item to remove.")

        elif action == "list":
            list_items(shopping_list)

        elif action == "clear":
            clear_list(shopping_list)

        elif action == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid command. Available commands: add, remove, list, clear, exit")


if __name__ == "__main__":
    main()
