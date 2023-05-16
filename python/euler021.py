"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a � b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Created on Sep 20, 2010

@author: Greg Charles
"""
import math

def properFactors(value):   
    limit = int(math.sqrt(value))
    factors = [1]
    for x in range(2,limit+1):
        if value % x == 0:
            factors.append(x)
            y = value / x
            if (y != x):
                factors.append(y)
    return factors

def isAmicable(a):
    b = sum(properFactors(a))
    return (a != b and sum(properFactors(b)) == a)
 

print sum(filter(isAmicable, xrange(2,10000)))
