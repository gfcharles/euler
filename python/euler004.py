"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import logging


def euler004(input_value:int) -> int:
    # Reset counter for diagnostics
    is_palindrome.counter = 0

    digits = input_value
    max_found = 0

    for x in range(10 ** digits - 1, 0, -1):
        if x * x <= max_found:
            break

        for y in range(x, 0, -1):
            test = x * y
            if test <= max_found:
                break
            if is_palindrome(test):
                max_found = test
                break

    logging.debug(f"Total palindrome tests for {digits} digits was {is_palindrome.counter}")
    return max_found

def is_palindrome(input_value) -> bool:
    is_palindrome.counter += 1

    string = str(input_value)
    for i in range(len(string)):
        if string[i] != string[-i - 1]:
            return False

    return True


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    print(euler004(2))
    print(euler004(3))
