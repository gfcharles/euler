"""
Consider quadratic Diophantine equations of the form:

x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 6492 - 13 x 1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 - 2 x 22 = 1
22 - 3 x 12 = 1
92 - 5 x 42 = 1
52 - 6 x 22 = 1
82 - 7 x 32 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.
"""
import logging

from common.continued_fraction import cf_for_sqrt
from euler import euler_problem


#
# x = sqrt(D y^2 + 1) so x/y is slightly less than sqrt(D). Therefore, we can use the Diophantine convergents
# of sqrt(D) to find solution candidates.
#
@euler_problem()
def euler066(n: int | str) -> int:
    answer = (0 , 0, 0)
    for D in range(1, int(n) + 1):
        try:
            cf = cf_for_sqrt(D)
            for convergent in cf.convergents():
                x, y = convergent.numerator, convergent.denominator
                if check_diophantine(x, y, D):
                    if x > answer[0]:
                        answer = (x, y, D)
                    break
        except ValueError:
            logging.debug(f'Skipping perfect square: {D}')

    logging.debug(f'answer [x,y,D] = {answer}')
    return answer[2]


def check_diophantine(x: int, y: int, d: int) -> bool:
    return x * x - d * y * y == 1


if __name__ == '__main__':
    print(euler066(7))
    print(euler066(1000))
