'''
We shall say that an n-digit number is pan-digital if it makes use of all the digits 1 to n exactly once; for example, 
the 5-digit number, 15234, is 1 through 5 pan-digital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 
1 through 9 pan-digital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

Created on Oct 30, 2010

@author: Greg Charles
'''
import itertools
from sets import Set

def testTwoThree(n):
    return int("".join(map(str,n[0:2]))) * int("".join(map(str,n[2:5]))) == int("".join(map(str,n[5:10])))

def testOneFour(n):
    return int("".join(map(str,n[0:1]))) * int("".join(map(str,n[1:5]))) == int("".join(map(str,n[5:10])))

products = Set([])
for p in itertools.permutations([1,2,3,4,5,6,7,8,9]):
    if testOneFour(p) or testTwoThree(p):
        products.add(int("".join(map(str,p[5:10]))))
 
print sum(products)   

