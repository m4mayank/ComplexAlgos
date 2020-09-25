#!/usr/local/bin/python3.7

#Given a matrix of integers A of size N x M in which each row is sorted.
#
#Find an return the overall median of the matrix A.
#
#Note: No extra memory is allowed.
#
#Note: Rows are numbered from top to bottom and columns are numbered from left to right.
#
#For Example
#Input 1:
#        A = [   [1, 3, 5],
#                [2, 6, 9],
#                [3, 6, 9]   ]
#Output 1:
#    5
#
#Explanation 1:
#    A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
#    Median is 5. So, we return 5.

import heapq
def findMedian(A):
    count = len(A)*len(A[0])
    for i in range(len(A)):
        A[i] = [A[i][0], A[i]]
    heapq.heapify(A)

    for i in range((count+1)//2):
        top = heapq.heappop(A)
        if i == (((count+1)//2)-1):
            return(top[1].pop(0))
        top[1].pop(0)
        temp = top[1]
        if len(temp) != 0:
            heapq.heappush(A, [top[1][0], top[1]])
        else:
            heapq.heappush(A, [2147483647, []])


A=[[1,3,5],[2,6,9],[3,6,9]]

print(findMedian(A))
