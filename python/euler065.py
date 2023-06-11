"""
Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
"""
import logging
from itertools import count

from common.continued_fraction import ContinuedFraction
from euler import euler_problem


# @euler_problem(logging_level=logging.DEBUG, timing=True)
@euler_problem()
def euler065(n: int | str) -> int:
    # CF class numbers convergents as 0, 1, 2 ..., so have to subtract 1 here
    pos = int(n) - 1

    # Represent e (Napier's constant as a base (2) and infinite, non-repeating generator of partial quotients
    cf = ContinuedFraction(2, pq_generator=napier_cf)
    logging.debug(f'Continued fraction: {cf}')

    # Get nth convergent
    conv = cf.convergent(pos)
    logging.debug(f"Convergent {n} is {conv}")

    return sum_digits(conv.numerator)


def napier_cf():
    """
    Generator for continued fractions Napier's (Euler's) constant.
    @return: infinite series of partial quotients
    """
    for k in count(start=1):
        yield 1
        yield 2 * k
        yield 1


def sum_digits(n: int) -> int:
    return sum(int(c) for c in str(n))


if __name__ == '__main__':
    print(euler065(10))
    print(euler065(100))
