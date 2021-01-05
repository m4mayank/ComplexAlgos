#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterative(self, root, llist):
        #count = 1
        if root.left == None and root.right == None:
            return 1
        l = 0
        r = 0
        if root.left:
            l += self.iterative(root.left, llist)
        if root.right:
            r += self.iterative(root.right, llist)
        
        if (l+r) > llist[0]:
            llist[0] = (l+r)
        if l > r:
            return l + 1
        else:
            return r + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        l = [0]
        self.iterative(root, l)
        return l[0]
            
            
            