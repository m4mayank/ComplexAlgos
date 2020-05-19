#!/usr/local/bin/python3.7

#You are given an n x n 2D matrix representing an image.
#
#Rotate the image by 90 degrees (clockwise).
#
#You need to do this in place.
#
#Note that if you end up using an additional array, you will only receive partial score.
#
#Example:
#
#    If the array is
#    [
#     [1, 2],
#     [3, 4]
#           ]
#Then the rotated array becomes:
#    [
#     [3, 1],
#     [4, 2]
#           ]

#def rotate(A):
#    length = len(A)
#    a = [[0 for i in range(length)] for i in range(length)]
#    print(a)
#    for i in range(len(A)):
#        for j in range(len(A)):
#            a[j][(len(A)-1)-i] = A[i][j]
#    A = a
#    print(A)

def rotate(A):
    length= len(A)
    for i in range(0,length//2):
        for j in range(i, length-1-i):
            temp = A[i][j]
            A[i][j]=A[length-1-j][i]
            A[length-1-j][i]=A[length-1-i][length-1-j]
            A[length-1-i][length-1-j]=A[j][length-1-i]
            A[j][length-1-i]=temp

A=[[1,2,3],[4,5,6],[7,8,9]]

rotate(A)
print(A)
