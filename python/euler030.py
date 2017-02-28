'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^(4) + 6^(4) + 3^(4) + 4^(4)
    8208 = 8^(4) + 2^(4) + 0^(4) + 8^(4)
    9474 = 9^(4) + 4^(4) + 7^(4) + 4^(4)

As 1 = 1^(4) is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Created on Oct 3, 2010

@author: Greg Charles
'''
def isSumOfDigits(n, power):
    return n == sum(map(lambda c: (ord(c) - ord('0')) ** power, str(n)))


def getUpperBound(power):
    base = 9 ** power
    digit_count = 2
    upper_bound = 0
    while True:
        digit_count += 1
        if (len(str(digit_count * base))) < digit_count:
            return upper_bound 
        upper_bound = digit_count * base

print sum(filter(lambda n : isSumOfDigits(n,5), xrange(10, getUpperBound(5)+1)))
