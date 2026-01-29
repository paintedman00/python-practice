import datetime

def get_event_details():
    """Gets the event name and date from the user."""
    while True:
        event_name = input("Enter the event name: ").strip()
        if not event_name:
            print("Event name cannot be empty.")
            continue
        try:
            event_date_str = input("Enter the event date (YYYY-MM-DD): ")
            event_date = datetime.datetime.strptime(event_date_str, "%Y-%m-%d").date()
            return event_name, event_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def calculate_days_remaining(event_date):
    """Calculates the number of days remaining until the event."""
    today = datetime.date.today()
    delta = event_date - today
    return delta.days


if __name__ == "__main__":
    event_name, event_date = get_event_details()
    days_remaining = calculate_days_remaining(event_date)

    if days_remaining < 0:
        print(f"{event_name} already happened {abs(days_remaining)} days ago.")
    elif days_remaining == 0:
        print(f"{event_name} is today!")
    else:
        print(f"Days until {event_name}: {days_remaining}")
