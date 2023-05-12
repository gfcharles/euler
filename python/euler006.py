"""
The sum of the squares of the first ten natural numbers is,
1^(2) + 2^(2) + ... + 10^(2) = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^(2) = 55^(2) = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

@author: Greg Charles

"""
def euler006(n: int) -> int:
    # Square of sum turns out to be the same as sum of cubes, so that simplifies things.
    return sum(x ** 3 - x ** 2 for x in range(1, n + 1))


if __name__ == '__main__':
    print(euler006(10))
    print(euler006(100))
