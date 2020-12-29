#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]

def findDisappearedNumbers(nums):
        x = set(nums)
        llist = []
        for i in range(1, len(nums)+1):
            if i not in x:
                llist.append(i)
        return llist   

result = findDisappearedNumbers([4,3,2,7,7,2,3,1])
print(result)