"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
import json
import logging
from typing import Tuple, Callable

from euler import euler_problem
from euler024 import extract


@euler_problem
def euler031(json_text:str=None, coins:list[int]=None, amount:int=None, callback:Callable=None) -> int:
    if coins is None:
        coins, amount = extract(json_text)

    return CoinCounter(coins, callback=callback).coin_combinations(amount)

def extract(json_text:str) -> (list[int], int):
    obj = json.loads(json_text)
    return obj['coins'], obj['amount']


class CoinCounter(object):
    def __init__(self, coins, callback:Callable = None):
        self.coins = coins
        self.coins.sort()
        self.callback = callback

    def coin_combinations(self, amount:int) -> int:
        return self._count_combos(amount, len(self.coins) - 1, list())

    def _count_combos(self, amount:int, pos:int, combo: list[Tuple[int, int]]) -> int:
        coin = self.coins[pos]  # Current coin value

        if pos == 0:
            if amount % coin == 0:
                combo = self._append((amount // coin, coin), combo)
                if self.callback:
                    self.callback(combo)
                return 1

            # Combination is impossible with given coins
            return 0

        return sum(self._count_combos(amount - x * coin, pos - 1, self._append((x, coin), combo))
                   for x in range(amount // self.coins[pos] + 1))

    @staticmethod
    def _append(my_tuple:Tuple[int,int], my_list:list[Tuple[int,int]]) -> list[Tuple[int,int]]:
        copy_list = my_list.copy()
        copy_list.append(my_tuple)
        return copy_list

def format_combo(combo:list[Tuple[int,int]]) -> str:
    return ', '.join(list(map(lambda el: f'{el[0]} of {el[1]}', filter(lambda el: el[0] > 0, combo))))


if __name__ == '__main__':
    print(euler031(json_text='{"coins": [1,2,5,10,20,50,100,200], "amount": 200}'))
    print(euler031(coins=[1,2,5,10,20,50,100,200], amount=200, callback=lambda c: logging.debug(format_combo(c))))
