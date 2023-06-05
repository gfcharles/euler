"""
The cube, 41063625 (345^(3)), can be permuted to produce two other cubes: 56623104 (384^(3)) and 66430125 (405^(3)).
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""
import logging
from collections import defaultdict
from itertools import count

from euler import euler_problem


@euler_problem()
def euler062(n: int | str) -> int:
    n = int(n)
    cubes = defaultdict(set)

    for c in count(start=100):
        cube = c ** 3
        key = "".join(sorted(str(cube)))
        cubes[key].add(cube)

        if len(cubes[key]) == n:
            logging.debug(sorted(cubes[key]))
            return min(cubes[key])


if __name__ == '__main__':
    print(euler062(3))
    print(euler062(5))
