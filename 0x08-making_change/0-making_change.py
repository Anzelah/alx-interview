#!/usr/bin/python3
"""Coin change"""


def makeChange(coins, total):
    """Function to return minimum coin number for change"""
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for j in coins:
        for i in range(j, total + 1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + 1)

    return dp[total] if dp[total] != total + 1 else -1
