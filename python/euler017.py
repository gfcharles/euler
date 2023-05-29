"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""
from euler import euler_problem


@euler_problem()
def euler017(n:int|str) -> int:
    return sum(len(number_to_string(x)) for x in range(1, int(n) + 1))

def number_to_string(num:int) -> str:
    if num >= 10000:
        raise Exception('Largest possible value is 9999')

    ones = ['','one', 'two', 'three','four','five','six','seven','eight','nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen','sixteen','seventeen','eighteen','nineteen']
    tens = ['', '', 'twenty','thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    hundred = 'hundred'
    thousand = 'thousand'
    and_term = 'and'

    digits = list(map(int, str(num))) # get list of decimal digits
    terms = list()
    
    # Thousands 
    if len(digits) > 3:
        terms.append(ones[digits[-4]])
        terms.append(thousand)
        
    # Hundreds (with British 'and' if needed)
    if len(digits) > 2 and digits[-3] > 0:
        terms.append(ones[digits[-3]])
        terms.append(hundred)
        if digits[-1] > 0 or digits[-2] > 0:
            terms.append(and_term)
    
    # Tens and ones
    if len(digits) > 1 and digits[-2] == 1:
        terms.append(teens[digits[-1]])
    else:
        if len(digits) > 1:
            terms.append(tens[digits[-2]])
        terms.append(ones[digits[-1]])
        
    return ''.join(terms)  


if __name__ == '__main__':
    print(euler017(5))
    print(euler017(1000))
