from math import log

from euler import euler_problem

"""
Determine the largest value in a file containing a long list of values separated into base and exponent.

Return the line number containing the largest value.
"""


@euler_problem()
def euler099(filename: str) -> int:
    with open(f'./euler_data/{filename}', newline='') as datafile:
        max_line = 0
        max_value = 0

        for i, row in enumerate(datafile.readlines()):
            base, exp = map(int, row.split(','))
            value = exp * log(base)
            if value > max_value:
                max_value = value
                max_line = i + 1

        return max_line


if __name__ == '__main__':
    print(euler099('0099_base_exp.txt'))
