#!/usr/local/bin/python3.7

#You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
#f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
#
#For example,
#
#A=[1, 3, -1]
#
#f(1, 1) = f(2, 2) = f(3, 3) = 0
#f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
#f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
#f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5
#
#So, we return 5.

def funct(A):
    result = 0
    first = [A[i]+i for i in range(len(A))]
    second = [A[i]-i for i in range(len(A))]
    first_min, first_max = min(first), max(first)
    second_min, second_max = min(second), max(second)
    return max(first_max - first_min, second_max - second_min)


llist=[-1000000000, -1000000000, -1000000000, -1000000000, -1000000000]
print(funct(llist))
