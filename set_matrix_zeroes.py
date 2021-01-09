#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3

# Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

# Follow up:

# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Solution 1 : has a space complexity of m+n
        # row = set()
        # column = set()
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             row.add(i)
        #             column.add(j)
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if i in row or j in column:
        #             matrix[i][j] = 0
        #Solution 2: Has a space complexity of O(1)
        first_row = False
        first_column = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = True
                    if j == 0:
                        first_column = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] ==0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row == True:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if first_column == True:
            for i in range(len(matrix)):
                matrix [i][0] = 0