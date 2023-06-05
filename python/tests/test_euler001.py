from euler001 import euler001
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler001(TestEulerSetup, TestEuler):
    problem_number = 1
    function = euler001
