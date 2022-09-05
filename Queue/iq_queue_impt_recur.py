class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, data):
        self.stack.append(data)

    def dequeue(self):
        if len(self.stack) == 1:
            return self.stack.pop()

        item = self.stack.pop()

        dequeued_item = self.dequeue()

        self.stack.append(item)

        return dequeued_item

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(15)
print(q.dequeue())
q.enqueue(100)
print(q.dequeue())
print(q.dequeue())