#!/usr/local/bin/python3.7

import sys

def maximumGap(A):
    a=sorted(A)
    max_val = -(sys.maxsize)
    for i in range(1, len(a)):
        diff = a[i]-a[i-1]
        if diff > max_val:
            max_val = diff
    print(max_val)

A=[3, 30, 34, 5, 9]
maximumGap(A)
