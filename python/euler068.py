"""
What is the maximum 16-digit string for a "magic" 5-gon ring?

Full description with pictures at https://projecteuler.net/index.php?section=problems&id=68
"""
import itertools
import logging

from euler import euler_problem


@euler_problem()
def euler068(n: int | str) -> int:
    sides = int(n)
    number_list = [x for x in range(1, 2 * sides + 1)]
    maximum_allowed = 10 ** 16  # Imposed limit in problem statement

    return find_optimum_magic_polygon(sides, number_list, maximum_allowed)


def find_optimum_magic_polygon(sides: int, number_list: list[int], maximum_allowed: int = None) -> int:
    sum_of_all_numbers = sum(number_list)
    answer = 0

    for vertices in itertools.combinations(number_list, sides):
        # Total sum of n lines in ring must be a multiple of n if the n totals are going to match.
        # (The vertices are in included in two lines, and the other numbers in just one.)
        total_sum = sum(vertices) + sum_of_all_numbers
        if total_sum % sides == 0:
            # For possible vertices, try all possible permutations (taking into account rotational symmetry).
            for perm in itertools.permutations(vertices[0:-1]):
                permuted_vertices = list(perm)
                permuted_vertices.append(vertices[-1])
                try:
                    magic = rotate(make_magic_polygon(permuted_vertices, sides, total_sum, number_list))
                    logging.debug(magic)
                    number = to_int(magic)
                    if maximum_allowed is None or number < maximum_allowed:
                        answer = max(answer, number)
                except ValueError:
                    pass

    return answer


# Make a magic polygon if possible. Return false and an empty list if not possible.
def make_magic_polygon(vertices, sides, total_sum, number_list):
    target = total_sum // sides

    taken = list(vertices)
    triples = []
    for i in range(sides):
        y = vertices[i]
        z = vertices[(i + 1) % sides]
        x = target - y - z
        if x not in number_list or x in taken:
            raise ValueError('No magic')

        taken.append(x)
        triples.append([x, y, z])

    return rotate(triples)


# Rotate the triples list so the triple with the minimum outer value is first.
def rotate(triples):
    outer_values = list(map(lambda t: t[0], triples))
    min_index = outer_values.index(min(outer_values))
    return triples[min_index:] + triples[:min_index]


# Convert the triples list to an integer.
def to_int(magic):
    return int(''.join(map(str, [item for sub in magic for item in sub])))


if __name__ == '__main__':
    print(euler068(3))
    print(euler068(5))
