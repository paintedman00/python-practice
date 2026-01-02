def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    if not name or not phone or not email:
        print("Error: All fields are required.")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contacts ---")
    for i, contact in enumerate(contacts):
        print(f"{i+1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print("---------------")


def search_contact(contacts):
    search_term = input("Enter name to search for: ")
    found = False
    for contact in contacts:
        if search_term.lower() in contact['name'].lower():
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
    if not found:
        print("No contact found with that name.")


def main():
    contacts = []

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
