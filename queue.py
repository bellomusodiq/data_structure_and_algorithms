from linked_list import LinkedList


class Queue:
    """
    this is a queue class
    operations: enqueue, dequeue, peek
    """
    def __init__(self, *args):
        self.queue = LinkedList(*args)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        self.queue.delete(0)

    def peek(self):
        return self.queue.search(0)[1].value

    def __str__(self):
        return self.queue.__str__()


q = Queue(1, 2, 3)
print(q)
q.enqueue(35)
q.enqueue(35)
q.enqueue(100)
q.enqueue(35)
q.dequeue()
i = q.peek()
print(i)
print(q)
