#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dicti = {}
        for i in nums:
            if i not in dicti:
                dicti[i] = 1
            else:
                return i

#Solution 2 : Using the Hare and tortoise algorithm (No Extra space and O(n) runtime complexity)
#         hare = nums[0]
#         tortoise = nums[0]
#         while True:
#             hare = nums[nums[hare]]
#             tortoise = nums[tortoise]
#             if hare == tortoise:
#                 break
#         tortoise = nums[0]
#         while tortoise != hare:
#             tortoise = nums[tortoise]
#             hare = nums[hare]
        
#         return hare