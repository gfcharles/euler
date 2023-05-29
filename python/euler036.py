"""
The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
from euler import euler_problem


@euler_problem()
def euler036(n:int|str) -> int:
    return sum(x for x in range(1, int(n)) if is_palindrome(str(x)) and is_palindrome(binstr(x)))

def is_palindrome(s):
    # We only need to compare first half to revers of second half, but not really worth the savings.
    return s == s[::-1]

# Convert a positive integer to a binary string. 
# Will return an empty string for 0 or negative
def binstr(n):
    string = ""
    while n > 0:
        string += str(n & 1)
        n = n >> 1
    # reversing the string isn't strictly necessary because we're looking for palindromes, but I'm still doing it
    return string[::-1]

if __name__ == '__main__':
    print(euler036(1_000_000))
