'''
The sum of the squares of the first ten natural numbers is,
1^(2) + 2^(2) + ... + 10^(2) = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^(2) = 55^(2) = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

@author: Greg Charles

Note: square of sums = sum of cubes
'''
import time

start = time.clock()
 
a = 1;
total = 0;
while (a <= 100):
    square = a ** 2;
    cube = a * square;
    total += (cube - square)
    a += 1;
    
print total

print 'Total time = ', time.clock() - start
