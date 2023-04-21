
import requests
import time
import geopy6
# set API endpoint and parameters
url = 'https://developer.nrel.gov/api/solar/solar_resource/v1.json'
params = {
    'api_key': 'dAWs11PKS61dndfgYMwjHn2NSGBEAYzcnHOzHDsW',
    'lat': geopy6.location.latitude,  # latitude of the location
    'lon': geopy6.location.longitude,  # longitude of the location
    'format': 'json',  # response format
    'attributes': 'ghi',  # only retrieve GHI data
}

# send GET request to the API
response = requests.get(url, params=params)

# check if the request was successful
datadict = []
if response.status_code == 200:
    # extract GHI value from the response JSON
    data = response.json()['outputs']['avg_ghi']
    datadict = data['monthly']
    valuelist = []
    for keys, values in datadict.items():
        valuelist.append((keys,values))

    print(valuelist)
else:
    print("Error:", response.status_code, response.text)
    
seconds = time.time()
something=time.ctime(seconds).split(' ')
Gi = 0
for months in valuelist:

    if something[1].lower() == months[0]:
        Gi = months[1]
print(Gi)