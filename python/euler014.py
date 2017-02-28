'''
The following iterative sequence is defined for the set of positive integers:

n : n/2 (n is even)
n : 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Created on Sep 19, 2010

@author: Greg Charles
'''
import time

def collatzCount(n):
    count = 1
    while n != 1:
        if (n%2 == 0):
            n = n / 2
        else:
            n = 3 * n + 1
        count += 1

    return count


maxTerms = 0
maxN = 0
n = 500001
beginning = time.clock()
while n < 1000000:
    terms = collatzCount(n)
    if (terms > maxTerms):
        maxTerms, maxN = terms, n
    n += 2

print "Time elapsed ", time.clock() - beginning
print "MaxTerms = ", maxTerms, " for starting value ", maxN
