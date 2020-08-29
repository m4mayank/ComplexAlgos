#!/usr/local/bin/python3.7

#Given 2 non negative integers m and n, find gcd(m, n)
#
#GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
#Both m and n fit in a 32 bit signed integer.
#
#
#Example:
#m : 6
#n : 9
#
#GCD(m, n) : 3

import bisect

#def gcd(A, B):
#    llist = []
#    smaller = min(A,B)
#    larger = max(A,B)
#    if smaller == 0:
#        return larger
#    if A == 1 or B == 1:
#        return 1
#    else:
#        for i in range(1,int((smaller)**(0.5))+1):
#            if smaller%i == 0:
#                if larger%i == 0:
#                    bisect.insort(llist, i)
#                if i != (smaller)**(0.5):
#                    j = smaller//i
#                    if larger%j == 0:
#                        bisect.insort(llist, j)
#    print(llist)
#    return llist[-1]


#****Most Optimised Solution****
#Came across this solution while i was solving another problem
def gcd(A, B):
    while (B!=0):
        A, B = B, A%B

    return A

llist = gcd(2, 0)
print(llist)
