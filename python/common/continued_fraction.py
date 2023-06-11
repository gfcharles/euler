import itertools
from fractions import Fraction
from functools import cache
from typing import Generator, Callable


class ContinuedFraction(object):
    """
    Class that models continued fractions, either ones that take a base and list of repeated
    quotients (which repeat) like for an irrational square root, or for a base and generator functions, that
    doesn't repeat a block of partial quotients.
    """
    def __init__(self, base: int, pq_list: list[int] = None, pq_generator: Callable = None):
        def _generate_from_list(a_list: list[int]) -> Generator:
            while True:
                for item in a_list:
                    yield item

        self.base = base

        if not ((pq_list is None) ^ (pq_generator is None)):
            raise ValueError('Exactly one of pq_list or pq_generator must be specified')

        if pq_list is not None:
            # For repeating partial quotients, as is the case for irrational square roots
            self.period = len(pq_list)
            self.partial_quotient_list = pq_list
            self.partial_quotient_generator = _generate_from_list(pq_list)
        elif pq_generator is not None:
            # For non-repeating partial quotients, like for e (Euler's constant.)
            self.period = None
            self.partial_quotient_generator = pq_generator()
            # Kludge to get data for the __str__ method without depleting the generator.
            # Arguably the ugliness isn't worth having this data available for the string rep, but I like it.
            # This string rep is wicked cool.
            self.first_partial_quotients = itertools.islice(pq_generator(), 10)

    @cache
    def convergent(self, n: int) -> Fraction:
        """
        Computes the nth convergent of the continued fraction and returns it as a fraction.Fraction
        The counts the base by itself as convergent 0.

        @param n: which convergent to compute. The base itself is considered to be the 0th convergent.
        @return: nth convergent
        """
        if n == 0:
            return Fraction(self.base)
        if n == 1:
            return self.base + Fraction(1, next(self.partial_quotient_generator))

        x = self.convergent(n - 1)
        y = self.convergent(n - 2)
        next_pq = next(self.partial_quotient_generator)

        return Fraction(next_pq * x.numerator + y.numerator, next_pq * x.denominator + y.denominator)

    def convergents(self) -> Generator[Fraction, None, None]:
        """
        @return: Convergents in a generator
        """
        for i in itertools.count(start=0):
            yield self.convergent(i)

    @cache
    def __str__(self):
        if self.period:
            one_period = self.partial_quotient_list
            string = f'[{self.base}; ({",".join(map(str, one_period))})], period = {self.period}'
        else:
            # Print first 10 elements of infinite series
            string = f'[{self.base}; {",".join(map(str, self.first_partial_quotients))},...]'

        return string


def cf_for_sqrt(value: int, base: int = None) -> ContinuedFraction:
    """
    Returns a continued fraction for the square root of input value.

    @param value: the value to get as a square root
    @param base: the integer part of the square root such that base ** 2 <= value < (base + 1) ** 2
    @return: list of partial quotients for the first period of continued fraction. These would repeat infinitely.
    """
    if base is None:
        base = int(value ** 0.5)

    if base * base == value:
        raise ValueError(f'{value} is a perfect square')

    m, d, a = 0, 1, base
    md_list = []
    a_list = []

    while True:
        m = d * a - m
        d = (value - m * m) // d
        md = (m, d)

        if md in md_list:
            return ContinuedFraction(base, pq_list=a_list)

        md_list.append(md)
        a = (base + m) // d
        a_list.append(a)
