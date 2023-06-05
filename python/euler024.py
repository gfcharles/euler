"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic
permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import json
from functools import cache

from euler import euler_problem


@euler_problem()
def euler024(json_text: str = None, elements: list = None, position: int = 0):
    if elements is None:
        elements, position = extract(json_text)

    length = len(elements)
    if position > factorial(length):
        raise Exception(f'Position {position} is larger than number of permutations: {factorial(length)}')

    remaining_elements = list(elements)

    # Subtract 1 because the 1st position is after 0 permutations, etc.
    remainder = position - 1
    answer = []

    for x in reversed(range(length)):  # go from (length - 1) to 0
        # how many complete permutations of the x largest of the x + 1 remaining elements were there?
        next_index = remainder // factorial(x)
        # that gives us the index next element that will be in that position
        answer.append(remaining_elements.pop(next_index))

        remainder -= (next_index * factorial(x))

    return ''.join(map(str, answer))


def extract(json_text: str) -> (list, int):
    obj = json.loads(json_text)
    return obj['elements'], obj['position']


@cache
def factorial(n: int) -> int:
    if n < 2:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    print(euler024(elements=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], position=1_000_000))
    print(euler024(elements=[0, 1, 2], position=4))
    print(euler024('{"elements": [0, 1, 2], "position": 4}'))
