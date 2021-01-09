#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #Solution 1 : O(1) space
        llist = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                llist.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
            print(i)
        return llist
        
        #Solution 2
        # dicti = {}
        # llist = []
        # for i in nums:
        #     if i in dicti:
        #         llist.append(i)
        #     else:
        #         dicti[i] = 1
        # return llist