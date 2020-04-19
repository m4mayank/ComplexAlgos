#!/usr/local/bin/python3.7
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.


Input Format:
The first and the only argument contains an integer, A.

Output Format:
Return a 2-d matrix of size A x A satisfying the spiral order.

Examples:
    Input 1:A = 3
    Output 1:
        [[ 1, 2, 3 ],
         [ 8, 9, 4 ],
         [ 7, 6, 5 ]   ]

    Input 2: A = 4
    Output 2:
        [   [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]   ]

def spiralOrder(A):
    Arr = [A*[0] for i in range(A)]
    t = 0
    b = A-1
    l = 0
    r = A-1
    count = 1
    direction = 0
    while(t<=b and  l<=r):
        if direction == 0:
            for i in range(l, r+1):
                Arr[t][i] = count
                count+=1
            t += 1
        elif direction == 1:
            for i in range(t, b+1):
                Arr[i][r] = count
                count+=1
            r -= 1
        elif direction == 2:
            for i in range(r,l-1,-1):
                Arr[b][i] = count
                count+=1
            b -= 1
        elif direction == 3:
            for i in range(b ,t-1,-1):
                Arr[i][l] = count
                count+=1
            l += 1
        direction = (direction+1) % 4
    return Arr
imp_lst=4
spiralled = spiralOrder(imp_lst)
print(spiralled)
