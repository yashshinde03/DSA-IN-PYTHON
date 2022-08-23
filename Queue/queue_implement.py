class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data

    def peek(self):
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)

q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(5)
q.peek()
q.dequeue()