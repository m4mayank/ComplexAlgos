#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Here are the two solutions, the second one is more optimised.

#*****************************SOLUTION 1********************************************
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.val >= root.val and q.val <= root.val) or (p.val <= root.val and q.val >= root.val) :
            return root
        if p.val <= root.val and q.val <= root.val:
            answer = self.lowestCommonAncestor(root.left, p, q)
        if p.val >= root.val and q.val >= root.val:
            answer = self.lowestCommonAncestor(root.right, p, q)
        return answer

#*****************************SOLUTION 2********************************************
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node
