#!/usr/local/bin/python3.7

#You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. By flipping, we mean change character 0 to 1 and vice-versa.
#
#Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.
#
#For example,
#S = 010
#
#Pair of [L, R] | Final string
#_______________|_____________
#[1 1]          | 110
#[1 2]          | 100
#[1 3]          | 101
#[2 2]          | 000
#[2 3]          | 001
#
#We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
#
#Another example,
#No operation can give us more than three 1s in final string. So, we return empty array [].

def flip(A):
    diff = 0
    max1 = 0
    perm_l=1
    min1 = 0
    index_list = []
    for i in range(1, len(A)+1):
        temp_r = i
        temp_l = i
        if A[i-1] == '0':
            diff+=1
        if A[i-1] == '1':
            diff-=1

        if diff > 0:
            if diff > max1:
                max1 = diff
                perm_r = temp_r
                index_list.append([perm_l, perm_r, diff])
        if diff < 0:
            min1=diff
            diff=0
            perm_l = i+1
            continue
    print(index_list)
    if len(index_list):
        return(index_list[-1][0], index_list[-1][1])
    else:
        return(index_list)



#test cases =[0111000100010,0101111,111,001100111110000001]
sti = "001100111110000001"
print(sti)
print(flip(sti))
