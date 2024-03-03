#!/usr/bin/python3
"""Coin change"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort()
    
    n = len(coins)
    idx = n - 1
    ans = []

    while (idx >= 0):
        while (total >= coins[idx]):
            total -= coins[idx]
            ans.append(coins[idx])
        idx -= 1

    print(len(ans))
