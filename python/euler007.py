"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6^(th) prime is 13.

What is the 10001^(st) prime number?

@author: Greg Charles
"""

import prime

def euler007(n: int) -> int:
    gen = prime.prime_generator()
    for i in range(n - 1):
        next(gen)

    return next(gen)


if __name__ == '__main__':
    print(euler007(6))
    print(euler007(10_001))
