'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

@author: Greg Charles
'''
def IsPalindrome(n):
    string = str(n)
    i, j = 0, len(string) - 1
    while (i < j):
        if (string[i] != string[j]):
            return False
        i += 1
        j -= 1
    return True
    
def MaxPalindrome(digits):
        
    maxX = 0
    maxY = 0
    maxPalindrome = 0 

    x = (10 ** digits) - 1

    while (x ** 2 > maxPalindrome):
        y = x
        while (1):
            test = x * y
            if (test < maxPalindrome):
                break
            if IsPalindrome(test):
                maxX = x
                maxY = y
                maxPalindrome = test
                break
            y -= 1
        x -= 1
    
    return maxX, maxY, maxPalindrome
        
x, y, p = MaxPalindrome(3)
print x, y, p