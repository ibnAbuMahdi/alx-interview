#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

x = 3
nums = [2, 3, 4]
print("Winner: {}".format(isWinner(x, nums)))
x = 2
nums = [2, 3, 5, 7]
print("Winner: {}".format(isWinner(x, nums)))
x = 4
nums = []
print("Winner: {}".format(isWinner(x, nums)))
x = 5
nums = [10, 15, 20, 25, 30]
print("Winner: {}".format(isWinner(x, nums)))
x = 1
nums = [9973]
print("Winner: {}".format(isWinner(x, nums)))
x = 10
nums = [9973]
print("Winner: {}".format(isWinner(x, nums)))
x = 5
nums = [10, 17, 5]
print("Winner: {}".format(isWinner(x, nums)))
x = 2
nums = [-2, 3, 5]
print("Winner: {}".format(isWinner(x, nums)))
x = 0
nums = [2, 3, 4]
print("Winner: {}".format(isWinner(x, nums)))
x = 100
nums = [10007, 10009, 10013, 10019, 10007]
print("Winner: {}".format(isWinner(x, nums)))
x = 100
nums = [9973]
print("Winner: {}".format(isWinner(x, nums)))

