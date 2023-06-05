"""
The fraction ^(49)/_(98) is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that ^(49)/_(98) = ^(4)/_(8), which is correct, is obtained by canceling the 9s.

We shall consider fractions like, ^(30)/_(50) = ^(3)/_(5), to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
import logging
from functools import reduce
from math import gcd
from typing import Tuple

import euler


@euler.euler_problem()
def euler033(_='n/a') -> int:
    numerator, denominator = \
        reduce(lambda total, element: multiply_tuples(total, element),
               ((a, b) for a in range(10, 100) for b in range(a + 1, 100) if test_reduction(a, b)))

    return denominator // gcd(numerator, denominator)


def test_reduction(a: int, b: int) -> bool:
    digits_a = a // 10, a % 10
    digits_b = b // 10, b % 10

    # Reject "trivial" case.
    if digits_a[1] == 0 or digits_b[1] == 0:
        return False

    # The ratio to match
    ratio = a / b

    for i in range(2):
        for j in range(2):
            # If a digit in a matches with a digit in b, compare the ratio of two other digits with the full fraction
            if digits_a[i] == digits_b[j]:
                match = digits_a[1 - i] / digits_b[1 - j] == ratio
                if match:
                    logging.debug(f'Found: {(a, b)}')
                return match

    return False


def multiply_tuples(x: Tuple[int, int], y: Tuple[int, int]) -> Tuple:
    return tuple(z[0] * z[1] for z in zip(x, y))


if __name__ == '__main__':
    euler.config_log_level(logging.DEBUG)
    print(euler033())
