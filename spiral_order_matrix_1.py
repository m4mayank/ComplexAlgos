#!/usr/local/bin/python3.7

def spiralOrder(A):
    lst=[]
    t = 0
    b = len(A)-1
    l = 0
    r = len(A[0])-1
    direction = 0
    while(t<=b and  l<=r):
        if direction == 0:
            for i in range(l, r+1):
                lst.append(A[t][i])
            t += 1
        elif direction == 1:
            for i in range(t, b+1):
                lst.append(A[i][r])
            r -= 1
        elif direction == 2:
            for i in range(r,l-1,-1):
                lst.append(A[b][i])
            b -= 1
        elif direction == 3:
            for i in range(b ,t-1,-1):
                lst.append(A[i][l])
            l += 1
        direction = (direction+1) % 4
    return lst
imp_lst=([1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16])
#imp_lst=([1])
#imp_lst=([1,2,3,4])
#imp_lst=([1],[2],[3],[4])
spiralled = spiralOrder(imp_lst)
print(spiralled)
