'''
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

Created on Sep 20, 2010

@author: Greg Charles
'''
from datetime import date, timedelta

startDate = date(1901, 1, 1)
endDate = date(2000, 12, 31)

currentDate, counter = startDate, 0
while currentDate <= endDate:
    if currentDate.day == 1 and currentDate.weekday() == 6: # 6 is Sunday in Python
        counter += 1
    currentDate += timedelta(days = 1)
    
print counter
