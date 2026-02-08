def add_book(catalog):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    catalog[title] = author
    print(f'Book "{title}" by {author} added to the catalog.')


def view_catalog(catalog):
    if not catalog:
        print("The catalog is empty.")
        return
    print("Book Catalog:")
    for title, author in catalog.items():
        print(f'  - "{title}" by {author}')

def search_book(catalog):
    search_term = input("Enter the title to search for: ").lower()
    found = False
    for title, author in catalog.items():
        if search_term in title.lower():
            print(f'Found: "{title}" by {author}')
            found = True
    if not found:
        print(f'No book found matching "{search_term}".')


def main():
    catalog = {}

    while True:
        print("\nOptions:")
        print("1. Add a book")
        print("2. View catalog")
        print("3. Search for a book")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_book(catalog)
        elif choice == '2':
            view_catalog(catalog)
        elif choice == '3':
            search_book(catalog)
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
