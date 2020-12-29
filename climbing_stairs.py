#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

def climbStairs(n):
        ways = []
        ways.append(1)
        if n<=1:
            return 1
        ways.append(2)
        for i in range(2, n):
            way = ways[i-1] + ways[i-2]
            ways.append(way)
        return ways[-1]

print(climbStairs(13))