'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

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

max = 2000000

primes = [2]
candidate = 3
while (candidate < max):
    if IsPrime(candidate, primes):
        primes += [candidate]
        
    candidate += 2

   
#print reduce(lambda x, y: x+y, primes)
print sum(primes)

print 'Total time = ', time.clock() - start
    

