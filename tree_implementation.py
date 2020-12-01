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

root = Node(12)
llist = [5,1,87,40,10]
for i in llist:
    root.insert(i)

PrintTree(root)

