"""
Base class for Euler problem that takes integer input and returns integer result
"""
from unittest import TestCase
from time import time
from common.data_loader import load_solutions
import logging
from euler import config_logging

config_logging()
solutions = load_solutions()

def timing_decorator(function):
    def timing(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        class_name = type(args[0]).__name__
        logging.info(f'{class_name}.{function.__name__} completed in {(end - start) * 1000:.1f} ms')
        return result
    return timing


class TestEulerData:
    def __init__(self, sample_in='', sample_out='', challenge_in='', challenge_out=''):
        self.sample_in = sample_in or 'sample'
        self.sample_out = sample_out
        self.challenge_in = challenge_in or 'challenge'
        self.challenge_out = challenge_out


class TestEulerSetup(TestCase):
    def setUp(self):
        if not self.problem_number in solutions:
            logging.error(f'No sample data for problem number {self.problem_number}')
            self.data = TestEulerData()
        else:
            solution = solutions[self.problem_number]
            self.data = TestEulerData(
                solution['sample_in'],
                solution['sample_out'],
                solution['challenge_in'],
                solution['challenge_out'])


class TestEuler(object):
    function = None
    problem_number = 0
    data = TestEulerData()
    result = None

    def test_sample(self):
        # Some tests don't have sample in/out, so this can be skipped.
        if not self.data.sample_out:
            self.skipTest(f'No sample in/out data for problem {self.problem_number}')

        fnc = self.function.__func__
        result = fnc(self.data.sample_in)

        self.assertEqual(self.data.sample_out, str(result))
        logging.info(f'Result for problem {self.problem_number}: {result}')


    @timing_decorator
    def test_challenge(self):
        if not self.data.challenge_out:
            self.fail(f'No solution data for problem {self.problem_number}')

        fnc = self.function.__func__
        result = fnc(self.data.challenge_in)

        self.assertEqual(self.data.challenge_out, str(result))
        logging.info(f'Result for problem {self.problem_number}: {result}')
