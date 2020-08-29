#!/usr/local/bin/python3.7

#You are given two positive numbers A and B. You need to find the maximum valued integer X such that:
#    1. X divides A i.e. A % X = 0
#    2. X and B are co-prime i.e. gcd(X, B) = 1
#
#For example,
#A = 30
#B = 12

#We return
#X = 5

#import math
#def cpFact(A, B):
#    if A==1:
#        return A
#
#    if B==1:
#        return A
#
#    llist = []
#
#    smaller = min(A,B)
#    larger = max(A,B)
#
#    if smaller == 0:
#        return larger
#    if smaller == 1 or larger == 1:
#        return 1
#    else:
#        gcd = 0
#        while (gcd!=1):
#            gcd = math.gcd(A,B)
#            A = A//gcd
#    return A


def gcd(A, B):
    while (B!=0):
        A, B = B, A%B
    return A

def cpFact(A, B):
    gcda = 0
    while (gcda!=1):
        gcda = gcd(A,B)
        A = A//gcda
    return A

A=30
B=12
print(cpFact(A,B))
