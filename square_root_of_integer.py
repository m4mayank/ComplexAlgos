#!/usr/local/bin/python3.7

#Given an integar A.
#
#Compute and return the square root of A.
#
#If A is not a perfect square, return floor(sqrt(A)).
#
#DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY
#
#For Example:
#    Input 1:
#        A = 11
#    Output 1:
#        3
#
#    Input 2:
#        A = 9
#    Output 2:
#        3

def sqrt(A):
    def iterativeSqrt(l, h, val):
        low = l
        high = h
        mid = low + ((high-low)//2)
        if low > high:
            return high
        if (mid)**2 > val:
            return iterativeSqrt(low, mid-1, val)
        if (mid)**2 < val:
            return iterativeSqrt(mid+1, high, val)
        if (mid)**2 == val:
            return mid

    b = iterativeSqrt(0, A, A)
    return b

print(f"Answer : {sqrt(20)}")


