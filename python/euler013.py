'''
Created on Sep 19, 2010

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

(Note: numbers stored as lines in numbers.dat)

@author: Greg Charles
'''
import gregutils

f = open(gregutils.dataDir() + 'numbers.dat', "r")
sum = 0
for line in f:
    sum += int(line)

print str(sum)[0:10]

