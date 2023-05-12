'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

Created on Oct 30, 2010

@author: Greg Charles
'''
import prime
import re
from sets import Set

def rotate(n, pos=1):
    string = str(n)
    pos = pos % len(string)
    if pos == 0:
        return n
    else:
        return int(string[-pos:] + string[:-pos])

def rotations(n):
    set = Set([])
    for pos in xrange(0, len(str(n))):
        set.add(rotate(n, pos))
    return list(set)

def is_rotational_prime(n):
    if (n == 2):
        return True
    elif re.search("[02468]", str(n)):
        return False
     
    for x in rotations(n):
        if not prime.is_prime(x):
            return False

    return True

print len(filter(is_rotational_prime, prime.primes(1000000)))
