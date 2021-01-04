#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3

# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        
        node_queue = [root]
        child_queue = []
        each_level = []
        result = []
        while len(node_queue) != 0:
            for k in node_queue:
                each_level.append(k.val)
                if k.left:
                    child_queue.append(k.left)
                if k.right:
                    child_queue.append(k.right)
            node_queue = child_queue
            result.insert(0, each_level)
            each_level = []
            child_queue = []
        return result
                