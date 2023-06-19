from functools import cache

from euler import euler_problem


@euler_problem()
def euler097(problem_input: str) -> int:
    # Parse the input
    expression, digits = problem_input.split(';')
    digits = parse_term(digits)
    main, addend = expression.split('+')
    addend = parse_term(addend)
    coefficient, exponential = main.split('x')
    coefficient = parse_term(coefficient)
    base, exponent = exponential.split('^')
    base = parse_term(base)
    exponent = parse_term(exponent)

    return compute_mod(coefficient, base, exponent, addend, 10 ** digits)


def parse_term(term: str):
    return int(term.strip())


# Basic algorithm for computing modulos of very large numbers. However, it's not noticeably different in time
# from just letting Python work it out.
def compute_mod(coefficient: int, base: int, exp: int, addend: int, modulo: int) -> int:
    return ((coefficient % modulo) * compute_mod_for_base_and_exp(base, exp, modulo) + addend) % modulo


@cache
def compute_mod_for_base_and_exp(base: int, exp: int, modulo: int) -> int:
    if exp == 1:
        return base % modulo

    if exp % 2 == 1:
        multiplier = base % modulo
    else:
        multiplier = 1

    result = (multiplier * compute_mod_for_base_and_exp(base, exp // 2, modulo) ** 2) % modulo
    return result


if __name__ == '__main__':
    print(euler097('28433 x 2 ^ 7830457 + 1; 10'))
