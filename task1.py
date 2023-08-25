class Q:
    def __init__(self):
        self.elements = []

    def insert(self, value):
        self.elements.append(value)

    def pop(self):
        if not self.is_empty():
            return self.elements.pop(0)
        else:
            print("The queue is already empty")
            return None

    def is_empty(self):
        return len(self.elements) == 0



q= Q()
q.insert(5)
q.insert(2)
q.insert(3)

print(q.pop())

