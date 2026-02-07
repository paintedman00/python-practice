def add_book(catalog):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    if not title or not author:
      print("Error: Title and author are required.")
      return
    catalog[title] = author
    print(f'Book "{title}" by {author} added to catalog.')


def list_books(catalog):
    if not catalog:
        print("Catalog is empty.")
        return
    print("Book Catalog:")
    for title, author in catalog.items():
        print(f'  - "{title}" by {author}')


def search_book(catalog):
    search_term = input("Enter title to search for: ")
    found = False
    for title, author in catalog.items():
        if search_term.lower() in title.lower():
            print(f'  - "{title}" by {author}')
            found = True
    if not found:
        print(f'No books found matching "{search_term}".')


def main():
    catalog = {}

    while True:
        print("\nBook Catalog Menu:")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search Book")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_book(catalog)
        elif choice == '2':
            list_books(catalog)
        elif choice == '3':
            search_book(catalog)
        elif choice == '4':
            print("Exiting Book Catalog.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
