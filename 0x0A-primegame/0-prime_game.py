#!/usr/bin/python3
""" the prime game problem """


def is_prime(num):
    """ check if number is a prime number """
    # If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def update_nums(k, nums_stat):
    """ update the dict """
    key = k
    ml = 1
    while key in nums_stat:
        nums_stat[key] = 0
        ml += 1
        key = key * ml


def isWinner(x, nums):
    """ run the game x times and determine the winner """
    player_wins = {"Maria": 0, "Ben": 0}
    players = {"Maria": "Ben", "Ben": "Maria"}
    if len(nums) == 0 or not isinstance(x, int) or not \
            isinstance(nums, list) or not isinstance(nums[0], int):
        return None
    nums.sort()
    actual_nums = nums * (x//len(nums)) + nums[: x % len(nums)]
    history = tuple()
    for n in actual_nums:
        next_pl = "Maria"
        j = 0
        if len(history):
            next_pl, j = history
        nums_stat = {i: 1 for i in range(j+1, n+1)}
        prime_exist = True
        while 1 in list(nums_stat.values()) and prime_exist:
            keys = [k for k in nums_stat.keys() if nums_stat[k]]
            for k in keys:
                if is_prime(k):
                    update_nums(k, nums_stat)
                    next_pl = players[next_pl]
                    if keys[-1] == k:
                        player_wins[players[next_pl]] += 1
                        prime_exist = False
                        history = (next_pl, k)
                    break
                elif keys[-1] == k:
                    prime_exist = False
                    player_wins[players[next_pl]] += 1
                    history = (next_pl, k)
    max_score = max(list(player_wins.values()))
    if list(player_wins.values()).count(max_score) == 1:
        return list(player_wins.keys())[list(player_wins.values())
                                        .index(max_score)]
    return None
