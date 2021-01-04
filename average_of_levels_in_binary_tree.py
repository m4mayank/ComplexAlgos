#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root == None:
            return []
        root_queue = [root]
        children_queue = []
        result = []
        while len(root_queue) != 0:
            sumi = 0
            print(len(root_queue))
            for k in root_queue:
                sumi += k.val
                if k.left!=None:
                    children_queue.append(k.left)
                if k.right!=None:
                    children_queue.append(k.right)
            result.append(sumi/len(root_queue))
            root_queue = children_queue
            children_queue = []
        return result