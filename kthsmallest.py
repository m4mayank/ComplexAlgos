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

def kthsmallest(root, k):
    stack = [root]
    counter = 0
    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            counter += 1
            if counter == k:
                return node.data
        else:
            if node.right:
                stack.append(node.right)
                node.right = None
            stack.append(node)
            if node.left:
                stack.append(node.left)
                node.left = None


root = Node(12)
llist = [5,1,87,40,10]
for i in llist:
    root.insert(i)

PrintTree(root)

print(f"Kth smallest element is :{kthsmallest(root, 2)}")
