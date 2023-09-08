#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

x = 3
nums = [2, 3, 4]
print("Winner: {}".format(isWinner(x, nums)))
nums = [0] * 10000
for i in range(10000):
    nums[i] = i

print("Winner: {}".format(isWinner(10000, nums)))
