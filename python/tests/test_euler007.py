from euler007 import euler007
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler007(TestEulerSetup, TestEuler):
    problem_number = 7
    function = euler007
