import json

BOOK_LOG_FILE = 'book_log.json'


def load_book_log():
    try:
        with open(BOOK_LOG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_book_log(book_log):
    with open(BOOK_LOG_FILE, 'w') as f:
        json.dump(book_log, f, indent=4)


def add_book(book_log):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    while True:
        try:
            pages = int(input("Enter the number of pages: "))
            if pages <= 0:
                print("Number of pages must be a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    book = {
        'title': title,
        'author': author,
        'pages': pages
    }
    book_log.append(book)
    print(f"{title} by {author} added to the log.")



def view_book_log(book_log):
    if not book_log:
        print("Your book log is empty.")
        return

    print("\n--- Book Log ---")
    for i, book in enumerate(book_log):
        print(f"{i+1}. {book['title']} by {book['author']} ({book['pages']} pages)")
    print("------------------\n")



def main():
    book_log = load_book_log()

    while True:
        print("\nOptions:")
        print("1. Add a book")
        print("2. View book log")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(book_log)
        elif choice == '2':
            view_book_log(book_log)
        elif choice == '3':
            save_book_log(book_log)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
