#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Solution 1: 
        # forward_product = nums[0]
        # forward = []
        # for i in range(0, len(nums)):
        #     if i == 0:
        #         forward.append(1)
        #         continue
        #     forward.append(forward_product)
        #     forward_product *= nums[i]
        # backward_product = nums[-1]
        # backward = [0 for i in range(len(nums))]
        # count = 0
        # for i in range(len(nums)-1, -1, -1):
        #     if i == len(nums)-1:
        #         backward[i] = 1
        #         continue
        #     backward[i] = backward_product
        #     backward_product *= nums[i]
        # for i in range(0, len(nums)):
        #     forward[i] *= backward[i]
        
        #Solution 2 : Refined form of Solution 1. Refer to solution 1 for understanding the logic
        forward_product = nums[0]
        forward = [1,]
        for i in range(1, len(nums)):
            forward.append(forward_product)
            forward_product *= nums[i]
        backward_product = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                forward[i] *= 1
                continue
            forward[i] *= backward_product
            backward_product *= nums[i]
        return forward