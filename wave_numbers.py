#!/usr/local/bin/python3.7

def wave(A):
    A.sort()
    b = [0 for i in range(len(A))]
    for i in range(1, len(A)+1):
        if i%2 != 0:
            if i == len(A):
                b[i-1] = A[i-1]
            else:
                b[i] = A[i-1]
        else:
            b[i-2] = A[i-1]
        print(i)
    return b


#a = [1, 2, 3, 4]
a = [5, 1, 3, 2, 4]
print(wave(a))
