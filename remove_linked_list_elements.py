#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3

# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode(-1)
        new_head.next = head
        prev = new_head
        current = head
        while current!=None:
            if current.val == val:
                prev.next = current.next
                current = current.next
            else:
                prev = prev.next
                current = current.next
        
        return new_head.next