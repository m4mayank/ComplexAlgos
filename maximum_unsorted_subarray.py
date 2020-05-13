#!/usr/local/bin/python3.7

#You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
#Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
#If A is already sorted, output -1.
#
#Example :
#    Input 1:
#        A = [1, 3, 2, 4, 5]
#        Return: [1, 2]
#    Input 2:
#        A = [1, 2, 3, 4, 5]
#        Return: [-1]

def subUnsort(A):
    llist = []
    b = sorted(A)
    count = 0
    for i in range(0, len(A)):
        if A[i] != b[i]:
            llist.append(i)
            break
        else:
            count += 1
            pass

    if count == len(A):
        return [-1]

    for i in range(len(A)-1, -1, -1):
        if A[i] != b[i]:
            llist.append(i)
            break
        else:
            pass
    return llist

#A = [1, 3, 2, 4, 5] #1,2
#A =[1,1,10,10,15,10,15,10,10,15,10,15] #4, 10
#A = [3, 3, 4, 5, 5, 9, 11, 13, 14, 15, 15, 16, 15, 20, 16] #11, 14
#A=[1,1]
#A = [1, 2, 2, 3, 3, 5, 6, 6, 14, 17, 18, 17, 18, 15, 15, 17, 19, 14, 19, 18] #9 19
#A = [1,2,3, 4, 5]
#A=[16, 6, 18, 17, 13, 6, 18, 16, 6, 15, 15, 18, 16, 13, 16, 16, 6, 18, 15, 15]
A=[4, 15, 4, 4, 15, 18, 20]
print(subUnsort(A))

