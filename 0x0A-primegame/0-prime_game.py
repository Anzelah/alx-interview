#!/usr/bin/python3
"""Prime game leetcode"""


def sieve_algo(n):
    """Find the prime numbers using the sieve of eratosthenes"""
    numbers = []
    is_prime = [True] * (n + 1)

    for i in range(2, n + 1):
        if is_prime[i]:
            numbers.append(i)

            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return numbers


def isWinner(x, nums):
    """Find winner of each game"""
    Marias = 0
    Bens = 0

    if x == 0 or nums == []:
        return None

    for i in range(0, x):
        number = sieve_algo(nums[i])
        if len(number) % 2 == 0:
            Bens += 1
        else:
            Marias += 1

    if Bens > Marias:
        return "Ben"
    elif Marias > Bens:
        return "Maria"
    else:
        return None
