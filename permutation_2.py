# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permute(self, nums):
        subset = []
        if len(nums) == 1:
            return [nums]
        for i in range(0, len(nums)):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            tim = self.permute((nums[:i]+nums[i+1:]))
            for j in tim:
                subset.append(j + [nums[i]])
        return subset
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            return(self.permute(nums))
            