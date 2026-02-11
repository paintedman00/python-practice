def add_book(catalog):
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    if not title or not author:
        print("Error: Title and author are required.")
        return catalog

    catalog.append({"title": title, "author": author})
    print(f"Book '{title}' by {author} added to the catalog.")
    return catalog

def view_catalog(catalog):
    if not catalog:
        print("The catalog is empty.")
        return

    print("\n--- Book Catalog ---")
    for i, book in enumerate(catalog):
        print(f"{i+1}. {book['title']} by {book['author']}")
    print("--------------------\n")

def main():
    catalog = []

    while True:
        print("\nOptions:")
        print("1. Add a book")
        print("2. View catalog")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            catalog = add_book(catalog)
        elif choice == '2':
            view_catalog(catalog)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
