"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from euler import euler_problem
from common.euler_lib import prime_generator
from itertools import takewhile
from math import sqrt

@euler_problem()
def euler003(n: int|str) -> int:
    # Get list of possible prime factors for input value in descending value
    primes_list = list(takewhile(lambda p: p <= int(sqrt(int(n))), prime_generator()))

    # Return first (largest) prime that is a factor of input value
    return next(x for x in reversed(primes_list) if int(n) % x == 0)


if __name__ == '__main__':
    print(euler003(13195))
    print(euler003(600851475143))
