"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a � b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from euler import euler_problem
from common.euler_lib import proper_factors
import logging


@euler_problem()
def euler021(n: int|str) -> int:
    return sum(filter(is_amicable, range(2, int(n))))

def is_amicable(a):
    b = sum(proper_factors(a))
    amicable = a != b and sum(proper_factors(b)) == a
    logging.debug(f'{a} and {b} are amicable')
    return amicable


if __name__ == '__main__':
    print(euler021(10_000))
