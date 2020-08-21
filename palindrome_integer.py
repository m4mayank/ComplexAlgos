#!/usr/local/bin/python3.7


#Determine whether an integer is a palindrome. Do this without extra space.
#
#A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
#Negative numbers are not palindromic.
#
#Example :
#    Input : 12121
#    Output : 1
#
#    Input : 123
#    Output : 0

def isPalindrome(A):
    A = str(A)
    n = 0
    palindrome = 1
    if len(A)%2==0:
        n = len(A)//2

    if len(A)%2!=0:
        n = (len(A)//2)+1

    for i in range(0, n):
        if A[i] != A[-(i+1)]:
            palindrome = 0
            return 0

    return 1

print(isPalindrome(24))
