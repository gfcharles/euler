"""
n! means n x (n - 1) x ... x 3 x 2 x 1

Find the sum of the digits in the number 100!
"""
from functools import reduce

from euler import euler_problem


@euler_problem()
def euler020(n: int | str) -> int:
    return sum(map(int, str(reduce(lambda x, y: x * y, range(1, int(n) + 1)))))


if __name__ == '__main__':
    print(euler020(100))
