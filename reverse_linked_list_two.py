#!/usr/local/bin/python3.7

#Reverse a linked list from position m to n. Do it in-place and in one-pass.
#For example:
#    Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#    return 1->4->3->2->5->NULL.



# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

def reverse(A, B, C):
    start_node = ListNode(None)
    last_node = ListNode(None)
    head = A
    count = 1
    prev = ListNode(None)
    started_at_bottom = False
    if B == 1:
        started_at_bottom = True
    while A.next:
        curr = A
        A = A.next
        if count == B:
            start_node = prev
            last_node = curr
        if count >= B:
            curr.next = prev
        prev = curr
        if count == C:
            if B == 1:
                start_node = curr
                head = start_node
            else:
                start_node.next = curr
            last_node.next = A
            count = count - 1
            break
        count = count + 1

    if count == C:
        A.next = prev
        start_node.next = A
        last_node.next = None
        if started_at_bottom:
            return A

    return head
