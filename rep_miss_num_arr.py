#!/usr/local/bin/python3.7
#You are given a read only array of n integers from 1 to n.
#
#Each integer appears exactly once except A which appears twice and B which is missing.
#
#Return A and B.
#
#Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
#Note that in your output A should precede B.
#
#Example:
#
#    Input:[3 1 2 5 3]
#
#    Output:[3, 4]
#
#    A = 3, B = 4

def repeatedNumber(A):
    b = len(A)
    fin_sum = (b*(b+1))//2
    fin_square = (b*(b+1)*((2*b)+1))//6
    for i in A:
        fin_sum -= i
        fin_square -= i**2
    sum1 = (fin_square//fin_sum)
    return[(sum1-fin_sum)//2, (sum1+fin_sum)//2]

llist = [1,2,3,3,5]
print(repeatedNumber(llist))
