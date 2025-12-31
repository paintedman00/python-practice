def add_book(catalog):
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    if not title or not author:
        print("Error: Title and author are required.")
        return
    catalog[title] = author
    print(f"{title} by {author} added to the catalog.")

def list_books(catalog):
    if not catalog:
        print("The catalog is empty.")
        return
    print("Book Catalog:")
    for title, author in catalog.items():
        print(f"- {title} by {author}")

def search_book(catalog):
    search_term = input("Enter the title to search for: ")
    found = False
    for title, author in catalog.items():
        if search_term.lower() in title.lower():
            print(f"Found: {title} by {author}")
            found = True
    if not found:
        print(f"No book found with title containing '{search_term}'.")

def main():
    book_catalog = {}
    while True:
        print("\nOptions: add, list, search, exit")
        command = input("Enter a command: ").lower()

        if command == "add":
            add_book(book_catalog)
        elif command == "list":
            list_books(book_catalog)
        elif command == "search":
            search_book(book_catalog)
        elif command == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
