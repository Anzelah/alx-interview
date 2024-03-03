#!/usr/bin/python3
"""Coin change"""


def makeChange(coins, total):
    """Function to return minimum coin number for change"""
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in coins:
        if i > total:
            break
        for j in range(i, total + 1):
            dp[j] = min(dp[j], dp[j - i] + 1)

    return dp[total] if dp[total] != total + 1 else -1
