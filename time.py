import time

seconds = time.time()
something=time.localtime(seconds)
MMDDYYYY, TIME = time.strftime("%m/%d/%Y, %H:%M:%S", something).split(',')
month, day, year = MMDDYYYY.split('/')
hour, mins,sec = TIME.split(':')

