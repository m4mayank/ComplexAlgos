#!/usr/local/bin/python3.7

#Input :
#Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.
#
#Output :
#Return an Integer, i.e minimum number of steps.
#
#Example :
#Input : [(0, 0), (1, 1), (1, 2)]
#Output : 2

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

def coverPoints(A, B):
    lst_of_points = [[A[i],B[i]] for i in range(0,len(A))]
    distance = 0
    for i in range(0,len(lst_of_points)-1):
        a,b = lst_of_points[i],lst_of_points[i+1]
        x,y = abs(a[0]-b[0]), abs(a[1]-b[1])
        dist = max(x,y)
        distance += dist
    return distance

a = [0,1,1]
b = [0,1,2]
distance = coverPoints(a,b)
print(distance)
