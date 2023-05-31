from enum import Enum

def triangle(n:int) -> int:
    return n * (n + 1) // 2

def square(n:int) -> int:
    return n * n

def pentagonal(n:int) -> int:
    return n * (3 * n - 1) // 2

def hexagonal(n:int) -> int:
    return n * (2 * n - 1)

def heptagonal(n:int) -> int:
    return n * (5 * n - 3) // 2

def octagonal(n:int) -> int:
    return n * (3 * n - 2)

sides_map = {
    triangle: 3,
    square: 4,
    pentagonal: 5,
    hexagonal: 6,
    heptagonal: 7,
    octagonal: 8
}

# class syntax
class PolyFunction(Enum):
    triangle = triangle
    square = square



if __name__ == '__main__':
    # my_list = [PolyFunction.triangle, PolyFunction.pentagonal, PolyFunction.square]
    # print(sorted(my_list, key=lambda pf: sides_map[str(pf]))
    # for pf in my_list:
    #     print(str(pf.value))
    fnc = eval('triangle')
    print(fnc)
    print(fnc(5))


# def get_list_of_functions():
#     return [
#         triangle,
#         square,
#         pentagonal,
#         hexagonal,
#         heptagonal,
#         octagonal
#     ]