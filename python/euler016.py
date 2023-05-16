"""
2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^(1000)?
"""
from euler import euler_problem

@euler_problem
def euler016(n:int|str) -> int:
    n = int(n)
    return sum(map(lambda x: int(x), str(1 << n)))


if __name__ == '__main__':
    print(euler016(15))
    print(euler016(1000))
