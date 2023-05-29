"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the
right and down, is indicated in bold red and is equal to 2427.

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""
from typing import Tuple

from euler import euler_problem

sample_data = \
"""131,673,234,103,18
201,96,342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37,331"""

@euler_problem()
def euler081(file_name:str) -> int:
    if file_name == 'sample':
        text = sample_data
    else:
        with open(f'./euler_data/{file_name}', 'r') as data_file:
            text = data_file.read()

    data = list(list(map(lambda el: int(el), row.split(','))) for row in text.splitlines())
    dimension = len(data)

    for x, y in get_by_slice(dimension):
        data[x][y] += get_min_parent((x, y), data)

    # Answer is in bottom right corner
    return data[-1][-1]


def get_by_slice(dimension:int) -> list[Tuple[int,int]]:
    for n in range(2 * dimension - 1):
        if n < dimension:
            for i in range(n + 1):
                yield n - i, i
        else:
            for i in range(1, 2 * dimension - n):
                yield dimension - i, n - dimension + i

def get_min_parent(coordinates, data):
    x, y = coordinates
    if x == 0 and y == 0:
        return 0

    parent_values = []
    if x > 0:
        parent_values.append(data[x - 1][y])
    if y > 0:
        parent_values.append(data[x][y - 1])

    return min(parent_values)


if __name__ == '__main__':
    print(euler081('sample'))
    print(euler081('p081_matrix.txt'))
