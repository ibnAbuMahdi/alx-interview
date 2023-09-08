#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

x = 4
nums = [11, 30, 1, 7]
print("Winner: {}".format(isWinner(x, nums)))
