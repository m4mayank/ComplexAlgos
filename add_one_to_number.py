#!/usr/local/bin/python3.7
import time
def plusOne(A):
    val = 1
    for i in range(len(A),0,-1):
        val = val + A[i-1]
        borrow = int(val/10)
        if borrow == 0:
            A[i-1] = val
            break
        else:
            A[i-1] = val%10
            val = borrow
        print(borrow)
    A = [borrow] + A
    while A[0]==0:
        del A[0]
    return A
    """
    num_str = ""
    for i in A:
        num_str += str(i)

    number = int(num_str)
    number+=1
    number_str = str(number)
    num_lst=[]
    for i in number_str:
        num_lst.append(int(i))
    return num_lst
    """
lst = [1,3,9,9]
print(plusOne(lst))

