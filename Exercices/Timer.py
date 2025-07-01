class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        if isinstance(hours, int) and 0 <= hours < 24:  
            self.__hours = hours
        if isinstance(minutes, int) and 0 <= minutes < 60:
            self.__minutes = minutes
        if isinstance(seconds, int) and 0 <= seconds < 60:  
            self.__seconds = seconds


    def __str__(self):
        hours = str(self.__hours)
        minutes = str(self.__minutes)
        seconds = str(self.__seconds)
        if self.__hours < 10:
            hours = "0" + hours
        if self.__minutes < 10:
            minutes = "0" + minutes
        if self.__seconds < 10:
            seconds = "0" + seconds
        return hours + ":" + minutes + ":" + seconds

    def next_second(self):
        self.__seconds = (self.__seconds + 1) % 60
        if self.__seconds == 0:
            self.__minutes = (self.__minutes + 1) % 60
        if self.__minutes == 0:
            self.__hours = (self.__hours + 1) % 24


    def prev_second(self):
        self.__seconds = (self.__seconds - 1) % 60
        if self.__seconds == 59:
            self.__minutes = (self.__minutes - 1) % 60
        if self.__minutes == 59:
            self.__hours = (self.__hours - 1) % 24


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)