'''
The cube, 41063625 (345^(3)), can be permuted to produce two other cubes: 56623104 (384^(3)) and 66430125 (405^(3)).
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

Created on Jan. 17, 2011

@author: Greg Charles
'''
cubes = dict()
counter = 346

while True:
    n = counter ** 3
    key = "".join(sorted(str(n)))
    if key in cubes:
        list = cubes[key]
        if not n in list:
            list.append(n)
            if len(list) == 5:
                print list
                print list[0]
                break
    else:
        cubes[key] = [n]
    counter += 1

