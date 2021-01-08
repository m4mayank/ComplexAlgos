#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dicti = {}
        for i in nums:
            if i in dicti:
                dicti[i] += 1
                if dicti[i] >= (len(nums)/2):
                    return i
            elif i not in dicti:
                dicti[i] = 1