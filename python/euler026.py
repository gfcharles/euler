'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    ^(1)/_(2)    =     0.5
    ^(1)/_(3)    =     0.(3)
    ^(1)/_(4)    =     0.25
    ^(1)/_(5)    =     0.2
    ^(1)/_(6)    =     0.1(6)
    ^(1)/_(7)    =     0.(142857)
    ^(1)/_(8)    =     0.125
    ^(1)/_(9)    =     0.(1)
    ^(1)/_(10)    =     0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that ^(1)/_(7) has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^(1)/_(d) contains the longest recurring cycle in its decimal fraction part.

Created on Oct 3, 2010

@author: Greg Charles
'''
def countPeriod(n):
    while (n % 2 == 0):
        n /= 2 
    while (n % 5 == 0):
        n /= 5 

    count = 1
    remainder = 10 % n
    while (True):
        if (remainder == 0):
            return 0
        if (remainder == 1):
            return count
        
        remainder = (10 * remainder) % n
        count += 1

maxPeriod, max = 0, 0
for d in xrange(1000,0,-1): 
    period = countPeriod(d)
    if (period > maxPeriod):
        maxPeriod, max = period, d 
    if (maxPeriod >= d):
        break

print "The max repeat period is", maxPeriod, "for 1/", max

