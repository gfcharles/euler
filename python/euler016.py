'''
2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^(1000)?

Created on Sep 19, 2010

@author: Greg Charles
'''
n = 1000
print sum(map(lambda x: int(x), str(1<<n)))
