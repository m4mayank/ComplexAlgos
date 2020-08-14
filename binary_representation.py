#!/usr/local/bin/python3.7

#Given a number N >= 0, find its representation in binary.
#Example:
#    if N = 6,
#    binary form = 110

def findDigitsInBinary(A):
    stri = ""
    if A == 0:
        return 0
    while (A > 0):
        remainder = (A%2)
        stri = str(remainder)+stri
        A = (A//2)
    return stri

print(findDigitsInBinary(536870912))
