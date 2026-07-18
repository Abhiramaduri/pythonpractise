#Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime
now=datetime.now()
print(now)

day=now.day
month=now.month
year=now.year
hour=now.hour
minute=now.minute
timestamp=now.timestamp()
print(day,month,year,hour,minute)
print(timestamp)

