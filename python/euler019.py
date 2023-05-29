"""
You are given the following information, but you may prefer to do some research for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from datetime import date
from euler import euler_problem

@euler_problem()
def euler019(unused='') -> int:
    if unused and unused != 'challenge':
        raise Exception(f'Unexpected input parameter: {unused}')

    return count(
        filter(lambda d: d.weekday() == 6,
               (date(year, month, day=1) for year in range(1901, 2001) for month in range(1, 13))))

def count(it):
    return sum(1 for x in it)


if __name__ == '__main__':
    print(euler019())
