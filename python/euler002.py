"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not exceed four million.
"""
from euler import euler_problem
from common.euler_lib import fibonacci

@euler_problem()
def euler002(n: int|str) -> int:
    return sum(val for _, val in fibonacci(seed=(1, 2), limit=int(n), filtering_by=is_even))

def is_even(x):
    return x % 2 == 0


if __name__ == '__main__':
    print(euler002(89))
    print(euler002(4_000_000))
