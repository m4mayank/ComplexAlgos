#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3

# Problem Description

# Given two equally sized 1-D arrays A, B containing N integers each.

# A sum combination is made by adding one element from array A and another element of array B.

# Return the maximum C valid sum combinations from all the possible sum combinations.
from heapq import heappush, heappop
def solve(A, B, C):
        A.sort()
        B.sort()
        heap = []
        result = []
        n = len(A)
        my_set = set()
        my_set.add((n-1, n-1))
        heappush(heap, [-1*(A[n-1] + B[n-1]), (n-1, n-1)])
        i = n-1
        j = n-1
        
        for _ in range(C):
            temp = heappop(heap)
            result.append(-1 * temp[0])
            i, j = temp[1]
            
            if i >= 1:
                if (i-1, j) not in my_set:
                    heappush(heap, [-1 * (A[i-1] + B[j]), (i-1, j)])
                    my_set.add((i-1, j))
        
            
            if j >= 1:
                if (i, j-1) not in my_set:
                    heappush(heap, [-1 * (A[i] + B[j-1]), (i, j - 1)])
                    my_set.add((i, j-1))
        return result
        

A = [2000, 1990, 1989, 4, 5]
B = [100, 23, 8 ,6, 2]
C = 25
print(solve(A, B, C))