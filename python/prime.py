'''
Created on Oct 3, 2010

@author: http://www.daniweb.com/code/snippet216558.html
@author: http://www.daniweb.com/code/snippet216880.html
'''
# a fast prime number list 'generator' using a sieve algorithm
def primes(n):
    """
    returns a list of prime numbers from 2 to n
    """
    if n < 2:  return []
    if n == 2: return [2]
    # create a list of odd numbers from 3 to n
    nums = list(range(3, n+1, 2))
    nums_len = (n // 2) - 1 + (n % 2)
    idx = 0
    idx_sqrtn = (int(n**0.5) - 3) // 2
    while idx <= idx_sqrtn:
        nums_idx = (idx << 1) + 3
        for j in range(idx*(nums_idx+3)+3, nums_len, nums_idx):
            # if not a prime replace with zero
            nums[j] = 0
        idx += 1
        while idx <= idx_sqrtn:
            if nums[idx] != 0:
                break
            idx += 1
    # remove all the zero entries
    return [2] + [x for x in nums if x != 0]


# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)
def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True