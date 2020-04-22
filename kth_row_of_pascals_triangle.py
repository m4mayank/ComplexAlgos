#!/usr/local/bin/python3.7

#Given numRows, generate the first numRows of Pascal’s triangle.
#
#Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
#
#Example:
#
#    Given numRows = 5,
#
#    Return:
#        [
#        [1],
#        [1,1],
#        [1,2,1],
#        [1,3,3,1],
#        [1,4,6,4,1]
#        ]


def pascals(A):
    pascals_triangle=[]
    for i in range(A+1):
        current_list = []
        for j in range(i+1):
            if j == 0 or j == i:
                current_list.append(1)
            else:
                current_list.append(pascals_triangle[-1][j-1]+pascals_triangle[-1][j])
        pascals_triangle.clear()
        pascals_triangle.append(current_list[:])

    print(pascals_triangle[0])


pascals(2)
