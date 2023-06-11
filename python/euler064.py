"""
All square roots are periodic when written as continued fractions and can be written in the form:
sqrt(n) = a0 + (1 / (a1 + (1 /  ...


(The full problem statement is difficult to reproduce in plain text. See https://projecteuler.net/problem=64 )

Exactly four continued fractions, for N <= 13 have an odd period.
How many continued fractions for N ≤ 10000 have an odd period?
"""
import common.continued_fraction as cf

from euler import euler_problem


@euler_problem()
def euler064(n: int | str) -> int:
    max_value = int(n)

    # starting values
    counter = 0
    value, base = 1, 0

    while value <= max_value:
        if (base + 1) ** 2 == value:
            base += 1
        else:
            frac = cf.cf_for_sqrt(value, base=base)

            # Increment counter if period is odd.
            if frac.period  % 2 == 1:
                counter += 1

        value += 1

    return counter


if __name__ == '__main__':
    print(euler064(13))
    print(euler064(10_000))
