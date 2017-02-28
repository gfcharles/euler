'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

@author: Greg Charles
'''
import time

# Greatest common divisor of a and b
def gcd(a, b):
    while (1):
        if (a == b):
            return a
        
        if (a < b):
            a, b = b - a, a
        else:
            a, b = a - b, b

# Least common multiple of a and b
def lcm(a, b):
    if (a == b):
        return a;
    
    x = min(a, b)
    y = max(a, b)

    if (y % x == 0):
        return y

    return x * y / gcd(x,y)

# Get the least common multiple of all numbers from 1 to 20
start = time.clock()
total = lcm(2, 3)
a = 4
while (a <= 20):
    total = lcm(a, total)
    #print 'a = ', a, ' total = ', total
    a += 1
    
    
print total
print 'Total time = ', (time.clock() - start)

