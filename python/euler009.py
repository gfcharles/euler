"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^(2) + b^(2) = c^(2)

For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import logging
from euler import euler_problem

@euler_problem
def euler009(n:int|str) -> int:
    n = int(n)
    for c in range(n - 2, 2, -1):
        for b in range(n - c - 1, 0, -1):
            a = n - c - b
            if b <= a:
                break # Go to next value of c

            if a ** 2 + b ** 2 == c ** 2:
                logging.info(f'Found triplets {a}, {b}, {c}, which sum to {n}')
                return a * b * c

    raise ValueError(f'No pythagorean triplets sum to {n}')


if __name__ == '__main__':
    print(euler009(12))
    print(euler009(1000))
