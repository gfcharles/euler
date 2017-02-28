'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^(2) + b^(2) = c^(2)

For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

@author: Greg
'''
import time

sum = 1000

start = time.clock() 
    
max = 0
maxComponents = 0,0,0

for c in xrange (sum-2, 2, -1):
    b = sum - c - 1
    while (b > 0):
        a = sum - c - b
        if (b < a):
            # Go to next value of c
            break
        
        if (a**2 + b**2 == c**2):
            product = a * b * c
            if (product > max):
                maxComponents = a, b, c
                max = product
        
        b -= 1
            
print max
print maxComponents
        
print 'Total time = ', time.clock() - start
    
