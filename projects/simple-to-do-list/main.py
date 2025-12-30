import json

TODO_FILE = 'todo.json'


def load_todos():
    try:
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)


def add_todo(todos, task):
    todos.append({'task': task, 'completed': False})
    return todos


def mark_complete(todos, index):
    if 0 <= index < len(todos):
        todos[index]['completed'] = True
    return todos


def display_todos(todos):
    if not todos:
        print('No tasks in the to-do list.')
        return

    for i, todo in enumerate(todos):
        status = '[x]' if todo['completed'] else '[ ]'
        print(f'{i+1}. {status} {todo["task"]}')


def main():
    todos = load_todos()

    while True:
        print('\nOptions:')
        print('1. Add task')
        print('2. View tasks')
        print('3. Mark task as complete')
        print('4. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            task = input('Enter task: ')
            todos = add_todo(todos, task)
            save_todos(todos)
            print('Task added!')
        elif choice == '2':
            display_todos(todos)
        elif choice == '3':
            display_todos(todos)
            try:
                index = int(input('Enter the task number to mark as complete: ')) - 1
                if 0 <= index < len(todos):
                    todos = mark_complete(todos, index)
                    save_todos(todos)
                    print('Task marked as complete!')
                else:
                    print('Invalid task number.')
            except ValueError:
                print('Invalid input. Please enter a number.')
        elif choice == '4':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
