def add_book(catalog):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    while True:
        try:
            year = int(input("Enter the publication year: "))
            if year > 0:
                break
            else:
                print("Invalid year. Please enter a positive integer.")
        except ValueError:
            print("Invalid year. Please enter a number.")

    catalog.append({"title": title, "author": author, "year": year})
    print("Book added successfully!")


def view_books(catalog):
    if not catalog:
        print("The catalog is empty.")
        return

    print("\n--- Book Catalog ---")
    for i, book in enumerate(catalog):
        print(f"{i+1}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    print("------------------\n")

def search_books(catalog):
    search_term = input("Enter the title or author to search for: ").lower()
    results = []
    for book in catalog:
        if search_term in book['title'].lower() or search_term in book['author'].lower():
            results.append(book)

    if not results:
        print("No books found matching your search.")
        return

    print("\n--- Search Results ---")
    for i, book in enumerate(results):
        print(f"{i+1}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    print("----------------------\n")


def main():
    book_catalog = []

    while True:
        print("\n--- Book Catalog Menu ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

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
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
