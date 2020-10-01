#!/usr/local/bin/python3.7

#Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
#
#More formally,
#G[i] for an element A[i] = an element A[j] such that
#j is maximum possible AND
#j < i AND
#A[j] < A[i]
#
#Elements for which no smaller element exist, consider next smaller element as -1.
#
#For Example
#Input 1:
#    A = [4, 5, 2, 10, 8]
#Output 1:
#    G = [-1, 4, -1, 2, 2]
#Explaination 1:
#    index 1: No element less than 4 in left of 4, G[1] = -1
#    index 2: A[1] is only element less than A[2], G[2] = A[1]
#    index 3: No element less than 2 in left of 2, G[3] = -1
#    index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
#    index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]
#
#Input 2:
#    A = [3, 2, 1]
#Output 2:
#    [-1, -1, -1]
#
#Explaination 2:
#    index 1: No element less than 3 in left of 3, G[1] = -1
#    index 2: No element less than 2 in left of 2, G[2] = -1
#    index 3: No element less than 1 in left of 1, G[3] = -1

def prevSmaller(A):
    c = [0] * len(A)
    stk = []
    for i in range(len(A)):
        found = False
        if len(stk) == 0:
            c[i] = -1
            stk.append(A[i])
            continue

        while len(stk) != 0:
            if stk[-1] >= A[i]:
                stk.pop()

            elif stk[-1] < A[i]:
                c[i] = stk[-1]
                stk.append(A[i])
                found = True
                break
        if found == False:
            c[i] = -1
            stk.append(A[i])
    print(c)


A = [4, 5, 2, 10, 8]
prevSmaller(A)
