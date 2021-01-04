#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Let's call an array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        prev = arr[0]
        for i in range(1, len(arr)):
            diff = arr[i] - prev
            if diff <= 0:
                return i-1
            prev = arr[i]
            