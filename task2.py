class Queue:
    # class-level variable to keep track of all queue instances
    _all_queues = {}

    def __init__(self, name, size):
        self._name = name
        self._size = size
        self._queue = []

        # register the new instance to the class-level variable
        self._all_queues[name] = self

    def insert(self, value):
        if len(self._queue) < self._size:
            self._queue.append(value)
        else:
            raise QueueOutOfRangeException(f"Queue '{self._name}' is full")

    def pop(self):
        if not self.is_empty():
            return self._queue.pop(0)
        else:
            print(f"Warning: Queue '{self._name}' is empty")
            return None

    def is_empty(self):
        return len(self._queue) == 0

    # class-level method to get a queue instance by its name
    @classmethod
    def get_queue_by_name(cls, name):
        return cls._all_queues.get(name)


class QueueOutOfRangeException(Exception):
    pass



# create a new queue instance
q1 = Queue('q1', 2)

# insert values to the queue
q1.insert(1)
q1.insert(2)

# # try to insert more values than the queue's size
# try:
#     q1.insert(3)
# except QueueOutOfRangeException as e:
#     print(str(e))  # should print "Queue 'q1' is full"

# # pop values from the queue
# print(q1.pop())  # should print 1
# print(q1.pop())  # should print 2
# print(q1.pop())  # should print "Warning: Queue 'q1' is empty" and return None

# # create another queue instance and get the first one using its name
q2 = Queue('q2', 1)
q1 = Queue.get_queue_by_name('q1')
# print(q1)

# insert values to the queues
# q1.insert(1)
q2.insert(2)

# # pop values from the queues
# print(q1.pop())  # should print 1
print(q2.pop())  # should print 2







