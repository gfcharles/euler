"""
The 5-digit number, 16807=7^(5), is also a fifth power. Similarly, the 9-digit number, 134217728=8^(9),
is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
import logging
from itertools import count

from euler import euler_problem


@euler_problem()
def euler063(_: str = 'n/a') -> int:
    total = 0
    for power in count(start=1):
        # highest number for which number ** power has power digits is 9; Lowest is 1.
        for number in range(9, 0, -1):
            value = number ** power
            if len(str(value)) == power:
                total += 1
                logging.debug(f'{number} ** {power} = {value}')
            elif number < 9:
                # Try next power
                break
            else:
                return total


if __name__ == '__main__':
    print(euler063())
