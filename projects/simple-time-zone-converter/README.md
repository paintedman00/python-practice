# Simple Time Zone Converter

This is a simple command-line tool to convert a given time from one time zone to another.

## Usage

Run `python main.py` and follow the prompts to enter the time, source time zone, and target time zone.

## Supported Time Zones

This tool supports a limited set of time zones:

*   UTC
*   EST
*   PST
*   MST
*   GMT

## Example

```
$ python main.py
Enter time in HH:MM format: 14:30
Enter source time zone (UTC, EST, PST, MST, GMT): UTC
Enter target time zone (UTC, EST, PST, MST, GMT): PST
14:30 UTC is 07:30 PST
```
