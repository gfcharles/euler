from euler033 import euler033
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler033(TestEulerSetup, TestEuler):
    problem_number = 33
    function = euler033
