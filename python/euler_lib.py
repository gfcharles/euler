from functools import reduce
from typing import Generator

from data_loader import load_primes

primes_list = load_primes()

class FactorMap(dict):
    def factors(self):
        return self.keys()

    def counts(self):
        return self.values()

    def factor_counts(self):
        return self.items()

    def count(self, fct:int) -> int:
        return self[fct]


def compute_next_prime(last_prime: int) -> int:
    candidate = last_prime
    while True:
        candidate += 2
        if is_prime(candidate):
            return candidate

def prime_generator() -> Generator[int, None, None]:
    for p in primes_list:
        yield p

    last_prime = primes_list[-1]

    while True:
        last_prime = compute_next_prime(last_prime)
        yield last_prime


def factor_map(n:int) -> FactorMap:
    prime = prime_generator()
    residual = n
    fm = FactorMap()

    while residual > 1:
        exp = 0
        p = next(prime)
        while residual % p == 0:
            exp += 1
            residual //= p
        if exp > 0:
            fm[p] = exp
    return fm


def product_of(fm:FactorMap) -> int:
    def _prod(nums):
        return reduce(lambda x, y: x * y, nums)
        pass

    return _prod(fct ** fm[fct] for fct in fm.factors())

def lcm(*values: int) -> int:
    return lcm_by_factor_maps(list(map(factor_map, *values)))

def lcm_by_factor_maps(factor_maps) -> int:
    merged = FactorMap()
    for fm in factor_maps:
        for fact in fm.factors():
            cnt = fm[fact]

            if fact in merged.keys():
                merged[fact] = max(merged[fact], cnt)
            else:
                merged[fact] = cnt

    return product_of(merged)

def count_factors(n: int) -> int:
    # A quick way to count total factors. Get a map of the prime factors with counts,
    # add one to each count, and multiply.
    return reduce(lambda total, count: total * (count + 1), factor_map(n).values(), 1)

def count_proper_factors(n: int) -> int:
    # Is 1 an exception, or does it really have 0 proper factors?
    return count_factors(n) - 1


# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)
def is_prime(n:int|str) -> bool:
    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 and 3 are prime but are exceptions to mod 6 rule
    if n <= 3:
        return True

    # Test for invalid candidates
    r = n % 6
    if r != 1 and r != 5:
        return False

    # Check n against known primes.
    for x in primes_list:
        if x * x > n:
            return True
        if n == x or n % x == 0:
            return False

    # This method currently can only check up to the square of the last prime loaded from data.
    raise OverflowError
