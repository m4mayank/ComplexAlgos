#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = []
        positive = 0
        while positive < len(nums) and nums[positive] < 0:
            positive += 1
        negative = positive - 1
        while negative >= 0 and positive < len(nums):
            p = nums[positive]**2
            n = nums[negative]**2
            if n < p :
                l.append(n)
                negative-=1
            if n >= p:
                l.append(p)
                positive+=1
        while negative >= 0:
            l.append(nums[negative]**2)
            negative -= 1
        while positive < len(nums):
            l.append(nums[positive]**2)
            positive += 1
        return l