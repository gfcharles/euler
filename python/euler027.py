'''
Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when 
n = 40, 40^(2) + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly 
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive 
values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

for consecutive values of n, starting with n = 0.

Created on Oct 3, 2010

@author: Greg Charles
'''
import prime
import time

start = time.clock()

max = 0
product = 0

for a in xrange(-1000,1001):
    for b in prime.primes(1000):
        n = 1
        while True:
            if (not prime.isprime(n*n + a*n + b)):
                break
            n += 1

        if (n-1 > max):
            max = n-1
            product = a * b

print product

print time.clock() - start

