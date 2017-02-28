'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the 
result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

Created on Nov 11, 2010

@author: Greg Charles
'''
import prime

# Arbitrarily pick 10000 as the highest prime we will check. I don't know a better way to handle this.
allPrimes = prime.primes(10000)

# Test to see that the addition of m to the known set produces a valid a new set.
def tester(known, m):
    for n in known:
        if not prime.isprime(int(str(n) + str(m))):
            return False
        if not prime.isprime(int(str(m) + str(n))):
            return False

    return True

# Recursive function that prints the first set it finds of the requested size that fits the conditions. 
# It then stops looking. This doesn't guarantee the smallest sum, but works for this case.
def buildSet(known, setSize):
    if len(known) == setSize:
        print known, sum(known)
        return True
    
    for n in allPrimes:
        if len(known) > 0 and n <= known[-1]:
            continue;
        
        if tester(known, n):
            nowKnown = list(known)
            nowKnown.append(n)
            if buildSet(nowKnown, setSize):
                return True

    return False

# Build a set with five elements, starting from nothing.
buildSet([], 5)
