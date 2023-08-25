#!/usr/bin/python3
""" 0-making_change """


def makeChange(coins, num):
    """ make change coins """
    if num <= 0:
        return 0

    MAX_VALUE = float('inf')
    dp = [0] + [MAX_VALUE] * num

    for i in range(1, num + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[num] if dp[num] != MAX_VALUE else -1
