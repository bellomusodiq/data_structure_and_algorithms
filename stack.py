from linked_list import LinkedList

class Stack:
    """
    this class is use to create a stack data structure
    operations: push, pop, peek
    """

    def __init__(self):
        self.stack = LinkedList()

    def push(self, value):
        self.stack.prepend(value)

    def pop(self):
        item = self.stack.delete(0)
        return item

    def peek(self):
        item = self.stack.head.value
        return item

    def __str__(self):
        return self.stack.__str__()


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
i = stack.peek()
print(i)
stack.pop()
print(stack)
