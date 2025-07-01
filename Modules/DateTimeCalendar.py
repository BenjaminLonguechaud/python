from datetime import date
from datetime import datetime
from datetime import timedelta
from datetime import time as tm
import time

def showToday():
    today = date.today()
    print("Today:", today)
    print("Year:", today.year)
    print("Month:", today.month)
    print("Day:", today.day)
    if(today.isoweekday()):
        print("Work day: ", today.weekday())
    else:
        print("Weekend!: ", today.weekday())
    new_today = today.replace(year=2020)
    print("Year:", new_today.year)

def showMyBirthday():
    my_birthday = date(1988, 2, 27)
    my_birthday = date.fromisoformat('1988-02-27')
    print(my_birthday)
    print(my_birthday.strftime('%Y/%m/%d'))

def showTimeClass():
    timestamp = time.time()
    d = date.fromtimestamp(timestamp)
    print("Date:", d)
    print("Timestamp:", timestamp)
    st = time.gmtime(timestamp)
    # Converts a struct_time object or a tuple to a string.
    print(time.asctime(st))
    # Converts a struct_time object or a tuple that expresses the local time to the number of seconds since the Unix epoch.
    print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))
    # Returns a string representing date and time using date, time or datetime object.
    stc = time.strftime("%Y/%m/%d %H:%M:%S", st)
    print(stc)
    # Creates a datetime object from the given string.
    print(time.strptime(stc, "%Y/%m/%d %H:%M:%S"))

def showDateTime():
    dt = datetime(2019, 11, 4, 14, 53)
    print("Datetime:", dt)
    print("Date:", dt.date())
    print("Time:", dt.time())
    print("today:", datetime.today())
    print("now:", datetime.now())
    print("utcnow:", datetime.utcnow())
    print(dt.strftime("%y/%B/%d %H:%M:%S"))

# timedelta object
def showTimeOperator():
    d1 = date(2020, 11, 4)
    d2 = date(2019, 11, 4)
    print(d1 - d2)

def showDateTimeExercise():
    dt = datetime(2020, 11, 4, 14, 53)
    print(dt.strftime("%Y/%m/%d %H:%M:%S"))
    print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
    print(dt.strftime("%a, %Y %b %d"))
    print(dt.strftime("%A, %Y %B %d"))
    print("Weekday: ", dt.weekday())
    print("Day of the year: ", (dt - datetime(2020, 1, 1, 0, 0)).days + 1)
    print("Week number of the year: ", dt.isocalendar()[1])

import calendar

def showCalendar():
    print(calendar.calendar(2020))
    print(calendar.month(2020, 2))
    print(calendar.weekday(2022, 1, 26))

def createCalendar():
    c = calendar.Calendar(calendar.MONDAY)
    for date in c.itermonthdates(2019, 11):
        print(date, end=" ")

# showToday()
# showMyBirthday()
# showTimeClass()
# showDateTime()
# showTimeOperator()
# showDateTimeExercise()
# showCalendar()
#createCalendar()

dateTime = datetime(2019,11,27,11,27,22)
dateTime2 = datetime(2019,11,27,0,0,0)
print(dateTime-dateTime2)