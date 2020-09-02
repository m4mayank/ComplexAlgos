#!/usr/local/bin/python3.7

#Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.
#
#Examples:
#    Input:
#        0 1 5
#        1
#        2
#    Output:
#        2 (0 and 1 are possible)
#
#    Input:
#        0 1 2 5
#        2
#        21
#    Output:
#        5 (10, 11, 12, 15, 20 are possible)
#
#Constraints:
#    1 <= B <= 9, 0 <= C <= 1e9 & 0 <= A[i] <= 9

# @param A : list of integers
# @param B : integer that tells length
# @param C : integer used for comparing
# @return an integer

def solve(A, B, C):
    c = str(C)
    permutation = 0
    if B < len(c):
        if 0 in A and B != 1:
            permutation = (len(A)**(B-1)) * (len(A)-1)
        else:
            permutation = len(A)**B
        return permutation

    if B == len(c):
        b = len(c)
        for i in range(0,len(c)):
            if int(c[i]) in A:
                continue
            else:
                b = i
                break
        if b < len(c):
            k = (b+1)
        if b == len(c):
            k = b
        for i in range(0, k):
            llist = []
            for j in A:
                if j < int(c[i]):
                    if j == 0 and i==0:
                        if B == 1:
                            permutation = 1
                        continue
                    else:
                        llist.append(j)
            local_count = (len(llist)*((len(A))**(B-(i+1))))
            permutation = permutation + local_count
        return permutation

    if B > len(c):
        return 0

#A = [0,1,2,5]
#A = [4, 5, 7, 8]
#A = [0, 2, 3, 4, 5, 7, 8, 9 ]
#A = [0]
#A = [2]
A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
B = 5
C =10004
print(solve(A, B, C))
