from euler003 import euler003
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler003(TestEulerSetup, TestEuler):
    problem_number = 3
    function = euler003
