"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^(4) + 6^(4) + 3^(4) + 4^(4)
    8208 = 8^(4) + 2^(4) + 0^(4) + 8^(4)
    9474 = 9^(4) + 4^(4) + 7^(4) + 4^(4)

As 1 = 1^(4) is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
from itertools import count, takewhile

from euler import euler_problem


@euler_problem
def euler030(n:int|str) -> int:
    n = int(n)
    return sum(x for x in range(10, get_upper_bound(n)) if is_sum_of_digits(x, n))

def is_sum_of_digits(n:int, power:int):
    return n == sum(map(lambda digit: (int(digit)) ** power, str(n)))

# Establishes a rough upper bound for possibilities. It's not an optimal bound,
# but it is guaranteed to be higher than the max possible based on power.
def get_upper_bound(power):
    max_per_digit = 9 ** power
    max_digits = max(takewhile(lambda digits: len(str(digits * max_per_digit)) >= digits, count(start=2)))
    return max_digits * max_per_digit


if __name__ == '__main__':
    print(euler030(4))
    print(euler030(5))
