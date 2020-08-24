#!/usr/local/bin/python3.7

#Problem Description
#Given an integer A, return the number of trailing zeroes in A!.
#
#Note: Your solution should be in logarithmic time complexity.
#
#**Input Format**
#First and only argumment is integer A.
#
#**Output Format**
#Return an integer, the answer to the problem.
#
#**Example Input**
#Input 1:
#     A = 4
#
#Input 2:
#    A = 5
#
#**Example Output**
#Explaination : 4! = 24
#Output 1:
#    0
#
#Explaination : 5! = 120
#Output 2:
#    1

def trailingZeroes(A):
    number = 0
    for i in range(1, A+1):
        if i%5 == 0:
            j = i
            instance = 0
            while j%5 == 0:
                instance = instance + 1
                j = j//5
            number = number + instance
    return number

print(trailingZeroes(9247))
