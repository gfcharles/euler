import itertools
import logging
import math
from functools import reduce
from typing import Iterable

from euler import euler_problem

"""
A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour 
is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is 
taken at random.

The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize 
fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note 
that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the 
example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.
"""
@euler_problem()
# @euler_problem(logging_level=logging.DEBUG,timing=True)
def euler121(n:int|str) -> int:
    n = int(n)
    winning_combos = count_winning_combos(n)
    total_combos = math.factorial(n + 1)
    logging.debug(f'winning combos = {winning_combos}, total combos = {total_combos}')

    # Max prize to preserve house advantage is floor(total / winning)
    return total_combos // winning_combos


def count_winning_combos(n:int) -> int:
    """
    Counts the number of winning combinations in a game with n turns, given that a win means more successes
    than failures.

    @param n: the number of turns in the games.
    @return: count of winning combinations in the game, which is the count of k failures for k from 0 to m,
            where m < n - m (i.e., where successes outnumber failures)
            The total number of combinations (winning and losing) is (n + 1)!
    """
    win_threshold = n // 2 + 1
    max_failures = n - win_threshold

    return sum(count_k_failures_for_n_turns(n, k) for k in range(max_failures + 1))

def count_k_failures_for_n_turns(n:int, k:int) -> int:
    """
    Counts the number of ways to get exactly k failures in n turns. If each turn had equal probability of success,
    this would just be (n choose k). However, since each trial has a turn / (turn + 1) probability of failure,
    we have to sum the products of all (n choose k) combinations of numbers 1 - n. (This wasn't easy to work out.)

    @param n: the total number of turns in the game
    @param k: the number of failures
    @return: the total number of ways to get exactly k failures in n turns.
    """
    return sum(prod(key) for key in itertools.combinations(range(1, n + 1), k))

def prod(it:Iterable[int]) -> int:
    return reduce(lambda x, y: x * y, it, 1)


# Sanity check. Compute the approximate answer through random trials.
# def check_by_trials(turns:int):
#     trials = 1_000_000
#     wins = 0
#     threshold = turns // 2 + 1
#     for _ in range(trials):
#         count = 0
#         for turn in range(turns):
#             if random.random() < (1 / (turn + 2)):
#                 count += 1
#         if count >= threshold:
#             wins += 1
#
#     print(int(trials/wins), wins * math.factorial(turns + 1) / trials)

if __name__ == '__main__':
    print(euler121(4))
    print(euler121(15))
