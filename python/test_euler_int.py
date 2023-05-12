"""
Base class for Euler problem that takes integer input and returns integer result
"""
from unittest import TestCase
from time import time
from data_loader import load_solutions
import logging
from euler import config_logging

config_logging()
solutions = load_solutions()

def timer_metrics(function):
    def wrapper(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        class_name = type(args[0]).__name__
        logging.info(f'{class_name}.{function.__name__} executed in {(end - start) * 1000:.1f} ms')
        return result
    return wrapper

class TestEulerIntData:
    def __init__(self, sample_in=0, sample_out=0, challenge_in=0, challenge_out=0):
        self.sample_in = sample_in
        self.sample_out = sample_out
        self.challenge_in = challenge_in
        self.challenge_out = challenge_out


class TestEulerInt(TestCase):
    function = None
    problem_number = 0
    skip = False

    def setUp(self):
        if self.problem_number in solutions:
            solution = solutions[self.problem_number]
            self.data = TestEulerIntData(
                int(solution['sample_in']),
                int(solution['sample_out']),
                int(solution['challenge_in']),
                int(solution['challenge_out']) )
        else:
            self.data = TestEulerIntData()
            self.skip = True

    def test_sample(self):
        if self.skip:
            return

        fnc = self.function.__func__
        self.assertEqual(self.data.sample_out, fnc(self.data.sample_in))

    @timer_metrics
    def test_challenge(self):
        if self.skip:
            return

        fnc = self.function.__func__
        self.assertEqual(self.data.challenge_out, fnc(self.data.challenge_in))
