"""
We shall say that an n-digit number is pan-digital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pan-digital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is
1 through 9 pan-digital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pan-digital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
import itertools
import logging
from typing import Tuple

import euler


@euler.euler_problem
def euler032(_='n/a') -> int:
    product_set = set()
    for p in itertools.permutations('123456789'):
        permutation = stringify(p)

        # The only possible breakdowns of the 9 digits are:
        #    1 digit x 4 digits = 5 digits
        #    2 digit x 3 digits = 4 digits

        factor_one, factor_two, product = split(permutation, 1, 4)
        if is_product(factor_one, factor_two, product):
            logging.debug(f'{factor_one}, {factor_two}, {product}')
            product_set.add(product)

        factor_one, factor_two, product = split(permutation, 2, 3)
        if is_product(factor_one, factor_two, product):
            logging.debug(f'{factor_one}, {factor_two}, {product}')
            product_set.add(product)

    return sum(product_set)


def split(permutation:str, first_factor:int, second_factor:int) -> Tuple[int,int,int]:
    return (
        int(permutation[0:first_factor]),
        int(permutation[first_factor: first_factor + second_factor]),
        int(permutation[first_factor + second_factor:])
    )

def stringify(digits) -> str:
    return ''.join(digits)

def is_product(factor_1:int, factor_2:int, product:int) -> bool:
    return factor_1 * factor_2 == product


if __name__ == '__main__':
    euler.config_log_level(logging.DEBUG)
    print(euler032())
