'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

@author: gcharles
'''
def LargestPrimeFactor(n):
    max = n
    divisor = 2
    while (n >= divisor ** 2):
        if (n % divisor == 0):
            n = n / divisor
            max = n
        else:
            divisor += 1
    
    return max
        

print LargestPrimeFactor(600851475143)

