'''
n! means n x (n - 1) x ... x 3 x 2 x 1

Find the sum of the digits in the number 100!

Created on Sep 20, 2010

@author: Greg Charles
'''
print sum(map(int, str(reduce(lambda x, y : x * y, range(1,101)))))
