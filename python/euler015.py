'''
Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?

Created on Sep 19, 2010

@author: Greg Charles

Note: The only moves are right and down, and every solution must have 40 moves, with 20 rights, and 20 downs.
      Therefore, the number of solutions is the same as the number of ways to choose 20 rights from 40 moves.

'''
def prod(x,y):
    return x * y

def nCr(n,r):
    # Sanity
    if r <= 0 or n <= 0 or n < r:
        return 0
    
    # Improves efficiency
    r = min(n - r, r)

    return reduce(prod, range(n, (n-r), -1)) / reduce(prod, range(1,r+1))

print nCr(40,20)