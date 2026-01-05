import json

def load_notes():
    try:
        with open('notes.json', 'r') as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = {}
    return notes

def save_notes(notes):
    with open('notes.json', 'w') as f:
        json.dump(notes, f, indent=4)

def add_note(notes):
    title = input("Enter note title: ")
    if not title:
        print("Title cannot be empty.")
        return
    content = input("Enter note content: ")
    if not content:
        print("Content cannot be empty.")
        return
    notes[title] = content
    print("Note added.")

def view_notes(notes):
    if not notes:
        print("No notes found.")
        return
    print("\nAvailable Notes:")
    for title in notes:
        print(f"- {title}")
    
    title_to_view = input("Enter the title of the note you want to view (or press Enter to go back): ")
    if not title_to_view:
        return
    
    if title_to_view in notes:
        print(f"\n--- {title_to_view} ---")
        print(notes[title_to_view])
        print("---------------------\n")
    else:
        print("Note not found.")


def main():
    notes = load_notes()

    while True:
        print("\nSimple Note Taker")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_note(notes)
        elif choice == '2':
            view_notes(notes)
        elif choice == '3':
            save_notes(notes)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
