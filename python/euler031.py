# coding=UTF8
'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

Created on Oct 30, 2010

@author: Greg Charles
'''
import math

class CoinCounter(object):
    
    def __init__(self, coins):
        self.coins = coins
        self.coins.sort()

    def count_combos(self, amount, pos):
        if (pos == 0):
            return 1 if (amount % self.coins[pos] == 0) else 0
         
        return reduce(
                      lambda sum, count : sum + self.count_combos(amount - count * self.coins[pos], pos-1), 
                      xrange(0, int(math.floor(amount/self.coins[pos]))+1),
                      0)

    def coin_combinations(self,amount):
        return self.count_combos(amount, len(self.coins)-1)

cc = CoinCounter([1,2,5,10,20,50,100,200])
print cc.coin_combinations(200)
