def add_book(catalog):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    while True:
        try:
            year = int(input("Enter publication year: "))
            if year > 0:
                break
            else:
                print("Year must be a positive number.")
        except ValueError:
            print("Invalid year format. Please enter a number.")

    catalog.append({"title": title, "author": author, "year": year})
    print("Book added successfully!")


def view_books(catalog):
    if not catalog:
        print("Catalog is empty.")
        return

    print("\n--- Book Catalog ---")
    for i, book in enumerate(catalog):
        print(f"{i+1}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    print("------------------\n")

def search_books(catalog):
    search_term = input("Enter search term (title or author): ").lower()
    results = []
    for book in catalog:
        if search_term in book['title'].lower() or search_term in book['author'].lower():
            results.append(book)

    if not results:
        print("No books found matching your search term.")
        return

    print("\n--- Search Results ---")
    for i, book in enumerate(results):
        print(f"{i+1}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    print("----------------------\n")


def main():
    book_catalog = []

    while True:
        print("\n--- Simple Book Catalog ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(book_catalog)
        elif choice == '2':
            view_books(book_catalog)
        elif choice == '3':
            search_books(book_catalog)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
