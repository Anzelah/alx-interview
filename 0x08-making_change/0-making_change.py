#!/usr/bin/python3
"""Coin change"""


def makeChange(coins, total):
    """Function to return minimum coin number for change"""
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for j in coins:
            if (i - j >= 0):
                dp[i] = min(dp[i], 1 + dp[i - j])

    return dp[total] if dp[total] != total + 1 else -1
