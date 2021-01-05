#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Example 3:
# Input: root = []
# Output: 0

# Example 4:
# Input: root = [0]
# Output: 1

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterative(self, root, count):
        if root.left == None and root.right == None:
            return 1
        l = 0
        r = 0
        if root.left:
            l = self.iterative(root.left, count)
        if root.right:
            r = self.iterative(root.right, count)
        
        if l > r:
            return l + count
        else:
            return r + count
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.iterative(root, 1)