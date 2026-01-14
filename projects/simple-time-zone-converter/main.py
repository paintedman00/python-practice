def convert_time(time, source_tz, target_tz):
    """Converts time from source timezone to target timezone."""
    timezones = {
        "UTC": 0,
        "EST": -5,
        "PST": -8,
        "MST": -7,
        "GMT": 0
    }

    if source_tz not in timezones or target_tz not in timezones:
        return "Invalid time zone(s)."

    try:
        hours, minutes = map(int, time.split(':'))
        if not (0 <= hours <= 23 and 0 <= minutes <= 59):
            return "Invalid time format. Use HH:MM format."
    except ValueError:
        return "Invalid time format. Use HH:MM format."

    source_offset = timezones[source_tz]
    target_offset = timezones[target_tz]

    total_minutes = hours * 60 + minutes
    utc_minutes = total_minutes - source_offset * 60
    target_minutes = utc_minutes + target_offset * 60

    target_hours = (target_minutes // 60) % 24
    target_minutes = target_minutes % 60

    return f"{target_hours:02d}:{target_minutes:02d}"


def main():
    """Main function to get input and print the converted time."""
    time = input("Enter time in HH:MM format: ")
    source_tz = input("Enter source time zone (UTC, EST, PST, MST, GMT): ").upper()
    target_tz = input("Enter target time zone (UTC, EST, PST, MST, GMT): ").upper()

    result = convert_time(time, source_tz, target_tz)

    if result.startswith("Invalid"):
        print(result)
    else:
        print(f"{time} {source_tz} is {result} {target_tz}")


if __name__ == "__main__":
    main()
