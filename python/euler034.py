'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Created on Oct 30, 2010

@author: Greg Charles
'''
factorials = [1,1]
for i in xrange(2,10):
    factorials.append(factorials[-1] * i)
         
def is_sum_of_digits(n):
    return n == sum(map(lambda x : factorials[int(x)], str(n)))

def get_upper_bound():
    base = factorials[9]
    digit_count = 2
    upper_bound = 0
    while True:
        digit_count += 1
        if (len(str(digit_count * base))) < digit_count:
            return upper_bound 
        upper_bound = digit_count * base

print sum(x for x in xrange(10,get_upper_bound()) if is_sum_of_digits(x))

