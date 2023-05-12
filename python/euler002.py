#! /usr/bin/python
"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not exceed four million.
"""
def euler002(input_value: object) -> int:
    return sum(fibonacci(input_value, filtering_by=is_even))

def fibonacci(limit, filtering_by = lambda x : True):
    a, b = 1, 2
    if  1 <= limit and filtering_by(a):
        yield a

    while b <= limit:
        if filtering_by(b):
            yield b
        a, b = b, a + b

def is_even(x):
    return x % 2 == 0


if __name__ == '__main__':
    print(euler002(89))
