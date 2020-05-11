#!/usr/local/bin/python3.7

#Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].
#
#If there is no solution possible, return 0.
#
#Example :
#    A : [3 5 4 2]
#
#    Output : 2 for the pair (3, 4)

from operator import itemgetter
import sys

def maximumGap(A):
    indexes,b = zip(*sorted(enumerate(A), key=itemgetter(1)))
    mini = -(sys.maxsize)-1
    max_index = indexes[-1]
    for i in range(len(indexes)-2,-1,-1):
        ans=max_index-indexes[i]
        if (ans) > mini:
            mini = ans
        max_index = max(max_index, indexes[i])
    if mini < 0:
        return 0
    return mini


A=[3, 2, 1]
#A=[-3,-2,-3,-4,-5,-1,-1]
#A=[10,9,1,6,3,0]
print(maximumGap(A))
