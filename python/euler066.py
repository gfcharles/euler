'''
Consider quadratic Diophantine equations of the form:

x2 - Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 - 13 x 1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 - 2 x 22 = 1
22 - 3 x 12 = 1
92 - 5 x 42 = 1
52 - 6 x 22 = 1
82 - 7 x 32 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.

Created on Jan 30, 2011

@author: Greg Charles
'''
import math
from fractions import Fraction

class ContinuedFraction(object):

    def __init__(self, value):
        self.value = value
        self.base = self.__computeBase(value)
        self.list = self.__computeList(value, self.base)
        self.period = len(self.list)

    def __computeBase(self,value):
        return int(math.floor(math.sqrt(value)))

    def __computeList(self, s, base):
        mdList = []
        aList = []
        m, d, a = 0,1,base

        finished = (base * base == s)

        while not finished:
            m = d * a - m
            d = (s - m*m) / d
            md = [m,d]
            if md in mdList:
                finished = True
            else:
                mdList.append(md)
                a = int(math.floor((base + m) / d))
                aList.append(a)

        return aList

    def convergents(self):
        hList = [self.base, self.list[0]*self.base + 1]
        kList = [1, self.list[0]]

        yield Fraction(hList[0], kList[0])
        yield Fraction(hList[1], kList[1])

        n = 1
        while True:
            i = n % self.period
            h = self.list[i] * hList[-1] + hList[-2]
            k = self.list[i] * kList[-1] + kList[-2]
            hList.append(h)
            kList.append(k)
            n += 1
            yield Fraction(h,k)

    def __str__( self ):
        string = 'sqrt(' + str(self.value) + ') = [' + str(self.base)
        if self.period > 0:
            string += '; ('
            string += ','.join(map(str,self.list))
            string += ')'
        string += '], period = ' + str(self.period)

        return string


def checkDiophantine(x,y,D):
    return x * x - D * y * y == 1

answer = [0,0,0]

for D in xrange(1,1001):
    cf = ContinuedFraction(D)
    if cf.period > 0:
        for convergent in cf.convergents():
            x, y = convergent.numerator, convergent.denominator
            if checkDiophantine(x, y, D):
                print x, y, D
                if x > answer[0]:
                    answer = [x,y,D]
                break

print 'answer [x,y,D] = ', answer

