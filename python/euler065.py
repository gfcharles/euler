'''
Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
Created on Jan. 21, 2011

@author: Greg Charles
'''
from fractions import Fraction
from gregutils import sumDigits

class ContinuedFraction(object):

    def __init__(self, base, list):
        self.base = base
        self.list = list

    def asFraction(self):
        baseFraction = 0
        for el in reversed(self.list):
            baseFraction = Fraction(1,el+baseFraction)

        return self.base + baseFraction

    def __str__( self ):
        string = '[' + str(self.base)
        if len(self.list) > 0:
            string += '; '
            string += ','.join(map(str,self.list))
        string += ']'

        return string



def eulerConstantMapper(x):
    if (x % 3 == 1):
        return 2 * (x/3 + 1)
    else:
        return 1


cf = ContinuedFraction(2, map(eulerConstantMapper, range(0,99)))
fraction =  cf.asFraction()
print cf
print fraction
print float(fraction)
print sumDigits(fraction.numerator)

for x in range(0,99):
    cf = ContinuedFraction(2, map(eulerConstantMapper, range(0,x)))
    print cf.asFraction()

    


