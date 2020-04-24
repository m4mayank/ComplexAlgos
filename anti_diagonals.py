#!/usr/local/bin/python3.7

def diagonal(a):
    B = [[] for i in range((len(a)*2)-1)]
    for i in range(len(a)):
        for j in range(len(a)):
            B[i+j].append(a[i][j])
    return B

llist = [[1,2,3],[2,3,4],[3,4,5]]
print(diagonal(llist))





