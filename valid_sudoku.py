#!/usr/local/bin/python3.7

#Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
#
#The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.
#
#The input corresponding to the above configuration :
#    ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
#
#A partially filled sudoku which is valid.
#Return 0 / 1 ( 0 for false, 1 for true ) for this problem

def isValidSudoku(A):
    for i in range(0, len(A)):
        d = {}
        for j in range(0 , len(A[i])):
            if A[i][j] != ".":
                if A[i][j] in d:
                    return 0
                d[A[i][j]]=1

    for i in range(0,3):
        for l in range(0,3):
            d = {}
            for j in range(3*l, 3*(l+1)):
                for k in range(3*i, 3*(i+1)):
                    if A[k][j] != ".":
                        if A[k][j] in d:
                            return 0
                        d[A[k][j]]=1

    for i in range(0, len(A)):
        d = {}
        for j in range(0, len(A)):
            if A[j][i] != ".":
                if A[j][i] in d:
                    return 0
                d[A[j][i]]=1

    return 1


a = ["53..7....", "5..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
print(isValidSudoku(a))
