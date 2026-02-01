def add_book(catalog):
    title = input("Enter book title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    author = input("Enter author name: ").strip()
    if not author:
        print("Author cannot be empty.")
        return
    catalog[title] = author
    print(f"Book '{title}' by {author} added.")


def list_books(catalog):
    if not catalog:
        print("Catalog is empty.")
        return
    print("\nBook Catalog:")
    for title, author in catalog.items():
        print(f"- '{title}' by {author}")


def search_book(catalog):
    search_term = input("Enter title to search for: ").strip().lower()
    if not search_term:
        print("Search term cannot be empty.")
        return
    found = False
    for title, author in catalog.items():
        if search_term in title.lower():
            print(f"Found: '{title}' by {author}")
            found = True
    if not found:
        print("No books found matching that title.")


def main():
    catalog = {}
    while True:
        print("\nOptions:")
        print("1. Add book")
        print("2. List books")
        print("3. Search book")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_book(catalog)
        elif choice == '2':
            list_books(catalog)
        elif choice == '3':
            search_book(catalog)
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
