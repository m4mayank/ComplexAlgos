#!/usr/local/bin/python3.7


#Reverse digits of an integer.
#Example1:
#    x = 123,
#    return 321
#
#Example2:
#    x = -123,
#    return -321
#
#Return 0 if the result overflows and does not fit in a 32 bit signed integer

def reverse(A):
    b = ""
    if A < 0:
        b = "-"
    A = str(A)
    for i in range(len(A)-1,-1,-1):
        if A[i] == "-":
            continue
        b = b+A[i]

    if abs(int(b)) > (1<<31):
        return 0

    return int(b)

print(reverse(-1146467285))
