#!/usr/local/bin/python3.7

#Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.
#
#Example:
#    Input : [1, 0]
#    Return : [0, 1]
#Lets say N = size of the array. Then, following holds true :
#    1) All elements in the array are in the range [0, N-1]
#    2) N * N does not overflow for a signed integer


def arrange(A):
    for i in range(0, len(A)):
        A[i] = A[i] + (len(A)*((A[A[i]])%len(A)))

    for i in range(0, len(A)):
        A[i] = A[i]//len(A)

#A= [1, 2, 7, 0, 9, 3, 6, 8, 5, 4 ]
#Answer = [2, 7, 8, 1, 4, 0, 6, 5, 3, 9]
A = [3,4,2,1,0]
#Answer=[1, 0, 2, 4, 3]
arrange(A)
print(A)
