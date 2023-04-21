from geopy.geocoders import GoogleV3
from timezonefinder import TimezoneFinder
import datetime
import pytz
from Requests import extract_hour


def main():

    # Define the address for which you want to find the timezone
    geolocator = GoogleV3(api_key="AIzaSyAOlXE709gmbTW4gPyVGCxS33Px4pYlnGo")
    place = "Old Trafford"
    location = geolocator.geocode(place)



    # Create a timezone finder object and get the timezone at the location coordinates
    tf = TimezoneFinder()
    timezone = tf.timezone_at(lng=location.longitude, lat=location.latitude)

    print(time_diff(timezone))

def time_diff(string):
    tz1 = pytz.timezone('US/Mountain')  # MDT
    tz2 = pytz.timezone(f'{string}')  # EDT

    # Get the current time in each time zone
    now1 = extract_hour(str(datetime.datetime.now(tz1)))

    now2 = extract_hour(str(datetime.datetime.now(tz2)))


    # Calculate the time difference in hours
    return (int(now2) - int(now1))

    

    

if __name__ == "__main__":
    main()