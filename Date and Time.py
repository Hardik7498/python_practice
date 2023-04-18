# Print current date and time in Python
import datetime

# Print date and time
print(datetime.datetime.now())

# only time
print(datetime.datetime.now().time())

#Convert string into a datetime object
from datetime import datetime

date_string = "Feb 25 2020  4:20PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)

#Subtract a week (7 days)  from a given date in Python
from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)
print("Given date")
print(given_date)

days_to_subtract = 7
res_date = given_date - timedelta(days=days_to_subtract)
print("New Date")
print(res_date)

#Print a date in a the following format
from datetime import datetime

given_date = datetime(2020, 2, 25)
print("Given date is")
print(given_date.strftime('%A %d %B %Y'))

# Find the day of the week of a given date
import calendar
from datetime import datetime

given_date = datetime(2020, 7, 26)
weekday = calendar.day_name[given_date.weekday()]
print(weekday)

# Add a week (7 days) and 12 hours to a given date
from datetime import datetime, timedelta

given_date = datetime(2020, 3, 22, 10, 00, 00)
print("Given date")
print(given_date)

days_to_add = 7
res_date = given_date + timedelta(days=days_to_add, hours=12)
print("New Date")
print(res_date)

#Print current time in milliseconds
import time

milliseconds = int(round(time.time() * 1000))
print(milliseconds)

#Convert the following datetime into a string
from datetime import datetime

given_date = datetime(2020, 2, 25)
string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string_date)

#Calculate the date 4 months from the current date
from datetime import datetime

from dateutil.relativedelta import relativedelta

# 2020-02-25
given_date = datetime(2020, 2, 25).date()

months_to_add = 4
new_date = given_date + relativedelta(months=+ months_to_add)
print(new_date)

#Calculate number of days between two given dates
from datetime import datetime

# 2020-02-25
date_1 = datetime(2020, 2, 25).date()
# 2020-09-17
date_2 = datetime(2020, 9, 17).date()

delta = None
if date_1 > date_2:
    print("date_1 is greater")
    delta = date_1 - date_2
else:
    print("date_2 is greater")
    delta = date_2 - date_1
print("Difference is", delta.days, "days")
