# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_root = ListNode()
        new_node = new_root
        carry = 0
        while l1 and l2:
            linked_sum = (l1.val + l2.val) + carry
            carry = linked_sum//10
            linked_sum = linked_sum%10
            new_node.val = linked_sum
            if l1.next or l2.next or (carry!=0):
                another_node = ListNode()
                new_node.next = another_node
                new_node = new_node.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            linked_sum = l1.val + carry
            carry = linked_sum//10
            linked_sum = linked_sum%10
            new_node.val = linked_sum
            if l1.next or (carry!=0):
                another_node = ListNode()
                new_node.next = another_node
                new_node = new_node.next
            l1 = l1.next
        
        while l2:
            linked_sum = l2.val + carry
            carry = linked_sum//10
            linked_sum = linked_sum%10
            new_node.val = linked_sum
            if l2.next or (carry!=0):
                another_node = ListNode()
                new_node.next = another_node
                new_node = new_node.next
            l2 = l2.next
            
        if carry!=0:
            new_node.val = carry
        
        return new_root