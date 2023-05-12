"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from prime import prime_generator
from itertools import takewhile
from math import sqrt

def euler003(input_value: int) -> int:
    # Get list of possible prime factors for input value in descending value
    primes_list = list(takewhile(lambda p: p <= int(sqrt(input_value)), prime_generator()))

    # Return first (largest) prime that is a factor of input value
    return next(x for x in reversed(primes_list) if input_value % x == 0)

if __name__ == '__main__':
    print(euler003(13195))
    print(euler003(600851475143))
