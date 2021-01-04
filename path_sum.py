#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterative(self, root, sumi, current_sum):
        if root == None:
            return False
        k = root.val + current_sum
        if root.left == None and root.right == None:
            if sumi == k:
                return True
        return self.iterative(root.left, sumi, k) or self.iterative(root.right, sumi, k)
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.iterative(root, sum, 0)
            
            
