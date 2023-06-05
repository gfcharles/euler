from euler011 import euler011
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler011(TestEulerSetup, TestEuler):
    problem_number = 11
    function = euler011
