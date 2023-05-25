"""
The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
import logging
import euler


@euler.euler_problem
def euler036(n:int|str) -> int:
    return sum(x for x in range(1, int(n)) if test_palindrome(x))


def test_palindrome(n: int) -> bool:
    decimal = str(n)
    binary = binstr(n)

    if is_palindrome(decimal) and is_palindrome(binary):
        logging.debug(f"Found: {decimal} ({binary})")
        return True
    return False

def is_palindrome(s:str) -> bool:
    half = len(s) // 2
    return  s[:half] == s[-1: -(half + 1): -1]

# Convert a positive integer to a binary string. 
# Will return an empty string for 0 or negative
def binstr(n:int) -> str:
    string = ""
    while n > 0:
        string += str(n & 1)
        n = n >> 1 
    return string[::-1]


if __name__ == '__main__':
    euler.config_log_level(logging.DEBUG)
    print(euler036(1_000_000))
