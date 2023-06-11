from tests.test_euler import TestEuler, TestEulerSetup
from euler066 import euler066


class TestEuler066(TestEulerSetup, TestEuler):
    problem_number = 66
    function = euler066
