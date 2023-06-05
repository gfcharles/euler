"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from itertools import takewhile

from common.euler_lib import prime_generator
from euler import euler_problem


@euler_problem()
def euler010(n: int | str) -> int:
    return sum(takewhile(lambda p: p < int(n), prime_generator()))


if __name__ == '__main__':
    print(euler010(10))
    print(euler010(2_000_000))
