from euler012 import euler012
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler012(TestEulerSetup, TestEuler):
    problem_number = 12
    function = euler012
