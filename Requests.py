import requests
import json

# Define API key and location
API_KEY = "453cee262bc66f1fc5dac26338a9a09f"
LOCATION = "Lagos"

# Define API endpoint and parameters
url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": LOCATION, "appid": API_KEY}

# Send API request and parse response
response = requests.get(url, params=params)
data = json.loads(response.text)

# Extract cloud coverage data and print result
cloud_coverage = data["clouds"]["all"]
print(f"The current cloud coverage in {LOCATION} is {cloud_coverage}%")
