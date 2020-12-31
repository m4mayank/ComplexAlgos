#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3

# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:

# Input: 1->1->2
# Output: 1->2
# Example 2:

# Input: 1->1->2->3->3
# Output: 1->2->3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dicti = {}
        prev = head
        if head==None:
            return head
        current = head.next
        dicti[prev.val] = 1
        while current!=None:
            if current.val in dicti:
                prev.next = current.next
                current = current.next
            else:
                dicti[current.val] = 1
                prev = prev.next
                current = current.next
        
        return head