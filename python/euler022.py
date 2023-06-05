"""
Using names.txt  (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is
the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""
from euler import euler_problem


@euler_problem()
def euler022(filename) -> int:
    with open(f'./euler_data/{filename}', 'r') as names_file:
        names = sorted(nm.strip('"') for nm in names_file.readline().split(","))
        return sum(positional_name_value(idx + 1, n) for idx, n in enumerate(names))


def positional_name_value(pos: int, name: str) -> int:
    return pos * name_value(name)


def name_value(name: str) -> int:
    return sum(map(lambda c: ord(c) - ord('A') + 1, name))


if __name__ == '__main__':
    print(euler022('p022_names.txt'))
