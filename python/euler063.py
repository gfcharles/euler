'''
The 5-digit number, 16807=7^(5), is also a fifth power. Similarly, the 9-digit number, 134217728=8^(9),
is a ninth power.

How many n-digit positive integers exist which are also an nth power?


Created on Jan. 18, 2011

@author: Greg Charles
'''
counter = 0
min, max, power = 1, 9, 1
while max >= min:
    base = max
    while base >= min:
        value = base ** power
        if len(str(value)) == power:
            print base, "^", power, "=", value
            counter += 1
        else:
            min = base + 1
        base -= 1
    power += 1

print "Total =", counter
