#!/usr/local/bin/python3.7

#Given a positive integer n and a string s consisting only of letters D or I, you have to find any permutation of first n positive integer that satisfy the given input string.
#
#D means the next number is smaller, while I means the next number is greater.
#
#Notes
#
#Length of given string s will always equal to n - 1
#Your solution should run in linear time and space.
#
#Example :
#    Input 1:
#    n = 3
#    s = ID
#    Return: [1, 3, 2]

#A : string
#B : integer

def findPerm(A, B):
    a=[]
    n = B
    current_pointer = 1
    upper_bound = n
    lower_bound = 1
    last_one = 1
    for i in range(0,B-1):
        if A[i] == "D":
            a.append(upper_bound)
            upper_bound = upper_bound-1
            last_one = 1
        if A[i] == "I":
            a.append(lower_bound)
            lower_bound = lower_bound+1
            last_one = 0

    if last_one == 0:
        a.append(upper_bound)
    else:
        a.append(lower_bound)

    return a

print(findPerm("IDDID",6))
