#!/usr/local/bin/python3.7

#Problem Description
#Given a positive integer A, return its corresponding column title as appear in an Excel sheet.
#
#Input Format:
#    First and only argument is integer A.
#
#Output Format:
#    Return a string, the answer to the problem.
#
#Example Input:
#    Input 1:
#        A = 1
#
#    Input 2:
#        A = 28
#
#    Output 1:
#        "A"
#
#    Output 2:
#        "AB"
#
#Explanation:
#    1 -> A
#    2 -> B
#    3 -> C
#    ...
#    26 -> Z
#    27 -> AA
#    28 -> AB


def convertToTitle(A):
    num_dict ={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
    stri = ""
    while (A > 0):
        remainder = ((A-1)%26)
        stri = num_dict[remainder]+stri
        A = ((A-1)//26)
    return stri

print(convertToTitle(943566))
