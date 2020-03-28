#!/usr/local/bin/python3.7

#Input 1:
#A = [1, 2, 3, 4, -10]
#
#Output 1:
#10
#
#Explanation 1:
#The subarray [1, 2, 3, 4] has the maximum possible sum of 10.
#
#Input 2:
#A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
#Output 2:
#6
#
#Explanation 2:
#The subarray [4,-1,2,1] has the maximum possible sum of 6.


def maxSubArray(A):
    sum_list=[]
    int_sum=0
    max_sum=A[0]
    for i in range(len(A)):
        int_sum += A[i]
        if int_sum > max_sum:
            max_sum = int_sum
        if int_sum < 0:
            int_sum = 0
    return max_sum


#A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
A = [ -3 , -4, 1, -2, 0]
maximum_val = maxSubArray(A)
print(maximum_val)
