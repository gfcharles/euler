'''
Created on Sep 19, 2010

@author: Greg Charles
'''
from math import gcd


def dataDir():
    return '../euler-data/'


def sumDigits(n):
    return sum(map(int, str(n)))


def continue_fractions():
    numerator, denominator = 3, 2
    for i in range(2, 101):
        numerator, denominator = numerator + 2 * denominator, numerator + denominator
        print(i, find_period(numerator, denominator))

def find_period(numerator:int, denominator:int):
    numerator = numerator % denominator
    reducer = gcd(numerator, denominator)
    numerator //= reducer
    denominator //= reducer

    remainders = []
    while True:
        numerator = (10 * numerator) % denominator
        if numerator == 0:
            return 0
        if numerator in remainders:
            return len(remainders) - remainders.index(numerator)

        remainders.append(numerator)


if __name__ == '__main__':
    # print(find_period(4111, 33300))
    continue_fractions()
