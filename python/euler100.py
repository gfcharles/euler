"""
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were
taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21) * (14/20)
.
The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box
containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10 ^ 12 discs in total, determine the number of
blue discs that the box would contain.
"""
import logging
import math
import typing
from itertools import count, dropwhile

from euler import euler_problem


# @euler_problem(logging_level=logging.DEBUG, timing =True)
@euler_problem()
def euler100(n: int | str) -> int:
    solution = next(dropwhile(lambda s: s.total <= int(n), solutions_generator()))
    return solution.blue


# Trying out (typed) named tuple just for fun
Solution = typing.NamedTuple('Solution', [('total', int), ('blue', int)])


def solutions_generator():
    def is_solution(tot: int, blue: int):
        return tot * (tot - 1) == 2 * blue * (blue - 1)

    # Seed the generator with first two solutions
    a, b = Solution(4, 3), Solution(21, 15)

    logging.debug(a)
    yield a

    logging.debug(b)
    yield b

    divisor = math.sqrt(2)

    # A couple of points makes this problem possible to solve in a reasonable amount of time:
    #   1. To fit the solution, the count of blue discs must be slightly above the total discs / sqrt(2)
    #   2. The ratio of total discs to previous solution's total converges from below on a fixed ratio (~5.28)
    #      Why? I don't entirely understand that, but it's related to Diophantine equations and
    #      continued fractions.
    while True:
        # Use point two above
        start_with = int(b.total * (b.total / a.total))

        for total in count(start=start_with):
            blue_count = int(math.ceil(total / divisor))
            if is_solution(total, blue_count):
                a, b = b, Solution(total, blue_count)
                logging.debug(b)
                yield b
                break


if __name__ == '__main__':
    print(euler100(21))
    print(euler100(10 ** 12))
