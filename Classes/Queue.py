class QueueError(IndexError):  # Choose base class for the new exception.
    def __init__(self):
        self.message = "Queue error"
        super().__init__(self.message)

class Queue:
    def __init__(self):
        self._queue_list = []

    def put(self, elem):
        self._queue_list.insert(0,elem)

    def get(self):
        if len(self._queue_list) < 1:
            raise QueueError
        val = self._queue_list[-1]
        del self._queue_list[-1]
        return val


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    
    def isempty(self):
        return len(self._queue_list) < 1

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
print(que.__dict__)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")