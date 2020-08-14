#!/usr/local/bin/python3.7

#Problem Description
#Given a column title A as appears in an Excel sheet, return its corresponding column number.
#
#Input 1:
#    "A"
#
#Input 2:
#    "AB"
#
#Output 1:
#    1
#
#Output 2:
#    28
#
#Explanation:
#    A  -> 1
#    B -> 2
#    C -> 3
#    ...
#    ...
#    ...
#    Z -> 26
#    AA -> 27
#    AB -> 28

def titleToNumber(A):
    num_dict ={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    llist = list(map(str, A))
    distance = 0
    for i in range(1, len(llist)+1):
        distance += (num_dict[llist[-i]])*((26)**(i-1))

    return distance

print(titleToNumber('AABB'))

