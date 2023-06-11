"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from
top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem,
as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""
from euler018 import find_max_path
from euler import euler_problem


@euler_problem()
def euler067(filename: str) -> int:
    # Read data in from file
    with open(f'./euler_data/{filename}', 'r') as datafile:
        triangle = datafile.read()
        rows = []
        for row in triangle.splitlines():
            rows.append(list(int(el) for el in row.strip().split(' ')))

        return find_max_path(rows)


if __name__ == '__main__':
    print(euler067('0067_triangle.txt'))
