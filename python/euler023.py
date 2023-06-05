"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum
of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from functools import cache

from common.euler_lib import proper_factors
from euler import euler_problem

MINIMUM_ABUNDANT_NUMBER = 12


@euler_problem()
def euler023(n: int | str) -> int:
    return sum(x for x in range(1, int(n) + 1) if not is_sum_of_two_abundant_numbers(x))


@cache
def is_abundant(n: int) -> bool:
    """
        An Abundant number is one where the sum of proper factors is greater than the number.
        The smallest abundant number is 12.

        @param n: the number to check for abundant
        @return: True/False if n is an abundant number
    """
    if n <= 0:
        raise Exception(f'Invalid input {n}. Must be a positive integer.')
    if n < MINIMUM_ABUNDANT_NUMBER:
        return False
    return sum(proper_factors(n)) > n


def is_sum_of_two_abundant_numbers(n: int):
    if n < 2 * MINIMUM_ABUNDANT_NUMBER:
        return False

    for i in range(MINIMUM_ABUNDANT_NUMBER, n // 2 + 1):
        if is_abundant(i) and is_abundant(n - i):
            return True

    return False


if __name__ == '__main__':
    print(euler023(28123))
