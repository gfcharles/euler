"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import logging
from functools import cache
from itertools import takewhile, count

import euler


@euler.euler_problem()
def euler034(_='n/a'):
    return sum(x for x in range(10, get_upper_bound()) if is_sum_of_digit_factorials(x))


@cache
def factorial(n: int) -> int:
    if n < 2:
        return 1
    return n * factorial(n - 1)


def is_sum_of_digit_factorials(n):
    if n == sum(map(lambda x: factorial(int(x)), str(n))):
        logging.debug(f'Found {n}')
        return True
    return False


def get_upper_bound():
    max_per_digit = factorial(9)
    max_digits = max(takewhile(lambda digits: len(str(digits * max_per_digit)) >= digits, count(start=2)))
    return max_digits * max_per_digit


if __name__ == '__main__':
    euler.config_log_level(logging.DEBUG)
    print(euler034())
