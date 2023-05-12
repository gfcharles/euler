from data_loader import load_primes

primes_list = load_primes()

# a fast prime number list 'generator' using a sieve algorithm
# def primes(n):
#     """
#     returns a list of prime numbers from 2 to n
#     """
#     if n < 2:  return []
#     if n == 2: return [2]
#     # create a list of odd numbers from 3 to n
#     nums = list(range(3, n+1, 2))
#     nums_len = (n // 2) - 1 + (n % 2)
#     idx = 0
#     idx_sqrtn = (int(n**0.5) - 3) // 2
#     while idx <= idx_sqrtn:
#         nums_idx = (idx << 1) + 3
#         for j in range(idx*(nums_idx+3)+3, nums_len, nums_idx):
#             # if not a prime replace with zero
#             nums[j] = 0
#         idx += 1
#         while idx <= idx_sqrtn:
#             if nums[idx] != 0:
#                 break
#             idx += 1
#     # remove all the zero entries
#     return [2] + [x for x in nums if x != 0]


def compute_next_prime(last_prime: int) -> int:
    candidate = last_prime
    while True:
        candidate += 2
        if is_prime(candidate):
            return candidate

def prime_generator():
    for p in primes_list:
        yield p

    last_prime = primes_list[-1]

    while True:
        last_prime = compute_next_prime(last_prime)
        yield last_prime


def factor(n: int) -> dict:
    prime = prime_generator()
    residual = n
    factor_map = dict()

    while residual > 1:
        exp = 0
        p = next(prime)
        while residual % p == 0:
            exp += 1
            residual //= p
        if exp > 0:
            factor_map[p] = exp

    return factor_map


def multiply(factor_map:dict) -> int:
    prod = 1
    for fact, exp in factor_map.items():
        prod *= (fact ** exp)

    return prod


def lcm_by_factor_maps(factor_maps) -> int:
    merged = dict()
    for factor_map in factor_maps:
        for fact in factor_map:
            exp = factor_map[fact]

            if fact in merged.keys():
                merged[fact] = max(merged[fact], exp)
            else:
                merged[fact] = exp

    return multiply(merged)


def lcm(*values: int) -> int:
    factor_maps = list(map(factor, *values))
    return lcm_by_factor_maps(factor_maps)


# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)
def is_prime(n: int) -> bool:
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

