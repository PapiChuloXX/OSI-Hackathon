import requests
import json

# Define API key and location
API_KEY = "AIzaSyAOlXE709gmbTW4gPyVGCxS33Px4pYlnGo"
LOCATION = "St. Cloud"

# Define API endpoint and parameters
url = "https://maps.googleapis.com/maps/api/geocode/json"
params = {"address": LOCATION, "key": API_KEY}

# Send API request and parse response
response = requests.get(url, params=params)
data = json.loads(response.text)

# Extract latitude and longitude data and print result
lat = data["results"][0]["geometry"]["location"]["lat"]
lng = data["results"][0]["geometry"]["location"]["lng"]
print(f"The latitude and longitude of {LOCATION} are ({lat}, {lng})")
