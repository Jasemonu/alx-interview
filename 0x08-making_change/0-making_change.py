#!/usr/bin/python3
"""
 determine the fewest number of coins needed to meet a given amount
"""


def makeChange(coins, total):
    if total < 0:
        return 0
    if total == 0:
        return 0

    # Initialize an array to store minimum coins needed
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total 0

    # Calculate minimum coins needed for each value from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1  # total cannot be met by any combination of coins
    else:
        return dp[total]
