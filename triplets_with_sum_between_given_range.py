#!/usr/local/bin/python3.7

def solve(A):
    a_small=[0,0]
    a_large=[0,0,0]
    b_small=[0,0]
    c_small=[0]
    for i in A:
        f = float(i)
        if f >=0 and f <= (2/3):
            if a_small[1] == 0 and a_large[2] == 0:
                a_small[1]=f
                a_large[2]=f
            if f < a_small[1]:
                a_small[0] = a_small[1]
                a_small[1] = f
            if f > a_large[2]:
                a_large[0]=a_large[1]
                a_large[1]=a_large[2]
                a_large[2]=f
        if f >= (2/3) and f < 1.00:
            if b_small[1]==0:
                b_small[1]=f
            if f < b_small[1]:
                b_small[0] = b_small[1]
                b_small[1] = f
        if f >= 1.00 and f < 2.00:
            if c_small[0]==0:
                c_small[0]=f
            if f < c_small[0]:
                c_small[0] == f
    print(f"a_small : {a_small}")
    print(f"a_large : {a_large}")
    print(f"b_small : {b_small}")
    print(f"c_small : {c_small}")

A=["1.1", "1.2", "1.3", "0.7", "0.99","0.88", "0.55", "0.65", "0.33", "0.22", "0.11", "0.567", ".44"]
solve(A)
