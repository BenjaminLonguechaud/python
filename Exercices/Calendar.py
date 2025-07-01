from datetime import date
from datetime import datetime
import calendar

class MyCalendar (calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        total = 0
        for month in range(1,13):
            date = datetime(year, month, 1)
            print("Month of " + date.strftime("%B"))
            weeks = self.monthdays2calendar(year, month)
            for week in weeks:
                for days in week:
                    if days[0] > 0 and days[1] == weekday:
                        total += 1
        return total



cal = MyCalendar()
year=2000
weekday=6
numberOfCccurrences = cal.count_weekday_in_year(year, weekday)
print("There are", numberOfCccurrences, calendar.day_name[weekday], "in", year)
