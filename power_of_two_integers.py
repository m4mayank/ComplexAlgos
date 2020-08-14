#!/usr/local/bin/python3.7

#Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

#def isPower(A):
#    if A == 1:
#        return 1
#    for i in range(2, int((A)**(0.5))+1):
#        dividend = A
#        divisor = i
#        while (dividend%divisor) == 0:
#            dividend = dividend // divisor
#            if dividend == 1:
#                return 1
#
#    return 0

def isPower(A):
    for i in range(2, 63):
        num = round((A)**(1/i))
        if ((num)**(i)) == A:
            print(i)
            print(num)
            return 1
    return 0

print(isPower(823543))

