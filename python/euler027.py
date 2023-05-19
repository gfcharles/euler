"""
Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when
n = 40, 40^(2) + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive
values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| <= 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients a and b for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0.
"""
from itertools import count
import logging
from common.euler_lib import is_prime
from euler import euler_problem


@euler_problem
def euler027(n:int|str) -> int:
    n = abs(int(n))
    primes, a, b =  max_by_sequence_length(
        consecutive_primes(a, b)
                 for a in range(-(n - 1), n)  # |a| < n
                 for b in range(-n, n + 1)  # |b| <= n
    )

    logging.info(f"Longest sequence of primes is {primes} for coefficients a = {a} and b = {b}.")
    return a * b

def max_by_sequence_length(items):
    # Sequence count store in first position of tuple, coefficients are in the second and third positions
    max_item = None
    for item in items:
        if max_item is None or item[0] > max_item[0]:
            max_item = item

    return max_item

def consecutive_primes(a: int, b: int):
    n = 0
    for n in count(start=0):
        if not is_prime(n * n + a * n + b):
            break

    return n, a, b


if __name__ == '__main__':
    print(euler027(1000))
