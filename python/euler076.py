"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""
from functools import cache

from euler import euler_problem


@euler_problem()
def euler076(n: int | str) -> int:
    n = int(n)

    # Count all possible combos that sum to n without using n itself.
    return count_combos(n, n - 1)


@cache
def count_combos(amount: int, max_addend: int) -> int:
    if max_addend == 1:
        return 1

    return sum(count_combos(amount - cnt * max_addend, max_addend - 1) for cnt in range(amount // max_addend + 1))


if __name__ == '__main__':
    print(euler076(5))
    print(euler076(100))
