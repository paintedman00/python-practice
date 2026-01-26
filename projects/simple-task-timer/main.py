import time


def format_time(seconds):
    """Formats seconds into HH:MM:SS"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"


def start_timer():
    """Starts a timer for a given task."""
    task_name = input("Enter the task name: ")

    if not task_name:
        print("Error: Task name cannot be empty.")
        return

    start_time = time.time()
    print(f"Timer started for task: {task_name}")

    input("Press Enter to stop the timer...")

    end_time = time.time()
    elapsed_time = end_time - start_time

    formatted_time = format_time(elapsed_time)

    print(f"Time spent on task '{task_name}': {formatted_time}")


if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Start Timer")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            start_timer()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
