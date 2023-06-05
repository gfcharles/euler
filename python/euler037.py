"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly, we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncate-able from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncate-able primes.
"""
import re
from itertools import takewhile
from typing import Generator

from common.euler_lib import is_prime, prime_generator
from euler import euler_problem


@euler_problem()
def euler037(n: int | str) -> int:
    gen = takewhile(lambda x: x < int(n), prime_generator())
    return sum(x for x in gen if is_truncations_prime(x))


def truncations(n: int) -> Generator[int, None, None]:
    string = str(n)
    for i in range(1, len(string)):
        yield int(string[:i])
        yield int(string[-i:])


def is_truncations_prime(n: int) -> bool:
    if n < 10:
        return False

    string = str(n)
    if re.search("[0468]", string) or re.search(".[25]", string):
        return False

    for x in truncations(n):
        if not is_prime(x):
            return False
    return True


if __name__ == '__main__':
    print(euler037(1_000_000))
