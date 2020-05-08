import json


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    """
    this is a class for tree data structure
    operations: insert, search, view_tree, delete
    """
    def __init__(self):
        self.root = Node(value=5, left=Node(3), right=Node(10))

    def search(self, value, node=None):
        if not self.root:
            return False
        if not node:
            node = self.root
        if node.value == value:
            return True
        if (value > node.value) and node.right:
            return self.search(value, node=node.right)
        if (value < node.value) and node.left:
            return self.search(value, node=node.left)
        return False

    def insert(self, value, node=None):
        if not self.root:
            self.root = Node(value)
        if not node:
            node = self.root
        if value == node.value:
            return
        if value > node.value:
            if node.right:
                return self.insert(value, node.right)
            node.right = Node(value)
        if value < node.value:
            if node.left:
                return self.insert(value, node.left)
            node.left = Node(value)

    def view_tree(self, node):
        t = {'value': node.value}
        if node.left:
            t['left'] = self.view_tree(node.left)
        else:
            t['left'] = None
        if node.right:
            t['right'] = self.view_tree(node.right)
        else:
            t['right'] = None
        return t

    def __str__(self):
        return json.dumps(self.view_tree(self.root))


tree = BST()
a = tree.search(10)
tree.insert(20)
tree.insert(9)
tree.insert(4)
tree.insert(2)
print(tree)
