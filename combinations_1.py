# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# You may return the answer in any order.

 

# Example 1:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]

class Solution:
    def combo(self, nums, p):
        subset = []
        if p == 0:
            return [[]]
        for i in range(0, (len(nums)-p)+1):
            result = self.combo(nums[i+1:], p-1)
            for j in result:
                subset.append(([nums[i]]+j))
        return subset
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combo([i for i in range(1, n+1)], k)
        