#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        slow = head
        fast = head
        while fast != None and fast.next != None:
            print(fast.val)
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow != None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        from_front = head
        from_back = prev
        
        while from_front!=None and from_back!=None:
            if from_front.val != from_back.val:
                return False
            from_front = from_front.next
            from_back = from_back.next
        return True