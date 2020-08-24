#!/usr/local/bin/python3.7

#Given a string, find the rank of the string amongst its permutations sorted lexicographically.
#Assume that no characters are repeated.
#
#Example :
#    Input : 'acb'
#    Output : 2
#
#    The order permutations with letters 'a', 'c', and 'b' :
#        abc
#        acb
#        bac
#        bca
#        cab
#        cba
#
#The answer might not fit in an integer, so return your answer % 1000003


import math

def findRank(A):
    llist = sorted(list(A))
    already_used=[]
    permutations = 0
    for i in range(0,len(A)):
        before_this = []
        per_alpha = math.factorial(len(A)-(i+1))
        before_this = [llist[x] for x in range(0,llist.index(A[i])) if llist[x] not in already_used]
        already_used.append(A[i])
        permutations = permutations + (len(before_this) * per_alpha)

    return (permutations+1)%1000003

print(findRank("aAbBcC"))
