import json

def load_books():
    try:
        with open('books.json', 'r') as f:
            books = json.load(f)
    except FileNotFoundError:
        books = []
    return books

def save_books(books):
    with open('books.json', 'w') as f:
        json.dump(books, f, indent=4)

def add_book(books):
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    books.append({'title': title, 'author': author, 'read': False})
    print(f'Book "{title}" by {author} added!')

def list_books(books):
    if not books:
        print("No books in your tracker yet.")
        return
    print("\nYour Books:\n")
    for i, book in enumerate(books):
        status = "(Read)" if book['read'] else "(Unread)"
        print(f"{i+1}. {book['title']} by {book['author']} {status}")

def mark_read(books):
    list_books(books)
    if not books:
        return
    try:
        index = int(input("Enter the number of the book to mark as read: ")) - 1
        if 0 <= index < len(books):
            books[index]['read'] = True
            print(f'Book "{books[index]['title']}" marked as read!')
        else:
            print("Invalid book number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    books = load_books()

    while True:
        print("\nBook Tracker Menu:\")
        print("1. Add a book")
        print("2. List all books")
        print("3. Mark a book as read")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            list_books(books)
        elif choice == '3':
            mark_read(books)
        elif choice == '4':
            save_books(books)
            print("Exiting Book Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
