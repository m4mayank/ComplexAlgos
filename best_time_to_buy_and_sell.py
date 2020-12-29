#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

def maxProfit(prices):
        if len(prices) == 0 or len(prices)==1:
            return 0
        sp = [0, 0]
        bp = [prices[0], 0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < bp[0]:
                bp[0] = prices[i]
                bp[1] = i
            if sp[1] < i:
                sp[0] = prices[i]
                sp[1] = i
            if prices[i] >= sp[0]:
                sp[0] = prices[i]
                sp[1] = i
            if sp[1] >= bp[1]:
                current  = sp[0] - bp[0]
                if current > profit:
                    profit = current
        return profit

print(maxProfit([3,3,5,0,0,3,1,4]))