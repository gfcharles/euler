"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

@author: Greg Charles
"""
import time

def euler005(input_value: int) -> int:
    return lcm_of_list(list(range(2, input_value + 1)))


# Recursively split the list to reduce the number of lcm computations.
def lcm_of_list(number_list:list) -> int:
    length = len(number_list)
    if length == 0:
        # Normally this won't happen
        return 1
    if length == 1:
        return number_list[0]
    if length == 2:
        return lcm(number_list[0], number_list[1])

    return lcm(
        lcm_of_list(number_list[:length // 2]),
        lcm_of_list(number_list[length // 2:])
    )


# Least common multiple of a and b
def lcm(a: int, b: int) -> int:
    if a == b:
        return a

    x = min(a, b)
    y = max(a, b)

    if y % x == 0:
        return y

    return x * y // gcd(x, y)


# Greatest common divisor of a and b
def gcd(a: int, b: int) -> int:
    while True:
        if a == b:
            return a
        
        if a < b:
            a, b = b - a, a
        else:
            a, b = a - b, b


# Get the least common multiple of all numbers from 1 to 20
if __name__ == '__main__':
    start = time.time()
    print(euler005(10))
    print(euler005(20))
    print(f"{(time.time() - start) * 1000} ms")
