#!/usr/local/bin/python3.7
import bisect


#Given a number N, find all factors of N.
#Example:
#    N = 6
#    factors = {1, 2, 3, 6}
#Return list should be sorted

def allFactors(A):
    llist = []
    if A == 1:
        llist.append(1)
    else:
        for i in range(1,int((A)**(0.5))+1):
            if A%i == 0:
                bisect.insort(llist, i)
                if i != (A)**(0.5):
                    bisect.insort(llist, A//i)
    return llist



llist = allFactors(131)
print(llist)
