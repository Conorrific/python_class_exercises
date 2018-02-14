from datetime import datetime
time = datetime.now()
day = time.day
month = time.month
year = time.year
second = time.second
minute = time.minute
hour = time.hour
print(time)
print(time.year)
print(time.month)
print(time.day)
print(("today's date is %s/%s/%s") % (day, month, year))
#alternately without first declaring time, day , month variables
print(("today's date is %s/%s/%s") % (time.day, time.month, time.year))
#printing seconds
print(("the time is currently %s:%s:%s") % (hour, minute, second))
#alternately
print(("the time is currently %s:%s:%s") % (time.hour, time.minute, time.second))
#and another way with both combined
print(("current date and time is %s/%s/%s %s:%s:%s") % (month, day, year, hour, minute, second))





