#!/usr/local/bin/python3.7


#Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.
#
#Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.
#
#Input 1:
#        [[1, 0, 1],
#         [1, 1, 1],
#         [1, 1, 1]]
#
#Output 1:
#       [[0, 0, 0],
#        [1, 0, 1],
#        [1, 0, 1]]
#
#Input 2:
#       [[1, 0, 1],
#        [1, 1, 1],
#        [1, 0, 1]]
#
#Output 2:
#       [[0, 0, 0],
#        [1, 0, 1],
#        [0, 0, 0]]

def setZeroes(A):
    numRows = len(A)
    numColumns = len(A[0])
    firstRow = 1
    firstColumn = 1
    if 0 in A[0]:
        firstRow = 0

    for i in range(numRows):
        if A[i][0] == 0:
            firstColumn = 0
            break

    for i in range(1,numRows):
        for j in range(1,numColumns):
            if A[i][j] == 0:
                A[i][0] = 0
                A[0][j] = 0
    for i in range(1,numRows):
        if A[i][0] == 0:
            for j in range(numColumns):
                A[i][j] = 0

    for j in range(1,numColumns):
        if A[0][j] == 0:
            for i in range(numRows):
                A[i][j] = 0

    if firstRow == 0:
        for j in range(numColumns):
            A[0][j] = 0

    if firstColumn == 0:
        for i in range(numRows):
            A[i][0] = 0

    return A



A = [[1, 0, 1],[1, 1, 1],[1, 1, 1]]
#A = [[0, 0, 0],[1, 0, 1],[1, 0, 1]]
#A = [[1, 0, 1],[1, 1, 1],[1, 0, 1]]
#A=[[0, 0],[1, 0]]
print(setZeroes(A))
