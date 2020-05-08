class LinkedListIndexError(Exception):
    def __init__(self, ):
        Exception.__init__(self, "Index error, invalid index was specified")


class Node:
    def __init__(self, value=None, next_val=None):
        self.value = value
        self.next = next_val


class LinkedList:
    """
    this is a linked list class,
    operations: create empty or non empty linked list, remove item, add item,
    get all items, insert item, append item, prepend item
    """
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.length = 0
        for i in args:
            self.append(i)

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1
            return
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return

    def search(self, index):
        if not self.head:
            return None
        if index == 0:
            return None, self.head
        if index >= self.length:
            raise LinkedListIndexError
        counter = 1
        parent = self.head
        current = self.head.next
        while counter < index:
            parent = current
            current = current.next
            counter += 1
        return parent, current

    def insert(self, index, value):
        parent, current = self.search(index)
        new_node = Node(value, next_val=current)
        parent.next = new_node
        self.length += 1

    def __str__(self):
        res = ''
        current = self.head
        res += str(current.value) + ' -> '
        while current.next:
            current = current.next
            res += str(current.value) + ' -> '
        return res

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return

    def delete(self, index):
        if not self.head:
            raise LinkedListIndexError
        if index == 0:
            val = self.head
            self.head = self.head.next
            self.length -= 1
            return val
        parent, current = self.search(index)
        parent.next = current.next
        self.length -= 1
        return current

    def pop(self):
        self.delete(self.length - 1)

#
# ll = LinkedList(1, 2, 3, 4, 5, 6, 7, 8, 9)
# ll.insert(2,200)
# print(ll)
