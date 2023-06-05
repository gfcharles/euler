from euler100 import euler100
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler100(TestEulerSetup, TestEuler):
    problem_number = 100
    function = euler100
