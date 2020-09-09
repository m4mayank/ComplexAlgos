#!/usr/local/bin/python3.7

#   *-------*-------*-------*
#   | start |       |       |
#   *-------*-------*-------*
#   |       |       |       |
#   *-------*-------*-------*
#   |       |       | finish|
#   *-------*-------*-------*
#
#   A robot is located at the top-left corner of an A x B grid(in the diagram above)
#   The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid
#
#   How many possible unique paths are there?
#
#   Example :
#       Input : A = 2, B = 2
#       Output : 2
#       2 possible routes : (0, 0) -> (0, 1) -> (1, 1)
#                     OR  : (0, 0) -> (1, 0) -> (1, 1)

import math

def uniquePaths(A, B):
    total = (A+B)-2
    down = (A-1)
    right = (B-1)
    if A == 1 || B == 1 || A == 0 || B == 0:
        return 1
    possibilities = math.factorial(total)//((math.factorial(down))*(math.factorial(right)))
    return possibilities
