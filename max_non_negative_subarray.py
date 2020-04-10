#!/usr/local/bin/python3.7

#Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.
#
#The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.
#
#Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
#
#Find and return the required subarray.
#
#1. If there is a tie, then compare with segment's length and return segment which has maximum length.
#2. If there is still a tie, then return the segment with minimum starting index.
#
#Input 1:
#        A = [1, 2, 5, -7, 2, 3]
#
#Output 1:
#        [1, 2, 5]
#
#Explanation 1:
#        The two sub-arrays are [1, 2, 5] [2, 3].
#        The answer is [1, 2, 5] as its sum is larger than [2, 3].
#
#Input 2:
#        A = [10, -1, 2, 3, -4, 100]
#
#Output 2:
#        [100]
#
#Explanation 2:
#        The three sub-arrays are [10], [2, 3], [100].
#        The answer is [100] as its sum is larger than the other two.

def maxNonNegativeArray(A):
    sum_list=[]
    int_sum=0
    max_sum=0
    loop_list=[]
    final_count = 0
    temp_count=0
    for i in range(len(A)):
        if A[i] < 0:
            int_sum = 0
            loop_list.clear()
            temp_count = 0
            continue
        int_sum += A[i]
        temp_count+=1
        loop_list.append(A[i])
        if int_sum == max_sum:
            if temp_count == final_count:
                if loop_list <= sum_list[0]:
                    sum_list.clear()
                sum_list.append(loop_list[:])
            if temp_count > final_count:
                sum_list.clear()
                sum_list.append(loop_list[:])
                final_count = temp_count
        if int_sum > max_sum:
            sum_list.clear()
            sum_list.append(loop_list[:])
            max_sum = int_sum
            final_count = temp_count
    if sum_list:
        return sum_list[0]
    else:
        return []
#A = [11, -4, 5, 6, -7, 7, 4, -10 , 8, 5, 4, -9 , 9 , 8]
#A = [-1,-1,-1,-1,-1]
A=[0,0,-1,0]
result = maxNonNegativeArray(A)
print(result)
