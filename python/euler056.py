'''
A googol (10^(100)) is a massive number: one followed by one-hundred zeros; 100^(100) is almost unimaginably large: 
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^(b), where a, b < 100, what is the maximum digital sum?

Created on Oct 30, 2010

@author: Greg Charles
'''
maxSum = 0
for a in xrange(1,100):
    for b in xrange(1,100):
        maxSum = max(maxSum, sum(map(int, str(a**b))))
        
print maxSum
        
