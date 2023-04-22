import SolarTime
import time
import math
import geopy6
#calculates daily power in Kilowatts

#calculates the hour angle of the sun 
Hour_angle = 15*(int(SolarTime.Solartime[0])-12)
#gets number of days so far in the year
seconds = time.time()
time1=time.localtime(seconds)
#get Declination Angle
decAngle= math.degrees(0.408407)*math.cos(360/365*(time1[7]+10))
#get elevation angle
elevAngle = (math.sin(decAngle) * math.sin(geopy6.location.latitude)) + (math.cos(decAngle) * math.cos(geopy6.location.latitude) * math.cos(Hour_angle))
#Variable that holds the value of the solar Constant
solarConstant = 1367
#get Incident Solar Radiation
incidentSolarRadiation = solarConstant * math.cos(90-elevAngle)
#get estimated wattage for the day
estimated_Wattage = incidentSolarRadiation * .2 * area

