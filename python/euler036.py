'''
The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

Created on Oct 30, 2010

@author: Greg Charles
'''
def is_palindrome(s):
    return s == s[::-1]

# Convert a positive integer to a binary string. 
# Will return an empty string for 0 or negative
def binstr(n):
    string = ""
    while n > 0:
        string = ("1" if n & 1 else "0") + string
        n = n >> 1 
    return string

print sum(n for n in xrange(1,1000000) if (is_palindrome(str(n)) and is_palindrome(binstr(n))))