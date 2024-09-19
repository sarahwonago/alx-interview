#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    p = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            p[i] = min(p[i], p[i - coin] + 1)
    return p[-1] if p[-1] != float("inf") else -1
