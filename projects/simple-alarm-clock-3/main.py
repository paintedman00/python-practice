import time
import datetime
import os

def get_alarm_time():
    while True:
        alarm_time_str = input("Enter alarm time (HH:MM): ")
        try:
            datetime.datetime.strptime(alarm_time_str, '%H:%M')
            return alarm_time_str
        except ValueError:
            print("Invalid time format. Please use HH:MM (24-hour).")

def wait_for_alarm(alarm_time):
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        if current_time == alarm_time:
            print("ALARM!")
            # Play a simple beep sound (cross-platform)
            for i in range(3):
                print("BEEP!")
                time.sleep(0.5)
            break
        time.sleep(60) # Check every minute

if __name__ == "__main__":
    alarm_time = get_alarm_time()
    print(f"Alarm set for {alarm_time}")
    wait_for_alarm(alarm_time)
