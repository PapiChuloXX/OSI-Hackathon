import datetime
import pytz

def main():
    # Set the time zones you want to compare
    tz1 = pytz.timezone('US/Mountain')  # MDT
    tz2 = pytz.timezone('US/Central')  # EDT

    # Get the current time in each time zone
    now1 = extract_hour(str(datetime.datetime.now(tz1)))
    
    now2 = extract_hour(str(datetime.datetime.now(tz2)))


    # Calculate the time difference in hours
    diff_hours = (int(now2) - int(now1))

    print(f"The time difference between {tz1.zone} and {tz2.zone} is {diff_hours} hours.")

def extract_hour(string):
    date, _ = string.split('.')
    _, time = date.split()
    return (time.split(":"))[0]

if __name__ == "__main__":
    main()
