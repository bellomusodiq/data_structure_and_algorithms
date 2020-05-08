class ArrayIndexError(Exception):
    def __init__(self, ):
        Exception.__init__(self, "Index error, invalid index was specified")


class Array():
    """
    This is an array class.
    You can perform the following options: create array, add item, remove item, update item,
    get length of array, lookup, append, insert
    """
    def check_item(self, index):
        item = self.array.get(index)
        if item:
            return item
        raise ArrayIndexError

    def __init__(self, *args):
        self.length = 0
        self.array = {}
        if len(args) > 0:
            for i in range(len(args)):
                self.array[i] = args[i]
                self.length += 1

    def append(self, item):
        self.array[self.length] = item
        self.length += 1

    def remove(self, index):
        item = self.check_item(index)
        del item
        self.length -= 1

    def pop(self):
        item = self.check_item(self.length - 1)
        del item
        self.length -= 1

    def __str__(self):
        res = '['
        for i in range(self.length):
            res = res + ' ' + str(self.array[i])
            if i != (self.length - 1): res += ','
        res += ' ]'
        return res

    def get(self, index):
        item = self.check_item(index)
        return item

    def replace(self, index, item):
        self.check_item(index)
        self.array[index] = item

    def insert(self, index, item):
        self.check_item(index)
        i = self.length
        while i > index:
            self.array[i] = self.array[i - 1]
            i -= 1
        self.array[index] = item
        self.length += 1

    def prepend(self, item):
        self.insert(0, item)

    def delete(self, index):
        self.check_item(index)
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i+1]
        self.length -= 1


arr = Array(1, 2, 3)
print(arr)
arr.prepend(100)
print(arr)
arr.delete(2)
print(arr)
# arr.pop()
# print(arr)

