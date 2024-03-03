#!/usr/bin/python3
"""Coin change"""


def makeChange(coins, total):
    """Function to return minimum coin number for change"""
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for j in coins:
        if j > total:
            break
        for i in range(j, total + 1):
            dp[i] = min(dp[i], dp[i - j] + 1)

    return dp[total] if dp[total] != float('inf') else -1
