#!/usr/local/bin/python3.7

Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:
    Expected solution is linear in time and constant in space.

For example,
    List 1-->2-->1 is a palindrome.
    List 1-->2-->3 is not a palindrome.

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

def lPalin(A):
    l = []
    n = 0
    while A.next:
        l.append(A.val)
        A = A.next
    l.append(A.val)

    if len(l)%2==0:
        n = len(l)//2

    if len(l)%2!=0:
        n = (len(l)//2)+1

    for i in range(0, n):
        if l[i] != l[-(i+1)]:
            return 0

    return 1
