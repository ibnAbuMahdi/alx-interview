#!/usr/bin/python3
def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def can_win(n):
        if n % 2 == 0:
            return "Ben"  # If n is even, Ben will win
        return "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = can_win(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [6, 10, 15]
winner = isWinner(x, nums)
print(winner)  # This will print "Maria"

