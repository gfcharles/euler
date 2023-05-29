"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pan-digital, 192384576. We will call 192384576 the concatenated
product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pan-digital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pan-digital 9-digit number that can be formed as the concatenated product of an integer with
(1,2, ... , n) where n > 1?
"""
import itertools

from euler import euler_problem


@euler_problem()
def euler038(_:str = 'n/a') -> int:
    for p in itertools.permutations("987654321"):
        if int(''.join(p[0:4])) * 2 == int("".join(p[4:9])):
            return int(''.join(p))

if __name__ == '__main__':
    print(euler038())
