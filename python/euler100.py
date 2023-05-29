import math
import random


def success(turns):
    trials = 10_000_000
    wins = 0
    threshold = turns // 2 + 1
    for _ in range(trials):
        count = 0
        for turn in range(0, turns):
            if random.random() < (1 / (turn + 2)):
                count += 1
        if count >= threshold:
            wins += 1

    return wins, wins / trials, wins * math.factorial(turns + 1) / trials



if __name__ == '__main__':
    print(success(15))
