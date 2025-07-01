
def read_int(prompt, min, max):
    valid = False
    while not valid:
        try:
            a = int(input(prompt))
            assert a < max and a > min
            valid = True
        except ValueError:
            print("Error: wrong input")
        except:
            print("Error: the value is not within permitted range (min..max)")
    return a


class QueueError(IndexError):  # Choose base class for the new exception.
    def __init__(self):
        self.message = "Queue error"
        super().__init__(self.message)

class QueueError2(IndexError):  # Choose base class for the new exception.
    pass

class Queue:
    def __init__(self):
        self.__queue_list = []

    def put(self, elem):
        self.__queue_list.append(elem)

    def get(self):
        try:
            if len(self.__queue_list) < 1:
                raise QueueError
                # raise QueueError2
            val = self.__queue_list[0]
            del self.__queue_list[0]
            return val
        except QueueError2: # Does not prevent the function from returning None!!!
            print("Queue2 error")


print(__name__)