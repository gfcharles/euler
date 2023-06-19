import itertools
import logging
import typing

from euler import euler_problem


# @euler_problem(timing=True, logging_level=logging.DEBUG)
@euler_problem()
def euler719(n: int | str) -> int:
    return sum(sqr.square for sqr in itertools.takewhile(lambda sqr: sqr.square <= int(n), squares())
               if check_s_number(*sqr))


Square = typing.NamedTuple('Square', [('square', int), ('base', int)])


def squares() -> typing.Generator[Square, None, None]:
    for i in itertools.count(start=2):
        yield Square(i * i, i)


def check_s_number(digits, target) -> bool:
    """
    Do a modulo test for given number and target sum, and if that passes, check for s-number by
    summing up every possible partition of the digits.

    Modulo test is cheating here, because I didn't come up with it, but it's so neat I wanted to include it anyway.
    It's a property of any decimal integer that the sum of any partition of its digits will have the same mod 9
    os the original number. Knowing that, we can eliminate most of the candidate with a simple check.

    @param digits: the number to partition into digits
    @param target: the target that we want the partitioned digits to sum to
    @return: True if any partition of digits sums to target, otherwise false.
    """
    return digits % 9 == target % 9 and is_s_number(digits, target)


def is_s_number(digits, target, lvl=1, partitions=None):
    if target < 0:
        return False

    if digits < target:
        return False

    if digits == target:
        # for debugging logs
        partitions.append(target)

        return True

    if partitions is None:
        partitions = []

    for i in range(1, len(str(digits))):
        #  Split digits into last i and the rest, and then recurse
        left, right = digits % (10 ** i), digits // (10 ** i)

        if is_s_number(left, target - right, lvl + 1, partitions):
            # for debugging logs
            if partitions is not None:
                partitions.append(right)
                if lvl == 1:
                    logging.debug(f'{digits}, {target}, {list(reversed(partitions))}')

            return True

    return False


if __name__ == '__main__':
    print(euler719(10_000))
    print(euler719(10 ** 12))
