from euler004 import euler004
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler004(TestEulerSetup, TestEuler):
    problem_number = 4
    function = euler004
