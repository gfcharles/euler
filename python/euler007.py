'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6^(th) prime is 13.

What is the 10001^(st) prime number?

@author: Greg Charles
'''
import time

# Determines if candidate is prime given that all the prime numbers
# less than candidate are stored in primes.
def IsPrime(candidate, primes):
    for prime in primes:
        if (candidate % prime == 0):
            return False
        if (prime * prime > candidate):
            return True
        
    return True

# Compute the first 10001 primes.
start = time.clock() 

primes = [2]
candidate = 3
while (len(primes) != 10001):
    if IsPrime(candidate, primes):
        primes += [candidate]
        
    candidate += 2
    
print primes[-1]

print 'Total time = ', time.clock() - start
    

