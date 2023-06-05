from euler010 import euler010
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler010(TestEulerSetup, TestEuler):
    problem_number = 10
    function = euler010
