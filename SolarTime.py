import ephem
import datetime
import math
import geopy6

# Set the observer's location
obs = ephem.Observer()
obs.lat = geopy6.location.latitude   # Latitude of observer in degrees
obs.lon = geopy6.location.longitude   # Longitude of observer in degrees

# Get the current date and time in UTC
utc_datetime = datetime.datetime.utcnow()

# Convert UTC datetime to PyEphem format
obs.date = ephem.Date(utc_datetime)

# Calculate the local sidereal time
lst = obs.sidereal_time()

# Calculate the Equation of Time
sun = ephem.Sun()
sun.compute(obs)
eqt = ephem.hours(sun.ra - lst)

# Calculate the local solar time
solar_time = ephem.Date(obs.date + eqt)

# Print the local solar time in hh:mm:ss format
Solartime = ephem.localtime(solar_time).strftime('%H:%M:%S').split(':')

