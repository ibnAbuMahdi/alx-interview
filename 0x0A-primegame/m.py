#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

x = 5
nums = [1, 2, 3, 4, 5]
print("Winner: {}".format(isWinner(x, nums)))
