#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3

#Given a binary tree A with N nodes.
#You have to remove all the half nodes and return the final binary tree.
#
#NOTE:
#    Half nodes are nodes which have only one child.
#    Leaves should not be touched as they have both children as NULL.

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

def RemoveHalfNodes(node):
    if not node:
        return node

    if node.left == None and node.right:
        return RemoveHalfNodes(node.right)

    if node.right == None and node.left:
        return RemoveHalfNodes(node.left)

    if bool(node.left) == bool(node.right):
        if node.left and node.right:
            node.left = RemoveHalfNodes(node.left)
            node.right = RemoveHalfNodes(node.right)
        return node
    #if node.left == None and node.right == None:
    #    return node

    #node.left = RemoveHalfNodes(node.left)
    #node.right = RemoveHalfNodes(node.right)
    #return node
root = Node(12)
llist = [6,5,8,7,15,14,16,17]
for i in llist:
    root.insert(i)

PrintTree(root)
print("after removal")
RemoveHalfNodes(root)
PrintTree(root)
