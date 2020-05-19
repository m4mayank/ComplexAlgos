#!/usr/local/bin/python3.7

#Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.
#
#Sample Input:
#    [3 4 1 4 1]
#
#Sample Output:
#    1

If there are multiple possible answers ( like in the sample case above ), output any one.
If there is no duplicate, output -1

def repeatedNumber(A):
    count_map= {}
    answer_list=[]
    for i in range(0, len(A)):
        if A[i] in count_map:
            answer_list.append(A[i])
            break
        else:
            count_map[A[i]]=1

    if len(answer_list):
        return answer_list[0]
    else:
        return -1

A = [3,4,1,2,5]
print(repeatedNumber(A))
