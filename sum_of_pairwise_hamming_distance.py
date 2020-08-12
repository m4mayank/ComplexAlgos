#!/usr/local/bin/python3.7

#Problem Description
#Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.
#
#Given an array A of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array. Return the answer modulo 1000000007.
#
#Example Input:
#    Input 1:
#         A = [1]
#
#    Input 2:
#        A = [2, 4, 6]
#
#Example Output:
#    Output 1:
#         0
#
#    Output 2:
#        8
#
#Example Explanation
#Explanation 1:
#    No pairs are formed.
#
#Explanation 2:
#    We return, f(2, 2) + f(2, 4) + f(2, 6) + f(4, 2) + f(4, 4) + f(4, 6) + f(6, 2) + f(6, 4) + f(6, 6) = 8


#***********************************************************
                        #SOLUTION 1
#***********************************************************
#def hammingDistance(A):
#    llist = [(i,j) for i in A for j in A]
#    distance = 0
#    for i in llist:
#        dist = 0
#        a = max(i[0], i[1])
#        b = min(i[1], i[0])
#        if a == b:
#            dist = 0
#            continue
#
#        while (a>0):
#            remaindera = (a%2)
#            if b > 0:
#                remainderb = (b%2)
#                b = b//2
#            else:
#                remainderb = 0
#            a = a//2
#            if remaindera != remainderb:
#                dist = dist +  1
#
#        distance += dist
#    return (distance%1000000007)
#***********************************************************

#***********************************************************
                        #SOLUTION 2
#***********************************************************
#def hammingDistance(A):
#    llist = [(i,j) for i in A for j in A]
#    distance = 0
#    for i in llist:
#        a = (i[0])^(i[1])
#        stri = ""
#        while (a>0):
#            if (a%2) == 1:
#                distance+=1
#            a = a//2
#    return distance


#***********************************************************
           #SOLUTION 3 (Most Optimised Solution)

# Explaination : So in this approach we apply the simple
# method of permutation and combination.

# For example : hamming distance will be 1 if at a
# particular bit position, the bits are (1,0) or (0,1)
# but if the bits are same then it wont contribute to
# hamming distance. So in this case we find the number of
# ones and zeroes at a particular bit position.

# Depending upon the number of zeroes and ones we get at a
# particular bit position, we can decide how many (1,0)
# pairs are possible and accordingly the hamming distance.

# if we find the hamming distance between 10
# and 100.
# 10 when written in binary is  0001010
# 100 when written in binary is 1100100
# hamming distance for position 1: 0(0,0)
# hamming distance for position 2: 1(1,0)
# hamming distance for position 3: 1(1,0) and so on

# In the actual algo, we calculate upto 31 bits because that
# is the maximum possible limit for an int
#***********************************************************
#def hammingDistance(A):
    dist = 0
    for i in range(0, 32):
        ones = 0
        zeroes = 0
        for j in A:
            if j & (1<<i):
                ones += 1
            else:
                zeroes += 1
        dist += (ones*zeroes)
    print(dist)
    return (2*dist)%1000000007

#A = [88, 5, 47, 88, 60, 23]
A = [10,100]
print(hammingDistance(A))
