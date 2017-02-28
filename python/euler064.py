'''
How many continued fractions for N ≤ 10000 have an odd period?

Created on Jan. 20, 2011

@author: Greg Charles
'''
import math

class ContinuedFraction(object):

    def __init__(self, value):
        self.value = value
        self.base = self.computeBase(value)
        self.list = self.computeList(value, self.base)
        self.period = len(self.list)

    def computeBase(self,value):
        return int(math.floor(math.sqrt(value)))

    def computeList(self, s, base):
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

    def __str__( self ):
        string = 'sqrt(' + str(self.value) + ') = [' + str(self.base)
        if (self.period > 0):
            string += '; ('
            string += ','.join(map(str,self.list))
            string += ')'
        string += '], period = ' + str(self.period)

        return string


counter = 0
for s in xrange(2,10001):
    cf = ContinuedFraction(s)
#    print cf
    if cf.period % 2 == 1:
        counter += 1

print counter