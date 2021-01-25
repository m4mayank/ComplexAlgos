# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

class Solution:
    def combination(self, candidates, target):
        subset = []
        for i in range(0, len(candidates)):
            if candidates[i] > target:
                return subset
            if i == 0 or candidates[i] != candidates[i - 1]:
                result = self.combination(candidates[(i+1):], (target-candidates[i]))
            else:
                continue
                
            if candidates[i] == target:
                subset.append([candidates[i]])
                return subset
            if result != None:
                for j in result:
                    subset.append([candidates[i]]+j)
        return subset
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.combination(candidates, target)
        