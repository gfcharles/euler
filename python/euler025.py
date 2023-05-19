"""
The Fibonacci sequence is defined by the recurrence relation:

    F_(n) = F_(n-1) + F_(n-2), where F_(1) = 1 and F_(2) = 1.

Hence, the first 12 terms will be:

    F_(1) = 1
    F_(2) = 1
    F_(3) = 2
    F_(4) = 3
    F_(5) = 5
    F_(6) = 8
    F_(7) = 13
    F_(8) = 21
    F_(9) = 34
    F_(10) = 55
    F_(11) = 89
    F_(12) = 144

The 12th term, F_(12), is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""
from common.euler_lib import fibonacci
from euler import euler_problem


@euler_problem
def euler025(n: int|str) -> int:
    fibonacci_gen = fibonacci(filtering_by=lambda f: len(str(f)) >= int(n))
    return next(fibonacci_gen)[0]

if __name__ == '__main__':
    print(euler025(3))
    print(euler025(1000))
