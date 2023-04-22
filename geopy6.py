import ephem # pip install pyephem (on Python 2)
             # pip install ephem   (on Python 3)
def main():
    observer = ephem.Observer()
    observer.lat, observer.long = 45.5579451, -94.16324039999999
    print(solartime(observer=observer))

def solartime(observer, sun=ephem.Sun()):
    sun.compute(observer)
    # sidereal time == ra (right ascension) is the highest point (noon)
    hour_angle = observer.sidereal_time() - sun.ra
    return ephem.hours(hour_angle + ephem.hours('12:00')).norm  # norm for 24h

main()