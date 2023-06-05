from euler016 import euler016
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler016(TestEulerSetup, TestEuler):
    problem_number = 16
    function = euler016
