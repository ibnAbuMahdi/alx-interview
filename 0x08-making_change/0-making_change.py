#!/usr/bin/python3
""" 0-making_change """


def makeChange(coins, num):
    """ make change coins """
    if num <= 0:
        return 0

    change = [float('inf')] * (num + 1)
    change[0] = 0

    for i in range(1, num + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                sub_res = change[i - coins[j]]
                if sub_res != float('inf') and sub_res + 1 < change[i]:
                    change[i] = sub_res + 1

    if change[num] == float('inf'):
        return -1
    else:
        return change[num]
