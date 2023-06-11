from tests.test_euler import TestEuler, TestEulerSetup
from euler076 import euler076


class TestEuler076(TestEulerSetup, TestEuler):
    problem_number = 76
    function = euler076
