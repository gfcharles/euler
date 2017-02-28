'''
The fraction ^(49)/_(98) is a curious fraction, as an inexperienced mathematician in attempting to simplify it may 
incorrectly believe that ^(49)/_(98) = ^(4)/_(8), which is correct, is obtained by canceling the 9s.

We shall consider fractions like, ^(30)/_(50) = ^(3)/_(5), to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits 
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

Created on Oct 30, 2010

@author: Greg Charles
'''
import fractions

def testReduction(a, b):
    if (a % 10 == 0 or b % 10 == 0):
        return False
    
    sa, sb = str(a), str(b)
    if (sa[0] == sb[0]):
        return float(sa[1]) / float(sb[1]) == float(a) / float(b)
    elif (sa[0] == sb[1]):
        return float(sa[1]) / float(sb[0]) == float(a) / float(b)
    elif (sa[1] == sb[0]):
        return float(sa[0]) / float(sb[1]) == float(a) / float(b)
    elif (sa[1] == sb[1]):
        return float(sa[0]) / float(sb[0]) == float(a) / float(b)
    else:
        return False

num, den = 1, 1
for a in xrange(11,100):
    for b in xrange(a+1,100):
        if testReduction(a,b):
            num, den = num*a, den*b
            
print den / fractions.gcd(num,den)

