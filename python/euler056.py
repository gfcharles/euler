"""
A googol (10^(100)) is a massive number: one followed by one-hundred zeros; 100^(100) is almost unimaginably large:
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^(b), where a, b < 100, what is the maximum digital sum?
"""
import logging

from euler import euler_problem


@euler_problem()
def euler056(n:int|str) -> int:
    n = int(n)
    return max(sum_of_digits(a ** b) for a in range(n) for b in range(n))


def sum_of_digits(n: int):
    return sum(map(int, str(n)))

if __name__ == '__main__':
    print(euler056(10))
    print(euler056(100))
