"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Created on Oct 3, 2010

@author: Greg Charles
"""
from euler import euler_problem


@euler_problem
def euler028(n:int|str) -> int:
    # Sort of a tricksy solution. The sum of the diagonals can be thought of as the sum of the corners of the
    # concentric square, each with an odd number of elements per side, and dimension two smaller tha square it nests in.
    # For example, the 5x5 square shown above has a 3x3 square nested inside of it, and that has a 1x1 square
    # in it. It's clear that the upper-right corners of each nested square are squares of each square's dimension.
    # Duh, that's literally why we call the 2nd power of something its square. Moreover, each of the other three
    # corners are the square of the dimension minus 1, 2, or 3 times the dimension minus one.
    #
    # Therefore, the sum of the diagonals are the sum of each nested square's corners, which for dimension x is:
    #     4x^2 - 6x + 6.
    # The 1x1 square is a special case because it's just 1, and doesn't have four distinct corners. Therefore, we
    # can sum all corners for the 3x3 square, 5x5, 7x7, ... up to nxn, and then add 1 to sum for the center.
    n = int(n)
    if n < 1 or n % 2 == 0:
        raise Exception(f"Input parameter {n} is not a positive odd integer.")

    return sum(4 * x ** 2  - 6 * x + 6 for x in range(3, n + 1, 2)) + 1

if __name__ == '__main__':
    print(euler028(5))
    print(euler028(1001))
