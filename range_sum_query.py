#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3

# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
# numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
# numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

# P.S. : Please consider that this function maybe called multiple times and hence has to be efficient for that

class NumArray:

    def __init__(self, nums: List[int]):
        self.num = nums
        self.total_sum = []
        self.total_sum.append(0)
        for i in range(0,len(self.num)):
            self.total_sum.append(self.total_sum[i] + self.num[i])
            
    def sumRange(self, i: int, j: int) -> int:
        return (self.total_sum[j+1] - self.total_sum[i])
