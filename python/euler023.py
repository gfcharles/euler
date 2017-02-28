'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum 
of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two 
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as 
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is 
known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Created on Sep 26, 2010

@author: Greg Charles
'''
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

# An Abundant number is one where the sum of proper factors is greater than the number.
# The smallest abundant number is 12.
def isAbundant(value):
    if (value < 12): return False
    return sum(properFactors(value)) > value


# The theoretical maximum number that isn't the sum of two abundant numbers is 28123.
maxSumOfAbundants = 28183

# First, find all abundant number less than this maximum.
abundants =  filter(isAbundant, xrange(1,maxSumOfAbundants))

# Create an array of possible sum of abundant numbers, initially all false.
candidates = [False]*(maxSumOfAbundants+1)

# Find all possible sums of two abundant numbers, where the sum is less than or equal to the maximum. 
for i in xrange(0, len(abundants)):
    for j in xrange(0, len(abundants)):
        sumOfAbundants = abundants[i] + abundants[j]
        if sumOfAbundants > maxSumOfAbundants:
            break
        else:
            candidates[sumOfAbundants] = True

# Find sum of all positive integers now known not to be sums of two abundant numbers
print sum(filter(lambda x: candidates[x] == False, xrange(1,maxSumOfAbundants+1)))
