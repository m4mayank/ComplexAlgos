#!/usr/local/bin/python3.7

# @param A : list of integers
# @param B : list of integers
# @return an integer



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
