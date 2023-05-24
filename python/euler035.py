"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import re
from itertools import takewhile
from typing import Iterator
import logging

import euler
from common.euler_lib import is_prime, prime_generator

@euler.euler_problem
def euler035(n:int|str) -> int:
    return count(filter(is_rotational_prime, (x for x in primes(int(n)))))


def rotate(n, pos=1):
    string = str(n)
    pos = pos % len(string)
    if pos == 0:
        return n
    else:
        return int(string[-pos:] + string[:-pos])

def rotations(n):
    rotation_set = set()
    for pos in range(len(str(n))):
        rotation_set.add(rotate(n, pos))
    return list(rotation_set)

def is_rotational_prime(n):
    if n == 2:
        logging.debug(f"Found: {n}")
        return True
    elif re.search("[02468]", str(n)):
        return False
     
    for x in rotations(n):
        if not is_prime(x):
            return False

    logging.debug(f"Found: {n}")
    return True

def count(it:Iterator) -> int:
    return sum(1 for _ in it)

def primes(limit:int) -> Iterator[int]:
    return (x for x in takewhile(lambda p: p < limit, prime_generator()))


if __name__ == '__main__':
    euler.config_log_level(logging.DEBUG)

    print(euler035(100))
    print(euler035(1_000_000))
