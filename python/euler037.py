'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from 
left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Created on Oct 30, 2010

@author: Greg Charles
'''
from sets import Set
import re


def truncations(n):
    truncations = Set([])
    
    string = str(n)
    for i in xrange(1,len(string)):
        truncations.add(int(string[:i]))
        truncations.add(int(string[-i:]))
                        
    return truncations

def is_truncatable_prime(n):
    if (n < 10):
        return False
    
    string = str(n)
    if re.search("[0468]", string) or re.search(".2", string):
        return False
    
    for x in truncations(n):
        if (not prime.is_prime(x)):
            return False
        
    return True
 
print sum(x for x in prime.primes(1000000) if is_truncatable_prime(x))     
