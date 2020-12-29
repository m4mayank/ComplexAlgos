#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1


def singleNumber(nums):
        dicti = {}
        for i in nums:
            if i in dicti:
                if dicti[i] == 1:
                    del dicti[i]
            else:
                dicti[i] = 1
        
        if len(dicti) == 1:
            for key in dicti:
                return key

result = singleNumber([2,2,1])
print(result)