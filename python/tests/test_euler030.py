from euler030 import euler030
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler030(TestEulerSetup, TestEuler):
    problem_number = 30
    function = euler030
