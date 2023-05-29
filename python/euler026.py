"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    ^(1)/_(2)    =     0.5
    ^(1)/_(3)    =     0.(3)
    ^(1)/_(4)    =     0.25
    ^(1)/_(5)    =     0.2
    ^(1)/_(6)    =     0.1(6)
    ^(1)/_(7)    =     0.(142857)
    ^(1)/_(8)    =     0.125
    ^(1)/_(9)    =     0.(1)
    ^(1)/_(10)    =     0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that ^(1)/_(7) has a
6-digit recurring cycle.

Find the value of d < 1000 for which ^(1)/_(d) contains the longest recurring cycle in its decimal fraction part.
"""
import logging

from euler import euler_problem


@euler_problem()
def euler026(n:int|str) -> int:
    max_x = 0
    max_cycle = 0

    for x in reversed(range(int(n))):
        # Max length of cycle for a number x is x - 1
        if (x - 1) < max_cycle:
            logging.debug(f"Skipping values {x} and below.")
            break

        current = cycle_length(x)
        if current > max_cycle:
            max_x = x
            max_cycle = current

    logging.info(f"Max cycle for fractions 1/n with denominators less than {n} is {max_cycle} for 1/{max_x}.")
    return max_x

def cycle_length(n: int) -> int:
    """
    Counts the cycle length of repeating decimals for 1/n. Returns 0 for terminating decimals.

    @param n: positive integer to count cycle length.
    @return: cycle length of repeating decimals
    """
    while n % 2 == 0:
        n /= 2 
    while n % 5 == 0:
        n /= 5

    count = 1
    remainder = 10 % n
    while True:
        if remainder == 0:
            return 0
        if remainder == 1:
            return count
        remainder = (10 * remainder) % n
        count += 1


if __name__ == '__main__':
    print(euler026(10))
    print(euler026(1000))
