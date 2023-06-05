from euler013 import euler013
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler013(TestEulerSetup, TestEuler):
    problem_number = 13
    function = euler013
