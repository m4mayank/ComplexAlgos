#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

def PrintTree(node):
    if node.left:
        PrintTree(node.left)

    print(node.data)

    if node.right:
        PrintTree(node.right)

class BSTIterator:
    def __init__(self, root):
        self.stack = [root]
        self.counter = 0
        self.value = 0
        self.nextVal = None

    def kthsmallest(self):
        while self.stack:
            node = self.stack.pop()
            if not node:
                return node
            if not node.left and not node.right:
                self.counter += 1
                if self.counter == self.value:
                    return node.data
            else:
                if node.right:
                    self.stack.append(node.right)
                    node.right = None
                self.stack.append(node)
                if node.left:
                    self.stack.append(node.left)
                    node.left = None

    def hasNext(self):
        #self.counter = 0
        self.value += 1
        self.nextVal = self.kthsmallest()
        if self.nextVal != None:
            return True
        else:
            return False

    def next(self):
        return self.nextVal


root = Node(12)
llist = [5,1,87,40,10]
for i in llist:
    root.insert(i)

i = BSTIterator(root)

while i.hasNext():
    print(i.next())
