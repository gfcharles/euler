"""
The following iterative sequence is defined for the set of positive integers:

n : n/2 (n is even)
n : 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import logging
from functools import cache

from euler import euler_problem

@euler_problem
def euler014(n:int|str) -> int:
    n = int(n)
    max_collatz = 0
    max_x = None

    # Since the double of every number in the lower half of the range exists in the upper half,
    # the max collatz count must be in the upper half. This only gives a marginal improvement when
    # using the recursive method (with caching), but doubles the speed of the iterative.
    for x in range((n - 1) // 2, n):
        count = collatz_count_r(x)
        if count > max_collatz:
            max_collatz = count
            max_x = x

    logging.info(f"Max: {max_collatz} steps for {max_x}")

    return max_x


# Caching could help in some scenarios, but not for this problem domain because we never call it
# twice with the same value.
def collatz_count(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1

    return count

# Caching with recursion is the best approach here, since all chains will share some part of their tails.
@cache
def collatz_count_r(n):
    if n == 1:
        return 1

    if n % 2 == 0:
        return 1 + collatz_count_r(n // 2)
    else:
        return 1 + collatz_count_r(3 * n + 1)

if __name__ == '__main__':
    print(euler014(10))
    print(euler014(1000000))
