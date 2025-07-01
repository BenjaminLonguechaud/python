class WeekDayError(Exception):
    pass
	

class Weeker:
    __weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    __day = 0

    def __init__(self, day):
        if day in self.__weekdays:
            self.__day = self.__weekdays.index(day)
        else:
            raise WeekDayError

    def __str__(self):
        return self.__weekdays[self.__day]

    def add_days(self, n):
        if isinstance(n, int):
            self.__day = (self.__day + n) % 7

    def subtract_days(self, n):
        if isinstance(n, int):
            self.__day = (self.__day - n) % 7

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")