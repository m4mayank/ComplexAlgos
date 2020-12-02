#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 

# Given A : [1, 2, 3]
# A height balanced BST  : 

#       2
#     /   \
#    1     3

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if data < root.data:
        if root.left is None:
            root.left = Node(data)
        else:
            insert(root.left, data)
    elif data > root.data:
        if root.right is None:
            root.right = Node(data)
        else:
            insert(root.right, data)

def sortedArrayToBST(A):
        if len(A) == 0:
            return None
        mid = len(A)//2
        root = Node(A[mid])
        root.left = sortedArrayToBST(A[:mid])
        root.right = sortedArrayToBST(A[mid+1:])
        return root

def PrintTree(node):
    if node.left:
        PrintTree(node.left)

    print(node.data)

    if node.right:
        PrintTree(node.right)



array = [1,2,3,4,5,6,7,8,9]
root = sortedArrayToBST(array)
PrintTree(root)

