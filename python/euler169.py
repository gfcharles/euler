"""
Define f(0) = 1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers of 2
using each power no more than twice.

For example, f(10) = 5 since there are five different ways to express 10:
1 + 1 + 8
1 + 1 + 4 + 4
1 + 1 + 2 + 2 + 4
2 + 4 + 4
2 + 8

What is f(10^25)?
"""
from functools import cache


def euler169(n: int | str) -> int:
    """
    Using brute force, we can compute the first 200 or so elements of this sequence ...
    1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3, 8, 5, 7, 2, 7, 5, 8, 3, 7, 4, 5,
    1, 6, 5, 9, 4, 11, 7, 10 ...

    Notes:
        1. For any number n = 2^m, the f(n) result is m + 1
        2. For any number n = 2^m -1, f(n) = 1
        3. For any odd number n, f(n) = f((n - 1) / 2)
        4. For any even number n, f(n) = f(n/2) + f((n/2) - 1)

    1 makes sense because the possibilities are n, n/2 + n/2, n/2 + n/4 + n/4, n + n / 2 ... + 2 + 1 + 1 which will
      always be 1 more the power of 2 that n is.

    2 makes sense because the only possibility will be (n + 1) / 2 + (n + 1) / 4 + ... 4 + 2 + 1

    3 makes sense because if you take any combo for n, then double each of the addends and add 1, that will
      be a valid combo for 2n + 1, and no other combos will exist.

    4 I don't get yet, but the pattern is evident in the brute-forced examples.

    Apparently, this sequence is called Stern's diatomic series, and is described at
    https://oeis.org/A002487
    """
    return f(int(n))


@cache
def f(n: int) -> int:
    if n == 0:
        return 1

    # Note 3 above
    if n % 2 == 1:
        return f(n // 2)

    # Note 4 above
    return f(n // 2) + f(n // 2 - 1)


if __name__ == '__main__':
    print(euler169(10))
    print(euler169(10 ** 25))
