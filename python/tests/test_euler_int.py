"""
Base class for Euler problem that takes integer input and returns integer result
"""
from unittest import TestCase
from time import time
from data_loader import load_solutions

solutions = load_solutions()

def timer_metrics(function):
    def wrapper(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        class_name = type(args[0]).__name__
        print(f'{class_name}.{function.__name__} executed in {(end - start) * 1000:.1f} ms')
        return result
    return wrapper

def hello(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


class TestEulerIntData:
    @hello
    def __init__(self, sample_in=0, sample_out=0, challenge_in=0, challenge_out=0):
        self.sample_in = sample_in
        self.sample_out = sample_out
        self.challenge_in = challenge_in
        self.challenge_out = challenge_out


class TestEulerInt(TestCase):
    def __init__(self, problem_number:int, fnc: callable, *args):
        super().__init__(*args)

        self.problem_number = problem_number
        self.fnc = fnc

        solution:dict = solutions[problem_number]
        if solution:
            self.data = TestEulerIntData(
                int(solution['sample_in']),
                int(solution['sample_out']),
                int(solution['challenge_in']),
                int(solution['challenge_out']) )
        else:
            self.data = TestEulerIntData()

    def test_sample(self):
        self.assertEqual(self.data.sample_out, self.fnc(self.data.sample_in))

    @timer_metrics
    def test_challenge(self):
        self.assertEqual(self.data.challenge_out, self.fnc(self.data.challenge_in))
