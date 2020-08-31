#!/usr/local/bin/python3.7

#*************************************************MOST DIFFICULT QUESTION TILL NOW********************************************

#Given a string, find the rank of the string amongst its permutations sorted lexicographically.
#Note that the characters might be repeated. If the characters are repeated, we need to look at the rank in unique permutations.
#Look at the example for more details.
#
#Example :
#    Input : 'aba'
#    Output : 2
#
#    The order permutations with letters 'a', 'a', and 'b' :
#        aab
#        aba
#        baa
#
#The answer might not fit in an integer, so return your answer % 1000003

import math

def count(name):
    d = {}
    for i in name:
        if i in d.keys():
            d[i] = d[i]+1
        else:
            d[i] = 1
    return d

def findRank(A):
    d = count(A)
    llist = list(sorted(set(list(A))))
    already_used=[]
    permutations = 0
    for i in range(0,len(A)):
        k = A[i]
        before_this = []
        per_alpha = (math.factorial(len(A)-(i+1)))
        before_this = [llist[x] for x in range(0,llist.index(A[i])) if llist[x] not in already_used]
        for i in before_this:
            lower_factorial = 1
            for key, value in d.items():
                if value != 0:
                    if key == i:
                        lower_factorial = lower_factorial * math.factorial(value-1)
                    else:
                        lower_factorial = lower_factorial * math.factorial(value)
            permutations = permutations + (per_alpha//lower_factorial)
        d[k] = d[k] - 1
        if d[k] == 0:
            d.pop(k)
            already_used.append(k)
    return (permutations+1)%1000003

print(findRank("bacbac"))
