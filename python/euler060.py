"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
import logging
from functools import cache
from itertools import takewhile

from common.euler_lib import prime_generator, is_prime
from euler import euler_problem


# @euler_problem(logging_level=logging.DEBUG, timing=True)
@euler_problem()
def euler060(n:int|str) -> int:
    prime_set = [0] * int(n)  # Start set of primes as a list of n 0
    if not build_prime_set(prime_set, 0, int(n)):
        raise Exception('No set of primes found that fits the conditions')

    logging.debug(f'Set = {prime_set}')
    return sum(prime_set)


def build_prime_set(prime_set, current_size, target_size):
    """
    Recursive function that prints the first set it finds of the requested size that fits the conditions.
    It then stops looking. This doesn't guarantee the smallest sum, but works for this case.
    build_set_recursive
    """
    if current_size == target_size:
        return True

    # If digits add to a multiple of three, then the number is divisible by three.
    # So when concatenate two primes, the result can't be prime if the modulo 3s add to 3.
    # That means that if we have any primes in the set, except for 3 itself, then each additional
    # member must have the same module-3 as the other members. 2 + 2 = 4 (1 modulo 3) and 1 + 1 = 2.
    # This allows us to skip about half of our checks.
    mod_to_match = 0
    if current_size > 0:
        mod_to_match = prime_set[current_size - 1] % 3

    for next_prime in limited_prime_generator(10_000):
        if mod_to_match != 0 and (next_prime % 3) != mod_to_match:
            continue
        if next_prime <= prime_set[current_size - 1] or next_prime == 2 or next_prime == 5:
            continue

        if tester(prime_set, current_size, next_prime):
            prime_set[current_size] = next_prime
            if build_prime_set(prime_set, current_size + 1, target_size):
                return True

    return False

# Test to see that the addition of m to the known set produces a valid a new set.
def tester(prime_set, size, candidate):
    candidate_digits = len(str(candidate))
    for i, prime in enumerate(prime_set):
        if i >= size:
            break

        prime_digits = len(str(prime))
        if not is_prime_cached(prime * 10 ** candidate_digits + candidate):
            return False
        if not is_prime_cached(candidate * 10 ** prime_digits + prime):
            return False

    return True

@cache
def is_prime_cached(n:int) -> bool:
    return is_prime(n)


def limited_prime_generator(limit:int):
    return takewhile(lambda p: p < limit, prime_generator())


if __name__ == '__main__':
    # Build a set with five elements, starting from nothing.
    print(euler060(4))
    print(euler060(5))
