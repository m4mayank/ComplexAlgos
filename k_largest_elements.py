#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Problem Description

# Given an 1D integer array A of size N you have to find and return the B largest elements of the array A.

# NOTE:

# Return the largest B elements in any order you like.

# Input Format
# First argument is an 1D integer array A

# Second argument is an integer B.

# Output Format
# Return a 1D array of size B denoting the B largest elements.

# Example Input
# Input 1:

#  A = [11, 3, 4]
#  B = 2
# Input 2:

#  A = [11, 3, 4, 6]
#  B = 3

#  Example Output
# Output 1:

#  [11, 4]
# Output 2:

#  [4, 6, 11]

import heapq
class Solution:
    
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        l = []
        for i in A:
            val = (i* (-1))
            heapq.heappush(l, val)
        llist = []
        for i in range(0, B):
            llist.append(heapq.heappop(l)*(-1))
            
        return llist