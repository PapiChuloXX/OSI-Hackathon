from geopy.geocoders import GoogleV3
import geopy.distance
import googlemaps

geolocator = GoogleV3(api_key="AIzaSyAOlXE709gmbTW4gPyVGCxS33Px4pYlnGo")
place = "St. Cloud"
location = geolocator.geocode(place)

print(location.address)
print(location.latitude, location.longitude)