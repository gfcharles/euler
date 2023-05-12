"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from prime import prime_generator
from itertools import takewhile

def euler010(n: int) -> int:
    return sum(takewhile(lambda p: p < n, prime_generator()))


if __name__ == '__main__':
    print(euler010(10))
    print(euler010(2_000_000))
