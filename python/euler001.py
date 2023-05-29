#! /usr/bin/python
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from euler import euler_problem


@euler_problem()
def euler001(n: int|str) -> int:
    return sum(x for x in range(int(n)) if x % 3 == 0 or x % 5 == 0)

if __name__ == '__main__':
    print(euler001(10))
    print(euler001(1000))
